"""Utility to download faculty portraits from Google Cloud Storage and
create local thumbnails for the Inquiry Institute website.

The script expects faculty portraits to live in the bucket ``gs://afaculty``
under a per-person prefix, e.g. ``gs://afaculty/jane-doe/``.  For each
identifier passed on the command line the script pulls down the largest image
found in that prefix and generates two resized thumbnails: a cover image and a
profile image.

Example usage::

    python scripts/collect_portraits.py --id jane-doe --id john-smith \
        --output portraits/

Authentication to Google Cloud follows the standard environment configuration
(for example ``GOOGLE_APPLICATION_CREDENTIALS``).
"""

from __future__ import annotations

import argparse
import io
import logging
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Sequence

from google.cloud import storage
from PIL import Image


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif"}


@dataclass
class ThumbnailSpec:
    """Configuration for a generated thumbnail."""

    name: str
    size: Sequence[int]
    suffix: str = ".jpg"

    def destination(self, base_path: Path) -> Path:
        return base_path / f"{self.name}{self.suffix}"


THUMBNAILS = (
    ThumbnailSpec(name="cover", size=(512, 512)),
    ThumbnailSpec(name="profile", size=(256, 256)),
)


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--bucket",
        default="afaculty",
        help="Name of the Google Cloud Storage bucket that stores portraits.",
    )
    parser.add_argument(
        "--id",
        dest="identifiers",
        action="append",
        default=[],
        help="Faculty identifier (may be specified multiple times).",
    )
    parser.add_argument(
        "--from-file",
        type=Path,
        help="Optional newline separated file with faculty identifiers.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Directory where downloaded originals and thumbnails will be stored.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging.",
    )
    return parser.parse_args(argv)


def build_identifier_list(args: argparse.Namespace) -> List[str]:
    identifiers: List[str] = []
    if args.from_file:
        identifiers.extend(
            line.strip()
            for line in args.from_file.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
    if args.identifiers:
        identifiers.extend(i.strip() for i in args.identifiers if i.strip())

    deduped = sorted(set(identifiers))
    if not deduped:
        raise SystemExit("No identifiers provided. Use --id or --from-file.")
    return deduped


def initialize_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


def is_image_blob(name: str) -> bool:
    return Path(name).suffix.lower() in IMAGE_EXTENSIONS


def choose_primary_blob(blobs: Iterable[storage.Blob]) -> storage.Blob | None:
    """Return the largest blob from the iterable."""

    blobs = list(blobs)
    if not blobs:
        return None
    return max(blobs, key=lambda blob: blob.size or 0)


def download_image(blob: storage.Blob) -> Image.Image:
    data = blob.download_as_bytes()
    image = Image.open(io.BytesIO(data))
    if image.mode not in ("RGB", "RGBA"):
        image = image.convert("RGB")
    return image


def save_thumbnail(image: Image.Image, destination: Path, size: Sequence[int]) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    thumbnail = image.copy()
    thumbnail.thumbnail(size, Image.LANCZOS)
    thumbnail.save(destination, format="JPEG", optimize=True, quality=85)


def process_identifier(client: storage.Client, bucket_name: str, identifier: str, output_dir: Path) -> None:
    logger = logging.getLogger(__name__)
    bucket = client.bucket(bucket_name)
    prefix = f"{identifier.rstrip('/')}/"

    blobs = [
        blob
        for blob in bucket.list_blobs(prefix=prefix)
        if not blob.name.endswith("/") and is_image_blob(blob.name)
    ]

    if not blobs:
        logger.warning("No portrait images found for '%s'", identifier)
        return

    blob = choose_primary_blob(blobs)
    if blob is None:
        logger.warning("Could not determine a portrait for '%s'", identifier)
        return

    logger.info("Downloading %s (size=%s) for %s", blob.name, blob.size, identifier)
    image = download_image(blob)

    person_dir = output_dir / identifier
    for spec in THUMBNAILS:
        destination = spec.destination(person_dir)
        save_thumbnail(image, destination, spec.size)
        logger.info("Saved %s", destination)


def main(argv: Sequence[str]) -> int:
    args = parse_args(argv)
    initialize_logging(args.verbose)

    identifiers = build_identifier_list(args)
    client = storage.Client()

    for identifier in identifiers:
        process_identifier(client, args.bucket, identifier, args.output)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

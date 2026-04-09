#!/usr/bin/env python3
"""
Generate card illustrations via FAL AI API.

Reads all definitions/*.json files, checks which images/ PNGs are missing,
and generates them using the fal-ai/flux/schnell model.
"""

import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path

import fal_client
from PIL import Image, PngImagePlugin

SCRIPT_DIR = Path(__file__).parent
DEFINITIONS_DIR = SCRIPT_DIR / "definitions"
MODEL = "fal-ai/flux/schnell"

FAL_PARAMS = {
    "num_inference_steps": 4,
    "num_images": 1,
    "enable_safety_checker": True,
    "image_size": "portrait_4_3",
    "output_format": "png",
}


def check_fal_key():
    key = os.environ.get("FAL_KEY")
    if not key:
        print("Error: FAL_KEY environment variable is not set.", file=sys.stderr)
        print("Set it with: export FAL_KEY=your_api_key", file=sys.stderr)
        sys.exit(1)


def load_definitions():
    """Load all card definition JSON files from the definitions directory."""
    defs = []
    for path in sorted(DEFINITIONS_DIR.glob("*.json")):
        with open(path) as f:
            data = json.load(f)
        data["_source"] = path
        defs.append(data)
    return defs


def card_id_from_def(defn):
    """Return the card id, falling back to the filename stem."""
    return defn.get("id") or defn["_source"].stem


def generate_image(card_id, prompt, image_path):
    """Call FAL API, download result, save as PNG with metadata."""
    print(f"  Generating image for '{card_id}'...")
    arguments = {"prompt": prompt, **FAL_PARAMS}

    result = fal_client.subscribe(MODEL, arguments=arguments)

    url = result["images"][0]["url"]
    seed = result.get("seed")

    print(f"  Downloading from {url}")
    with urllib.request.urlopen(url) as response:
        image_data = response.read()

    # Write to a temporary location, then re-open with Pillow to embed metadata.
    tmp_path = Path(str(image_path) + ".tmp")
    tmp_path.write_bytes(image_data)

    img = Image.open(tmp_path)
    meta = PngImagePlugin.PngInfo()
    meta.add_text("card_id", card_id)
    meta.add_text("image_prompt", prompt)
    meta.add_text("model", MODEL)
    if seed is not None:
        meta.add_text("seed", str(seed))

    image_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(image_path, "PNG", pnginfo=meta)
    tmp_path.unlink()

    print(f"  Saved to {image_path}")


def process_card(defn, force=False):
    """Process a single card definition.

    Returns one of: "generated", "skipped", "error".
    """
    card_id = card_id_from_def(defn)

    prompt = defn.get("image-prompt")
    if not prompt:
        print(f"Warning: '{card_id}' has no 'image-prompt' field — skipping.")
        return "skipped"

    image_field = defn.get("image")
    if not image_field:
        print(f"Warning: '{card_id}' has no 'image' field — skipping.")
        return "skipped"

    image_path = SCRIPT_DIR / image_field

    if image_path.exists() and not force:
        print(f"Skipping '{card_id}' — {image_path} already exists. Use --force to regenerate.")
        return "skipped"

    try:
        generate_image(card_id, prompt, image_path)
        return "generated"
    except Exception as exc:
        print(f"Error generating image for '{card_id}': {exc}", file=sys.stderr)
        return "error"


def main():
    parser = argparse.ArgumentParser(
        description="Generate card illustrations via FAL AI (fal-ai/flux/schnell).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 generate-image.py               Generate all missing card images
  python3 generate-image.py --id swat-raid  Generate a single card's image
  python3 generate-image.py --force       Regenerate all images, even existing ones
""",
    )
    parser.add_argument(
        "--id",
        metavar="CARD_ID",
        help="Generate only the card with this id (e.g. swat-raid)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Regenerate images even if they already exist",
    )
    args = parser.parse_args()

    check_fal_key()

    all_defs = load_definitions()
    if not all_defs:
        print(f"No definition files found in {DEFINITIONS_DIR}")
        sys.exit(0)

    if args.id:
        matching = [d for d in all_defs if card_id_from_def(d) == args.id]
        if not matching:
            print(f"Error: No definition found with id '{args.id}'.", file=sys.stderr)
            available = [card_id_from_def(d) for d in all_defs]
            print(f"Available ids: {', '.join(available)}", file=sys.stderr)
            sys.exit(1)
        targets = matching
    else:
        targets = all_defs

    counts = {"generated": 0, "skipped": 0, "error": 0}

    for defn in targets:
        status = process_card(defn, force=args.force)
        counts[status] += 1

    print(
        f"\nDone. Generated: {counts['generated']}, "
        f"Skipped: {counts['skipped']}, "
        f"Errors: {counts['error']}"
    )


if __name__ == "__main__":
    main()

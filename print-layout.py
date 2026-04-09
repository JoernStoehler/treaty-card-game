#!/usr/bin/env python3
"""Arrange rendered card images into a print-ready PDF (2 columns x 3 rows per page)."""

import argparse
import math
import sys
from pathlib import Path

from PIL import Image

# --- Constants ---
A4_W_PX = 2480   # A4 width at 300 DPI (210mm)
A4_H_PX = 3508   # A4 height at 300 DPI (297mm)

CARD_NATIVE_W = 827   # 70mm at 300 DPI
CARD_NATIVE_H = 1417  # 120mm at 300 DPI

COLS = 2
ROWS = 3
CARDS_PER_PAGE = COLS * ROWS

# Margins and gaps: 5mm at 300 DPI = 59px
MARGIN_PX = 59  # page edge margin (top/bottom/left/right)
GAP_PX = 59     # gap between cards (for cutting guides)

# Calculate scaled card dimensions to fit 2x3 on A4 with margins/gaps
# Available space for cards:
#   width:  A4_W - 2*margin - (COLS-1)*gap  divided by COLS
#   height: A4_H - 2*margin - (ROWS-1)*gap  divided by ROWS
_avail_w = A4_W_PX - 2 * MARGIN_PX - (COLS - 1) * GAP_PX
_avail_h = A4_H_PX - 2 * MARGIN_PX - (ROWS - 1) * GAP_PX

_max_card_w = _avail_w // COLS
_max_card_h = _avail_h // ROWS

_scale = min(_max_card_w / CARD_NATIVE_W, _max_card_h / CARD_NATIVE_H)

CARD_W = int(CARD_NATIVE_W * _scale)
CARD_H = int(CARD_NATIVE_H * _scale)

# Recompute actual grid size and center it on the page
_grid_w = COLS * CARD_W + (COLS - 1) * GAP_PX
_grid_h = ROWS * CARD_H + (ROWS - 1) * GAP_PX

ORIGIN_X = (A4_W_PX - _grid_w) // 2
ORIGIN_Y = (A4_H_PX - _grid_h) // 2

RENDERED_DIR = Path("rendered")
PRINT_DIR = Path("print")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Arrange rendered card PNGs into a print-ready PDF (print/cards.pdf)."
    )

    color_group = parser.add_mutually_exclusive_group(required=True)
    color_group.add_argument(
        "--color",
        action="store_true",
        help="Output pages in full color.",
    )
    color_group.add_argument(
        "--greyscale",
        action="store_true",
        help="Output pages in greyscale.",
    )

    parser.add_argument(
        "--id",
        metavar="ID,...",
        help="Comma-separated list of card IDs to include (e.g. swat-raid,garage-cluster). "
             "Defaults to all rendered front-face cards.",
    )

    return parser.parse_args()


def collect_card_paths(id_filter=None):
    """Return sorted list of card image paths to include."""
    if id_filter:
        ids = [s.strip() for s in id_filter.split(",") if s.strip()]
        paths = []
        missing = []
        for card_id in ids:
            p = RENDERED_DIR / f"{card_id}-f.png"
            if p.exists():
                paths.append(p)
            else:
                missing.append(str(p))
        if missing:
            print(f"Warning: the following card files were not found: {', '.join(missing)}", file=sys.stderr)
    else:
        paths = sorted(RENDERED_DIR.glob("*-f.png"))

    if not paths:
        print("Error: no card images found.", file=sys.stderr)
        sys.exit(1)

    return paths


def build_page(card_paths_on_page, greyscale=False):
    """Create a single A4 PIL Image with the given cards arranged in a 2x3 grid."""
    page = Image.new("RGB", (A4_W_PX, A4_H_PX), color=(255, 255, 255))

    for idx, card_path in enumerate(card_paths_on_page):
        col = idx % COLS
        row = idx // COLS

        x = ORIGIN_X + col * (CARD_W + GAP_PX)
        y = ORIGIN_Y + row * (CARD_H + GAP_PX)

        card_img = Image.open(card_path).convert("RGB")
        card_img = card_img.resize((CARD_W, CARD_H), Image.LANCZOS)

        page.paste(card_img, (x, y))

    if greyscale:
        page = page.convert("L")

    return page


def main():
    args = parse_args()

    card_paths = collect_card_paths(args.id)
    num_cards = len(card_paths)
    num_pages = math.ceil(num_cards / CARDS_PER_PAGE)

    PRINT_DIR.mkdir(exist_ok=True)

    pages = []
    for page_num in range(num_pages):
        start = page_num * CARDS_PER_PAGE
        end = start + CARDS_PER_PAGE
        cards_on_page = card_paths[start:end]

        page_img = build_page(cards_on_page, greyscale=args.greyscale)
        pages.append(page_img)
        print(f"  Built page {page_num + 1}  ({len(cards_on_page)} card(s))")

    # Save as single multi-page PDF
    pdf_path = PRINT_DIR / "cards.pdf"
    pages[0].save(
        pdf_path, "PDF", resolution=300, save_all=True,
        append_images=pages[1:] if len(pages) > 1 else [],
    )
    print(f"Saved {pdf_path}  ({num_pages} page(s), {num_cards} card(s)).")


if __name__ == "__main__":
    main()

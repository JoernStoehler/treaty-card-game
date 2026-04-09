#!/usr/bin/env python3
"""
render-card.py — Render card definitions into print-ready PNG images.

Reads definitions/*.json, renders each card using an HTML template via
Playwright (headless Chromium), outputs rendered/<id>-f.png.

Card dimensions: 70×120mm at 300 DPI = 827×1417 pixels.
"""

import argparse
import base64
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image, PngImagePlugin
from playwright.sync_api import sync_playwright

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CARD_WIDTH_PX = 827
CARD_HEIGHT_PX = 1417

DEFINITIONS_DIR = Path("definitions")
IMAGES_DIR = Path("images")
RENDERED_DIR = Path("rendered")


# ---------------------------------------------------------------------------
# Image helpers
# ---------------------------------------------------------------------------

def load_image_as_data_uri(image_path: str) -> str | None:
    """Read an image from disk and return a base64 data URI, or None if missing."""
    path = Path(image_path)
    if not path.exists():
        return None
    suffix = path.suffix.lower()
    mime = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
    }.get(suffix, "image/png")
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{data}"


def image_html(card: dict, height_percent: int = 60) -> str:
    """Return an <img> or placeholder <div> for the card illustration."""
    src = load_image_as_data_uri(card.get("image", ""))
    if src:
        return (
            f'<img src="{src}" style="width:100%;height:100%;'
            f'object-fit:cover;display:block;" />'
        )
    return (
        '<div style="width:100%;height:100%;background:#555;'
        'display:flex;align-items:center;justify-content:center;'
        'color:#aaa;font-size:48px;letter-spacing:2px;">NO IMAGE</div>'
    )


# ---------------------------------------------------------------------------
# HTML templates
# ---------------------------------------------------------------------------

def template_treaty_flat(card: dict) -> str:
    """treaty-flat: category stripe on left, name header, illustration, description."""
    color = card.get("color", "#444444")
    name = card.get("name", "")
    description = card.get("description", "")
    category = card.get("category", "")
    illus = image_html(card)

    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: {CARD_WIDTH_PX}px;
    height: {CARD_HEIGHT_PX}px;
    overflow: hidden;
    font-family: 'Liberation Sans', 'DejaVu Sans', Arial, sans-serif;
    background: #1a1a2e;
    display: flex;
  }}

  /* Left stripe */
  .stripe {{
    width: 59px;
    min-width: 59px;
    height: 100%;
    background: {color};
    flex-shrink: 0;
  }}

  /* Main card body */
  .body {{
    flex: 1;
    display: flex;
    flex-direction: column;
    height: 100%;
    background: #faf8f2;
    overflow: hidden;
  }}

  /* Header bar */
  .header {{
    background: #1a1a2e;
    padding: 28px 32px 22px 32px;
    flex-shrink: 0;
  }}
  .header .type-label {{
    font-size: 22px;
    color: {color};
    text-transform: uppercase;
    letter-spacing: 4px;
    font-weight: 700;
    margin-bottom: 8px;
  }}
  .header .name {{
    font-size: 64px;
    font-weight: 900;
    color: #ffffff;
    line-height: 1.05;
    text-transform: uppercase;
    letter-spacing: 1px;
  }}

  /* Illustration */
  .illustration {{
    flex: 0 0 auto;
    height: 620px;
    overflow: hidden;
    border-top: 4px solid {color};
    border-bottom: 4px solid {color};
  }}

  /* Description area */
  .description {{
    flex: 1;
    padding: 36px 36px 24px 36px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow: hidden;
  }}
  .description .text {{
    font-size: 42px;
    line-height: 1.45;
    color: #1a1a1a;
    font-weight: 400;
  }}

  /* Category label bottom */
  .category-label {{
    display: flex;
    align-items: center;
    gap: 16px;
  }}
  .category-label .dot {{
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: {color};
    flex-shrink: 0;
  }}
  .category-label .text {{
    font-size: 30px;
    font-weight: 700;
    color: {color};
    text-transform: uppercase;
    letter-spacing: 3px;
  }}

  /* Thin color accent line at very bottom */
  .footer-line {{
    height: 8px;
    background: {color};
    flex-shrink: 0;
  }}
</style>
</head>
<body>
  <div class="stripe"></div>
  <div class="body">
    <div class="header">
      <div class="type-label">Treaty Clause</div>
      <div class="name">{name}</div>
    </div>
    <div class="illustration">{illus}</div>
    <div class="description">
      <div class="text">{description}</div>
      <div class="category-label">
        <div class="dot"></div>
        <div class="text">{category}</div>
      </div>
    </div>
    <div class="footer-line"></div>
  </div>
</body>
</html>"""


def template_event_flat(card: dict) -> str:
    """event-flat: dark/red frame, name, illustration, scenario, tier boxes."""
    name = card.get("name", "")
    scenario = card.get("scenario", "")
    tiers = card.get("tiers", [])
    illus = image_html(card)

    # Build tier failure ranges and HTML boxes
    tier_boxes_html = ""
    prev_max = -1
    for i, tier in enumerate(tiers):
        max_f = tier.get("max_failures", 99)
        text = tier.get("text", "")

        # Label
        if max_f >= 99:
            label = f"{prev_max + 1}+"
        elif prev_max < 0:
            label = f"0–{max_f}"
        else:
            label = f"{prev_max + 1}–{max_f}"

        # Visual intensity: more red/warning at higher tiers
        intensity = i / max(len(tiers) - 1, 1)  # 0.0 to 1.0
        # Background: dark grey → dark red
        r = int(40 + intensity * 120)
        g = int(35 - intensity * 25)
        b = int(35 - intensity * 25)
        bg = f"rgb({r},{g},{b})"
        border_r = int(100 + intensity * 155)
        border_color = f"rgb({border_r},30,30)"
        label_bg_r = int(120 + intensity * 135)
        label_bg = f"rgb({label_bg_r},30,30)"
        text_color = "#ffffff" if intensity > 0.3 else "#e8e8e8"

        # EXTINCTION marker
        is_extinction = "EXTINCTION" in text.upper()
        extinction_badge = ""
        if is_extinction:
            extinction_badge = (
                '<div style="display:inline-block;background:#ff0000;color:#fff;'
                'font-size:22px;font-weight:900;padding:4px 14px;border-radius:4px;'
                'letter-spacing:2px;margin-bottom:8px;">⚠ EXTINCTION</div><br>'
            )

        tier_boxes_html += f"""
        <div style="display:flex;align-items:stretch;border:3px solid {border_color};
                    margin-bottom:10px;border-radius:6px;overflow:hidden;
                    background:{bg};flex-shrink:0;">
          <div style="background:{label_bg};padding:16px 18px;display:flex;
                      align-items:center;justify-content:center;flex-shrink:0;
                      min-width:110px;border-right:3px solid {border_color};">
            <div style="text-align:center;">
              <div style="font-size:19px;color:#ffcccc;font-weight:600;
                          text-transform:uppercase;letter-spacing:1px;
                          margin-bottom:4px;">failures</div>
              <div style="font-size:46px;font-weight:900;color:#ffffff;
                          line-height:1;">{label}</div>
            </div>
          </div>
          <div style="padding:16px 20px;display:flex;align-items:center;flex:1;">
            <div style="font-size:34px;line-height:1.35;color:{text_color};
                        font-weight:500;">{extinction_badge}{text}</div>
          </div>
        </div>"""

        prev_max = max_f

    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: {CARD_WIDTH_PX}px;
    height: {CARD_HEIGHT_PX}px;
    overflow: hidden;
    font-family: 'Liberation Sans', 'DejaVu Sans', Arial, sans-serif;
    background: #1a0a0a;
  }}

  .card {{
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    border: 12px solid #6b1010;
    background: #1a0a0a;
    overflow: hidden;
  }}

  /* Top header with name over illustration */
  .header {{
    position: relative;
    flex: 0 0 420px;
    overflow: hidden;
    flex-shrink: 0;
  }}
  .header .illustration {{
    width: 100%;
    height: 100%;
  }}
  .header .name-overlay {{
    position: absolute;
    top: 0; left: 0; right: 0;
    background: linear-gradient(to bottom, rgba(20,0,0,0.92) 0%, rgba(20,0,0,0.6) 70%, transparent 100%);
    padding: 28px 32px 40px 32px;
  }}
  .header .type-label {{
    font-size: 21px;
    color: #ff6b6b;
    text-transform: uppercase;
    letter-spacing: 4px;
    font-weight: 700;
    margin-bottom: 8px;
  }}
  .header .name {{
    font-size: 66px;
    font-weight: 900;
    color: #ffffff;
    line-height: 1.05;
    text-transform: uppercase;
    text-shadow: 0 2px 8px rgba(0,0,0,0.8);
  }}

  /* Scenario section */
  .scenario {{
    flex-shrink: 0;
    padding: 28px 32px 20px 32px;
    border-top: 3px solid #6b1010;
    border-bottom: 3px solid #6b1010;
    background: #110505;
  }}
  .scenario .label {{
    font-size: 20px;
    color: #ff6b6b;
    text-transform: uppercase;
    letter-spacing: 3px;
    font-weight: 700;
    margin-bottom: 10px;
  }}
  .scenario .text {{
    font-size: 38px;
    line-height: 1.4;
    color: #e8d8d8;
    font-weight: 400;
  }}

  /* Tier boxes */
  .tiers {{
    flex: 1;
    padding: 20px 28px 20px 28px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    overflow: hidden;
  }}
  .tiers .tiers-label {{
    font-size: 20px;
    color: #ff6b6b;
    text-transform: uppercase;
    letter-spacing: 3px;
    font-weight: 700;
    margin-bottom: 12px;
    flex-shrink: 0;
  }}
</style>
</head>
<body>
  <div class="card">
    <div class="header">
      <div class="illustration">{illus}</div>
      <div class="name-overlay">
        <div class="type-label">Crisis Event</div>
        <div class="name">{name}</div>
      </div>
    </div>
    <div class="scenario">
      <div class="label">Scenario</div>
      <div class="text">{scenario}</div>
    </div>
    <div class="tiers">
      <div class="tiers-label">Escalation Tiers</div>
      {tier_boxes_html}
    </div>
  </div>
</body>
</html>"""


def template_safety_flat(card: dict) -> str:
    """safety-flat: bright green, name, illustration, description."""
    name = card.get("name", "")
    description = card.get("description", "")
    illus = image_html(card)

    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: {CARD_WIDTH_PX}px;
    height: {CARD_HEIGHT_PX}px;
    overflow: hidden;
    font-family: 'Liberation Sans', 'DejaVu Sans', Arial, sans-serif;
    background: #0d2b1a;
  }}

  .card {{
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    border: 14px solid #00c853;
    background: #0d2b1a;
    overflow: hidden;
  }}

  /* Header */
  .header {{
    background: linear-gradient(135deg, #00c853 0%, #00e676 50%, #69f0ae 100%);
    padding: 28px 34px 24px 34px;
    flex-shrink: 0;
    border-bottom: 6px solid #00c853;
  }}
  .header .type-label {{
    font-size: 22px;
    color: #003d1f;
    text-transform: uppercase;
    letter-spacing: 4px;
    font-weight: 700;
    margin-bottom: 8px;
    opacity: 0.75;
  }}
  .header .name {{
    font-size: 62px;
    font-weight: 900;
    color: #001a0d;
    line-height: 1.05;
    text-transform: uppercase;
  }}

  /* Illustration */
  .illustration {{
    flex: 0 0 680px;
    overflow: hidden;
    border-bottom: 6px solid #00c853;
  }}

  /* Description */
  .description {{
    flex: 1;
    padding: 36px 36px 30px 36px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background: #0d2b1a;
    overflow: hidden;
  }}
  .description .text {{
    font-size: 44px;
    line-height: 1.45;
    color: #c8ffd8;
    font-weight: 400;
  }}

  /* Victory badge */
  .victory {{
    display: flex;
    align-items: center;
    gap: 18px;
    flex-shrink: 0;
  }}
  .victory .star {{
    font-size: 44px;
    color: #00e676;
  }}
  .victory .text {{
    font-size: 28px;
    font-weight: 800;
    color: #00e676;
    text-transform: uppercase;
    letter-spacing: 3px;
  }}

  /* Bottom accent bar */
  .footer-bar {{
    height: 14px;
    background: linear-gradient(90deg, #00c853, #69f0ae, #00c853);
    flex-shrink: 0;
  }}
</style>
</head>
<body>
  <div class="card">
    <div class="header">
      <div class="type-label">Safety Breakthrough</div>
      <div class="name">{name}</div>
    </div>
    <div class="illustration">{illus}</div>
    <div class="description">
      <div class="text">{description}</div>
      <div class="victory">
        <div class="star">★</div>
        <div class="text">Collect 3 to Win</div>
      </div>
    </div>
    <div class="footer-bar"></div>
  </div>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Template dispatch
# ---------------------------------------------------------------------------

TEMPLATES = {
    "treaty-flat": template_treaty_flat,
    "event-flat": template_event_flat,
    "safety-flat": template_safety_flat,
}


def render_html_to_png(html: str, output_path: Path, browser) -> None:
    """Use Playwright to screenshot the HTML at card dimensions."""
    page = browser.new_page(viewport={"width": CARD_WIDTH_PX, "height": CARD_HEIGHT_PX})
    page.set_content(html, wait_until="networkidle")
    page.screenshot(path=str(output_path), full_page=False, type="png")
    page.close()


def embed_png_metadata(path: Path, card: dict) -> None:
    """Embed card metadata into the PNG using Pillow PngInfo."""
    img = Image.open(path)
    meta = PngImagePlugin.PngInfo()
    meta.add_text("card_id", card.get("id", ""))
    meta.add_text("card_type", card.get("type", ""))
    meta.add_text("render_timestamp", datetime.now(timezone.utc).isoformat())
    img.save(path, "PNG", pnginfo=meta)


# ---------------------------------------------------------------------------
# Core rendering logic
# ---------------------------------------------------------------------------

def load_definitions() -> list[dict]:
    """Load all card JSON files from the definitions directory."""
    defs = []
    for f in sorted(DEFINITIONS_DIR.glob("*.json")):
        with f.open() as fh:
            defs.append(json.load(fh))
    return defs


def render_card(card: dict, browser) -> None:
    """Render a single card to rendered/<id>-f.png."""
    card_id = card.get("id", "unknown")
    card_type = card.get("type", "")

    template_fn = TEMPLATES.get(card_type)
    if template_fn is None:
        print(f"  [skip] {card_id}: unknown type '{card_type}'", file=sys.stderr)
        return

    html = template_fn(card)

    RENDERED_DIR.mkdir(exist_ok=True)
    output_path = RENDERED_DIR / f"{card_id}-f.png"

    print(f"  Rendering {card_id} ({card_type}) -> {output_path}")
    render_html_to_png(html, output_path, browser)
    embed_png_metadata(output_path, card)
    print(f"  Done: {output_path} ({output_path.stat().st_size // 1024} KB)")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Render card definitions into print-ready PNG images.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 render-card.py              # render all cards
  python3 render-card.py --id swat-raid   # render one card
""",
    )
    parser.add_argument(
        "--id",
        metavar="CARD_ID",
        help="Render only the card with this id (e.g. swat-raid)",
    )
    args = parser.parse_args()

    cards = load_definitions()
    if not cards:
        print("No card definitions found in definitions/", file=sys.stderr)
        sys.exit(1)

    if args.id:
        matched = [c for c in cards if c.get("id") == args.id]
        if not matched:
            available = ", ".join(c.get("id", "?") for c in cards)
            print(
                f"No card with id '{args.id}' found. Available: {available}",
                file=sys.stderr,
            )
            sys.exit(1)
        cards = matched

    print(f"Rendering {len(cards)} card(s)...")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for card in cards:
            render_card(card, browser)
        browser.close()
    print("All done.")


if __name__ == "__main__":
    main()

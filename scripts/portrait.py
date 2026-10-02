#!/usr/bin/env python3
"""Turn a photo into the text-art portrait shown on the home page.

Writes data/portrait.json, which layouts/home.html renders inside the photo window.
Re-run whenever the photo changes:

    python3 scripts/portrait.py assets/images/me.jpg
    python3 scripts/portrait.py assets/images/me.jpg --charset blocks --cols 48

Requires Pillow (pip install pillow).
"""

import argparse
import json
from pathlib import Path

from PIL import Image, ImageOps

CHARSETS = {
    # ordered from least to most "ink"
    "blocks": " ░▒▓█",
    "ascii": " .:-=+*#%@",
}
# Fira Code glyphs are 0.6em wide; with line-height 1 a cell is 0.6 times as wide as it is tall
CELL_ASPECT = 0.6


def render(gray, chars, invert):
    levels = len(chars) - 1
    rows = []
    for y in range(gray.height):
        row = ""
        for x in range(gray.width):
            v = gray.getpixel((x, y)) / 255
            # dark theme draws light ink on a dark background, so bright pixels get dense glyphs
            ink = v if invert else 1 - v
            row += chars[round(ink * levels)]
        rows.append(row.rstrip())
    return "\n".join(rows)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("image", type=Path)
    parser.add_argument("--cols", type=int, default=64, help="characters per line (default 64)")
    parser.add_argument("--charset", choices=CHARSETS, default="ascii")
    parser.add_argument("--out", type=Path, default=Path("data/portrait.json"))
    args = parser.parse_args()

    img = ImageOps.exif_transpose(Image.open(args.image)).convert("L")
    # same centre square crop as the photo shown on hover
    img = ImageOps.fit(img, (min(img.size),) * 2)
    img = ImageOps.autocontrast(img, cutoff=2)
    rows = int(args.cols * CELL_ASPECT)  # round down so the art never overflows the square frame
    gray = img.resize((args.cols, rows), Image.LANCZOS)

    chars = CHARSETS[args.charset]
    data = {
        "cols": args.cols,
        "dark": render(gray, chars, invert=True),
        "light": render(gray, chars, invert=False),
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {args.out} ({args.cols}x{rows}, {args.charset})")


if __name__ == "__main__":
    main()

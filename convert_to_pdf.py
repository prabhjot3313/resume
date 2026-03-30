#!/usr/bin/env python3
"""
Convert resume HTML to PDF using Playwright.
Preserves hyperlinks, no headers/footers, margins controlled by @page CSS.

Usage:
    python3 convert_to_pdf.py resume-c.html
    python3 convert_to_pdf.py resume-c.html output.pdf
"""

import sys
import os
from pathlib import Path
from playwright.sync_api import sync_playwright


def convert(html_file: str, output_pdf: str = None):
    html_path = Path(html_file).resolve()
    if not html_path.exists():
        print(f"Error: {html_file} not found")
        sys.exit(1)

    if output_pdf is None:
        output_pdf = str(html_path.with_suffix(".pdf"))

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file://{html_path}", wait_until="networkidle")
        page.pdf(
            path=output_pdf,
            format="Letter",
            print_background=True,
            display_header_footer=False,   # no date/title/page number
        )
        browser.close()

    print(f"Saved: {output_pdf}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 convert_to_pdf.py <input.html> [output.pdf]")
        sys.exit(1)
    convert(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)

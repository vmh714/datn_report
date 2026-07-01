#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pdf_to_text.py - Trich xuat PDF ra van ban de AI/nguoi doc.

Cach dung:
    python pdf_to_text.py "ĐỒ ÁN TỐT NGHIỆP.pdf"
    python pdf_to_text.py input.pdf -o output.md --format md
    python pdf_to_text.py input.pdf --format txt
    python pdf_to_text.py input.pdf --images        # trich them anh ra thu muc

Ho tro:
    - Trich text theo tung trang (co danh dau so trang).
    - Xuat ra Markdown (.md) hoac plain text (.txt).
    - Neu trang khong co text (anh scan) -> canh bao de biet can OCR.
    - Tuy chon trich xuat anh nhung trong PDF.
"""
import argparse
import os
import sys

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("Thieu PyMuPDF. Cai bang: pip install pymupdf")


def extract(pdf_path, out_path, fmt="md", dump_images=False):
    doc = fitz.open(pdf_path)
    base = os.path.splitext(os.path.basename(pdf_path))[0]
    img_dir = None
    if dump_images:
        img_dir = os.path.join(os.path.dirname(out_path) or ".", base + "_images")
        os.makedirs(img_dir, exist_ok=True)

    parts = []
    empty_pages = []

    if fmt == "md":
        parts.append(f"# {base}\n")
        parts.append(f"> Nguon: `{os.path.basename(pdf_path)}` — {doc.page_count} trang\n")

    for i in range(doc.page_count):
        page = doc[i]
        text = page.get_text("text").strip()
        if not text:
            empty_pages.append(i + 1)

        if fmt == "md":
            parts.append(f"\n\n---\n\n## Trang {i + 1}\n\n{text}\n")
        else:
            parts.append(f"\n===== Trang {i + 1} =====\n\n{text}\n")

        if dump_images:
            for j, img in enumerate(page.get_images(full=True)):
                xref = img[0]
                try:
                    pix = fitz.Pixmap(doc, xref)
                    if pix.n - pix.alpha >= 4:  # CMYK -> RGB
                        pix = fitz.Pixmap(fitz.csRGB, pix)
                    fn = os.path.join(img_dir, f"p{i + 1:03d}_{j + 1}.png")
                    pix.save(fn)
                    pix = None
                except Exception as e:
                    print(f"  [!] Loi anh trang {i+1}: {e}", file=sys.stderr)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("".join(parts))

    print(f"[OK] Da xuat: {out_path}")
    print(f"     Tong: {doc.page_count} trang")
    if empty_pages:
        print(f"     [!] {len(empty_pages)} trang KHONG co text (co the la anh scan, "
              f"can OCR): {empty_pages}")
    if img_dir:
        n = len(os.listdir(img_dir))
        print(f"     Anh: {n} file trong {img_dir}")
    doc.close()


def main():
    ap = argparse.ArgumentParser(description="Trich xuat PDF ra text/markdown de AI doc.")
    ap.add_argument("pdf", help="Duong dan file PDF")
    ap.add_argument("-o", "--output", help="File dau ra (mac dinh: <ten>.md)")
    ap.add_argument("-f", "--format", choices=["md", "txt"], default="md",
                    help="Dinh dang dau ra (mac dinh: md)")
    ap.add_argument("--images", action="store_true", help="Trich xuat anh trong PDF")
    args = ap.parse_args()

    if not os.path.isfile(args.pdf):
        sys.exit(f"Khong tim thay file: {args.pdf}")

    out = args.output
    if not out:
        base = os.path.splitext(os.path.basename(args.pdf))[0]
        out = base + ("." + args.format)

    extract(args.pdf, out, fmt=args.format, dump_images=args.images)


if __name__ == "__main__":
    main()

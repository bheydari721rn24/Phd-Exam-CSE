"""Index the local exam archive without treating scan OCR as verified question text."""

import argparse
import json
from pathlib import Path

from pypdf import PdfReader


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("exam_root", type=Path, help="Path to the repository's Exams directory")
    parser.add_argument("output", type=Path, help="Output JSON file")
    args = parser.parse_args()
    if not args.exam_root.is_dir():
        parser.error(f"Missing exam directory: {args.exam_root}")

    files = []
    for path in sorted(args.exam_root.rglob("*.pdf")):
        parts = path.relative_to(args.exam_root).parts
        if len(parts) != 4:
            continue
        level, field, year, name = parts
        reader = PdfReader(path)
        sample = (reader.pages[0].extract_text() or "") if reader.pages else ""
        files.append({
            "level": level,
            "field": field,
            "year": year,
            "filename": name,
            "repoPath": path.relative_to(args.exam_root.parent).as_posix(),
            "pages": len(reader.pages),
            "firstPageTextCharacters": len(sample),
            "questionAudit": "not_started",
        })

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps({
        "note": "File inventory only. Page count and filename are verified; subject and question labels need image review.",
        "files": files,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Indexed {len(files)} PDF files")


if __name__ == "__main__":
    main()

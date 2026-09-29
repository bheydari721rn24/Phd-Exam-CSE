"""Validate local links and the English-only published study assets."""

from __future__ import annotations

import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1] / "dist"


class Links(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.urls: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if key in {"href", "src"} and value:
                self.urls.append(value)


pages = list(ROOT.rglob("*.html"))
assert pages
missing: list[tuple[str, str]] = []
arabic: list[str] = []
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix not in {".html", ".js", ".json", ".css"}:
        continue
    source = path.read_text(encoding="utf-8")
    if re.search(r"[\u0600-\u06ff]", source):
        arabic.append(str(path.relative_to(ROOT)))
    if path.suffix == ".html":
        parser = Links()
        parser.feed(source)
        for url in parser.urls:
            parts = urlsplit(url)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            target = path.parent / unquote(parts.path)
            if not target.is_file():
                missing.append((str(path.relative_to(ROOT)), url))

plan = json.loads((ROOT / "schedule.en.json").read_text(encoding="utf-8"))
daily = json.loads((ROOT / "week1-daily.en.json").read_text(encoding="utf-8"))
lessons = json.loads((ROOT / "lessons.json").read_text(encoding="utf-8"))
assert len(plan["ielts"]["stages"]) == len(plan["weeks"]) == 11
assert all(len(stage) == 4 for stage in plan["ielts"]["stages"])
assert sum(block["hours"] for day in daily["days"] for block in day["blocks"] if block.get("subject") == "english") == 4
assert lessons[0]["chapters"][0]["status"] == "ready"
assert lessons[0]["chapters"][1]["status"] == "draft"
assert lessons[0]["chapters"][1]["url"] == "chapters/d_sets.html"
assert not arabic, arabic
assert not missing, missing
print(f"English site checks passed: {len(pages)} HTML pages; local links, IELTS stages, hours, approved logic status, and script coverage.")

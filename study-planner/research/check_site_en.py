"""Validate local links and the English-only published study assets."""

from __future__ import annotations

import json
import re
import unicodedata
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


class MathCoverage(HTMLParser):
    """Flag mathematical characters left in the prose typeface of a lesson."""

    def __init__(self) -> None:
        super().__init__()
        self.stack: list[tuple[str, dict[str, str | None]]] = []
        self.unstyled: list[str] = []
        self.styled_runs = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        details = dict(attrs)
        self.stack.append((tag, details))
        if "math-inline" in (details.get("class") or ""):
            self.styled_runs += 1

    def handle_endtag(self, tag: str) -> None:
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data: str) -> None:
        if not any(tag == "article" for tag, _ in self.stack):
            return
        if any(tag in {"svg", "math", "code", "pre", "script", "style"} for tag, _ in self.stack):
            return
        if any(
            "math-inline" in (details.get("class") or "")
            or "formula-block" in (details.get("class") or "")
            for _, details in self.stack
        ):
            return
        self.unstyled.extend(
            char for char in data
            if unicodedata.category(char) in {"Sm", "No"}
            or "\u0370" <= char <= "\u03ff"
            or char in "ΓΔΩΘℕℤℚℝ∅"
        )


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
assert lessons[0]["chapters"][1]["status"] == "ready"
assert lessons[0]["chapters"][1]["url"] == "chapters/d_sets.html"
assert lessons[0]["chapters"][2]["status"] == "ready"
assert lessons[0]["chapters"][2]["url"] == "chapters/d_proof.html"
assert lessons[0]["chapters"][3]["status"] == "ready"
assert lessons[0]["chapters"][3]["url"] == "chapters/d_induction.html"
assert lessons[0]["chapters"][4]["status"] == "ready"
assert lessons[0]["chapters"][4]["url"] == "chapters/a_model.html"
for chapter_id in ("d_logic", "d_sets", "d_proof", "d_induction", "a_model"):
    chapter_html = (ROOT / "chapters" / f"{chapter_id}.html").read_text(encoding="utf-8")
    text_without_diagrams = re.sub(r"<(?:svg|math)\b.*?</(?:svg|math)>", "", chapter_html, flags=re.S)
    assert not re.search(r"[₀-₉₊₋ₙₖᵢ⁰-⁹⁺⁻ⁿʲᵏᵗᴺⁱ]", text_without_diagrams), chapter_id
    assert "class\u2009=\u2009" not in chapter_html, chapter_id
    coverage = MathCoverage()
    coverage.feed(chapter_html)
    assert not coverage.unstyled, (chapter_id, coverage.unstyled)
    assert coverage.styled_runs >= 100, (chapter_id, coverage.styled_runs)
chapter_css = (ROOT / "chapters" / "chapter.en.css").read_text(encoding="utf-8")
assert 'font-family:"STIX Two Math"' in chapter_css
assert 'font-family:"Math Glyphs"' in chapter_css
assert '.logic-diagram svg text,.logic-diagram svg tspan{font-family:"STIX Two Math"' in chapter_css
for font_name in ("newsreader-latin.woff2", "source-sans-3-latin.woff2", "stix-two-math.woff2"):
    font_path = ROOT / "fonts" / font_name
    assert font_path.is_file() and font_path.read_bytes()[:4] == b"wOF2", font_path
for license_name in ("OFL-Newsreader.txt", "OFL-SourceSans3.txt", "OFL-STIXTwoMath.txt"):
    assert (ROOT / "fonts" / license_name).is_file(), license_name
assert not arabic, arabic
assert not missing, missing
print(f"English site checks passed: {len(pages)} HTML pages; local links, IELTS stages, hours, chapter status, and math-index typography.")

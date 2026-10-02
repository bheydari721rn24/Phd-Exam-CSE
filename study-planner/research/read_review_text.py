"""Print bounded manuscript text, preserving sub/superscript grouping."""
from pathlib import Path
import re, html, sys

path = Path(sys.argv[1])
text = path.read_text(encoding="utf-8")
text = text.replace('<sub>', '_{').replace('</sub>', '}')
text = text.replace('<sup>', '^{').replace('</sup>', '}')
text = re.sub(r'<span class="overline">(.*?)</span>', r'conj(\1)', text, flags=re.S)
text = re.sub(r"<svg\b.*?</svg>", "[SVG inspected separately]", text, flags=re.S)
text = html.unescape(re.sub(r"</?(?:span|div|figure|figcaption|table|thead|tbody|tr|th|td|details|summary|p|ul|ol|li|strong|em|code|pre|a|br|h[1-6]|section|aside|blockquote)\b[^>]*>", "", text))
start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
end = int(sys.argv[3]) if len(sys.argv) > 3 else len(text)
print(f"{path}: plain characters {start}:{min(end,len(text))}; total {len(text)}")
print(text[start:end])

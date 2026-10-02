from pathlib import Path
from markdown_it import MarkdownIt
root=Path(__file__).resolve().parents[1]
md=(root/'research/LIBRARY_FINAL_REVIEW.en.md').read_text(encoding='utf-8')
body=MarkdownIt('commonmark',{'html':True}).enable('table').render(md)
body=body.replace('<h1>Existing chapter library: final review</h1>','')
html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Library Review · Doctoral CSE 1406</title><link rel="stylesheet" href="chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="index.html#library">← Back to the chapter library</a></p><header class="hero"><p class="eyebrow">Library revision · 2 October 2026</p><h1>Existing chapters: final review</h1><p>16 chapters · 446 worked problems · 29 figures</p></header><article class="lesson">{body}</article></main></body></html>'''
(root/'dist/library-review.html').write_text(html,encoding='utf-8')
print('Rendered the final review report.')

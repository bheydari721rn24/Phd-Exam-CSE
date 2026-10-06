from pathlib import Path
B=Path(__file__).parent;s=(B/'qa_a_stackqueue_browser.py').read_text(encoding='utf-8')
s=s[:s.index(" report['counts']")].replace('a_stackqueue','a_sort').replace('a-stackqueue','a-sort').replace('sqLoaded','sortLoaded')
s+=(B/'a_sort_browser_body.py.txt').read_text(encoding='utf-8')
(B/'qa_a_sort_browser.py').write_text(s,encoding='utf-8')

"""Replace legacy approved-state assertions after the user's library rejection."""
from pathlib import Path
p=Path(__file__).with_name('check_site_en.py');s=p.read_text()
start=s.index('assert lessons[0]');end=s.index('for chapter_id in (',start)
s=s[:start]+'''chapters = [c for w in lessons for c in w['chapters']]
assert len(chapters) == 22
assert all(c['status'] == 'draft' and c['revisionState'] == 'rewritten_draft' for c in chapters)
assert all(c['url'] == 'chapters/' + c['topicId'] + '.html' for c in chapters)
'''+s[end:]
start=s.index('for chapter_id in (');end=s.index(':',start)
s=s[:start]+"for chapter_id in [c['topicId'] for c in chapters]"+s[end:]
p.write_text(s)
print('Site checker now validates all 22 rejected-and-revised chapters as drafts.')

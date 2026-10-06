from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json
R=Path(__file__).resolve().parents[1];D=R/'dist'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=set()
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.add(a['id'])
  for k in ['src','href']:
   if k in a:self.links.append(a[k])
count=0
for p in [D/'chapters/s_descriptive.html',D/'reviews/s_descriptive-sources.html',D/'reviews/s_descriptive-quality.html']:
 pg=Page();pg.feed(p.read_text(encoding='utf-8'))
 for href in pg.links:
  u=urlsplit(href)
  if u.scheme or u.netloc:continue
  target=(p.parent/unquote(u.path)).resolve() if u.path else p
  assert target.is_relative_to(D.resolve()) and target.is_file(),(p,href)
  if u.fragment and target.suffix=='.html':
   if target==D/'index.html' and u.fragment.startswith('week-'):
    app=(D/'app.en.js').read_text();assert 'location.hash.match(/^#week-' in app;count+=1;continue
   other=Page();other.feed(target.read_text(encoding='utf-8'));assert unquote(u.fragment) in other.ids,(p,href)
  count+=1
(R/'research/s_descriptive-evidence/local-links.json').write_text(json.dumps(dict(status='passed',internalReferences=count),indent=2)+'\n')
print(f'{count} internal links and assets passed.')

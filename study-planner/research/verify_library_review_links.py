from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='a' and 'href' in a:self.links.append(a['href'])
R=Path(__file__).resolve().parents[1];d=R/'dist';s=(d/'library-visual-question-review.html').read_text(encoding='utf-8');p=Links();p.feed(s)
assert s.count('<tr>')==36
for v in p.links:
 if not v.startswith(('http','#')):assert (d/unquote(v.split('#')[0])).exists(),v
print('Review page: 35 chapter rows; every local link exists.')

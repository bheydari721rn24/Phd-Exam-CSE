"""Cache primary written sources outside the repository for a reproducible review."""
from pathlib import Path
import sys, tempfile, json, hashlib, urllib.request, logging
logging.getLogger('pypdf').setLevel(logging.ERROR)
sys.path.insert(0,str(Path(tempfile.gettempdir())/'phd-study-pydeps'))
from pypdf import PdfReader
from html.parser import HTMLParser
OUT=Path(tempfile.gettempdir())/'p_types_sources'; OUT.mkdir(exist_ok=True)
SOURCES={
 'stanford': 'https://web.stanford.edu/class/archive/cs/cs107/cs107.1204/lectures/2/Lecture2.pdf',
 'cmu': 'https://www.cs.cmu.edu/~rjsimmon/15122-f14/lec/03-ints.pdf',
 'mit': 'https://live.ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/e921a690079369751bcce3e34da6c6ee_MIT6_0001F16_Lec1.pdf',
 'standard':'https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf',
 'harvard':'https://cs50.harvard.edu/x/2025/notes/1/',
 'berkeley':'https://notes.cs61c.org/content/c-basics/c-variables/',
 'berkeley-syntax':'https://notes.cs61c.org/content/c-basics/c-syntax/',
 'princeton':'https://introcs.cs.princeton.edu/java/12types/',
 'cmu213':'https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15213-f04/lectures/class03.pdf',
}
class Text(HTMLParser):
 def __init__(self): super().__init__(); self.parts=[]; self.hide=0
 def handle_starttag(self,tag,attrs):
  if tag in ('script','style'): self.hide+=1
 def handle_endtag(self,tag):
  if tag in ('script','style'): self.hide-=1
  if tag in ('p','h1','h2','h3','li','pre','tr'): self.parts.append('\n')
 def handle_data(self,data):
  if not self.hide: self.parts.append(data)
manifest=[]
for key,url in SOURCES.items():
 suffix='.pdf' if url.endswith('.pdf') else '.html'; path=OUT/(key+suffix)
 if not path.exists():
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
  try: path.write_bytes(urllib.request.urlopen(req,timeout=25).read())
  except Exception as exc:
   manifest.append({'key':key,'url':url,'error':type(exc).__name__}); continue
 if suffix=='.pdf':
  reader=PdfReader(path); pages=[p.extract_text() or '' for p in reader.pages]
  (OUT/(key+'.pages.json')).write_text(json.dumps(pages,ensure_ascii=False),encoding='utf-8')
  content='\n\n'.join(f'PDF page {i+1}\n{p}' for i,p in enumerate(pages))
 else:
  parser=Text(); parser.feed(path.read_text(encoding='utf-8')); content=''.join(parser.parts)
 (OUT/(key+'.txt')).write_text(content,encoding='utf-8')
 manifest.append({'key':key,'url':url,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'pages':len(pages) if suffix=='.pdf' else None})
(OUT/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(OUT); print(json.dumps(manifest,indent=2))

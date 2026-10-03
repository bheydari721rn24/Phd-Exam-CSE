"""Cache written sources outside the published site; do not call downloads reading."""
import concurrent.futures,hashlib,json,re,tempfile
from pathlib import Path
from urllib.parse import urljoin
from html.parser import HTMLParser
import requests
from pypdf import PdfReader
BASE=Path(__file__).resolve().parent;CACHE=Path(tempfile.gettempdir())/'phd-conditional-sources';CACHE.mkdir(exist_ok=True)
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[]
 def handle_starttag(self,tag,attrs):
  if tag=='a':
   d=dict(attrs)
   if d.get('href'):self.links.append(d['href'])
sources=[
 ('mit-conditioning','MIT','https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/resources/mit6_041scf13_l02/','landing'),
 ('mit-independence','MIT','https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/resources/mit6_041scf13_l03/','landing'),
 ('stanford-conditional','Stanford','https://chrispiech.github.io/probabilityForComputerScientists/en/part1/cond_prob/','html'),
 ('stanford-independence','Stanford','https://chrispiech.github.io/probabilityForComputerScientists/en/part1/independence/','html'),
 ('stanford-chain','Stanford','https://chrispiech.github.io/probabilityForComputerScientists/en/part1/prob_and/','html'),
 ('harvard-practice2','Harvard','https://stat110.hsites.harvard.edu/sites/g/files/omnuum10111/files/stat110/files/strategic_practice_and_homework_2.pdf','pdf'),
 ('cmu-events','CMU','https://www.cs.cmu.edu/~harchol/Probability/chapters/chpt2.pdf','pdf'),
 ('berkeley-lecture2','Berkeley','https://www.stat.berkeley.edu/~aldous/134/lecture2.pdf','pdf'),
 ('berkeley-lecture3','Berkeley','https://www.stat.berkeley.edu/~aldous/134/lecture3.pdf','pdf'),
 ('oxford-applied','Oxford','https://www.stats.ox.ac.uk/~winkel/bs3a07.pdf','pdf'),
 ('cambridge-probability','Cambridge','https://www.statslab.cam.ac.uk/~rrw1/prob/prob.pdf','pdf')]
def fetch(item):
 id,university,url,kind=item
 try:
  r=requests.get(url,timeout=35);r.raise_for_status();original=url
  if kind=='landing':
   links=Links();links.feed(r.text);url=urljoin(url,next(s for s in links.links if s.lower().endswith('.pdf')));r=requests.get(url,timeout=35);r.raise_for_status();kind='pdf'
  p=CACHE/(id+'.'+kind);p.write_bytes(r.content);row=dict(id=id,university=university,url=url,landing=original,path=str(p),sha256=hashlib.sha256(r.content).hexdigest(),bytes=len(r.content),readingState='acquired_not_yet_reviewed')
  if kind=='pdf':
   pdf=PdfReader(p);row['pages']=len(pdf.pages)
   (CACHE/(id+'.txt')).write_text('\n\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+(pg.extract_text() or '') for i,pg in enumerate(pdf.pages)),encoding='utf-8')
  return row
 except Exception as e:return dict(id=id,university=university,url=url,error=str(e),readingState='unavailable')
rows=list(concurrent.futures.ThreadPoolExecutor(max_workers=6).map(fetch,sources))
ledger=BASE/'s_conditional-source-downloads.json'
previous={r['id']:r for r in json.loads(ledger.read_text())} if ledger.exists() else {}
for row in rows:
    old=previous.get(row['id'],{})
    if row.get('sha256') and row['sha256']==old.get('sha256') and 'reviewed' in old.get('readingState',''):
        for key in ['readingState','reviewedPdfPages']:
            if key in old:row[key]=old[key]
(BASE/'s_conditional-source-downloads.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps([{k:r[k] for k in ['id','pages','error','url'] if k in r} for r in rows],indent=2))

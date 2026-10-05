"""Cache official written sources privately and extract numbered pages for review."""
from pathlib import Path
import requests,json,hashlib,tempfile
from pypdf import PdfReader
import html,re
B=Path(__file__).resolve().parent;C=Path(tempfile.gettempdir())/'phd-discrete-counting-sources';C.mkdir(exist_ok=True)
sources={
'mit':'https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf',
'berkeley':'https://www.su19.eecs70.org/static/notes/n12.pdf',
'berkeley-advanced':'https://www.su19.eecs70.org/static/notes/n12.5.pdf',
'stanford':'https://web.stanford.edu/class/archive/cs/cs109/cs109.1206/lectureNotes/LN02_combinatorics.pdf',
'stanford-basic':'https://web.stanford.edu/class/archive/cs/cs109/cs109.1206/lectureNotes/LN01_counting.pdf',
'cmu':'https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15251-f10/Site/Materials/Lectures/Lecture07/lecture07.pdf',
'cmu-advanced':'https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15251-f10/Site/Materials/Lectures/Lecture08/lecture08.pdf',
'cornell':'https://www.cs.cornell.edu/courses/cs2800/2017fa/lectures/lec16-combinatorics.html',
}
rows=[]
for key,url in sources.items():
 try:
  ext='.pdf' if url.endswith('.pdf') else '.html';p=C/(key+ext)
  if not p.exists():r=requests.get(url,timeout=40);r.raise_for_status();p.write_bytes(r.content)
  if ext=='.pdf':
   reader=PdfReader(p);pages=[page.extract_text() or '' for page in reader.pages]
   text='\n'.join('\n=== PDF PAGE '+str(i+1)+' ===\n'+v for i,v in enumerate(pages))
  else:pages=[html.unescape(re.sub('<[^>]+>',' ',p.read_text(encoding='utf-8')))];text=pages[0]
  (C/(key+'.txt')).write_text(text,encoding='utf-8')
  rows.append(dict(key=key,url=url,path=str(p),textPath=str(C/(key+'.txt')),pages=len(pages),sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
  print(key,len(pages),'pages',len(text),'characters',flush=True)
 except Exception as e:rows.append(dict(key=key,url=url,error=str(e)));print(key,'unavailable',str(e),flush=True)
(B/'d_counting-source-downloads.json').write_text(json.dumps(rows,indent=2)+'\n')

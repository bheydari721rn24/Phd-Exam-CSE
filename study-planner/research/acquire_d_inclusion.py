from pathlib import Path
import requests,hashlib,json,concurrent.futures
import fitz
B=Path(__file__).resolve().parent;C=Path('C:/Users/bheydari/AppData/Local/Temp/phd-inclusion-sources');C.mkdir(exist_ok=True)
sources={
 'cornell':'https://www.cs.cornell.edu/courses/cs2800/2016sp/handouts/pass_tseng_discmath.pdf',
 'oxford':'https://www.cs.ox.ac.uk/andrew.ker/docs/discretemaths-lecture-notes-mt2010.pdf',
 'cmu':'https://www.math.cmu.edu/users/math/mtait/301/Notes.pdf',
 'berkeley':'https://sp20.eecs70.org/static/notes/n14.pdf',
 'stanford':'https://web.stanford.edu/class/archive/cs/cs109/cs109.1206/lectureNotes/LN01_counting.pdf'}
def get(pair):
 key,url=pair;p=C/(key+'.pdf')
 try:
  if not p.exists():r=requests.get(url,timeout=35);r.raise_for_status();assert r.content.startswith(b'%PDF');p.write_bytes(r.content)
  doc=fitz.open(p);text='\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+page.get_text() for i,page in enumerate(doc));(C/(key+'.txt')).write_text(text,encoding='utf-8')
  return dict(key=key,url=url,pages=len(doc),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),cache=str(p))
 except Exception as ex:return dict(key=key,url=url,error=str(ex))
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:a=list(pool.map(get,sources.items()))
p=Path('C:/Users/bheydari/AppData/Local/Temp/phd-invariants-sources/mit.pdf');d=fitz.open(p);(C/'mit.txt').write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+page.get_text() for i,page in enumerate(d)),encoding='utf-8');a.append(dict(key='mit',url='https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf',pages=len(d),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),cache=str(p),access='Existing original cached course PDF'))
(B/'d_inclusion-downloads.json').write_text(json.dumps(a,indent=2)+'\n');print(json.dumps(a,indent=2))

"""Cache official written sources outside the published checkout."""
import requests,re,html,json,hashlib,tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from pypdf import PdfReader
OUT=Path(tempfile.gettempdir())/'phd-gauss-sources';OUT.mkdir(exist_ok=True)
URLS={
 'mit':'https://ocw.mit.edu/courses/18-700-linear-algebra-fall-2013/b144082f6883d02faeec26d7f708c63e_MIT18_700F13_gauss.pdf',
 'cmu1':'https://www.math.cmu.edu/~wgunther/241/m14/notes/week1/1.pdf',
 'cmu2':'https://www.math.cmu.edu/~wgunther/241/m14/notes/week1/2.pdf',
 'cmu8':'https://www.math.cmu.edu/~wgunther/241/m14/notes/week2/8.pdf',
 'berkeley':'https://math.berkeley.edu/~apaulin/Systems%20of%20Linear%20Equations.pdf',
 'oxford':'https://courses.maths.ox.ac.uk/pluginfile.php/25471/mod_folder/content/0/lecture_notes22.pdf?forcedownload=1',
 'stanford-index':'https://web.stanford.edu/class/math114/pages/modules.html',
 'stanford-home':'https://web.stanford.edu/class/math114/',
 'stanford-ge1':'https://web.stanford.edu/class/math114/decks/linear_systems/gauss_elim21.html',
 'stanford-ge3':'https://web.stanford.edu/class/math114/decks/linear_systems/gauss_elim37.html',
 'stanford-lu1':'https://web.stanford.edu/class/math114/decks/linear_systems/lu_factorization.html',
}
def fetch(pair):
 name,url=pair
 try:
  r=requests.get(url,timeout=25);r.raise_for_status();data=r.content
  pdf=data.startswith(b'%PDF');path=OUT/(name+('.pdf' if pdf else '.html'));path.write_bytes(data)
  if pdf:
   reader=PdfReader(path);texts=[p.extract_text() or '' for p in reader.pages]
   (OUT/(name+'.txt')).write_text('\n\n'.join(f'PDF PAGE {i+1}\n{t}' for i,t in enumerate(texts)),encoding='utf-8')
  else:
   s=re.sub(r'<(script|style)\b[^>]*>[\s\S]*?</\1>','',r.text)
   (OUT/(name+'.txt')).write_text(html.unescape(re.sub('<[^>]*>',' ',s)),encoding='utf-8')
  return dict(id=name,url=url,sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),cache=str(path),pages=len(reader.pages) if pdf else None)
 except Exception as e:return dict(id=name,url=url,error=str(e))
if __name__=='__main__':
 with ThreadPoolExecutor(max_workers=6) as pool:results=list(pool.map(fetch,URLS.items()))
 (OUT/'acquisition.json').write_text(json.dumps(results,indent=2)+'\n')
 for x in results:print(x)
 s=(OUT/'stanford-index.html').read_text()
 print('MODULE LINKS',[(re.sub('<[^>]*>',' ',txt),u) for u,txt in re.findall(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>',s,re.S) if any(w in txt.lower() for w in ['gauss','factor','permut','pivot'])])
 print('HOME', (OUT/'stanford-home.txt').read_text()[-12000:])

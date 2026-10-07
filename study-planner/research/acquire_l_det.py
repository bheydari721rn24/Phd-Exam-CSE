from pathlib import Path
import requests,fitz,json,hashlib,re,tempfile,concurrent.futures
R=Path(__file__).resolve().parents[1];E=R/'research/l_det-evidence';CACHE=Path(tempfile.gettempdir())/'l-det-sources';CACHE.mkdir(exist_ok=True)
urls={
 'oxford':'https://courses.maths.ox.ac.uk/mod/resource/view.php?id=61510',
 'berkeley':'https://math.berkeley.edu/~apaulin/Determinants.pdf',
 'mit-properties':'https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/5dd3f8ec0a398fd74264fef3fd591f81_MIT18_06SCF11_Ses2.5sum.pdf',
 'harvard':'https://people.math.harvard.edu/~knill/teaching/math21b2023/handouts/lecture14.pdf',
 'cmu-advertised':'https://www.math.cmu.edu/~wgunther/241/m14/notes/week3/12.pdf',
 'eth-hosted':'https://people.math.ethz.ch/~halorenz/4students/linalg/linalgln.pdf',
 'stanford-sumo':'https://sumo.stanford.edu/pdfs/LinearAlgebraNotes.pdf'}
pages={
 'mit-cofactors':'https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/least-squares-determinants-and-eigenvalues/determinant-formulas-and-cofactors/',
 'mit-cramer':'https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/pages/least-squares-determinants-and-eigenvalues/cramers-rule-inverse-matrix-and-volume/'}
for name,url in pages.items():
 resp=requests.get(url,timeout=45);resp.raise_for_status();(CACHE/(name+'.html')).write_text(resp.text,encoding='utf-8')
 pdfs=re.findall(r'href="([^"<>]+\.pdf)"',resp.text)
 for pdf in dict.fromkeys(pdfs):
  if 'sum.pdf' in pdf:urls[name]=requests.compat.urljoin(url,pdf);break
def get(pair):
 name,url=pair
 try:
  resp=requests.get(url,timeout=90);resp.raise_for_status();assert resp.content.startswith(b'%PDF'),resp.headers.get('Content-Type')
  path=CACHE/(name+'.pdf');path.write_bytes(resp.content);doc=fitz.open(path)
  text=''.join('\n\n--- PDF PAGE '+str(i+1)+' ---\n'+p.get_text()for i,p in enumerate(doc));(CACHE/(name+'.txt')).write_text(text,encoding='utf-8')
  return dict(id=name,url=url,finalUrl=resp.url,pages=len(doc),sha256=hashlib.sha256(resp.content).hexdigest(),bytes=len(resp.content),cachePath=str(path),textCharacters=len(text))
 except Exception as e:return dict(id=name,url=url,error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=6)as pool:result=list(pool.map(get,urls.items()))
(E/'acquisition.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

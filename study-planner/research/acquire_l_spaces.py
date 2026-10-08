from pathlib import Path
import requests,fitz,json,hashlib,concurrent.futures
B=Path(__file__).resolve().parent;E=B/'l_spaces-evidence';C=Path('C:/Users/bheydari/AppData/Local/Temp/l-spaces-sources');C.mkdir(exist_ok=True)
urls={
'oxford':'https://courses.maths.ox.ac.uk/pluginfile.php/25471/mod_folder/content/0/lecture_notes22.pdf?forcedownload=1',
'mit-summary':'https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/0bbc30e3f1d7933ea07a2d2e9ab050d9_MIT18_06SCF11_Ses1.9sum.pdf',
'mit-problems':'https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/562c31026033b44a05491b57834a5a0e_MIT18_06SCF11_Ses1.9prob.pdf',
'mit-solutions':'https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/793cbea8c118cf3b30ba2944a5c61dee_MIT18_06SCF11_Ses1.9sol.pdf',
'cmu-abstract':'https://www.math.cmu.edu/~wgunther/241/m14/notes/week5/22.pdf',
'cmu-bases':'https://www.math.cmu.edu/~wgunther/241/m14/notes/week6/23.pdf',
'berkeley-spaces':'https://math.berkeley.edu/~apaulin/Vector%20Spaces%20and%20Linear%20Transformations.pdf',
'berkeley-subspaces':'https://math.berkeley.edu/~apaulin/Subspaces,%20Kernels%20and%20Ranges.pdf',
'berkeley-bases':'https://math.berkeley.edu/~apaulin/Spanning,%20Linear%20Independence%20and%20Dimension.pdf',
'berkeley-coordinates':'https://math.berkeley.edu/~apaulin/Bases%20and%20Coordinate%20Systems.pdf',
'eth':'https://ti.inf.ethz.ch/ew/courses/LA24/notes_part_I.pdf',
'stanford':'https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/lin-alg2.pdf',
'harvard':'https://people.math.harvard.edu/~knill/teaching/math21b2023/handouts/lecture04.pdf'}
def get(kv):
 k,u=kv;p=C/(k+'.pdf')
 try:
  if not p.exists():
   r=requests.get(u,timeout=75);r.raise_for_status();assert r.content.startswith(b'%PDF');p.write_bytes(r.content)
  d=fitz.open(p);(C/(k+'.txt')).write_text('\n\n'.join('PDF PAGE '+str(i+1)+'\n'+x.get_text()for i,x in enumerate(d)),encoding='utf-8')
  return dict(id=k,url=u,pages=len(d),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),cachePath=str(p))
 except Exception as ex:return dict(id=k,url=u,error=str(ex))
with concurrent.futures.ThreadPoolExecutor(max_workers=8)as pool:a=list(pool.map(get,urls.items()))
(E/'acquisition.json').write_text(json.dumps(a,indent=2)+'\n');print(json.dumps(a,indent=2))
# External read-only source page renders remain outside the publication repository.
images=C/'reading-images';images.mkdir(exist_ok=True)
for k,pgs in {'cmu-bases':[2,3],'berkeley-spaces':[0,1,2,3],'berkeley-subspaces':[0,1,2,3],'berkeley-bases':[0,1,2,3],'berkeley-coordinates':[0,1,2,3]}.items():
 p=C/(k+'.pdf')
 if p.exists():
  d=fitz.open(p)
  for i in pgs:d[i].get_pixmap(matrix=fitz.Matrix(1.3,1.3)).save(images/(k+'-'+str(i+1)+'.png'))

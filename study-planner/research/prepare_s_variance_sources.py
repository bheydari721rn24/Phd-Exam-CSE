from pathlib import Path
import json,hashlib,requests,fitz
B=Path(__file__).resolve().parent;C=Path('C:/Users/bheydari/AppData/Local/Temp/s-variance-sources');C.mkdir(exist_ok=True);E=B/'s_variance-evidence';E.mkdir(exist_ok=True)
urls={'cmu4':'https://www.stat.cmu.edu/~siva/teaching/700/lec4.pdf','berkeley17':'https://fa16.eecs70.org/static/notes/n17.pdf','eth':'https://people.math.ethz.ch/~ziegelj/WTSkript.pdf','cambridge':'https://www.cl.cam.ac.uk/teaching/2425/IntroProb/slides/07-covariance-all-handout.pdf'}
rows=[]
for name,url in urls.items():
 p=C/(name+'.pdf')
 try:
  if not p.exists():
   r=requests.get(url,timeout=(10,35));r.raise_for_status();assert r.content[:4]==b'%PDF';p.write_bytes(r.content)
  d=fitz.open(p);(C/(name+'.txt')).write_text('\n'.join('PAGE '+str(i+1)+'\n'+x.get_text()for i,x in enumerate(d)),encoding='utf-8');row=dict(name=name,url=url,pages=len(d),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),status='cached_not_automatically_read')
 except Exception as ex:row=dict(name=name,url=url,status='acquisition_failed',error=str(ex))
 rows.append(row);print(json.dumps(row))
(E/'acquisition.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')

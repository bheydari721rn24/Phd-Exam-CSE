from pathlib import Path
import requests,fitz,json,hashlib,concurrent.futures
R=Path(__file__).resolve().parents[1];O=R/'research/s_discrete-evidence';C=Path('C:/Users/bheydari/AppData/Local/Temp/s-discrete-sources');C.mkdir(exist_ok=True)
rows=[('mit','MIT 18.05, Jeremy Orloff and Jonathan Bloom','https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/mit18_05_s22_probability.pdf'),('berkeley','UC Berkeley CS70, Fall 2016','https://www.eecs70.org/assets/pdf/notes/n16.pdf'),('berkeley16','UC Berkeley CS70, Fall 2016','https://www.eecs70.org/static/notes/n16.pdf'),('berkeley-archive','UC Berkeley CS70, Fall 2016','https://www-inst.eecs.berkeley.edu/~cs70/fa16/notes/n16.pdf'),('stanford','Stanford CS109, Chris Piech, Winter 2025','https://web.stanford.edu/class/archive/cs/cs109/cs109.1254/lectures/6-RandomVariables/6-RandomVariables.pdf'),('oxford','Oxford Prelims Probability, James Martin, 2019','https://courses.maths.ox.ac.uk/mod/resource/view.php?id=48553'),('harvard','Harvard Statistics 110, Joe Blitzstein, 2011','https://stat110.hsites.harvard.edu/sites/g/files/omnuum10111/files/stat110/files/strategic_practice_and_homework_4.pdf'),('cmu-index','Carnegie Mellon 36-225, Jing Lei, 2012','https://stat.cmu.edu/~jinglei/syllabus_f12.pdf')]
def get(row):
 id,course,url=row
 try:
  r=requests.get(url,timeout=45);r.raise_for_status();assert r.content.startswith(b'%PDF')
  p=C/(id+'.pdf');p.write_bytes(r.content);d=fitz.open(p);(C/(id+'.txt')).write_text('\n'.join('PDF PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(d)),encoding='utf-8')
  return dict(id=id,course=course,url=url,path=str(p),pages=len(d),sha256=hashlib.sha256(r.content).hexdigest(),status='acquired_not_reviewed')
 except Exception as e:return dict(id=id,course=course,url=url,status='unavailable',error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:out=list(ex.map(get,rows))
(O/'acquisition.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps([{k:v for k,v in x.items() if k not in ['sha256','path','course']} for x in out]))

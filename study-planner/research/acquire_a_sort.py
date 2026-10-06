from pathlib import Path
import requests,fitz,hashlib,json,concurrent.futures,tempfile
B=Path(__file__).resolve().parent;D=Path(tempfile.gettempdir())/'a-sort-sources';D.mkdir(exist_ok=True)
sources={
 'mit3':'https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/6d1ae5278d02bbecb5c4428928b24194_MIT6_006S20_lec3.pdf',
 'mit5':'https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/78a3c3444de1ff837f81e52991c24a86_MIT6_006S20_lec5.pdf',
 'mitr5':'https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/cda4cc0c0e626bfbd30bc15fb78c3994_MIT6_006S20_r05.pdf',
 'oxford':'https://www.robots.ox.ac.uk/~vedaldi/assets/teach/2024/b16/b16-notes.pdf',
 'princeton21':'https://www.cs.princeton.edu/courses/archive/spring26/cos226/lectures/21ElementarySorts.pdf',
 'princeton22':'https://www.cs.princeton.edu/courses/archive/spring26/cos226/lectures/22Mergesort.pdf',
 'princeton23':'https://www.cs.princeton.edu/courses/archive/spring26/cos226/lectures/23Quicksort.pdf',
 'princeton24':'https://www.cs.princeton.edu/courses/archive/spring26/cos226/lectures/24PriorityQueues.pdf',
 'stanfordproof':'https://cs161-stanford.github.io/assets/Lectures/Lecture2/CS161Lecture02_handout.pdf',
 'stanford5':'https://cs161-stanford.github.io/assets/Lectures/Lecture5/Lecture5-compressed.pdf',
 'stanford6':'https://cs161-stanford.github.io/assets/Lectures/Lecture6/Lecture6-compressed.pdf',
 'cmu7':'https://www.cs.cmu.edu/~15122-archive/s26/handouts/lectures/07-quicksort.pdf'}
def get(t):
 k,u=t;p=D/(k+'.pdf')
 try:
  if not p.exists():r=requests.get(u,timeout=35);r.raise_for_status();p.write_bytes(r.content)
  d=fitz.open(p);s='\n'.join('\n--- PDF page '+str(i+1)+' ---\n'+q.get_text() for i,q in enumerate(d));(D/(k+'.txt')).write_text(s,encoding='utf-8')
  return dict(id=k,url=u,path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),pages=len(d),state='acquired_not_yet_read')
 except Exception as e:return dict(id=k,url=u,state='download_failed',reason=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:a=list(ex.map(get,sources.items()))
(B/'a_sort-downloads.json').write_text(json.dumps(a,indent=2)+'\n',encoding='utf-8')
print(json.dumps(a,indent=2))

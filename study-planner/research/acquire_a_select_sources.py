"""Acquire public primary texts; no acquisition is counted as a completed reading."""
from pathlib import Path
import requests,json,hashlib,concurrent.futures,tempfile,re
import fitz
B=Path(__file__).resolve().parent;O=B/'a_select-evidence';T=Path(tempfile.gettempdir())/'a-select-sources';T.mkdir(exist_ok=True)
S=[
 ('mit','MIT','6.046J, Spring 2015; Erik Demaine, Srini Devadas, Nancy Lynch','https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/7463c413c944ed72b46a3c3d02b49448_MIT6_046JS15_lec02.pdf'),
 ('stanford','Stanford','CS161, Winter 2023; Moses Charikar and Nima Anari','https://stanford-cs161.github.io/winter2023/assets/files/lecture4-notes.pdf'),
 ('stanford-checks','Stanford','CS161 Winter 2023, selection concept checks','https://stanford-cs161.github.io/winter2023-bank/select.pdf'),
 ('cmu','Carnegie Mellon','15-451, Fall 2024, Introduction and Linear-time Selection','https://www.cs.cmu.edu/~15451-f24/lectures/lecture01-selection.pdf'),
 ('princeton','Princeton','COS226, Spring 2025; Robert Sedgewick and Kevin Wayne, slide authors','https://www.cs.princeton.edu/courses/archive/spring25/cos226/lectures/23Quicksort.pdf'),
 ('princeton-search','Princeton','Introduction to Programming, Robert Sedgewick and Kevin Wayne, §4.2','https://introcs.cs.princeton.edu/java/42sort/'),
 ('cornell','Cornell','CS4820, Spring 2024, February 28 randomized median notes','https://www.cs.cornell.edu/courses/cs4820/2024sp/notes/16_Median.pdf'),
 ('cornell-two','Cornell','CS4820, Spring 2024, March 1 analysis of randomized median','https://www.cs.cornell.edu/courses/cs4820/2024sp/notes/17_Median.pdf'),
 ('berkeley','UC Berkeley','CS170 assigned DPV textbook, Chapter 2','https://people.eecs.berkeley.edu/~vazirani/algorithms/chap2.pdf'),
 ('oxford','Oxford','B16 2024–25 v2.1; Andrea Vedaldi','https://www.robots.ox.ac.uk/~vedaldi/assets/teach/2024/b16/b16-notes.pdf'),
 ('uci','UC Irvine','ICS161, David Eppstein, January 25, 1996, Selection and order statistics','https://ics.uci.edu/~eppstein/161/960125.html'),
 ('cmu-two','Carnegie Mellon','15-451, Fall 2005, Homework 2, median of two sorted arrays','https://www.cs.cmu.edu/afs/cs/academic/class/15451-f05/www/assignments/hwk2.pdf')]
def get(s):
 id,univ,course,url=s
 try:
  r=requests.get(url,timeout=45);r.raise_for_status();pdf=r.content.startswith(b'%PDF');path=T/(id+('.pdf' if pdf else '.html'));path.write_bytes(r.content)
  row=dict(id=id,university=univ,course=course,url=url,path=str(path),sha256=hashlib.sha256(r.content).hexdigest(),status='acquired_not_yet_reviewed')
  if pdf:
   doc=fitz.open(path);row['pages']=len(doc);(T/(id+'.txt')).write_text('\n'.join(f'\n--- PDF PAGE {i+1} ---\n'+p.get_text() for i,p in enumerate(doc)),encoding='utf-8')
  else:
   from lxml import html
   tree=html.fromstring(r.content);(T/(id+'.txt')).write_text(tree.text_content(),encoding='utf-8')
  return row
 except Exception as ex:return dict(id=id,university=univ,course=course,url=url,status='unavailable',error=str(ex))
rows=list(concurrent.futures.ThreadPoolExecutor(max_workers=6).map(get,S));(O/'acquisition.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8');print(json.dumps([{k:r.get(k) for k in ['id','status','pages','error']} for r in rows]))

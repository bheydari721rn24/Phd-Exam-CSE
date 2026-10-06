from pathlib import Path
import requests,hashlib,json,tempfile,concurrent.futures
import fitz
from html.parser import HTMLParser
class TextParser(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.hidden=0
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.hidden+=1
  if t in ['p','div','h1','h2','h3','li','tr']:self.parts.append('\n')
 def handle_endtag(self,t):
  if t in ['script','style']:self.hidden=max(0,self.hidden-1)
 def handle_data(self,d):
  if not self.hidden:self.parts.append(d)
B=Path(__file__).resolve().parent;T=Path(tempfile.gettempdir())/'s-descriptive-sources';T.mkdir(exist_ok=True)
S=[
('berkeley-location','UC Berkeley','SticiGui, Philip B. Stark, Chapter 4','https://www.stat.berkeley.edu/~stark/SticiGui/Text/location.htm'),
('berkeley-correlation','UC Berkeley','SticiGui, Philip B. Stark, Chapter 8','https://www.stat.berkeley.edu/~stark/SticiGui/Text/computeR.htm'),
('mit','MIT','15.075J Fall 2011, Cynthia Rudin et al.; Chapter 4','https://ocw.mit.edu/courses/15-075j-statistical-thinking-and-data-analysis-fall-2011/e8d615e72bb6d384e34fc2a10a8f03cb_MIT15_075JF11_chpt04.pdf'),
('stanford-center','Stanford','STATS60 Spring 2026, Michael Howes and Tselil Schramm; Lecture 5','https://web.stanford.edu/class/stats60/lectures/05-lecture-mean.html'),
('stanford-spread','Stanford','STATS60 Spring 2026; Lecture 7','https://web.stanford.edu/class/stats60/lectures/07-lecture-variability.html'),
('stanford-robust','Stanford','STATS60 Spring 2026; Lecture 8','https://web.stanford.edu/class/stats60/lectures/08-lecture-robustness.html'),
('stanford-visual','Stanford','STATS60 Spring 2026; Lecture 6','https://web.stanford.edu/class/stats60/lectures/06-lecture-data-viz.html'),
('cmu','Carnegie Mellon','36-309, Howard Seltman, Experimental Design and Analysis Chapter 4','https://www.stat.cmu.edu/~hseltman/309/Book/chapter4.pdf'),
('oxford','Oxford','IAUL and Department of Statistics, Descriptive Statistics for Research, Hilary 2002, Lecture 1; named individual author not confirmed','https://www.stats.ox.ac.uk/pub/bdr/IAUL/Course1Notes1.pdf'),
('berkeley-hist','UC Berkeley','SticiGui, Philip B. Stark, Chapter 3','https://www.stat.berkeley.edu/~stark/SticiGui/Text/histograms.htm'),
('berkeley-toc','UC Berkeley','SticiGui, Philip B. Stark, table of contents','https://www.stat.berkeley.edu/~stark/SticiGui/Text/toc.htm'),
('harvard','Harvard','Introduction to Data Science, Rafael Irizarry, Chapter 12','https://rafalab.dfci.harvard.edu/dsbook/summary-statistics.html'),
('eth','ETH Zurich','Fundamentals of Mathematical Statistics AS2022 course index; screening only','https://stat.ethz.ch/lectures/as22/mathstat.php')]
def get(t):
 id,u,c,url=t
 try:
  r=requests.get(url,timeout=45);r.raise_for_status();pdf=r.content.startswith(b'%PDF');p=T/(id+('.pdf' if pdf else '.html'));p.write_bytes(r.content)
  if pdf:
   d=fitz.open(p);text='\n'.join('\n--- PDF PAGE '+str(i+1)+' ---\n'+pg.get_text() for i,pg in enumerate(d));pages=len(d)
  else:
   h=TextParser();h.feed(r.text);text=''.join(h.parts);pages=None
  (T/(id+'.txt')).write_text(text,encoding='utf-8')
  return dict(id=id,university=u,course=c,url=url,path=str(p),pages=pages,sha256=hashlib.sha256(r.content).hexdigest(),status='acquired_not_reviewed')
 except Exception as ex:return dict(id=id,university=u,course=c,url=url,status='unavailable',error=str(ex))
rows=list(concurrent.futures.ThreadPoolExecutor(max_workers=6).map(get,S));(B/'s_descriptive-evidence/acquisition.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8');print(json.dumps([{k:r.get(k) for k in ['id','pages','status','error']} for r in rows]))

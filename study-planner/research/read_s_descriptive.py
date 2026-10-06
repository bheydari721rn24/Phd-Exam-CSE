from pathlib import Path
import sys,tempfile,re,json,fitz
from html.parser import HTMLParser
T=Path(tempfile.gettempdir())/'s-descriptive-sources'
if sys.argv[1]=='links':
 class P(HTMLParser):
  def handle_starttag(self,t,a):
   d=dict(a)
   if t=='a' and 'href' in d:print(d['href'])
 P().feed((T/'berkeley-toc.html').read_text(encoding='utf-8'))
elif sys.argv[1]=='pages':
 text=(T/(sys.argv[2]+'.txt')).read_text(encoding='utf-8');a=int(sys.argv[3]);b=int(sys.argv[4]);print(text[text.index('--- PDF PAGE '+str(a)+' ---'):text.index('--- PDF PAGE '+str(b+1)+' ---') if b+1<=100 and '--- PDF PAGE '+str(b+1)+' ---' in text else len(text)])
elif sys.argv[1]=='text':
 print((T/(sys.argv[2]+'.txt')).read_text(encoding='utf-8')[int(sys.argv[3]):int(sys.argv[4])])
elif sys.argv[1]=='exam':
 root=Path(tempfile.gettempdir())/'exam-calibration-1406/source/Exams'
 for rel,pg in [('MS/CS/1405',27),('Phd/CS/1405',15),('Phd/CS/1404',16)]:
  p=next((root/rel).glob('*.pdf'));doc=fitz.open(p);out=T/('exam-'+rel.replace('/','-')+'.png');doc[pg-1].get_pixmap(matrix=fitz.Matrix(2,2)).save(out);print(out)

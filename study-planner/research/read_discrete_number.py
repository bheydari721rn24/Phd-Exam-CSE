"""Read exact page ranges; an index pass identifies chapter boundaries."""
import sys,tempfile
from pathlib import Path
from pypdf import PdfReader
key=sys.argv[1]
p=Path(tempfile.gettempdir())/('phd-invariants-sources' if key=='mit' else 'phd-discrete-number-sources')/(key+'.pdf')
r=PdfReader(p)
if len(sys.argv)==2:
 for i,x in enumerate(r.pages):
  s=x.extract_text() or ''
  if key=='mit' and 230<i<330 or key=='cambridge' and 65<i<165:print(i+1,s[:200].replace('\n',' '))
else:
 for i in range(int(sys.argv[2])-1,int(sys.argv[3])):print('\n--- PDF PAGE',i+1,'---\n',r.pages[i].extract_text())

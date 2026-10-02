"""Print bounded page ranges for genuine source reading without hidden truncation."""
import sys,tempfile
from pathlib import Path
from pypdf import PdfReader
root=Path(tempfile.gettempdir())/'phd-recurrence-sources'
key=sys.argv[1];reader=PdfReader(root/(key+'.pdf'))
lo=int(sys.argv[2]) if len(sys.argv)>2 else 1;hi=int(sys.argv[3]) if len(sys.argv)>3 else len(reader.pages)
for i in range(lo-1,hi):print('PAGE',i+1,'\n',reader.pages[i].extract_text())

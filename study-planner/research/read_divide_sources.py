"""Print bounded page ranges for genuine chapter-specific source reading."""
import sys,tempfile
from pathlib import Path
from pypdf import PdfReader
r=PdfReader(Path(tempfile.gettempdir())/'phd-divide-sources'/(sys.argv[1]+'.pdf'))
lo=int(sys.argv[2]) if len(sys.argv)>2 else 1
hi=int(sys.argv[3]) if len(sys.argv)>3 else len(r.pages)
for i in range(lo-1,hi):
 print(f'\nPAGE {i+1}\n'+r.pages[i].extract_text())

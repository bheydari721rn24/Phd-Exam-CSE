"""Print a bounded PDF text interval for close review against its page markers."""
import re,sys,tempfile
from pathlib import Path
p=Path(tempfile.gettempdir())/'phd-invariants-sources'/f'{sys.argv[1]}.txt'
s=p.read_text(encoding='utf-8');pages=re.split(r'\n=== PDF PAGE (\d+) ===\n',s)
lo,hi=map(int,sys.argv[2:4])
for i in range(1,len(pages),2):
 if lo<=int(pages[i])<=hi:print(f'=== PDF PAGE {pages[i]} ===\n{pages[i+1]}')

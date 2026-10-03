"""Make mathematical source literals raw; remove obsolete corrected drafts."""
import io,tokenize,subprocess,sys
from pathlib import Path
BASE=Path(__file__).resolve().parent
for name in ('author_actual','author_discrete','author_algorithms','author_math','author_computing'):
 p=BASE/(name+'.py');s=p.read_text(encoding='utf-8');tokens=list(tokenize.generate_tokens(io.StringIO(s).readline))
 lines=s.splitlines(keepends=True);starts=[];offset=0
 for line in lines:starts.append(offset);offset+=len(line)
 edits=[]
 for t in tokens:
  if t.type==tokenize.STRING and '$' in t.string and '\\' in t.string and t.string[0] in ('\"',"'"):
   edits.append(starts[t.start[0]-1]+t.start[1])
 for i in reversed(edits):s=s[:i]+'r'+s[i:]
 p.write_text(s,encoding='utf-8')
 subprocess.run([sys.executable,'-X','utf8',str(p)],check=True)

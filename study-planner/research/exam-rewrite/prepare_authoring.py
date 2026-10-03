"""Keep authored TeX literal in Python data; then reproduce the chapter sources."""
import io,tokenize,re,runpy
from pathlib import Path
base=Path(__file__).parent
for p in sorted(base.glob('write_*.py')):
 tokens=list(tokenize.generate_tokens(io.StringIO(p.read_text(encoding='utf-8')).readline));changed=False
 for i,t in enumerate(tokens):
  if t.type==tokenize.STRING and t.string.startswith(("'",'"')) and re.search(r'\\[A-Za-z]',t.string):
   tokens[i]=t._replace(string='r'+t.string);changed=True
 if changed:p.write_text(tokenize.untokenize(tokens),encoding='utf-8')
 runpy.run_path(str(p))

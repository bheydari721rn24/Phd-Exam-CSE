from pathlib import Path
import tempfile,logging,json,subprocess
from pypdf import PdfReader
logging.getLogger('fontTools').setLevel(logging.ERROR)
out=Path(tempfile.gettempdir())/'g_boolean_qa';reader=PdfReader(out/'print-cdp.pdf')
texts=[page.extract_text() for page in reader.pages]
selected={1,len(reader.pages)}
for term in ('Deriving De Morgan','Boolean difference','Shannon decomposition','Problem 29.','Sixty high-yield'):
 for i,s in enumerate(texts):
  if term in s:selected.add(i+1);break
poppler=Path('C:/Users/bheydari/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe')
for page in sorted(selected):
 subprocess.run([str(poppler),'-f',str(page),'-l',str(page),'-scale-to','1500','-png',str(out/'print-cdp.pdf'),str(out/f'page{page}')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
summary={'pages':len(reader.pages),'rendered':sorted(selected),'textCharacters':sum(map(len,texts)),'problemHeadings':sum(s.count('Problem ') for s in texts)}
print(json.dumps(summary,indent=2));(out/'print-summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')

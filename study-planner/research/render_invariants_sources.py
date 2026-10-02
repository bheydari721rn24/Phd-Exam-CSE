"""Render representative original source pages to inspect mathematical notation."""
import subprocess,tempfile
from pathlib import Path
OUT=Path(tempfile.gettempdir())/'phd-invariants-sources'
BIN=Path('C:/Users/bheydari/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin/pdftoppm.exe')
for key,page in [('mit',144),('stanford',5),('cmu_structural',7),('cambridge',67)]:
 subprocess.run([str(BIN),'-f',str(page),'-l',str(page),'-scale-to','1300','-png','-singlefile',str(OUT/f'{key}.pdf'),str(OUT/f'{key}-original-page')],check=True,stdout=subprocess.DEVNULL)
 print(OUT/f'{key}-original-page.png')

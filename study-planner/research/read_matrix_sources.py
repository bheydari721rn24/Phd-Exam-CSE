"""Download written matrix sources to a temporary, nonpublished review cache."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import tempfile
import urllib.request
import logging
from pypdf import PdfReader
logging.getLogger('pypdf').setLevel(logging.ERROR)
OUT = Path(tempfile.gettempdir()) / 'l_matrices_sources'
OUT.mkdir(exist_ok=True)
SOURCES = {
 'stanford': 'https://ee263.stanford.edu/archive/matrix-primer-lect2.pdf',
 'berkeley-algebra': 'https://math.berkeley.edu/~apaulin/Matrix%20Algebra.pdf',
 'berkeley-inverse': 'https://math.berkeley.edu/~apaulin/Inverse%20of%20a%20Matrix.pdf',
 'mit-product': 'https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/1963da71c4d96e5d14e7939780f79bcc_MIT18_06SCF11_Ses1.3sum.pdf',
 'mit-transpose': 'https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/33b21afab62ea8df6c7bd241240df60d_MIT18_06SCF11_Ses1.5sum.pdf',
 'mit-problems': 'https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/8e9ccbcc13300a9bda7f24a684bd16b6_MIT18_06SCF11_Ses1.3prob.pdf',
 'mit-solutions': 'https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/d2dc903ca48f3d1ffa1528abde719c94_MIT18_06SCF11_Ses1.3sol.pdf',
 'harvard-product': 'https://people.math.harvard.edu/~knill/teaching/math21b2023/handouts/lecture06.pdf',
 'harvard-inverse': 'https://people.math.harvard.edu/~knill/teaching/math21b2023/handouts/lecture07.pdf',
 'cmu-product': 'https://www.math.cmu.edu/~wgunther/241/m14/notes/week2/7.pdf',
}
def read(item):
 name,url=item
 path=OUT/f'{name}.pdf'
 if not path.exists():
  with urllib.request.urlopen(url,timeout=25) as response:
   path.write_bytes(response.read())
 reader=PdfReader(path)
 text='\n\n'.join(f'PAGE {i+1}\n{p.extract_text()}' for i,p in enumerate(reader.pages))
 (OUT/f'{name}.txt').write_text(text,encoding='utf-8')
 return name,len(reader.pages),len(text)
with ThreadPoolExecutor(max_workers=5) as pool:
 jobs={pool.submit(read,item):item[0] for item in SOURCES.items()}
 for job in as_completed(jobs):
  try: print(job.result(),flush=True)
  except Exception as error: print(jobs[job],str(error)[:150],flush=True)

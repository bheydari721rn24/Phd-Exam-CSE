"""Cache official written chapter sources outside the repository for review."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import tempfile
import urllib.request
import logging
from pypdf import PdfReader
logging.getLogger("pypdf").setLevel(logging.ERROR)

OUT = Path(tempfile.gettempdir()) / "l_vectors_sources"
OUT.mkdir(exist_ok=True)
SOURCES = {
    "mit-dot": "https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/6082f2744b609da87e23f3d8feed0565_MIT18_02SC_notes_1.pdf",
    "mit-projection": "https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/f1b2876cbb4207c972b90eb04ebc861d_MIT18_02SC_notes_2.pdf",
    "oxford": "https://courses.maths.ox.ac.uk/pluginfile.php/25471/mod_folder/content/0/lecture_notes22.pdf?forcedownload=1",
    "stanford-review": "https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/lin-alg.pdf",
    "stanford-orthogonal": "https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/lectures/qr.pdf",
    "berkeley-vectors": "https://math.berkeley.edu/~apaulin/Vectors%20in%20Rn.pdf",
    "berkeley-dot": "https://math.berkeley.edu/~apaulin/Inner%20Products,%20Length%20and%20Orthogonality.pdf",
    "berkeley-projections": "https://math.berkeley.edu/~apaulin/Orthogonal%20Projections.pdf",
    "berkeley-inner": "https://math.berkeley.edu/~apaulin/Inner%20Product%20Spaces.pdf",
    "cmu-vectors": "https://www.math.cmu.edu/~wgunther/241/m14/notes/week1/3.pdf",
    "cmu-dot": "https://www.math.cmu.edu/~wgunther/241/m14/notes/week4/17.pdf",
    "cambridge": "https://www.damtp.cam.ac.uk/user/sjc1/teaching/VandM/notes.pdf",
}

def read_source(item):
    name, url = item
    path = OUT / f"{name}.pdf"
    if not path.exists():
        with urllib.request.urlopen(url, timeout=25) as response:
            path.write_bytes(response.read())
    reader = PdfReader(path)
    text = "\n\n".join(f"PAGE {i+1}\n{page.extract_text()}" for i, page in enumerate(reader.pages))
    (OUT / f"{name}.txt").write_text(text, encoding="utf-8")
    return name, len(reader.pages), len(text)

with ThreadPoolExecutor(max_workers=5) as pool:
    jobs = {pool.submit(read_source, item): item[0] for item in SOURCES.items()}
    for job in as_completed(jobs):
        try:
            print(read_source_result := job.result(), flush=True)
        except Exception as error:
            print(jobs[job], "unavailable:", str(error)[:120], flush=True)

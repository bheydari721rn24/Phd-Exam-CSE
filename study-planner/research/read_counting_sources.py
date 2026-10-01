"""Cache official written sources outside the repository for chapter review."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import tempfile
import urllib.request
from pypdf import PdfReader

OUT = Path(tempfile.gettempdir()) / "s_counting_sources"
OUT.mkdir(exist_ok=True)
SOURCES = {
    "mit-independence": "https://ocw.mit.edu/courses/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/b200b6217af1cd5dbea8c659ebbf046a_MIT6_041F10_L03.pdf",
    "mit-counting": "https://ocw.mit.edu/courses/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/f25004e3104e9bb7cf51ed0111ed7cf2_MIT6_041F10_L04.pdf",
    "stanford-counting": "https://web.stanford.edu/class/archive/cs/cs109/cs109.1206/lectureNotes/LN01_counting.pdf",
    "stanford-combinatorics": "https://web.stanford.edu/class/archive/cs/cs109/cs109.1206/lectureNotes/LN02_combinatorics.pdf",
    "stanford-independence": "https://web.stanford.edu/class/archive/cs/cs109/cs109.1206/lectureNotes/LN05_independence.pdf",
    "berkeley-counting": "https://www.su19.eecs70.org/static/notes/n12.pdf",
    "berkeley-counting2": "https://www.su19.eecs70.org/static/notes/n12.5.pdf",
    "berkeley-conditional": "https://www.su19.eecs70.org/static/notes/n14.pdf",
}

def cache(item):
    key, url = item
    target = OUT / (key + ".pdf")
    if not target.exists():
        target.write_bytes(urllib.request.urlopen(url,timeout=40).read())
    pages = PdfReader(target).pages
    (OUT / (key + ".txt")).write_text("\n\n".join(f"PDF PAGE {i+1}\n" + page.extract_text() for i,page in enumerate(pages)),encoding="utf-8")
    return f"{key}: {len(pages)} pages"

with ThreadPoolExecutor(max_workers=4) as pool:
    futures = {pool.submit(cache,item):item[0] for item in SOURCES.items()}
    for future in as_completed(futures):
        try:
            print(future.result())
        except Exception as error:
            print(f"{futures[future]}: cache unavailable ({type(error).__name__}); use the verified official web PDF when accessible.")

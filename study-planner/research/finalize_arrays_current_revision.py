"""Integrate the bounded review, its evidence and exact progress; no other chapter rewrite."""
from pathlib import Path
import json,re,shutil,sys,subprocess,hashlib
from markdown_it import MarkdownIt
R=Path(__file__).resolve().parents[1];B=R/'research';E=B/'deep-library-revision';D=R/'dist';T=Path('C:/Users/bheydari/AppData/Local/Temp')
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def load(p):return json.loads(p.read_text(encoding='utf8'))
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
F=E/'p_arrays-independent-evidence';F.mkdir(exist_ok=True)
for folder,names in {
'arrays-written-refresh-20261020':['source-refresh.en.md','acquisition.json','python-checks.json','check_written_examples.py'],
'arrays-remaining-20261020':['report.en.md','oracle.py','oracle-report.json','final-wording-review.en.md','final-wording-review.json'],
'arrays-originals-20261020':['report.en.md','acquisition.json','independent-checks.json']}.items():
    dest=F/folder;dest.mkdir(exist_ok=True)
    for name in names:shutil.copy2(T/folder/name,dest/name)
# Persist independently authored checks with a repository-relative root.
for name in ['oracle.py','check_written_examples.py']:
    p=next(F.rglob(name));s=p.read_text(encoding='utf8')
    s=re.sub(r"ROOT=Path\('C:/Users/[^\n]+/study-planner'\)","ROOT=Path(__file__).resolve().parents[4]",s)
    s=re.sub(r"RESEARCH = Path\('C:/Users/[^\n]+/study-planner/research'\)","RESEARCH = Path(__file__).resolve().parents[4] / 'research'",s)
    p.write_text(s,encoding='utf8')
main=B/'p_arrays.en.md';s=main.read_text(encoding='utf8').replace(r'\mathrm{SIZE\_MAX}',r'\operatorname{SIZE_MAX}')
extra=(E/'p_arrays-contract-method.en.md').read_text(encoding='utf8')
if '### Why a range check can itself be unsafe'not in s:s=s.replace('## Python slices, sharing and nested rows',extra+'\n\n## Python slices, sharing and nested rows')
main.write_text(s,encoding='utf8')
p=D/'chapters/p_arrays.html';s=p.read_text(encoding='utf8')
if 'id="range-contract-method"'not in s:s=s.replace('<h2 id="python">','<section id="range-contract-method">'+mathml.markdown_math(extra,md)+'</section><h2 id="python">',1)
s=s.replace('SIZE\\_MAX','SIZE_MAX')
# Avoid the old automatic letter-highlighting in a professor's personal name.
s=s.replace('David <span class="math-inline">J</span>. Malan','David J. Malan')
p.write_text(s,encoding='utf8')
print('Copied bounded evidence and added range-contract proof and examination method.')

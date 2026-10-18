"""Check the actual empty-update repair and preserve a portable layout oracle."""
from pathlib import Path
import hashlib,json,re,subprocess,sys,xml.etree.ElementTree as ET
R=Path(__file__).resolve().parents[1];B=R/'research';E=B/'deep-library-revision';T=Path('C:/Users/bheydari/AppData/Local/Temp')
code=(T/'phd-arrays-layout-20261018/oracle.py').read_text()
code=code.replace("OUT=pathlib.Path(__file__).parent","OUT=ROOT/'research/deep-library-revision'").replace("(OUT/'oracle-results.json')","(OUT/'p_arrays-layout-independent-checks.json')")
(B/'verify_arrays_layout_start.py').write_text(code,encoding='utf8');subprocess.run([sys.executable,str(B/'verify_arrays_layout_start.py')],check=True)
checks=0
for n in range(16):
    original=[k*k-3*k+2 for k in range(n)]
    difference=[]if n==0 else[original[0]]+[original[k]-original[k-1]for k in range(1,n)]
    for l in range(n+1):
        for r in range(l,n+1):
            for c in [-7,-1,0,1,9]:
                d=difference.copy()
                if l<r:
                    d[l]+=c
                    if r<n:d[r]-=c
                got=[];s=0
                for v in d:s+=v;got.append(s)
                expected=[v+c if l<=k<r else v for k,v in enumerate(original)]
                assert got==expected;checks+=1
live=(R/'dist/chapters/p_arrays.html').read_text(encoding='utf8')
old=subprocess.check_output(['git','show','bf98c9185f64c53caf469394d7045babca082688:dist/chapters/p_arrays.html'],cwd=R).decode('utf8')
question_sections=lambda s:re.findall(r'<section class="exam-question"[\s\S]*?</section>',s)
assert len(question_sections(live))==83 and question_sections(live)==question_sections(old)
assert 'l equal to r is a no-op'in live and 'For a positive requested size'in live
for m in re.findall(r'<math\b[\s\S]*?</math>',live):ET.fromstring(m)
record={'status':'partial_arrays_review_start_checked','rangeUpdateCases':checks,'all83QuestionBodiesPreserved':True,'rewrittenAnswersSavedOnlyAsManuscript':12,'completeChapterReview':False,'limitations':'Only the two identified lesson boundary repairs and the first-twelve mathematical manuscript are covered. The other 69 original solutions, exact question visuals, remaining sources and browser gates remain pending.'}
(E/'p_arrays-boundary-repair-checks.json').write_text(json.dumps(record,indent=2)+'\n');print(record)

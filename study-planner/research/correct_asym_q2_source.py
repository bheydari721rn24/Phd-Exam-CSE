"""Correct only the source-verified fourth option and its explanation."""
from pathlib import Path
import ast,hashlib,json,re,sys
from markdown_it import MarkdownIt
B=Path(__file__).resolve().parent;R=B.parent;sys.path.insert(0,str(B/'exam-rewrite'));import mathml
md=MarkdownIt('commonmark',{'html':True})
p=B/'exam-calibration/actual-items.json';all_items=json.loads(p.read_text());q=next(q for q in all_items if q['id']=='Phd_CE_1405_Q2');before=q['options'][3]
q['options'][3]=r'$\Theta(n\log^2 n)$'
q['solution']=q['solution'].replace('option 4 counts only levels','option 4 proposes a much larger tight order, n times the root toll')
q['translationStatus']='Original PDF page visually rechecked on 11 October 2026; fourth option corrected to Theta(n log^2 n).'
p.write_text(json.dumps(all_items,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=B/'exam-calibration/author_actual.py';v=p.read_text();a=v.index("add('Phd_CE_1405',2,2,");z=v.index("add('Phd_CE_1405',2,3,",a);segment=v[a:z].replace("r'$\\Theta(\\log n)$'","r'$\\Theta(n\\log^2 n)$'").replace('option 4 counts only levels','option 4 proposes a much larger tight order, n times the root toll');p.write_text(v[:a]+segment+v[z:],encoding='utf-8')
changes=[]
for topic in ['a_asym','a_recurrence']:
    p=R/'dist/chapters'/(topic+'.html');v=p.read_text();a=v.index('data-source-id="Phd_CE_1405_Q2"');z=v.index('</details></section>',a)+len('</details></section>');segment=v[a:z];pat=r'(<div class="exam-option"><b>4\.</b><div>)[\s\S]*?(</div></div>)';assert len(re.findall(pat,segment))==1
    segment=re.sub(pat,lambda m:m[1]+mathml.markdown_math(q['options'][3],md)+m[2],segment).replace('option 4 counts only levels','option 4 proposes a much larger tight order, n times the root toll');oldhash=hashlib.sha256(v.encode()).hexdigest();v=v[:a]+segment+v[z:];p.write_text(v,encoding='utf-8');changes.append(dict(topicId=topic,beforeSha256=oldhash,afterSha256=hashlib.sha256(v.encode()).hexdigest()))
p=B/'deep-library-revision/a_asym-solutions.md';v=p.read_text();v=v.replace('Option 4 counts the levels while treating each toll as constant.','Option 4 multiplies a root-sized squared-logarithm toll by a linear number of inputs rather than a logarithmic number of levels: its proposed tight order is $\\Theta(n\\log^2 n)$, whose ratio to the actual cost grows as $n/\\log n$.');p.write_text(v,encoding='utf-8')
(B/'deep-library-revision/Phd_CE_1405_Q2-source-correction.json').write_text(json.dumps(dict(id=q['id'],originalPdfPage=2,oldFourthOption=before,correctedFourthOption=q['options'][3],answerRemains=3,reason='The original fourth option visibly includes n multiplying log squared; the earlier translation omitted n and the square.',changedPlacements=changes,fullReviewStatus='a_asym in progress; a_recurrence source correction only, not full revision'),indent=2)+'\n')
print(json.dumps(dict(corrected=q['id'],placements=2,answer=3)))

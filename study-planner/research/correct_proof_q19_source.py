"""Correct the visually confirmed identity/injectivity source transcription."""
from pathlib import Path
import ast, hashlib, json, re, sys, subprocess
from markdown_it import MarkdownIt
B=Path(__file__).resolve().parent;R=B.parent;E=B/'deep-library-revision'
ns={};t=ast.parse((B/'deep_revision_inventory.py').read_text())
exec(compile(ast.Module(body=[x for x in t.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):
    v=mathml.markdown_math(s.replace(r'\prec','≺'),md)
    return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',v)
parts=re.split(r'^## Q(\d+)\s*$',(E/'d_proof-solutions.md').read_text(),flags=re.M)
answer=next(parts[i+1].strip()for i in range(1,len(parts),2)if parts[i]=='6')
path=B/'exam-calibration/actual-items.json';items=json.loads(path.read_text())
item=next(q for q in items if q['id']=='Phd_CS_1405_Q19')
item.update(title='Order preservation versus identity',stem=r'Evaluate (a) if $(A,<)$ is linearly ordered and $f:A\to A$ preserves that strict order, then $f$ is the identity function; (b) every countable set is well-orderable.',answer=2,solution=answer,pattern='identity versus injectivity and existence of a well-order',translationStatus='Original Persian identity-function wording visually rechecked at enlarged PDF page 8 on 11 October 2026; previous injectivity translation corrected.',correctionHistory=[dict(date='2026-10-11',previousTranslation='injective',originalMeaning='identity function',previousAnswer=3,correctedIndependentAnswer=2)])
path.write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# The proof builder consumes the corrected record. The functions page has not
# undergone its full individual review; repair only this confirmed source error.
path=R/'dist/chapters/d_functions.html';page=path.read_text();matches=[q for q in ns['questions'](page)if q[2].get('data-source-id')==item['id']];assert len(matches)==1
a,b,attrs,q=matches[0];prefix=q[:q.index('<details')]
end=re.search(r'<p class="exam-provenance">[\s\S]*?</p>',prefix).end()
prefix=prefix[:end]+render(item['stem'])+prefix[prefix.index('<div class="exam-options">'):]
prefix=prefix.replace('data-answer="3"','data-answer="2"').replace('Strict order and injectivity','Order preservation versus identity')
v=prefix+'<details class="exam-solution"><summary>Read the corrected proof and source distinction</summary><p class="source-correction"><strong>Source correction, 11 October 2026.</strong> The original asks whether the map must be the identity. Its earlier translation as injectivity was incorrect.</p>'+render(answer)+'</details></section>'
baseline=subprocess.check_output(['git','show','f890223f3111d27958eb483056556fded2d59ff3:dist/chapters/d_functions.html']).replace(b'\r\n',b'\n')
before=hashlib.sha256(baseline).hexdigest();page=page[:a]+v+page[b:];path.write_text(page,encoding='utf-8')
report=dict(sourceId=item['id'],sourcePdfSha256=item['sourceSha256'],pdfPage=8,originalMeaning='identity function',previousMeaning='injectivity',previousIndependentAnswer=3,correctedIndependentAnswer=2,actualPlacements=['d_proof','d_functions'],relationsReference='The relations chapter only names this question as a pattern reference; it has no authentic placement to correct.',functionsPageBefore=before,functionsPageAfter=hashlib.sha256(page.encode()).hexdigest(),functionsFullReview='still pending; only the authentic question is corrected',enlargedSourceInspection='C:/Users/bheydari/AppData/Local/Temp/proof-q19-detail.png')
(E/'Phd_CS_1405_Q19-source-correction.json').write_text(json.dumps(report,indent=2)+'\n')
print('Original identity wording and option 2 recorded; functions authentic placement corrected.')

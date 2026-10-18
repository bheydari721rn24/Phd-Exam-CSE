"""Individually integrate the rank review without rerunning global installers."""
from pathlib import Path
from html import escape
import hashlib,json,re,subprocess,sys
from markdown_it import MarkdownIt

R=Path(__file__).resolve().parents[1]; E=R/'research/deep-library-revision'
BASE='ce272ad83079d4e95f6e009fd89c603240a8a708'
def frozen(path):return subprocess.check_output(['git','show',BASE+':'+path],cwd=R).decode('utf8')
def blocks(path):
    t=(R/path).read_text(encoding='utf8')
    return {m[1]:m[2].strip() for m in re.finditer(r'^## ([^\n]+)\n([\s\S]*?)(?=^## |\Z)',t,re.M)}
def endtag(t,start,tag):
    first=t.index('>',start)+1; depth=1
    for m in re.finditer('<'+tag+r'\b[^>]*>|</'+tag+'>',t[first:]):
        depth+=-1 if m[0]=='</'+tag+'>'else 1
        if depth==0:return first+m.end()
    raise ValueError('Unclosed '+tag)
sys.path.insert(0,str(R/'research/exam-rewrite'))
import mathml
mathml.wrap_display=lambda s:s
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):return mathml.markdown_math(s,md)

qs=json.loads(frozen('research/l_rank-questions.json'))
add=blocks('research/deep-library-revision/l_rank-answer-additions.en.md'); assert len(add)==88
for q in qs:
    if q['id']=='LR88':
        q['solution']=q['solution'].replace('It is the single left-annihilator restriction on this three-dimensional row space in four coordinates.','It is the single annihilator restriction supplied by the right kernel for this three-dimensional row space in four coordinates.')
    q['solution']+='\n\n'+add[q['id']]
auth=json.loads(frozen('research/l_rank-authentic.json'))
aa=blocks('research/deep-library-revision/l_rank-authentic-expanded-solutions.en.md')
for q in auth:q['solution']=aa[q['id']]
for name,data in [('l_rank-questions.json',qs),('l_rank-authentic.json',auth)]:
    (R/'research'/name).write_text(json.dumps(data,indent=2)+'\n',encoding='utf8')

models=json.loads((R/'dist/chapters/problem-visual-models.json').read_text(encoding='utf8'))
page=frozen('dist/chapters/l_rank.html'); records={q['id']:q for q in qs+auth}
matched={'LR02':'rank-pivots','LR18':'rank-fibers','LR30':'rank-factorization','LR33':'rank-column-transform','LR46':'rank-parameters','LR59':'rank-projection'}
def fallback(key):
    m=models[key]; f=m['frames'][0]
    return '<div class="problem-visual" data-problem-visual="'+key+'"><h4>Visual solution aid</h4><p>'+escape(m['reading'])+'</p><div class="problem-stage">'+f['html']+'</div><p class="problem-caption">'+escape(f['caption'])+'</p><p class="problem-scope">'+escape(m['scope'])+'</p></div>'
replacements=[]; removed=page.count('class="question-concept-aid"')
for m in re.finditer(r'<section class="exam-question"[^>]*data-source-id="([^"]+)"[^>]*>',page):
    qid=m[1]; stop=endtag(page,m.start(),'section'); old=page[m.start():stop]
    head=old[:old.index('<details')]
    keys=re.findall(r'data-problem-visual="([^"]+)"',old)
    if qid=='MS_CS_1405_Q41':keys.append('l_rank-authentic-dimension')
    if qid=='Phd_CS_1404_Q30':keys.append('l_rank-authentic-norm')
    aids=''.join(fallback(k)for k in keys)
    if qid in matched:
        note='The checkpoints use the actual map or matrix of this problem. Finite examples supplement its complete written proof.'
        if qid=='LR46':note='The selected values use this question’s own parameter family. The symbolic derivation supplies all real branches.'
        aids+='<div class="question-concept-aid"><h4>Inspect this problem’s actual model</h4><p>'+note+'</p><div class="concept-animation" data-scenes="'+matched[qid]+'"></div></div>'
    new=head+'<details class="exam-solution"><summary>Read the complete derivation, verification and examination decision</summary>'+render(records[qid]['solution'])+aids+'</details></section>'
    replacements.append((m.start(),stop,new))
assert len(replacements)==90
for a,z,s in reversed(replacements):page=page[:a]+s+page[z:]

instruction=blocks('research/deep-library-revision/l_rank-instruction-additions.en.md')
def fragment(k):return '<section class="rank-revision-instruction"><h3>'+escape(k)+'</h3>'+render(instruction[k])+'</section>'
pair='Which kernel tests which membership question?'; sequence='A complete rank-and-fiber examination decision sequence'
page=page.replace('<h2 id="inverses">',fragment(pair)+'<h2 id="inverses">',1)
page=page.replace('<section class="review-rule">',fragment(sequence)+'<section class="review-rule">',1)
lesson=frozen('research/l_rank.en.md')
lesson=lesson.replace('## Injectivity, surjectivity, and one-sided inverses','### '+pair+'\n\n'+instruction[pair]+'\n\n## Injectivity, surjectivity, and one-sided inverses',1)
lesson=lesson.replace('<!-- INCLUDE:review -->','### '+sequence+'\n\n'+instruction[sequence]+'\n\n<!-- INCLUDE:review -->',1)
(R/'research/l_rank.en.md').write_text(lesson,encoding='utf8')
rules={
34:r'Over an infinite field, positive nullity gives infinitely many compatible solutions. Over a finite field of q elements the count is exactly $q^{n-r}$, through a bijection with the independent kernel coordinates. A field of order nine is not the non-field ring of integers modulo nine.',
35:r'A real load b is in the column space exactly when it is orthogonal to every left-kernel vector. Testing an independent left-kernel basis gives every required output restriction. In contrast, row-space membership is tested against the right kernel in the input-coordinate space.',
50:r'A positive uniform lower norm bound forces injectivity. A finite square map is consequently invertible with inverse norm at most the reciprocal bound, using the same induced norm. It does not imply positive definiteness; negative identity is an explicit counterexample. Complex eigenvalues need a justified complex extension of the real norm argument.',
59:r'Combine a negative Sylvester expression with the independent lower bound zero. Equality with the nonnegative formal expression requires the entire kernel of A to lie in the image of B. Equality of product rank with zero instead requires the image of B to lie in the kernel of A; these are different containments.',
73:r'Exact and numerical rank answer different questions. State the numerical threshold, whether its comparison is strict, and whether it is absolute or relative to a matrix scale. Rounding a nonzero coefficient to zero changes the exact matrix; it does not prove that the original exact matrix has lower rank.',
80:r'Subtract the rank of independent linear constraints from the number of ambient coordinates. Prove the constraint rank with witnesses, reduction or a full parameterization. Repeated evaluations do not impose derivative conditions, repeated trace equations do not add independence, and nonlinear inequalities are not kernels of linear constraint maps.'}
review=frozen('research/l_rank-review.en.md')
for n,s in rules.items():
    review,k=re.subn(r'^'+str(n)+r'\. [\s\S]*?(?=\n\n|\Z)',lambda _:str(n)+'. '+s,review,count=1,flags=re.M);assert k==1
    page,k=re.subn(r'<section class="review-rule"><h4>Rule '+str(n)+r'</h4>[\s\S]*?</section>',lambda _:f'<section class="review-rule"><h4>Rule {n}</h4>'+render(s)+'</section>',page,count=1);assert k==1
(R/'research/l_rank-review.en.md').write_text(review,encoding='utf8')
page,k=re.subn(r'<header class="hero">([\s\S]*?<h1>[\s\S]*?</h1>)<p>[\s\S]*?</p></header>',lambda m:'<header class="hero">'+m[1]+'<p>Individually revised review draft · four rechecked primary university courses · 90 fully explained problems · 80 examination rules</p></header>',page,count=1);assert k==1
page=re.sub(r'(<math\b[^>]*display="inline"[^>]*>[\s\S]*?</math>)',r'<span class="pr-inline">\1</span>',page)
page=page.replace('href="l_rank.css"','href="l_rank.css?v=rank-review-20261018"').replace('src="problem-visuals.js?player-behavior-2"','src="problem-visuals.js?v=rank-review-20261018"')
page=page.replace('src="l_rank.js"','src="l_rank.js?v=rank-review-20261018"')
from teaching_prose_spacing import fix
page=fix(page)
assert page.count('class="exam-question"')==90 and page.count('class="review-rule"')==80
assert page.count('data-problem-visual=')==27 and page.count('class="question-concept-aid"')==6
(R/'dist/chapters/l_rank.html').write_text(page,encoding='utf8')
report={'state':'integrated_revision_pending_final_audit','date':'2026-10-18','frozenBaseline':BASE,'originalCourseSolutionsIndividuallyExtended':88,'authenticSolutionsRewritten':2,'questionPlacements':90,'finalRules':80,'solutionWords':sum(len(q['solution'].split())for q in qs+auth),'instructionAdditions':list(instruction),'oldQuestionAliasesRemoved':removed,'matchedQuestionScenes':matched,'problemSpecificVisuals':27,'studentApproved':False,'pageSha256':hashlib.sha256((R/'dist/chapters/l_rank.html').read_bytes()).hexdigest()}
(E/'l_rank-answer-revision.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8'); print(report)

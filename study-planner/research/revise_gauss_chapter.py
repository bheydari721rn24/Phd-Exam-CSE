"""Integrate the individual revision while preserving the exact inspected assets."""
from pathlib import Path
from html import escape
import hashlib,json,re,subprocess,sys
from markdown_it import MarkdownIt

R=Path(__file__).resolve().parents[1];E=R/'research/deep-library-revision'
BASE='ed4a4c486cba3a388a32384faa68a916bfda9399'
def frozen(path):return subprocess.check_output(['git','show',BASE+':'+path],cwd=R).decode('utf8')
def read(path):return (R/path).read_text(encoding='utf8')
def blocks(path):
    text=read(path)
    return {m[1]:m[2].strip() for m in re.finditer(r'^## ([^\n]+)\n([\s\S]*?)(?=^## |\Z)',text,re.M)}
def endtag(text,start,tag):
    first=text.index('>',start)+1;depth=1
    for m in re.finditer('<'+tag+r'\b[^>]*>|</'+tag+'>',text[first:]):
        depth+=-1 if m[0]=='</'+tag+'>'else 1
        if depth==0:return first+m.end()
    raise ValueError('Unclosed '+tag)
sys.path.insert(0,str(R/'research/exam-rewrite'))
import mathml
mathml.wrap_display=lambda s:s
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(text):return mathml.markdown_math(text,md)

qs=json.loads(frozen('research/l_gauss-questions.json'))
elementary=blocks('research/deep-library-revision/l_gauss-elementary-answer-expansions.en.md')
middle=blocks('research/deep-library-revision/l_gauss-answer-expansions.en.md')
advanced=blocks('research/deep-library-revision/l_gauss-advanced-answer-expansions.en.md')
assert len(elementary)==12 and len(middle)==13 and len(advanced)==44
for q in qs:
    qid=q['id'];number=int(qid[2:])
    if number<=12:
        cut=re.search(r'Set every free coefficient variable|The final coefficient-zero row',q['solution'])
        assert cut,qid
        q['solution']=q['solution'][:cut.start()]+elementary[qid]
    elif number<=25:q['solution']=middle[qid]
    else:
        part=advanced[qid]
        for label,key in [('Title','title'),('Question','stem'),('Provenance','origin'),('Difficulty','difficulty')]:
            m=re.search(r'\*\*'+label+r'\.\*\* ([\s\S]*?)(?=\n\n|\Z)',part)
            assert m and m[1].strip()==q[key],(qid,key)
        q['solution']=part.split('### Teaching solution',1)[1].strip()
assert len({x['id'] for x in qs})==69
auth=json.loads(frozen('research/l_gauss-authentic.json'))
answers=blocks('research/deep-library-revision/l_gauss-authentic-answer-expansions.en.md')
for q in auth:q['solution']=answers[q['id']]
assert auth[1]['options'][0]=='32';auth[1]['options'][0]='37'
(R/'research/l_gauss-questions.json').write_text(json.dumps(qs,indent=2)+'\n',encoding='utf8')
(R/'research/l_gauss-authentic.json').write_text(json.dumps(auth,indent=2)+'\n',encoding='utf8')

models=json.loads(read('dist/chapters/problem-visual-models.json'))
page=frozen('dist/chapters/l_gauss.html');records={q['id']:q for q in qs+auth}
def assets(old,qid):
    chunks=[]
    for m in re.finditer(r'<div class="(?:problem-visual|question-concept-aid)"[^>]*>|<figure class="gauss-column-erratum"[^>]*>',old):
        tag='figure' if m[0].startswith('<figure')else'div'
        chunk=old[m.start():endtag(old,m.start(),tag)]
        if 'data-problem-visual=' in m[0]:
            modelid=re.search(r'data-problem-visual="([^"]+)"',m[0])[1]
            chunk=fallback(modelid)
        chunks.append(chunk)
    if qid=='MS_CS_1405_Q113':chunks.insert(0,fallback('l_gauss-q2'))
    return ''.join(chunks)
def fallback(modelid):
    model=models[modelid];frame=model['frames'][0]
    return '<div class="problem-visual" data-problem-visual="'+modelid+'"><h4>Visual solution aid</h4><p>'+escape(model['reading'])+'</p><div class="problem-stage">'+frame.get('html',frame.get('svg',''))+'</div><p class="problem-caption">'+escape(frame['caption'])+'</p><p class="problem-scope">'+escape(model['scope'])+'</p><noscript><p>The first diagram and complete written solution are available without scripts.</p></noscript></div>'
replacements=[]
for m in re.finditer(r'<section class="exam-question"[^>]*data-source-id="([^"]+)"[^>]*>',page):
    qid=m[1];stop=endtag(page,m.start(),'section');old=page[m.start():stop]
    head=old[:old.index('<details')]
    if qid=='MS_CS_1405_Q113':
        # The canonical 12 October page repair already corrected this option;
        # the copied Gaussian JSON bank was the remaining stale record.
        assert '<b>1.</b><div><p>37</p>' in head
    body='<details class="exam-solution"><summary>Read the complete derivation, verification and examination decision</summary>'+render(records[qid]['solution'])+assets(old,qid)+'</details></section>'
    replacements.append((m.start(),stop,head+body))
assert len(replacements)==71
for a,z,new in reversed(replacements):page=page[:a]+new+page[z:]

additions=blocks('research/deep-library-revision/l_gauss-instruction-additions.en.md')
column='Column-space transport and original pivot columns'
plu='Why later pivot permutations move earlier multipliers'
decision='A complete examination decision sequence'
def fragment(key):return '<section class="gauss-revision-instruction"><h3>'+escape(key)+'</h3>'+render(additions[key])+'</section>'
assert page.count('<h2 id="parameters">')==1
page=page.replace('<h2 id="parameters">',fragment(column)+'<h2 id="parameters">',1)
assert page.count('<p>For a blocked system with invertible upper-left block')==1
page=page.replace('<p>For a blocked system with invertible upper-left block',fragment(plu)+'<p>For a blocked system with invertible upper-left block',1)
page=page.replace('<section class="review-rule">',fragment(decision)+'<section class="review-rule">',1)

rules={
45:r'Invertible row operations preserve row space, kernel and rank. They transport the column space by the same left transformation; the resulting subspace need not equal the original one, even though its dimension is unchanged.',
46:r'Select original columns using the pivot indices of coefficient reduction when constructing an original column-space basis. Reduced pivot columns need not span that original space. Full row rank is an important equality case: both original and reduced column spaces are the entire ambient load space.',
65:r'A later active-row swap must move the already stored earlier multiplier columns of $L$. It fixes completed pivot coordinates. Swapping only the current upper array can leave a triangular-looking but false factorization; swapping the whole lower matrix would also disturb its prescribed unit diagonal.',
67:r'A Gauss transform $I-ge_k^T$ has inverse $I+ge_k^T$ because $e_k^Tg=0$ makes the rank-one square vanish. Later active-row permutations preserve this support condition. General lower triangular inverses require cross terms, and arbitrary pivot-coordinate swaps need not preserve a lower Gauss-transform structure.'}
review=frozen('research/l_gauss-review.en.md')
for n,text in rules.items():
    review,count=re.subn(r'^'+str(n)+r'\. [\s\S]*?(?=\n\n|\Z)',lambda _:str(n)+'. '+text,review,count=1,flags=re.M);assert count==1
    pattern=r'<section class="review-rule"><h4>Rule '+str(n)+r'</h4>[\s\S]*?</section>'
    page,count=re.subn(pattern,lambda _:f'<section class="review-rule"><h4>Rule {n}</h4>'+render(text)+'</section>',page,count=1);assert count==1
(R/'research/l_gauss-review.en.md').write_text(review,encoding='utf8')
lesson=frozen('research/l_gauss.en.md')
lesson=lesson.replace('## Parameter systems and exceptional branches','### '+column+'\n\n'+additions[column]+'\n\n## Parameter systems and exceptional branches',1)
lesson=lesson.replace('For a blocked system with invertible upper-left block','### '+plu+'\n\n'+additions[plu]+'\n\nFor a blocked system with invertible upper-left block',1)
lesson=lesson.replace('<!-- INCLUDE:review -->','### '+decision+'\n\n'+additions[decision]+'\n\n<!-- INCLUDE:review -->',1)
(R/'research/l_gauss.en.md').write_text(lesson,encoding='utf8')
page,n=re.subn(r'<header class="hero">([\s\S]*?<h1>[\s\S]*?</h1>)<p>[\s\S]*?</p></header>',lambda m:'<header class="hero">'+m[1]+'<p>Individually revised review draft · four rechecked primary university courses · 71 fully explained problems · 80 examination rules</p></header>',page,count=1);assert n==1
page=re.sub(r'(<math\b[^>]*display="inline"[^>]*>[\s\S]*?</math>)',r'<span class="pr-inline">\1</span>',page)
page=page.replace('href="l_gauss.css"','href="l_gauss.css?v=gauss-review-20261017"').replace('src="problem-visuals.js?player-behavior-2"','src="problem-visuals.js?v=gauss-review-20261017"')
page=page.replace('src="l_gauss.js"','src="l_gauss.js?v=gauss-review-20261017"')
from teaching_prose_spacing import fix
page=fix(page)
assert page.count('class="exam-question"')==71 and page.count('class="review-rule"')==80
assert len(re.findall(r'data-problem-visual=',page))==33
assert page.count('class="question-concept-aid"')==11 and page.count('class="gauss-column-erratum"')==1
(R/'dist/chapters/l_gauss.html').write_text(page,encoding='utf8')
report={'state':'integrated_revision_pending_final_audit','date':'2026-10-17','frozenBaseline':BASE,'originalCourseAnswersExpanded':69,'authenticAnswersExpanded':2,'questionPlacements':71,'finalRules':80,'problemSpecificVisuals':33,'matchedQuestionWalkthroughs':11,'solutionWords':sum(len(q['solution'].split())for q in qs+auth),'instructionAdditions':list(additions),'correctedAuthenticOption':{'id':'MS_CS_1405_Q113','option':1,'old':'32','new':'37'},'studentApproved':False,'pageSha256':hashlib.sha256((R/'dist/chapters/l_gauss.html').read_bytes()).hexdigest()}
(E/'l_gauss-answer-revision.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8');print(report)

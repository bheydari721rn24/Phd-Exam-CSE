"""Preserve the full lecture while replacing every question solution individually."""
from pathlib import Path
import ast,hashlib,json,re,subprocess,sys
from markdown_it import MarkdownIt
B=Path(__file__).resolve().parent;R=B.parent;E=B/'deep-library-revision';BASE='f890223f3111d27958eb483056556fded2d59ff3'
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'h','exec'),ns)
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',mathml.markdown_math(s,md))
from asym_diagrams import envelopes,hierarchy
raw=subprocess.check_output(['git','show',BASE+':dist/chapters/a_asym.html']).decode().replace('\r\n','\n');entries=ns['questions'](raw)
parts=re.split(r'^## Q(\d+)\s*$',(E/'a_asym-solutions.md').read_text(),flags=re.M);answers={int(parts[i]):parts[i+1].strip() for i in range(1,len(parts),2)};assert set(answers)==set(range(1,47)) and len(entries)==46
actual={q['id']:q for q in json.loads((B/'exam-calibration/actual-items.json').read_text())};original={q['title']:q for f in (B/'exam-calibration').glob('original-*.json') for q in json.loads(f.read_text()) if q.get('topic')=='a_asym'}
extensions=[r'After choosing the exact normalized quantity, prove tight quadratic order and solve for a threshold under a prescribed upper constant $c>3$. Distinguish that witness from the limiting ratio.',r'After selecting the exact normalized quantity, prove the sum\'s tight class and state the fixed-base assumption. Explain why reversing the ratio changes the comparison.',r'After choosing the requested nested-logarithm value, distinguish it from an intermediate logarithm, a squared logarithm and a binary digit count. Derive the result symbolically.',r'After selecting the exact harmonic quantity or valid rule, derive both integral bounds and explain why exact evaluation, tight order and asymptotic equivalence are different conclusions.',r'After selecting the exact retained fraction or valid rule, prove eventual positivity and both tight bounds. Give a contrasting leading-term cancellation that changes the order.',r'After selecting the exact normalized quantity or valid rule, prove a uniform maximum-term sandwich and explain its fixed-count and sign hypotheses.',r'After selecting the even-subsequence value or valid rule, derive the odd subsequence, construct tight witnesses and prove that the global normalized ratio has no limit.',r'After selecting the least integer capacity height or valid rule, compare neighboring powers, derive its growth and distinguish information capacity from algorithmic attainability.']
replacements=[];records=[]
for n,(a,b,attrs,q) in enumerate(entries,1):
    prefix=q[:q.index('<details')] if n<=44 else q[:re.search(r'<p><strong>Correct option:',q).start()]
    if n<=44:
        title=ns['plain'](re.search(r'<h3[^>]*>([\s\S]*?)</h3>',q)[1]);rec=actual[attrs['data-source-id']] if n<=4 else original[re.sub(r'^Question \d+\. ','',title)]
        stem=rec['stem']
        end=re.search(r'<p class="exam-provenance">[\s\S]*?</p>',prefix).end();prefix=prefix[:end]+render(stem)+prefix[prefix.index('<div class="exam-options">'):]
        if n==2:
            prefix=re.sub(r'(<div class="exam-option"><b>4\.</b><div>)[\s\S]*?(</div></div>)',lambda m:m[1]+render(rec['options'][3])+m[2],prefix,count=1)
            prefix+='<p class="source-correction"><strong>Source correction.</strong> The fourth option was rechecked against the original PDF and restored to include the factor n and the squared logarithm.</p>'
        if n>=13:
            family=(n-13)//4;i=prefix.index('<div class="exam-options">');prefix=prefix[:i]+render(extensions[family])+prefix[i:]
            prefix=prefix.replace('Original examination analogue · author-assessed medium difficulty','Original examination analogue · foundational exact calculation with a required proof extension')
    else:
        stem=(r'For positive integer $n$, let $f(n)=n^{2+\sin(\ln n)}$ and $g(n)=n^2$. Which relation holds? Construct integer subsequences and control their rounding errors in your proof.' if n==45 else r'For positive integers $n$, compare $f(n)=2^{\lfloor\log_2n\rfloor}$ with $n$. Prove exact envelopes and test convergence on two explicitly defined unbounded integer subsequences.')
        end=prefix.index('<p><strong>1.</strong>');start=prefix.index('</h3>')+5;prefix=prefix[:start]+'<p class="exam-provenance">Original integrated asymptotic challenge; not an authentic examination item.</p>'+render(stem)+prefix[end:]
    prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-deep-index="{n}"',1)
    visual=''
    scene={7:'asym-parity-ratio',45:'asym-log-oscillation',46:'asym-floor-ratio'}.get(n)
    if scene:visual=f'<section class="concept-animation question-specific-animation" data-scenes="{scene}" aria-label="Discrete normalized values for question {n}"><p>The complete derivation and assumptions are written above.</p></section>'
    v=prefix+'<details class="exam-solution"><summary>Read the full derivation, witnesses and counterexamples</summary>'+render(answers[n])+visual+'</details></section>';replacements.append((a,b,v));records.append(dict(index=n,answer=int(re.search(r'Correct option:\s*(\d+)',answers[n])[1]),sourceId=attrs.get('data-source-id'),words=len(answers[n].split()),solutionSha256=hashlib.sha256(answers[n].encode()).hexdigest(),state='rewritten_pending_checks'))
page=raw
for a,b,v in reversed(replacements):page=page[:a]+v+page[b:]
bridge=render((E/'a_asym-method-instruction.md').read_text()).replace('<h2>','<h2 id="mathematical-bridge">',1);page=page.replace('<h2 id="worked-problems">',bridge+'<h2 id="worked-problems">',1)
rules=render((E/'a_asym-final-rules.md').read_text()).replace('<h2>','<h2 id="quick-reference">',1);page=re.sub(r'<h2 id="quick-reference">[\s\S]*?(?=<h2 id="references">)',lambda m:rules,page,count=1)
page=page.replace('<a href="#worked-problems">','<a href="#mathematical-bridge">Mathematical constructions</a> <a href="#worked-problems">',1).replace('Student-approved chapter','Revised review draft')
notice='<aside class="deep-review-notice"><strong>Asymptotic revision · 11 October 2026.</strong> All 46 answers are individually rewritten with derivations, witness constants, option analysis and integer-subsequence counterexamples. Six construction sections and 32 final rules complement the retained full lesson and 18 derivation tutorials. Three question-specific animations show the actual normalized functions. Four official written university readings and four authentic source questions were rechecked within documented bounds. A missing factor in one authentic option was corrected against the original PDF. This is a review draft.</aside>';page=page.replace('<article',notice+'<article',1)
style=re.search(r'<style id="deep-review-layout">[\s\S]*?</style>',(R/'dist/chapters/d_logic.html').read_text())[0];page=page.replace('</head>',style+'</head>')
figs=list(re.finditer(r'<figure class="logic-diagram">[\s\S]*?</figure>',page));assert len(figs)==2
for m,value in reversed(list(zip(figs,[envelopes(render),hierarchy(render)]))):page=page[:m.start()]+value+page[m.end():]
page=page.replace('No archived Iranian exam questions were consulted.','Four authentic Iranian examination questions were rechecked against the original rendered PDF pages; their translated source wording and its recorded ambiguity remain disclosed.')
page=page.replace('This student-approved chapter is undergoing the requested final library review.','This new version remains a review draft pending evaluation.').replace('PDF pp. 10–11','PDF pp. 10–12')
page=re.sub(r'<p>Every problem below is original[\s\S]*?</p>','<p>The bank contains four authentic examination translations and individually authored problem solutions. The retained full lesson also contains 18 derivation tutorials. Complete source-course exercise collections are not reproduced.</p>',page,count=1)
(R/'dist/chapters/a_asym.html').write_text(page,encoding='utf-8');(E/'a_asym-revision.json').write_text(json.dumps(dict(topicId='a_asym',baselineCommit=BASE,status='rewritten_pending_checks',questionCount=46,studentApproval=False,records=records),indent=2)+'\n')
print(json.dumps(dict(questions=46,solutionWords=sum(q['words'] for q in records),questionTables=sum(v.count('<table>') for a,b,v in replacements),nativeMathExpressions=page.count('<math'),finalRules=32),indent=2))

from pathlib import Path
import hashlib,json,re,subprocess,sys
from markdown_it import MarkdownIt
from read_correctness_bank import rows,ns
from space_number_prose import fix
R=Path(__file__).resolve().parents[1];E=R/'research/deep-library-revision';BASE='c09d0bb';sys.path.insert(0,str(R/'research/exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',mathml.markdown_math(s,md)).replace('<mo>-</mo>','<mo>−</mo>')
parts=re.split(r'^### Solution (\d+)\s*$',(E/'a_correct-solutions.md').read_text(encoding='utf8'),flags=re.M);answers={int(parts[i]):parts[i+1].strip()for i in range(1,len(parts),2)}
answers[11]=answers[11].replace('The old question title mentioning failure at an unreachable state is misleading for this particular predicate; the replacement title will distinguish an inductive but insufficient invariant.','A failure of postcondition implication must not be reported as a failure of invariant preservation.')
rows[10]['title']='Question 11. An inductive invariant can be too weak'
rows[15]['stem']=r'A pair of nonnegative integers starts at $(1,0)$. One reset chooses any finite nonnegative integer $B$ and changes it to $(0,B)$. Thereafter, while its second coordinate is positive, each step decrements that coordinate by exactly one. Execution stops at $(0,0)$. Which is true?'
page=subprocess.check_output(['git','show',BASE+':dist/chapters/a_correct.html'],cwd=R).decode('utf8').replace('\r\n','\n');entries=ns['questions'](page);assert len(entries)==len(answers)==54;edits=[];records=[]
for n,(a,z,attrs,q)in enumerate(entries,1):
 end=q.find('<details');prefix=q[:end];m=re.search(r'<p class="exam-provenance">[\s\S]*?</p>',prefix);assert m,n;prefix=prefix[:m.end()]
 prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-deep-index="{n}"',1);prefix=re.sub(r'data-answer="\d+"',f'data-answer="{rows[n-1]["answer"]}"',prefix)
 prefix=re.sub(r'<h3[^>]*>[\s\S]*?</h3>','<h3>'+rows[n-1]['title']+'</h3>',prefix,count=1)
 prefix+=render(rows[n-1]['stem'])+'<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+render('$'+v+'$'if re.fullmatch(r'\d+',v)else v)+'</div></div>'for i,v in enumerate(rows[n-1]['options'],1))+'</div>'
 model='<div class="question-specific-instruction"><h4>Inspect this question\'s exact transition or declared witness</h4><div class="concept-animation question-specific-animation" data-scenes="correctness-question-q'+str(n)+'"><p>The model states its input, checkpoint and premise. The complete written proof remains available without JavaScript.</p></div></div>'
 edits.append((a,z,prefix+'<details class="exam-solution"><summary>Read the full derivation, boundary cases and option diagnoses</summary>'+render(answers[n])+model+'</details></section>'))
 records.append({'index':n,'answer':rows[n-1]['answer'],'words':len(answers[n].split()),'solutionSha256':hashlib.sha256(answers[n].encode()).hexdigest()})
for a,z,v in reversed(edits):page=page[:a]+v+page[z:]
needle='<h2 id="contracts">';assert needle in page;page=page.replace(needle,render((E/'a_correct-deeper-instruction.md').read_text(encoding='utf8')).replace('<h2>','<h2 id="proof-construction">',1)+needle,1)
a=page.index('<h2 id="review">');z=page.index('<h2 id="laboratory">',a);page=page[:a]+render((E/'a_correct-final-decisions.md').read_text(encoding='utf8')).replace('<h2>','<h2 id="review">',1)+page[z:]
a=page.index('<h2 id="sources">');z=page.index('<h2 id="proof-construction">',a)
intro='''<h2 id="sources">Reviewed written courses and chapter boundaries</h2><p>Four current selected written scopes were actually read: CMU 15-122 Contracts (all 24 pages), Stanford CS161 Winter 2022 Lecture 2 (pages 1–4), MIT 6.042J Mathematics for Computer Science (physical pages 140–152), and Cornell CS2110 Fall 2026 Lecture 4 (all available written text). Cambridge Specification and Verification I remains historical formal-rule support; a fresh retrieval failed and is not counted as the fourth current reading.</p><p>The full original lesson is retained. All 54 bank answers now contain independent mathematical or conceptual derivations, and each has a question-specific model or explicitly declared witness. Six deeper proof constructions and forty complete final decisions supplement the lesson. <a href="../reviews/a_correct-current-sources.html">Read exact scopes, candidate comparison, source qualifications and original-exam reconciliation →</a></p><p>The identified candidate pool supports a documented selection, not a claim to have examined every course in the world. Finite mathematical checks supplement the proofs; they do not guarantee perfect performance on unseen questions.</p>'''
page=page[:a]+intro+page[z:]
page=page.replace('Student-approved chapter','Revised English review draft').replace('74 complete examination notes','40 complete examination decisions')
page=page.replace('</nav>','<a href="#proof-construction">Complete proof constructions</a></nav>',1)
notice='<aside class="deep-review-notice"><strong>Correctness revision · 14 October 2026.</strong> All 54 answers are rewritten; exact question models, complete proof constructions and final decisions are integrated. This edition remains a review draft. Mathematical, animation and rendered audits are recorded separately and must pass before the revision is marked checked.</aside>'
page=page.replace('<article',notice+'<article',1)
style=re.search(r'<style id="deep-review-layout">[\s\S]*?</style>',(R/'dist/chapters/d_logic.html').read_text(encoding='utf8'))[0];page=page.replace('</head>',style+'</head>')
page=re.sub(r'(semantic-diagrams\.js|concept-unified\.js|advanced-simulations\.js|concept-animation\.js|teaching-transitions\.js)(?:\?[^"\s>]*)?',r'\1?v=deep-correctness-23-20261014',page)
page=page.replace('This chapter remains a draft until your explicit approval.','This rewritten edition remains a review draft; standing authorization permits sequential work on later chapters.')
# Fresh selected Cornell reference is appended without erasing historical citations.
cornell='<p><strong>Cornell University, CS2110 Fall 2026, Lecture 4: Loops and Invariants.</strong> All available written lecture text reviewed; image-only scaffolds are excluded from reading credit. <a href="https://www.cs.cornell.edu/courses/cs2110/2026fa/lectures/lec04/">Official lecture →</a></p>'
page=page.replace('<h2 id="references">','<h2 id="references">',1);i=page.index('</h2>',page.index('<h2 id="references">'))+5;page=page[:i]+cornell+page[i:]
page=fix(page);(R/'dist/chapters/a_correct.html').write_text(page,encoding='utf8')
review=R/'dist/reviews/a_correct-current-sources.html';review.write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Algorithm Correctness · Current Source Review</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p><a href="../chapters/a_correct.html">← Algorithm correctness</a></p><article class="lesson">'+md.render((E/'a_correct-current-source-review.md').read_text(encoding='utf8'))+'</article></main></body></html>',encoding='utf8')
db=R/'dist/chapters/concept-unified.js';script=subprocess.check_output(['git','show',BASE+':dist/chapters/concept-unified.js'],cwd=R).decode('utf8');script=re.sub(r'''concept-animations\.json\?[^'"\s]+''', 'concept-animations.json?v=deep-correctness-23-20261014',script);db.write_text(script,encoding='utf8')
(E/'a_correct-revision.json').write_text(json.dumps({'topicId':'a_correct','baselineCommit':BASE,'status':'integrated_pending_model_and_rendered_audits','studentApproved':False,'questions':54,'answerWords':sum(r['words']for r in records),'proofConstructions':6,'finalDecisions':40,'records':records,'sourceReview':'research/deep-library-revision/a_correct-current-source-review.md'},indent=2)+'\n')
print({'questions':54,'mathExpressions':page.count('<math'),'answers':len(answers),'answerWords':sum(r['words']for r in records)})

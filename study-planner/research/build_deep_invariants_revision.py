from pathlib import Path
import ast,json,re,hashlib,subprocess,sys
from markdown_it import MarkdownIt
from read_invariants_bank import rows
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';BASE='01015cc80d725c367957cace974050c90f96b64b'
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'pure_read_helpers','exec'),ns)
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',mathml.markdown_math(s,md)).replace('<mo>-</mo>','<mo>−</mo>').replace('<mo>‖</mo>','<mo stretchy="false">‖</mo>')
parts=re.split(r'^### Solution (\d+)\s*$',(E/'d_invariants-solutions.md').read_text(encoding='utf-8'),flags=re.M);answers={int(parts[i]):parts[i+1].strip()for i in range(1,len(parts),2)}
raw=subprocess.check_output(['git','show',BASE+':dist/chapters/d_invariants.html']).decode().replace('\r\n','\n');entries=ns['questions'](raw);assert len(entries)==len(answers)==46
scenes={1:'mass-full,mass-unary',2:'split-order',3:'copy-6,copy-7',4:'parity-authentic',5:'lattice-witness',6:'prefix',7:'power-13',8:'bounded-reset',9:'laurent',10:'full-nineteen',11:'integer-certificate',12:'split-order',45:'power-13',46:'modular-orbit'}
for start,name in[(13,'weighted'),(17,'euclid'),(21,'two-counter'),(25,'mixed'),(29,'arithmetic'),(33,'ternary'),(37,'period'),(41,'affine')]:
 for j,n in enumerate([5,8]):scenes[start+j]=name+'-'+str(n)
edits=[];records=[]
def visual(names,cls='question-specific-animation'):return '<section class="concept-animation '+cls+'" data-scenes="'+','.join('invariants-question-'+n for n in names.split(','))+'"><p>The model states its exact input, move rule and checkpoint. Complete traces, aggregates and illustrative counterexamples are identified separately.</p></section>'
for n,(a,b,attrs,q)in enumerate(entries,1):
 end=q.find('<details');end=end if end>=0 else q.index('<p><strong>Correct option:');prefix=q[:end];c=rows[n-1];anchor='exam-provenance'if n<=44 else'exam-label';match=re.search(r'<p class="'+anchor+r'">[\s\S]*?</p>',prefix);assert match,(n,anchor)
 retained=prefix[:match.end()];stem=c['stem'];options=c['options']
 if n==45:stem=r'An iterative power algorithm starts $y=1,b=a,e=13$. While $e>0$, multiply $y$ by the old $b$ if $e$ is odd, always square $b$, then set $e=\lfloor e/2\rfloor$. How many multiplications execute?';options=['$5$','$6$','$7$','$8$']
 if n==46:stem=r'States are residue pairs modulo five. The only move adds $(1,2)$ and reduces both coordinates modulo five. Starting at $(0,0)$, which target is unreachable?';options=['$(1,2)$','$(2,4)$','$(3,4)$','$(4,3)$']
 if n==11:stem+=' The candidate preservation check ranges over all integer states.'
 if n==9:stem+=' Interpret the product as a Laurent polynomial, where negative integer exponents are permitted.'
 stem=stem.replace('in the positive-integer parameter domain, subject to the additional conditions stated above','for all positive integers satisfying the stated conditions')
 retained=retained.replace('A conserved difference in a doubling transition','An affine difference in a doubling transition')
 if n>=5:retained=re.sub(r'Pattern reference:[\s\S]*?This is an original problem, not a question from those booklets\.','Independently authored invariant or recursive-reasoning problem; no specific authentic source item is claimed for this mechanism.',retained)
 prefix=retained+render(stem)+'<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+render(v)+'</div></div>'for i,v in enumerate(options,1))+'</div>'
 prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-deep-index="{n}"',1)
 answer='Correct option: '+str(c['answer'])+'.\n\n'+answers[n];model=visual(scenes[n])if n in scenes else''
 edits.append((a,b,prefix+'<details class="exam-solution"><summary>Read the full derivation, conceptual proof and individual option diagnoses</summary>'+render(answer)+model+'</details></section>'))
 records.append(dict(index=n,answer=c['answer'],sourceId=attrs.get('data-source-id'),words=len(answers[n].split()),solutionSha256=hashlib.sha256(answers[n].encode()).hexdigest(),state='rewritten_pending_checks'))
page=raw
for a,b,v in reversed(edits):page=page[:a]+v+page[b:]
bridge=(E/'d_invariants-method-instruction.md').read_text()+'\n\n'+(E/'d_invariants-transfer-challenges.md').read_text();needle='<h2 id="proof-tutorials">';assert needle in page;page=page.replace(needle,render(bridge).replace('<h2>','<h2 id="mathematical-bridge">',1)+needle,1)
for n,names in{1:'forward-six,backward-six',2:'lattice-witness',3:'affine-5',4:'power-13,power-32',5:'mass-irregular',6:'mixed-challenge',7:'flat-acc',8:'ackermann',9:'horner',10:'population-min,population-max'}.items():
 a=page.index('<h3>Challenge '+str(n)+'.');z=page.index('</h3>',a)+5;page=page[:z]+visual(names,'transfer-specific-animation')+page[z:]
a=page.index('<h2 id="review">');z=page.index('<h2 id="laboratory">',a);page=page[:a]+render((E/'d_invariants-exam-rules.md').read_text()).replace('<h2>','<h2 id="review">',1)+page[z:]
for anchor,names in{'states':'true-not-closed','loops':'prefix,horner','rankings':'bounded-reset,two-counter-5','recursion':'split-order,ackermann','accumulators':'flat-acc'}.items():page=re.sub(r'(<section id="animation-'+anchor+r'"[^>]*data-scenes=")[^"]+',lambda m:m[1]+','.join('invariants-question-'+v for v in names.split(',')),page)
page=page.replace('Student-approved chapter','Revised English review draft').replace('15 examination notes','34 detailed examination decisions').replace('Iranian examination archives remain reserved for the final month.','Four authentic examination items are identified and their original scanned pages have been reread for this revision.').replace('This chapter has been approved by the student.','This rewritten edition remains a review draft; approval of an earlier edition is not transferred to the revision.').replace('The chapter has not been calibrated against the deferred Iranian examination archive; universal coverage, literal certainty, and performance on all future questions are not asserted.','Four authentic source items and independently authored questions are individually identified. Recorded finite checks and scoped source reading do not establish universal perfection or future examination performance.')
page=page.replace('The principal readings are four genuinely reviewed written university courses.','The principal readings are four genuinely reviewed written university courses. This revision freshly rechecks the recorded MIT, Stanford, CMU and Cambridge scopes and an additional independently authored Cornell lecture; the audit separates those new readings from historical wider exercise scopes.')
notice='<aside class="deep-review-notice"><strong>Invariants revision · 13 October 2026.</strong> All 46 bank answers are rewritten, with eight further mathematical constructions, ten solved synthesis challenges and 34 detailed examination decisions. The full lesson and all 49 tutorials remain. Mathematical and rendered checks are pending.</aside>';page=page.replace('<article',notice+'<article',1)
page=page.replace('</nav>','<a href="#mathematical-bridge">Deeper constructions</a></nav>',1)
style=re.search(r'<style id="deep-review-layout">[\s\S]*?</style>',(R/'dist/chapters/d_logic.html').read_text())[0];page=page.replace('</head>',style+'</head>')
page=re.sub(r'(semantic-diagrams\.js|concept-unified\.js|advanced-simulations\.js|concept-animation\.js|teaching-transitions\.js)(?:\?[^"\s>]*)?',r'\1?v=deep-invariants-19-20261013',page)
page=page.replace('href="d_invariants.css"','href="d_invariants.css?v=deep-invariants-19-20261013"')
from space_number_prose import fix
page=fix(page)
for letter in ['F','R']:
 page=page.replace('<span class="math-inline">'+letter+'</span>.',letter+'.')
(R/'dist/chapters/d_invariants.html').write_text(page,encoding='utf-8')
(E/'d_invariants-revision.json').write_text(json.dumps(dict(topicId='d_invariants',baselineCommit=BASE,status='rewritten_pending_mathematical_and_rendered_checks',studentApproval=False,questionCount=46,retainedFullTutorials=49,lectureAdditionSections=8,addedSolvedTransferChallenges=10,finalDetailedDecisions=34,records=records,questionModelPlacements=len(scenes),sourceReview='research/deep-library-revision/d_invariants-course-recheck.json'),indent=2)+'\n',encoding='utf-8')
print({'answers':46,'words':sum(v['words']for v in records),'questionModelPlacements':len(scenes),'math':page.count('<math')})

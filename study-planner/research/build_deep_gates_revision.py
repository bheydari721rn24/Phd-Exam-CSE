from pathlib import Path
import ast,hashlib,json,re,subprocess,sys
from markdown_it import MarkdownIt
from read_gates_bank import rows
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';BASE='6dc081117f8724d4eb940e959073eb30e3577727'
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'helpers','exec'),ns)
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',mathml.markdown_math(s,md)).replace('<mo>-</mo>','<mo>−</mo>')
parts=re.split(r'^## Q(\d+)\s*$',(E/'g_gates-solutions.md').read_text(),flags=re.M);answers={int(parts[i]):parts[i+1].strip()for i in range(1,len(parts),2)}
raw=subprocess.check_output(['git','show',BASE+':dist/chapters/g_gates.html']).decode().replace('\r\n','\n');entries=ns['questions'](raw);assert len(entries)==len(answers)==46
scenes={1:'nand',2:'mux',3:'ring-5-5',4:'sizing-cases',5:'nand-01',6:'majority',7:'hazard-rise',8:'arrival',9:'positive-and',10:'power',11:'rc-charge',12:'noise',45:'hazard-fall',46:'noise-bottleneck'}
for a,name,params in [(13,'and-tree',[5,8]),(17,'nand-and',[5,8]),(21,'xor-chain',[5,8]),(25,'mux-tree',[5,8]),(29,'ripple',[5,8]),(33,'scaling',[5,8]),(37,'ring',[5,7]),(41,'consensus',[5,8])]:
 for j,n in enumerate(params):scenes[a+j]=name+'-'+str(n)+('-2'if name=='ring'else'')
edits=[];records=[]
for n,(a,b,attrs,q)in enumerate(entries,1):
 end=q.find('<details');end=end if end>=0 else q.index('<p><strong>Correct option:');prefix=q[:end];c=rows[n-1]
 anchor='exam-provenance'if n<=44 else'exam-label';stop=re.search(r'<p class="'+anchor+r'">[\s\S]*?</p>',prefix).end();retained=prefix[:stop]
 figures=''.join(re.findall(r'<figure\b[\s\S]*?</figure>',prefix))if n in [1,2,3]else''
 stem=c['stem'];options=c['options']
 if n==45:stem=r'$F=ab+(\neg a)c$ has stable $b=c=1$ and $a$ falls at $0$ ns. The $ab$ output falls at $2$ ns and $(\neg a)c$ rises at $5$ ns. An OR with equal $1$ ns transport delay follows them. What is its output low-pulse width?';options=[r'$1$ ns',r'$2$ ns',r'$3$ ns',r'$4$ ns']
 if n==46:stem=r'A driver guarantees $V_{OL}\le0.2$ V and $V_{OH}\ge2.4$ V. A receiver accepts lows through $0.7$ V and highs from $2.0$ V. What is the smaller guaranteed noise margin?';options=[r'$0.2$ V',r'$0.4$ V',r'$0.5$ V',r'$0.7$ V']
 stem=stem.replace('in the positive-integer parameter domain, subject to the additional conditions stated above','for positive integers satisfying the stated conditions')
 if n>=5:retained=re.sub(r'Pattern reference:[\s\S]*?This is an original problem, not a question from those booklets\.','Original authored circuit or timing question; no specific authentic source item is asserted for this mechanism.',retained)
 prefix=retained+render(stem)+figures+'<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+render(v)+'</div></div>'for i,v in enumerate(options,1))+'</div>'
 key=int(re.search(r'Correct option:\s*(\d+)',answers[n])[1]);assert key==c['answer'];prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-deep-index="{n}"',1)
 visual='<section class="concept-animation question-specific-animation" data-scenes="'+('gates-question-cmos-3,gates-question-sizing-cases'if n==4 else'gates-question-'+scenes[n])+'" aria-label="Circuit or timing mechanism for question '+str(n)+'"><p>The model uses this question’s netlist, exact parameters or explicitly labeled symbolic sizing cases.</p></section>'if n in scenes else''
 edits.append((a,b,prefix+'<details class="exam-solution"><summary>Read the derivation, circuit interpretation and alternative diagnoses</summary>'+render(answers[n])+visual+'</details></section>'))
 records.append(dict(index=n,answer=key,sourceId=attrs.get('data-source-id'),words=len(answers[n].split()),solutionSha256=hashlib.sha256(answers[n].encode()).hexdigest(),state='rewritten_pending_checks'))
page=raw
for a,b,v in reversed(edits):page=page[:a]+v+page[b:]
needle='<h2 id="proof-tutorials">';assert needle in page
bridge=(E/'g_gates-method-instruction.md').read_text()+'\n\n'+(E/'g_gates-transfer-challenges.md').read_text();page=page.replace(needle,render(bridge).replace('<h2>','<h2 id="mathematical-bridge">',1)+needle,1)
page=page.replace('<h2 id="references">',render((E/'g_gates-exam-rules.md').read_text()).replace('<h2>','<h2 id="final-decisions">',1)+'<h2 id="references">',1)
for anchor,names in {'netlists':'nand,mux','completeness':'positive-and','mapping':'majority,positive-and','cmos':'cmos','timing':'arrival,ripple-5,ring-5-5','hazards':'hazard-rise,hazard-fall'}.items():page=re.sub(r'(<section id="animation-'+anchor+r'"[^>]*data-scenes=")[^"]+',lambda m:m[1]+','.join('gates-question-'+v for v in names.split(',')),page)
page=page.replace('Student-approved chapter','Revised English review draft').replace('16 examination notes','36 detailed final decisions')
page=re.sub(r'<p>The student (?:explicitly )?approved[\s\S]*?</p>','<p>This new edition remains a review draft; earlier approval does not approve these revisions.</p>',page)
page=page.replace('Archived Iranian entrance-exam questions remain reserved for the final month.','Authentic source questions are identified separately under the later examination-analysis instruction.')
old='<p>The candidate search covered eight universities:';a=page.index(old);b=page.index('</p>',a)+4
page=page[:a]+render('The historical eight-university candidate pool was reassessed for this revision. Four university scopes were freshly read: MIT, Cambridge, Stanford and UC Berkeley. MIT supplies switch and timing contracts; Cambridge supplies hazards and device-level qualifications; Stanford supplies connected schematics and load reasoning; Berkeley supplies an independent primitive-gate cross-check. Historical UCSD material remains supplemental, but fresh access failed and was not counted. The source audit records exact page scopes, access limits and source errors; it does not claim a worldwide course census.')+page[b:]
page=page.replace('<h3>Sources selected for this chapter</h3>','<h3>Freshly selected sources and retained historical inventory</h3>').replace('<table>','<p>The table preserves the earlier scoped inventory. The fresh selection above supersedes its earlier four-core ranking; UCSD is historical supplemental material.</p><table>',1)
notice='<aside class="deep-review-notice"><strong>Gate implementation revision · 13 October 2026.</strong> All 46 bank answers are rewritten, with seven mathematical teaching constructions, ten solved synthesis challenges and twenty additional detailed decisions. The complete lesson and all 36 tutorials remain. Mathematical and rendered checks are pending.</aside>'
page=page.replace('<article',notice+'<article',1);page=page.replace('<a href="#proof-tutorials">','<a href="#mathematical-bridge">Circuit and timing derivations</a> <a href="#final-decisions">Detailed final decisions</a> <a href="#proof-tutorials">',1)
audit='### Fresh source scope and independent corrections\n\n'+(E/'g_gates-course-recheck.json').read_text()
source_note=render('### Source corrections that affect the derivations\n\nStanford’s reader reverses CNF/DNF names on physical page 39 and pass-level directions in page 65 prose. Table 5.3 on page 76 prints 6.68 for the product of 4 and 1.57; the correct product is 6.28. Its unrestricted hazard-free wording is limited here to the stated two-level, single-input context. The Elmore sizing analysis additionally rechecks every switching case because the maximizing case can change after resizing. The four fresh university scopes and original source-page verification are recorded in the accompanying source audit.')
page=page.replace('<h2 id="references">',source_note+'<h2 id="references">',1)
style=re.search(r'<style id="deep-review-layout">[\s\S]*?</style>',(R/'dist/chapters/d_logic.html').read_text())[0];page=page.replace('</head>',style+'</head>')
page=re.sub(r'(semantic-diagrams\.js|concept-unified\.js)(?:\?[^"\s>]*)?',r'\1?v=deep-gates-16-20261013',page)
from space_number_prose import fix
page=fix(page).replace('AOI 21','AOI21').replace('OAI 21','OAI21');(R/'dist/chapters/g_gates.html').write_text(page,encoding='utf-8')
(E/'g_gates-revision.json').write_text(json.dumps(dict(topicId='g_gates',baselineCommit=BASE,status='rewritten_pending_model_and_rendered_checks',questionCount=46,studentApproval=False,retainedFullTutorials=36,lectureAdditionSections=7,addedSolvedTransferChallenges=10,finalDetailedDecisions=36,records=records,questionModelPlacements=len(scenes),sourceReview='research/deep-library-revision/g_gates-course-recheck.json'),indent=2)+'\n',encoding='utf-8')
print({'answers':46,'words':sum(x['words']for x in records),'questionModelPlacements':len(scenes),'math':page.count('<math')})

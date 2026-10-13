from pathlib import Path
import ast,json,re,hashlib,subprocess,sys
from markdown_it import MarkdownIt
from read_discrete_number_bank import rows
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';BASE='77f4b6dd3bbabb32ac75667b0a2f83f6f8518306'
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'pure_helpers','exec'),ns)
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',mathml.markdown_math(s,md)).replace('<mo>-</mo>','<mo>−</mo>')
parts=re.split(r'^### Solution (\d+)\s*$',(E/'d_number-solutions.md').read_text(),flags=re.M);answers={int(parts[i]):parts[i+1].strip()for i in range(1,len(parts),2)}
raw=subprocess.check_output(['git','show',BASE+':dist/chapters/d_number.html']).decode().replace('\r\n','\n');entries=ns['questions'](raw);assert len(entries)==len(answers)==47
scenes={1:'dyadic',2:'coefficient',3:'parity-count',4:'mixed-subsets',5:'parity-recurrence',6:'interval',7:'shared',8:'six,two-transient',9:'cancel',10:'factorial30',11:'units30',12:'diophantine',13:'cosets',46:'interval100',47:'deadline'}
for start,name,values in[(14,'linear',[5,8]),(18,'adjacent',[5,8]),(22,'factorial',[6,10]),(26,'divisor',[5,8]),(30,'square',[5,8]),(34,'totient',[5,8]),(42,'gcd',[5,8])]:
 for j,n in enumerate(values):scenes[start+j]=name+'-'+str(n)
 scenes[start+2]=name+'-'+str(values[0])+','+name+'-'+str(values[1]);scenes[start+3]=name+'-'+str(values[0])
for n in range(38,42):scenes[n]='three'
def visual(names,cls='question-specific-animation'):
 return '<section class="concept-animation '+cls+'" data-scenes="'+','.join('discrete-number-question-'+v for v in names.split(','))+'"><p>The input, residue domain and exact checkpoint are declared. A complete enumeration, a coordinate aggregate and an illustrative witness are identified separately.</p></section>'
edits=[];records=[]
for n,(a,b,attrs,q)in enumerate(entries,1):
 end=q.find('<details');end=end if end>=0 else q.index('<p><strong>Correct option:');prefix=q[:end];c=rows[n-1];anchor='exam-provenance'if n<=45 else'exam-label';match=re.search(r'<p class="'+anchor+r'">[\s\S]*?</p>',prefix);assert match,(n,anchor)
 prefix=prefix[:match.end()];stem=c['stem'];options=c['options']
 if n==46:stem=r'How many integers $0\le x\le100$ solve $6x\equiv8\pmod{14}$?';options=['7','13','14','15']
 if n==47:stem=r'What is the least nonnegative $x$ satisfying $x\equiv5\pmod{12}$ and $x\equiv11\pmod{18}$?';options=['11','17','29','35']
 if n==7:stem=stem.replace('solution and period','solution and smallest positive period')
 if n==13:stem=r'On $\mathbb Z_{12}$, define $xRy$ exactly when integer representatives satisfy $x-y\equiv0\pmod4$. What pair gives the size of every class and the number of classes?'
 stem=stem.replace('in the positive-integer parameter domain, subject to the additional conditions stated above','for all positive integers satisfying the stated conditions')
 if n>5:prefix=re.sub(r'Pattern reference:[\s\S]*?This is an original problem, not a question from those booklets\.','Independently authored number-theory problem. No particular authentic source question is claimed for this different mechanism.',prefix)
 prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-deep-index="{n}"',1);prefix=re.sub(r'data-answer="\d+"',f'data-answer="{c["answer"]}"',prefix)
 prefix+=render(stem)+'<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+render('$'+v+'$'if re.fullmatch(r'\d+',v)else v)+'</div></div>'for i,v in enumerate(options,1))+'</div>'
 edits.append((a,b,prefix+'<details class="exam-solution"><summary>Read the full derivation, completeness proof and individual option diagnoses</summary>'+render('Correct option: '+str(c['answer'])+'.\n\n'+answers[n])+visual(scenes[n])+'</details></section>'))
 records.append(dict(index=n,answer=c['answer'],sourceId=attrs.get('data-source-id'),words=len(answers[n].split()),solutionSha256=hashlib.sha256(answers[n].encode()).hexdigest(),state='rewritten_pending_checks'))
page=raw
for a,b,v in reversed(edits):page=page[:a]+v+page[b:]
bridge=(E/'d_number-method-instruction.md').read_text()+'\n\n'+(E/'d_number-transfer-challenges.md').read_text();needle='<h2 id="proof-tutorials">';assert needle in page;page=page.replace(needle,render(bridge).replace('<h2>','<h2 id="mathematical-bridge">',1)+needle,1)
for n in range(1,11):
 a=page.index('<h3>Challenge '+str(n)+'.');z=page.index('</h3>',a)+5;page=page[:z]+visual('challenge'+str(n),'transfer-specific-animation')+page[z:]
a=page.index('<h2 id="review">');z=page.index('<h2 id="laboratory">',a);page=page[:a]+render((E/'d_number-exam-rules.md').read_text()).replace('<h2>','<h2 id="review">',1)+page[z:]
for anchor,names in{'integer-equations':'diophantine','crt':'shared,adjacent-5'}.items():page=re.sub(r'(<section id="animation-'+anchor+r'"[^>]*data-scenes=")[^"]+',lambda m:m[1]+','.join('discrete-number-question-'+v for v in names.split(',')),page)
page=re.sub(r'(<section id="animation-powers"[^>]*data-scenes=")[^"]+',lambda m:m[1]+'modular-power,discrete-number-question-six,discrete-number-question-two-transient',page)
page=page.replace('Student-approved chapter','Revised English review draft').replace('15 examination notes','36 detailed examination decisions').replace('Iranian examination archives remain reserved for the final month.','Five authentic source questions are individually identified; their original PDF pages were visually reread.').replace('This chapter has been approved by the student.','This rewritten edition remains a review draft; earlier-edition approval is not transferred automatically.')
notice='<aside class="deep-review-notice"><strong>Number theory revision · 13 October 2026.</strong> All 47 bank answers are rewritten. Eight deeper constructions, ten solved transfer challenges and 36 complete examination decisions are added; the full lesson and all 40 tutorials remain. The original exponent and total in two authentic questions are corrected. Mathematical, animation and browser audits are pending.</aside>';page=page.replace('<article',notice+'<article',1)
page=page.replace('</nav>','<a href="#mathematical-bridge">Deeper constructions</a></nav>',1)
style=re.search(r'<style id="deep-review-layout">[\s\S]*?</style>',(R/'dist/chapters/d_logic.html').read_text())[0];page=page.replace('</head>',style+'</head>')
page=re.sub(r'(semantic-diagrams\.js|concept-unified\.js|advanced-simulations\.js|concept-animation\.js|teaching-transitions\.js)(?:\?[^"\s>]*)?',r'\1?v=deep-discrete-number-20-20261013',page);page=re.sub(r'href="d_number.css(?:\?[^"]*)?"','href="d_number.css?v=deep-discrete-number-20-20261013"',page)
from space_number_prose import fix
page=fix(page);(R/'dist/chapters/d_number.html').write_text(page,encoding='utf-8')
(E/'d_number-revision.json').write_text(json.dumps(dict(topicId='d_number',baselineCommit=BASE,status='rewritten_pending_mathematical_and_rendered_checks',studentApproval=False,questionCount=47,retainedFullTutorials=40,lectureAdditionSections=8,addedSolvedTransferChallenges=10,finalDetailedDecisions=36,records=records,questionModelPlacements=len(scenes),sourceReview='research/deep-library-revision/d_number-course-recheck.json'),indent=2)+'\n',encoding='utf-8');print({'answers':47,'words':sum(v['words']for v in records),'placements':len(scenes),'math':page.count('<math')})

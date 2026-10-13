from pathlib import Path
import ast,json,re,hashlib,subprocess,sys
from markdown_it import MarkdownIt
from read_algorithm_recurrence_bank import rows,ns
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';BASE='86f1b64def331f48c7f9bfd1a05cdc463e99faa1'
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',mathml.markdown_math(s,md)).replace('<mo>-</mo>','<mo>−</mo>')
parts=re.split(r'^### Solution (\d+)\s*$',(E/'a_recurrence-solutions.md').read_text(),flags=re.M);answers={int(parts[i]):parts[i+1].strip()for i in range(1,len(parts),2)}
page=subprocess.check_output(['git','show',BASE+':dist/chapters/a_recurrence.html']).decode().replace('\r\n','\n');entries=ns['questions'](page);assert len(entries)==len(answers)==53
scenes=dict(enumerate(['prefix','unequal','polylog','sqrt','pivot','product','parity','balanced32','cubes16','four-sqrt','prefix-three','repeated-root','odd-squares','quadratic','fib'],1));scenes.update({52:'slow',53:'reuse'})
for start,name in[(16,'affine'),(20,'balanced'),(24,'leaf'),(28,'chain'),(32,'squares-seed'),(36,'squares-zero'),(40,'weighted-index'),(44,'ternary'),(48,'double-log')]:
 scenes[start]=name+'-5';scenes[start+1]=name+'-8';scenes[start+2]=name+'-5,'+name+'-8';scenes[start+3]=name+'-5'
def visual(names,cls='question-specific-animation'):
 return '<section class="concept-animation '+cls+'" data-scenes="'+','.join('algorithm-recurrence-question-'+v for v in names.split(','))+'"><p>The input, base region, cost model and exact checkpoint are declared. Complete level aggregates, full state lists and illustrative tree fragments are distinguished explicitly.</p></section>'
records=[];edits=[]
for n,(a,z,attrs,q)in enumerate(entries,1):
 end=q.find('<details');end=end if end>=0 else q.index('<p><strong>Correct option:');prefix=q[:end];anchor='exam-provenance'if n<=51 else'exam-label';m=re.search(r'<p class="'+anchor+r'">[\s\S]*?</p>',prefix);assert m,(n,anchor);prefix=prefix[:m.end()];c=rows[n-1];stem=c['stem'];options=c['options']
 if n==52:stem=r'For integer $n>1$, let $T(n)=T(n-\lceil\sqrt n\rceil)+1$, with bounded constant base cost for $n\le1$. What is its tight order?';options=[r'$\Theta(\log n)$',r'$\Theta(\sqrt n)$',r'$\Theta(n)$',r'$\Theta(n\log n)$']
 if n==53:stem=r'A program requests the identical size-$n/2$ state twice, then performs $n$ local work. The second request reuses the first result with bounded lookup cost. What is the tight executed-work order?';options=[r'$\Theta(\log n)$',r'$\Theta(n)$',r'$\Theta(n\log n)$',r'$\Theta(n^2)$']
 stem=stem.replace('for all parameters in the positive-integer parameter domain, subject to the additional conditions stated above','for all positive integer indices satisfying the stated conditions')
 if n>7:prefix=re.sub(r'Pattern reference:[\s\S]*?This is an original problem, not a question from those booklets\.','Independently authored recurrence problem. It is not attributed to an unrelated authentic question.',prefix)
 prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-deep-index="{n}"',1)
 if 'data-answer='in prefix:prefix=re.sub(r'data-answer="\d+"',f'data-answer="{c["answer"]}"',prefix)
 else:prefix=prefix.replace('data-deep-index=',f'data-answer="{c["answer"]}" data-deep-index=',1)
 prefix+=render(stem)+'<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+render('$'+v+'$'if re.fullmatch(r'\d+',v)else v)+'</div></div>'for i,v in enumerate(options,1))+'</div>'
 edits.append((a,z,prefix+'<details class="exam-solution"><summary>Read the complete derivation, base checks and individual option diagnoses</summary>'+render('Correct option: '+str(c['answer'])+'.\n\n'+answers[n])+visual(scenes[n])+'</details></section>'))
 records.append(dict(index=n,answer=c['answer'],sourceId=attrs.get('data-source-id'),words=len(answers[n].split()),solutionSha256=hashlib.sha256(answers[n].encode()).hexdigest(),state='rewritten_pending_checks'))
for a,z,v in reversed(edits):page=page[:a]+v+page[z:]
bridge=(E/'a_recurrence-method-instruction.md').read_text()+'\n\n'+(E/'a_recurrence-transfer-challenges.md').read_text();needle='<h2 id="proof-tutorials">';assert needle in page;page=page.replace(needle,render(bridge).replace('<h2>','<h2 id="mathematical-bridge">',1)+needle,1)
for n in range(1,11):
 a=page.index('<h3>Challenge '+str(n)+'.');z=page.index('</h3>',a)+5;page=page[:z]+visual('harmonic-1,harmonic-2'if n==3 else'challenge'+str(n),'transfer-specific-animation')+page[z:]
a=page.index('<h2 id="review">');z=page.index('<h2 id="laboratory">',a);page=page[:a]+render((E/'a_recurrence-exam-rules.md').read_text()).replace('<h2>','<h2 id="review">',1)+page[z:]
page=page.replace('Student-approved chapter','Revised English review draft').replace('18 examination notes','40 detailed examination decisions').replace('Iranian examination archives remain deferred.','Seven authentic items are individually identified and freshly reconciled with their original PDF images.').replace('This chapter has been approved by the student.','This rewritten edition remains a review draft; earlier-edition approval is not transferred automatically.')
notice='<aside class="deep-review-notice"><strong>Recurrence revision · 13 October 2026.</strong> All 53 bank answers are rewritten. Eight deeper constructions, ten solved transfer challenges and forty detailed decisions are added. The complete lesson and all forty tutorials remain. Three original exam options are corrected. Mathematical and rendered checks are pending.</aside>';page=page.replace('<article',notice+'<article',1);page=page.replace('</nav>','<a href="#mathematical-bridge">Deeper constructions</a></nav>',1)
style=re.search(r'<style id="deep-review-layout">[\s\S]*?</style>',(R/'dist/chapters/d_logic.html').read_text())[0];page=page.replace('</head>',style+'</head>')
page=re.sub(r'(semantic-diagrams\.js|concept-unified\.js|advanced-simulations\.js|concept-animation\.js|teaching-transitions\.js)(?:\?[^"\s>]*)?',r'\1?v=deep-algorithm-recurrence-21-20261013',page)
page=re.sub(r'href="a_recurrence.css(?:\?[^"]*)?"','href="a_recurrence.css?v=deep-algorithm-recurrence-21-20261013"',page)
from space_number_prose import fix
page=fix(page);(R/'dist/chapters/a_recurrence.html').write_text(page,encoding='utf8')
(E/'a_recurrence-revision.json').write_text(json.dumps(dict(topicId='a_recurrence',baselineCommit=BASE,status='rewritten_pending_mathematical_and_rendered_checks',studentApproval=False,questionCount=53,retainedFullTutorials=40,lectureAdditionSections=8,addedSolvedTransferChallenges=10,finalDetailedDecisions=40,records=records,questionModelPlacements=len(scenes),sourceReview='research/deep-library-revision/a_recurrence-course-recheck.json'),indent=2)+'\n',encoding='utf8');print({'answers':53,'words':sum(v['words']for v in records),'placements':len(scenes),'math':page.count('<math')})

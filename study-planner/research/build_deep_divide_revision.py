from pathlib import Path
import re,json,hashlib,subprocess,sys
from markdown_it import MarkdownIt
from read_divide_bank import rows,ns
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';BASE='0cf6fb27e8d200bd1c49f2e22f6689dc84308e3b'
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):return re.sub(r'(<math\b[^>]*display="inline"[\s\S]*?</math>)',r'<span class="math-inline">\1</span>',mathml.markdown_math(s,md)).replace('<mo>-</mo>','<mo>−</mo>')
def visual(name):return '<section class="concept-animation question-specific-animation" data-scenes="divide-question-'+name+'"><p>The specific input, measured quantity and validity conditions are declared. Read the checkpoint explanation and use the controls to inspect the full trace.</p></section>'
parts=re.split(r'^### Solution (\d+)\s*$',(E/'a_divide-solutions.md').read_text(),flags=re.M);answers={int(parts[i]):parts[i+1].strip()for i in range(1,len(parts),2)}
page=subprocess.check_output(['git','show',BASE+':dist/chapters/a_divide.html']).decode().replace('\r\n','\n');entries=ns['questions'](page);assert len(entries)==len(answers)==46;edits=[];records=[]
rows[44].update(stem=r'Work modulo $17$ with length-four primitive root $\omega=4$. For coefficients $a=[1,2,0,0]$ and positive-exponent forward transform, what is $Y$?',options=[r'$[3,9,16,10]$',r'$[3,10,16,9]$',r'$[1,2,0,0]$',r'$[3,8,15,9]$'])
rows[45].update(stem=r'An integer coefficient lies in $[-10,10]$ and has residue $7$ modulo $17$. Is its exact value uniquely determined?',options=[r'Yes, it must be $7$.',r'Yes, it must be $-10$.',r'No, both $7$ and $-10$ fit.','No value in the range fits.'])
for n,(a,z,attrs,q)in enumerate(entries,1):
 end=q.find('<details');end=end if end>=0 else q.index('<p><strong>Correct option:');prefix=q[:end];anchor='exam-provenance'if n<=44 else'exam-label';m=re.search(r'<p class="'+anchor+r'">[\s\S]*?</p>',prefix);assert m,(n,anchor);prefix=prefix[:m.end()];c=rows[n-1];assert c['options'] and (c['canonical']or n>44),n
 prefix=prefix.replace('<section class="exam-question"',f'<section class="exam-question" data-deep-index="{n}"',1)
 if 'data-answer='in prefix:prefix=re.sub(r'data-answer="\d+"',f'data-answer="{c["answer"]}"',prefix)
 else:prefix=prefix.replace('data-deep-index=',f'data-answer="{c["answer"]}" data-deep-index=',1)
 if n>4:prefix=re.sub(r'Pattern reference:[\s\S]*?This is an original problem, not a question from those booklets\.','Independently authored mathematical and conceptual problem. It is not attributed to an unrelated authentic examination item.',prefix)
 prefix+=render(c['stem'])+'<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+render('$'+v+'$'if re.fullmatch(r'\d+',v)else v)+'</div></div>'for i,v in enumerate(c['options'],1))+'</div>'
 edits.append((a,z,prefix+'<details class="exam-solution"><summary>Read the complete mathematical derivation and individual option diagnoses</summary>'+render('Correct option: '+str(c['answer'])+'.\n\n'+answers[n])+visual('q'+str(n))+'</details></section>'))
 records.append(dict(index=n,answer=c['answer'],sourceId=attrs.get('data-source-id'),words=len(answers[n].split()),solutionSha256=hashlib.sha256(answers[n].encode()).hexdigest()))
for a,z,v in reversed(edits):page=page[:a]+v+page[z:]
bridge=render((E/'a_divide-method-instruction.md').read_text()+'\n\n'+(E/'a_divide-transfer-challenges.md').read_text()).replace('<h2>','<h2 id="mathematical-bridge">',1)
for label,count,prefix in[('Construction ',8,'construction'),('Challenge ',10,'challenge')]:
 for n in range(1,count+1):
  a=bridge.index('<h3>'+label+str(n)+'.');z=bridge.index('</h3>',a)+5;bridge=bridge[:z]+visual(prefix+str(n))+bridge[z:]
needle='<h2 id="proof-tutorials">';assert needle in page;page=page.replace(needle,bridge+needle,1)
a=page.index('<h2 id="review">');z=page.index('<h2 id="laboratory">',a);page=page[:a]+render((E/'a_divide-exam-rules.md').read_text()).replace('<h2>','<h2 id="review">',1)+page[z:]
page=page.replace('Student-approved chapter','Revised English review draft').replace('19 examination notes','40 complete examination decisions')
page=page.replace("Four principal written university sources are MIT 6.006, Stanford CS161, UC Berkeley's CS170-associated Algorithms reader and CMU 15-<span class=\"math-inline\">451/651</span>. A fifth genuinely reviewed course, ETH Zurich's Data Structures and Algorithms, supplies maximum-subarray material.","Four freshly reviewed written university scopes are MIT 6.006, UC Berkeley's CS170-associated Algorithms reader, CMU 15-451/651 and ETH Zurich's Data Structures and Algorithms. Stanford CS161 remains historical supporting reading; a fresh retrieval timed out and is not counted in the four-course review.")
notice='<aside class="deep-review-notice"><strong>Divide-and-conquer revision · 14 October 2026.</strong> All 46 bank answers are rewritten. Eight deeper constructions, ten fully solved transfer challenges and forty complete examination decisions supplement the full lesson and all 48 retained tutorials. Dedicated subject-specific models are included. Mathematical checks of the new text passed; independent animation and rendered audits remain in progress. This edition remains a review draft.</aside>'
page=page.replace('<article',notice+'<article',1).replace('</nav>','<a href="#mathematical-bridge">Deeper constructions and solved transfers</a></nav>',1)
style=re.search(r'<style id="deep-review-layout">[\s\S]*?</style>',(R/'dist/chapters/d_logic.html').read_text())[0];page=page.replace('</head>',style+'</head>')
page=re.sub(r'(semantic-diagrams\.js|concept-unified\.js|advanced-simulations\.js|concept-animation\.js|teaching-transitions\.js)(?:\?[^"\s>]*)?',r'\1?v=deep-divide-22-20261014',page)
page=page.replace('Page 3 was visually inspected.','The deterministic text was freshly read; the original diagram was not newly retrievable in this revision. The replacement geometric model is independently authored and audited separately.')
page=page.replace('PDF pages 1–9 and 12–36 read; printed pages 55–63 and 66–90.','All 36 physical PDF pages of available text were freshly read. Selected original diagrams on physical pages 1–2, 14–15, 17–19 and 31 were also visually inspected.')
page=page.replace('PDF pages 1–7 read. The note is dated','Historical PDF pages 1–7 reading; the latest retrieval timed out, so this is not counted as a freshly read source. The note is dated')
page=page.replace('This chapter remains a draft until your explicit approval.','This rewritten edition is a review draft; earlier-edition approval is not automatically transferred.')
page=page.replace('data-scenes="merge-recursion,merge"','data-scenes="merge-recursion,divide-question-q3"')
from space_number_prose import fix
page=fix(page);(R/'dist/chapters/a_divide.html').write_text(page,encoding='utf8')
(E/'a_divide-revision.json').write_text(json.dumps(dict(topicId='a_divide',baselineCommit=BASE,status='integrated_pending_animation_and_rendered_audits',studentApproval=False,questionCount=46,retainedFullTutorials=48,lectureAdditionSections=8,addedSolvedTransferChallenges=10,finalDetailedDecisions=40,records=records,sourceReview='research/deep-library-revision/a_divide-course-recheck.json'),indent=2)+'\n');print(dict(questions=46,answerWords=sum(r['words']for r in records),math=page.count('<math'),tutorials=len(re.findall(r'<h3>Tutorial \d+',page))))

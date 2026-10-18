"""Render the original English manuscript and actual-input visual teaching draft."""
from pathlib import Path
from html import escape as e
from markdown_it import MarkdownIt
import re,json,sys
R=Path(__file__).resolve().parents[1];B=R/'research';D=R/'dist/chapters'
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
from teaching_prose_spacing import fix
mathml.wrap_display=lambda s:s;mathml.SYMBOLS['Longrightarrow']='⇒'
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):return re.sub(r'<math\b[^>]*display="inline"[\s\S]*?</math>',lambda m:'<span class="pr-inline">'+m[0]+'</span>',mathml.markdown_math(s,md))
def player(ids,title):
 if isinstance(ids,str):ids=[ids]
 return '<section class="game-player" data-models="'+','.join(ids)+'"><h3>'+e(title)+'</h3>'+('<label>Compare a declared case <select data-case aria-label="'+e(title)+' case">'+''.join('<option value="'+x+'">'+e(next(m['title']for m in models if m['id']==x))+'</option>'for x in ids)+'</select></label>'if len(ids)>1 else'')+'<div class="game-controls"><button type="button" data-first>Restart</button><button type="button" data-prev>Previous</button><button type="button" data-play aria-pressed="false">Play</button><button type="button" data-next>Next</button><label>Checkpoint <input type="range" data-seek min="0" value="0" aria-label="'+e(title)+' checkpoint"></label><label>Step time <select data-speed><option value="1400">1.4seconds</option><option value="900" selected>0.9seconds</option><option value="500">0.5seconds</option></select></label></div><p class="game-counter"></p><div class="game-stage"></div><p class="game-caption" aria-live="polite"></p><p class="game-why"></p><p class="game-legend">Blue: MAX · red: MIN · teal: CHANCE · pale terminal numbers: supplied inputs · grey dashed branch: pruned without evaluation. “Working” is not an exact-value flag.</p><div class="game-final-print"></div></section>'
def table(headers,rows,caption):return '<figure class="game-table"><figcaption>'+e(caption)+'</figcaption><div class="game-table-scroll"><table><thead><tr>'+''.join('<th scope="col">'+e(h)+'</th>'for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+e(str(x))+'</td>'for x in row)+'</tr>'for row in rows)+'</tbody></table></div></figure>'
models=json.loads((B/'i_games-tree-models.json').read_text(encoding='utf8'))['models']
extras={
 7:table(['Lottery','Original expected utility','Transformed expected utility'],[['A','2.1','21'],['B','1.3','40.9']],'Outcome order stays the same; expected-utility order reverses.'),
 17:table(['Error bound','First action range','Second action range','Decision certificate'],[['0.5','[7.7,8.7]','[6.5,7.5]','First is strictly greater'],['0.7','[7.5,8.9]','[6.3,7.7]','Overlap: reversal possible']],'Compare entire uncertainty intervals, not only the central estimates.'),
 20:table(['Frontier','A continuation score','B continuation score','Selected action'],[['One ply','1','0','A'],['Two plies','−10','10','B'],['True terminals','0','−1','A']],'The finite counterexample uses different heuristic errors at different horizons.'),
 21:'<section class="game-chance-bounds"><h4>Reveal the probability-bound construction</h4><button type="button" data-bound-step>Next calculation</button><div class="bounds-stage"></div><p class="bounds-caption" aria-live="polite"></p></section>',
 23:table(['Observed bit','Action A','Action B','Best informed action'],[['0','8','2','A'],['1','0','6','B'],['Uninformed expectation','4','4','Either fixed action']],'Knowing the column changes which policies are feasible.'),
 26:'<section class="game-uct"><h4>Compare exploitation, uncertainty and the final action rule</h4><label>Exploration coefficient <input type="range" data-uct-c min="0" max="2" step="0.1" value="1" aria-label="UCT exploration coefficient"></label><div class="uct-stage"></div><p class="uct-caption" aria-live="polite"></p><p>Only the coefficient changes. Counts are fixed at parent100, A20visits/16wins and B5visits/3wins. An unvisited child uses a separate initial-exploration rule.</p></section>',
 27:table(['Selecting player','Before (visits,reward sum)','After MAX win','After draw'],[['MAX','(20,12)','(21,13)','(21,12.5)'],['MIN','(8,3)','(9,3)','(9,3.5)'],['MAX','(3,2)','(4,3)','(4,2.5)']],'Each selected edge updates once, in its controlling player’s reward coordinates.'),
 30:table(['Decision','Candidate vectors','Selecting coordinate','Returned vector'],[['Left player2','(9,0,2) or (1,5,1)','Second','(1,5,1)'],['Right player2','(6,3,0) or (4,2,10)','Second','(6,3,0)'],['Root player1','(1,5,1) or (6,3,0)','First','(6,3,0)']],'A propagated vector belongs to one selected continuation.'),
 31:table(['MAX symbol / MIN symbol','First','Second'],[['First','1','−1'],['Second','−1','1']],'With simultaneous hidden actions the mixed value is0; with an observed first action MIN enforces−1.'),
 35:table(['Requested horizon','First action','Second action','Exact surrogate value'],[['One ply','10','0','10'],['Two plies','−5','2','2']],'An exact result at a different horizon need not equal the requested recurrence.'),
 38:table(['Comparison data','Incumbent','Candidate first leaf','Valid MIN cutoff?'],[['Exact','0.30004','0.30005','No'],['Rounded to three decimals','0.300','0.300','False equality introduced']],'Formatting must not replace the mathematical comparison inputs.'),
 49:table(['MIN row / event column','0','1','Unobserved expectation'],[['A','8','0','4'],['B','0','8','4'],['Observed best MIN reply','B gives0','A gives0','0']],'Moving MIN after the random observation changes its available policies.')}
mapping={1:'q1',2:['bins-min','bins-chance'],3:'bins-coin',4:'q4',5:'q5',6:'q6',9:['q9-x2','q9-x4','q9-x6','q9-x10'],10:['q10-x5','q10-x6','q10-x8'],11:'q11',12:'q12',13:'q13',16:'q16',24:'q24',40:'q40'}
raw=(B/'i_games.en.md').read_text(encoding='utf8').split('\n',1)[1]
raw=raw.split('## 19. Remaining manuscript components',1)[0]
raw=raw.replace('Authoring draft. The text is being developed and checked; the complete problem, visual, original-examination and browser gates have not passed. This manuscript is not yet an additional delivered library chapter.','Author-review draft. Study the explanations before using the worked-problem bank. Each tree player explains a declared example; the laboratory controls do not test or grade the learner.')
lesson=''
for part in re.split(r'(?=^## )',raw,flags=re.M):
 lesson+=render(part)
 if part.startswith('## 4.'):lesson+=player('intro','Back up the supplied tree and distinguish the guarantee')
bank=(B/'i_games-problems.en.md').read_text(encoding='utf8');questions=[]
lesson+='<section id="questions"><h2>50mathematical and conceptual problems with complete teaching solutions</h2>'+render(bank.split('## Problem1.')[0]if'## Problem1.'in bank else bank.split('## Problem 1.')[0].split('\n',1)[1])
for number,title,body in re.findall(r'^## Problem (\d+)\. (.+)\n([\s\S]*?)(?=^## Problem |\Z)',bank,re.M):
 n=int(number);stem,answer=body.strip().removeprefix('**Question.** ').split('**Solution.** ',1)
 questions.append({'id':'IG'+number.zfill(2),'title':title,'stem':stem,'solution':answer,'provenance':'Course attribution appears explicitly in the question when applicable; otherwise original.'})
 lesson+='<section class="exam-question" id="problem-'+number+'" data-source-id="IG'+number.zfill(2)+'"><h3>Problem '+number+'. '+e(title)+'</h3>'+render(stem)+'<details class="exam-solution"><summary>Read the complete derivation, interpretation and checks</summary>'+render(answer)+(player(mapping[n],'Walk through Problem'+number+' with its actual inputs')if n in mapping else'')+extras.get(n,'')+'</details></section>'
assert len(questions)==50
lesson+='</section><section id="authentic"><h2>Two original MS examination reconstructions</h2>'
archive=(B/'i_games-authentic.en.md').read_text(encoding='utf8')
lesson+=render(archive.split('## Authentic 1.')[0].split('\n',1)[1])
for n,title,body in re.findall(r'^## Authentic (\d+)\. (.+)\n([\s\S]*?)(?=^## Authentic |\Z)',archive,re.M):
 stem,answer=body.split('**Solution.** ',1)
 lesson+='<section class="exam-question authentic-question" id="authentic-'+n+'"><h3>'+e(title)+'</h3>'+render(stem)+'<details class="exam-solution"><summary>Read the full original-tree trace and boundary argument</summary>'+render(answer)+player('authentic-1403'if n=='1'else['authentic-1404-original','authentic-1404-lower-x','authentic-1404-y-equality','authentic-1404-x-too-large','authentic-1404-y-too-large'],'Inspect the original tree and declared variations')+'</details></section>'
lesson+='</section><section id="final-rules">'+render((B/'i_games-review.en.md').read_text(encoding='utf8').split('\n',1)[1])+'</section>'
audit=(B/'i_games-source-audit.md').read_text(encoding='utf8');refs=audit.split('## Exact references\n',1)[1]
lesson+='<section id="references"><h2>References and exact written sources</h2>'+render(refs)+'</section>'
payload=json.dumps({'models':models},separators=(',',':')).replace('<','\\u003c')
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Adversarial Search and Pruning</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="i_games.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#library">Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Artificial intelligence · author-review draft</p><h1>Adversarial Search and Pruning</h1><p>Strategies, exact certificates, uncertainty and computation</p><p>18teaching sections · 50fully solved mathematical/course problems · 2original MS examination reconstructions · 60final decisions</p><p>Author-reviewed edition · mathematical and interactive checks recorded · student approval pending.</p><p><a href="../reviews/i_games-sources.html">Written-source comparison and actual reading</a></p><p><a href="../reviews/i_games-quality.html">Mathematical, diagram and browser review</a></p></header><nav class="toc" aria-label="Chapter contents"><a href="#lesson">Teaching</a><a href="#questions">50 worked problems</a><a href="#authentic">Original examinations</a><a href="#final-rules">Summary and decisions</a><a href="#references">References</a></nav><article class="lesson" id="lesson">'''+lesson+'''</article></main><script type="application/json" id="games-model-data">'''+payload+'''</script><script src="i_games.js"></script></body></html>'''
(D/'i_games.html').write_text(fix(page),encoding='utf8')
(B/'i_games-questions.json').write_text(json.dumps(questions,indent=2)+'\n',encoding='utf8')
review='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Adversarial search source review</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p><a href="../chapters/i_games.html">Read the current draft</a></p>'+render(audit)+'</main></body></html>'
(R/'dist/reviews/i_games-sources.html').write_text(fix(review),encoding='utf8')
print({'originalOrCourseProblems':len(questions),'authenticProblems':2,'treePlacements':page.count('class="game-player"'),'treeModels':len(models),'htmlBytes':len(page.encode()),'state':'draft_final_review_pending_not_counted'})

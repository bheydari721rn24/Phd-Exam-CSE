"""Assemble original deep instruction, full solutions and actual-input CSP teaching aids."""
from pathlib import Path
from html import escape as e
from urllib.parse import quote
import json,re,sys
from markdown_it import MarkdownIt
R=Path(__file__).resolve().parents[1];B=R/'research';D=R/'dist/chapters'
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
from teaching_prose_spacing import fix
mathml.wrap_display=lambda s:s
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def written_math(s):
 """Format remaining explicit mathematical expressions, preserving existing TeX, links and code."""
 parts=re.split(r'(\$\$[\s\S]*?\$\$|\$[^$\n]+\$|```[\s\S]*?```|`[^`\n]+`|\[[^\]\n]+\]\([^\n]+?\))',s)
 atom=r'(?:[A-Za-z](?:_[A-Za-z0-9]+|[1-4])?|[0-9]+|\{[A-Za-z0-9, ]+\})'
 patterns=[r'O\([A-Za-z0-9δ²³⁴^+ −\-]+\)',r'(?<![A-Za-z0-9_/])'+atom+r'(?:\s*(?:!=|<=|>=|=|≠|≤|≥|<|>)\s*'+atom+r')+(?![A-Za-z0-9_])',r'\b[a-z]_[a-z0-9]+\b',r'\b[A-Z][1-4]\b',r'\b(?:[a-zδ]+[²³⁴][a-zδ]*|δd|d−[12]|n\+1)\b',r'\([0-9]+(?:,[0-9]+)+\)',r'\{[0-9]+(?:,[0-9]+)*\}']
 for i in range(0,len(parts),2):
  t=parts[i];slots=[]
  def hold(m):
   f=m[0].replace('²','^2').replace('³','^3').replace('⁴','^4').replace('−','-').replace('!=',r'\ne ').replace('<=',r'\le ').replace('>=',r'\ge ')
   f=re.sub(r'\b([A-Z])([1-4])\b',r'\1_\2',f).replace('{',r'\{').replace('}',r'\}')
   f=f.replace('log',r'\log ')
   slots.append('$'+f+'$');return 'CSPFORMULA'+str(len(slots)-1)+'END'
  for p in patterns:t=re.sub(p,hold,t)
  for j,v in enumerate(slots):t=t.replace('CSPFORMULA'+str(j)+'END',v)
  parts[i]=t
 return ''.join(parts)
def render(s):return re.sub(r'<math\b[^>]*display="inline"[\s\S]*?</math>',lambda m:'<span class="pr-inline">'+m[0]+'</span>',mathml.markdown_math(written_math(s),md))
def player(ids,title):return '<section class="csp-player" data-models="'+','.join([ids]if isinstance(ids,str)else ids)+'" data-title="'+e(title,quote=True)+'"></section>'
def special(name):return '<section class="csp-special" data-special="'+name+'"></section>'
def table(headers,rows,caption):return '<figure class="csp-table"><figcaption>'+e(caption)+'</figcaption><table><thead><tr>'+''.join('<th>'+e(x)+'</th>'for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+e(str(x))+'</td>'for x in row)+'</tr>'for row in rows)+'</tbody></table></figure>'
models=json.loads((B/'i_csp-models.json').read_text(encoding='utf8'))
bank=(B/'i_csp-problems.en.md').read_text(encoding='utf8');questions=[];bankhtml=''
mapping={2:('queens',None),3:('sum-four',None),4:('strict-4',None),5:('holes',None),6:('mit-colors',None),7:(['cycle-3','cycle-4'],None),8:('cycle-4',None),9:(['chain-fc','chain-mac'],None),10:('rollback',None),12:('lcv',None),13:('conjunction',None),14:('asymmetric',None),15:('strict-3',None),19:('tree',None),20:('star',None),22:('triangle-cutset',None),23:(['k4-root','k4-cutset'],None),25:('hall','special'),26:('hall-impossible',None),29:('path-consistency',None),30:('queens','special'),42:(['scope-root','scope-fail'],None)}
extras={
 1:table(['Object','Calculation','Count'],[['Complete tuples','3^5',243],['Action-order paths','5! ×3^5',29160],['Distinct partial maps','4^5',1024],['Fixed-order nodes','1+3+9+27+81+243',364]],'Count sets with different meanings.'),
 11:table(['Variable','Domain size','Unassigned neighbors','Selection'],[['A',2,'B,C','Second-step MRV tie'],['B',2,'A,C,E','Wins the second-step degree tie'],['C',3,'A,B,E,F','Not in the minimum-size tie'],['D',1,'none','First selection'],['E',4,'B,C','Not in MRV tie'],['F',4,'C','Not in MRV tie']],'The exact six-variable heuristic input.'),
 12:table(['Candidate','Y survivors','Z survivors','Deleted values','Affected neighbors','Completions'],[['a','1','1,2,3,4',3,1,4],['b','2,3,4','2,3,4',2,2,9]],'Value-count and neighbor-count policies rank these candidates differently.'),
 19:table(['Message','At parent color1','At parent color2','At parent color3'],[['C leaf to B',2,2,2],['B subtree to A',4,4,4],['Sum at root','4+4+4=12','','']],'Messages sum compatible alternatives and multiply independent child subtrees.'),
 22:table(['A color','B,C completions','Branch count'],[['1','(2,3),(3,2)',2],['2','(1,3),(3,1)',2],['3','(1,2),(2,1)',2]],'Conditioning removes one triangle vertex and leaves a supported edge.'),
 23:table(['Cutset assignment class','Number','Reason for rejection'],[['Same colors',3,'Internal cutset edge violated'],['Distinct colors',6,'Residual endpoints forced to the same third color']],'All nine cutset candidates fail for explicit reasons.'),
 27:table(['Hidden tuple state','X projection','Y projection','Z projection'],[['h0',0,0,0],['h1',0,1,1],['h2',1,0,1],['h3',1,1,0]],'A hidden state selects one whole tuple, preserving even parity.'),
 29:table(['Allowed X,Y pair','Z required by Y=Z','Z required by X!=Z','One common witness?'],[['(0,0)',0,1,'No'],['(1,1)',1,0,'No']],'Path consistency needs a joint extension of each allowed pair.'),
 33:table(['Assignment','First hard factor','Second hard factor','Agreement factor','Red factor','Product'],[['BBB',1,1,3,1,3],['BBR',1,1,2,2,4],['Every other tuple','0 or second0','','','','0']],'Explicit weighted-factor arithmetic.'),
 34:table(['Depth','X=0 branch','X=1 branch','Width-one decision'],[['1','weight3','weight2','Keep X=0; discard X=1'],['2','Both Y choices forbidden','Y=0 would succeed','No retained feasible completion']],'The factor is scored only when its scope is fully assigned; no lookahead is assumed.'),
 36:table(['Event','Conflict set','Next relevant decision'],[['Exhaust6','{4,1,0}','4'],['Merge into4','{2,0} union{1,0} = {2,1,0}','2 if4 later exhausts']],'The zero sentinel is not a decision variable.'),
 45:table(['A,B,C','A != B','B = C','At most one room2'],[['2,1,1','yes','yes','yes'],['1,2,2','yes','yes','no']],'Exact room assignments after the two pair relations.'),
 46:table(['P slot','Q slot','Slot-variable tuple'],[[1,2,'(P,Q,empty)'],[1,3,'(P,empty,Q)'],[2,3,'(empty,P,Q)']],'The three schedules form a bijection across the two encodings.'),
 49:table(['Cycle length','Two colors','Three colors'],[[3,0,6],[4,2,18],[5,0,30],[6,2,66]],'The closing-edge condition depends on parity and joint structure, not only domain size.')}
for ident,title,body in re.findall(r'^## (IC\d+) \| (.+)\n([\s\S]*?)(?=^## IC|\Z)',bank,re.M):
 origin,rest=body.strip().removeprefix('**Origin.** ').split('**Question.** ',1);stem,solution=rest.split('**Solution.** ',1);n=int(ident[2:]);questions.append(dict(id=ident,title=title,origin=origin.strip(),stem=stem.strip(),solution=solution.strip()))
 visual=''
 if n in mapping:
  mid,kind=mapping[n]
  visual=special(mid)if kind=='special'or mid=='queens'else player(mid,'Inspect the actual inputs of '+ident)
 bankhtml+='<section class="exam-question" id="'+ident+'" data-source-id="'+ident+'"><h3>'+e(ident+' · '+title)+'</h3><div class="source-label">'+render(origin)+'</div>'+render(stem)+'<details class="exam-solution"><summary>Read the complete mathematical derivation and interpretation</summary>'+render(solution)+visual+extras.get(n,'')+'</details></section>'
assert len(questions)==50
(B/'i_csp-questions.json').write_text(json.dumps(questions,indent=2)+'\n',encoding='utf8')
auth=json.loads((B/'i_csp-evidence/i_csp-authentic-research.json').read_text(encoding='utf8'));authhtml='<section id="authentic"><h2>Four original MS examination questions, with source qualifications</h2><p>Translations preserve the original choices. Answers are independently derived; no official answer key was verified. No doctoral CSP item was verified in the bounded archive pass.</p>'
authrecords=[]
map_svg='''<figure class="csp-map"><svg viewBox="0 0 300 300" role="img" aria-label="Reconstructed original five-region map"><path d="M20 20H280V280H20Z" fill="#f3f7f8" stroke="#4a6c79" stroke-width="2"/><path d="M160 20H280V150H225V80H160Z" fill="#f4d9d6"/><path d="M225 150H280V280H160V220H225Z" fill="#f8e9ae"/><path d="M20 150H85M160 20V80M160 220V280M225 150H280" fill="none" stroke="#4a6c79" stroke-width="2"/><rect x="85" y="80" width="140" height="140" fill="white" stroke="#4a6c79" stroke-width="2"/><g font-family="STIX Two Math" font-size="24" text-anchor="middle" fill="#214553"><text x="155" y="157">A</text><text x="53" y="102">B</text><text x="53" y="230">C</text><text x="247" y="60">E</text><text x="247" y="247">D</text></g></svg><figcaption>Original adjacency reconstructed from the inspected map: only shared boundary segments count. D is yellow; E is red.</figcaption></figure>'''
for item in auth['items']:
 ident=item['id'];source=item['source'];url='https://github.com/bheydari721rn24/Phd-Exam-CSE/blob/'+source['commit']+'/'+quote(source['repo_path'],safe='/')
 choices=[]
 for c in item['choices']:
  if 'X'in c:text='; '.join('$D_'+v+'='+r'\{'+','.join(map(str,c[v]))+r'\}$'for v in 'XYZW')
  else:text=c['text'];text=re.sub(r'O\(([^)]+)\)',r'$O(\1)$',text)
  choices.append(str(c['number'])+'. '+text)
 stem=item['statement']+'\n\n'+'\n'.join(choices)
 solution='\n\n'.join('**Step '+str(i+1)+'.** '+step for i,step in enumerate(item['solution_steps']))
 if ident.endswith('1402_Q74'):solution+='\n\n**Direction qualification.** The intended choice is2 under the usual directed-arc convention. If an undirected edge counts both orientations together, the exact numerical bound is2d, not d. The source wording alone must not hide that distinction.'
 if item.get('scope_note'):solution+='\n\n**Source qualification.** '+item['scope_note']
 solution+='\n\n**Derived selection:** option '+str(item['answer_option'])+'. This is an independent derivation, not a verified official key.'
 visual=player('auth-numeric','Reproduce the numeric question after its unary filter')if ident.endswith('1404_Q75')else map_svg+player('auth-map','Separate residual degree from three-color propagation')if ident.endswith('1404_Q73')else player(['scope-root','scope-fail','cycle-3'],'Check both scope and local-consistency distractors')if ident.endswith('1402_Q74')else player('tree','Inspect tree supports; read the required structural premise')
 authhtml+='<section class="exam-question authentic-question" id="'+ident+'"><h3>'+e(ident+' · '+item['topic'])+'</h3><p class="source-label"><a href="'+e(url)+'">Original pinned PDF, booklet '+e(item['booklet'])+', page '+str(source['pdf_page'])+'</a>. Independent answer; official key unverified.</p>'+render(stem)+'<details class="exam-solution"><summary>Read all steps, distractor checks and original-wording qualifications</summary>'+render(solution)+visual+'</details></section>'
 authrecords.append(dict(id=ident,source=source,stem=stem,solution=solution,answerOption=item['answer_option']))
authhtml+='</section>';(B/'i_csp-authentic.json').write_text(json.dumps(authrecords,indent=2)+'\n',encoding='utf8')
raw=(B/'i_csp.en.md').read_text(encoding='utf8').split('\n',1)[1]
lab='''<section class="csp-lab" id="laboratory"><h3>Editable exact binary-relation laboratory</h3><p>This is a teaching instrument, not a quiz. Supply at most six variables with at most five distinct integer values each, from −9 through9. Enter explicit allowed pairs; restrictions already applied to one variable belong in its domain. Repeated declarations on a pair are conjoined. The solver reports local consistency or a failure certificate; it does not call nonempty AC domains a solution.</p><label>Load a declared example <select data-preset aria-label="CSP laboratory example"></select></label><p><label for="csp-input">Finite domains and allowed pair tables</label></p><textarea id="csp-input" spellcheck="false" aria-label="CSP JSON input"></textarea><p><button type="button" data-run>Run exact AC-3</button></p><p class="csp-error" role="status"></p><div class="csp-lab-result"></div></section>'''
replace={'queens':special('queens'),'equality-chain':player(['chain-fc','chain-mac'],'Compare one-layer forward checking and propagation'),'sum-four':player('sum-four','Follow each tail candidate and its head witness'),'strict-chain':player('strict-3','See how a changed head requeues an earlier arc'),'odd-cycle':player(['cycle-3','cycle-4'],'Identical local domains can hide different global answers'),'rollback':player('rollback','Failure, full restoration and a successful sibling'),'hall':special('hall'),'questions':bankhtml+authhtml,'review':render((B/'i_csp-review.en.md').read_text(encoding='utf8').split('\n',1)[1]),'reference-code':'<p>The following complete reference uses integer-coded domains, one conjoined table per pair, explicit initial-domain guards and branch copies. Python hash tables give expected constant-cost membership; the asymptotic discussion separately states its lookup assumptions. The browser laboratory independently implements the same finite support semantics.</p>'+render('```python\n'+(B/'csp_exact.py').read_text(encoding='utf8')+'\n```')+lab}
lesson=render(raw)
factor='''<figure class="csp-special"><h3>A higher-arity factor keeps a joint tuple</h3><svg viewBox="0 0 500 230" role="img" aria-label="Three variables incident to one parity factor"><g stroke="#7d9eaa" stroke-width="2"><path d="M100 74L220 115M250 74V85M400 74L280 115" fill="none"/></g><g fill="#eaf3f4" stroke="#8baeb9"><circle cx="100" cy="50" r="24"/><circle cx="250" cy="50" r="24"/><circle cx="400" cy="50" r="24"/><rect x="220" y="85" width="60" height="60" rx="3" fill="#fff1d8"/></g><g text-anchor="middle"><text x="100" y="57">X</text><text x="250" y="57">Y</text><text x="400" y="57">Z</text><text x="250" y="122">f</text><text x="250" y="185" class="small">Allowed tuples: 000, 011, 101, 110</text><text x="250" y="212" class="small">One factor tests all three coordinates jointly.</text></g></svg><figcaption>Factor edges indicate participation in one relation. They are not three independently chosen binary projections.</figcaption></figure>'''
lesson=lesson.replace('<h2>5. Why assignment order',factor+'<h2>5. Why assignment order')
for key,value in replace.items():lesson=lesson.replace('<!-- CSP:'+key+' -->',value)
assert '<!-- CSP:'not in lesson
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Constraint Satisfaction, Propagation, and Structured Search</title><link rel="stylesheet" href="chapter.en.css"><link rel="stylesheet" href="i_csp.css"></head><body><main class="chapter"><p><a href="../index.html#library">Weekly plan and chapter library</a></p><header class="hero"><p class="eyebrow">Artificial intelligence · author-review draft</p><h1>Constraint Satisfaction, Propagation, and Structured Search</h1><p>Models, support witnesses, proofs, algorithms and exact scope</p><p>25 teaching sections · 50 original/course problems · 4 original MS items · 64 final examination decisions</p><p>Six written university scopes synthesized; four complementary primary offerings. Source and test boundaries are explicit.</p><p><a href="../reviews/i_csp-sources.html">Written-source comparison</a> · <a href="../reviews/i_csp-quality.html">Mathematical and visual review</a></p></header><nav class="toc" aria-label="Chapter contents"><a href="#lesson">Teaching</a><a href="#IC01">Worked problems</a><a href="#authentic">Original examinations</a><a href="#laboratory">Exact laboratory</a><a href="#final-review">Summary and decisions</a></nav><article class="lesson" id="lesson">'''+lesson+'''</article></main><script type="application/json" id="csp-model-data">'''+json.dumps(models,separators=(',',':')).replace('<','\\u003c')+'''</script><script src="i_csp.js"></script></body></html>'''
page=page.replace('<h2>27. Complete summary','<span id="final-review"></span><h2>27. Complete summary')
(D/'i_csp.html').write_text(fix(page),encoding='utf8')
for name in ['source','quality']:
 path=B/('i_csp-'+name+'-audit.md')
 if not path.exists():continue
 p='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Constraint satisfaction '+name+' review</title><link rel="stylesheet" href="../chapters/chapter.en.css"><link rel="stylesheet" href="../chapters/i_csp.css"></head><body><main class="chapter"><p><a href="../chapters/i_csp.html">Read the chapter</a></p><article class="lesson">'+render(path.read_text(encoding='utf8'))+'</article></main></body></html>'
 (R/'dist/reviews'/('i_csp-'+('sources'if name=='source'else'quality')+'.html')).write_text(fix(p),encoding='utf8')
print({'questions':54,'models':len(models['models']),'players':page.count('class="csp-player"'),'specials':page.count('class="csp-special"'),'htmlBytes':len(page.encode())})

from pathlib import Path
import json,hashlib,subprocess,sys,ast
B=Path(__file__).resolve().parent;R=B.parent;E=B/'p_recursion-evidence';E.mkdir(exist_ok=True)
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
qs=[];rules=[]
for block in (B/'p_recursion-problems.en.txt').read_text(encoding='utf-8').split('@@ ')[1:]:
 h,body=block.split('\n',1);a=h.split('|');stem,tail=body.split('---SOLUTION---');sol,rule=tail.split('---RULE---');q=dict(id='p-recursion-original-'+a[0],title=a[1],origin=a[2],stem=stem.strip(),solution=sol.strip())
 if len(a)>3:q['modelId']=a[3]
 qs.append(q);rules.append(a[0]+'. **'+a[1]+'.** '+rule.strip())
assert len(qs)==80
save(B/'p_recursion-questions.json',qs);(B/'p_recursion-review.en.md').write_text('\n\n'.join(rules)+'\n',encoding='utf-8')
q=next(x for x in json.loads((B/'p_arrays-authentic.json').read_text())if x['id']=='MS_CS_1393_Q167')
q['options']=['`if(n<0)return; b[i]=a[n]; store(n-2,i+1);`','`if(n<0)return; b[i+1]=a[n]; store(n-2,i+1);`','`if(n<0)return; b[i]=a[n]; store(n-2,i+2);`','`if(n<0)return; b[i+1]=a[n]; store(n-1,i+2);`']
q['verification']='Original PDF page 34 visually rechecked on 9 October 2026. Option guards and indices corrected from the printed page for this new adaptation. Explicit bridge revisit, not a new unique archive item.'
q['modelId']='stride-seven';q['visualQualification']='The animation specializes the general contract to N=7; the symbolic proof covers general N.'
q['solution']+='\n\n**Exact recursion counts.** There are $\\lceil N/2\\rceil$ copies and one additional negative-index base invocation. For N=7, indices are 6,4,2,0. All printed alternatives use n<0; option 2 writes into the wrong starting destination slot, option 3 skips destination slots, and option 4 also uses the wrong source stride. The negative sentinel belongs to the question\'s integer pseudocode, not unsigned C indexing.'
root=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source');assert hashlib.sha256((root/q['repoPath']).read_bytes()).hexdigest()==q['sourceSha256'];save(B/'p_recursion-authentic.json',[q])
save(E/'question-visual-decisions.json',[dict(questionId=x['id'],modelId=x.get('modelId'),decision='Exact trace specialization, identified in solution.'if x.get('modelId')else 'Full proof, algebra or code semantics; no unrelated animation.')for x in qs+[q]])
save(E/'reading.json',dict(reviewDate='2026-10-09',records=[dict(university='Berkeley',course='CS61A',instructor='John DeNero',material='Composing Programs, complete Section 1.7.1–1.7.5 extracted text; course-calendar textbook association checked',role='core'),dict(university='MIT',course='6.0001 Fall 2016',instructors='Ana Bell, Eric Grimson, John Guttag',material='Lecture 6, 58 pages extracted text; recursion pages 1–39 and memoization pages 54–57',role='core'),dict(university='Stanford',course='CS106B Winter 2015',instructor='Eric Roberts',material='Handouts 14 and 16, all six pages extracted text. Image-only 19A answers not counted as read.',role='core'),dict(university='CMU',course='15-112 Fall 2023',instructor='Pat Virtue',material='Week 9 Lecture 2, all 48 pages extracted text, relevant content pages 18–48',role='core'),dict(university='Harvard',course='CS50x 2025',instructor='David J. Malan',material='Notes 3 binary-search, recursion and merge-sort text',role='supplementary')],qualification='Finite accessible written candidate pool, not every course worldwide; image-only demonstrations are not read transcripts. Original reconstructions rather than wholesale exercise copying.'))
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
for f in ast.parse((B/'build_correct_chapter.py').read_text(encoding='utf-8')).body:
 if isinstance(f,ast.FunctionDef)and f.name=='scope_preserving_display':exec(compile(ast.Module(body=[f],type_ignores=[]),'wrap','exec'))
mathml.wrap_display=scope_preserving_display
p=R/'dist/chapters/p_recursion.js';s=p.read_text(encoding='utf-8');old=(R/'dist/chapters/p_strings.js').read_text(encoding='utf-8');mount=old[old.index('function mount(host,m)'):old.index('const controls=')].replace('st-','rc-').replace('byte-memory','recursion-stack|call-tree|hanoi-pegs|interval-shrink');s=s.replace('/* PLAYER_MOUNT */',mount).replace('q.x-28,y,56,40','q.x-24,y,48,40');p.write_text(s,encoding='utf-8')
css=(R/'dist/chapters/p_strings.css').read_text(encoding='utf-8').replace('st-','rc-');css+='\n.rc-stage svg .rc-code,.rc-print svg .rc-code{font-family:"JetBrains Mono",monospace!important;font-size:16px!important}.rc-stage svg .rc-math,.rc-print svg .rc-math{font-family:"STIX Two Math",serif!important;font-size:17px!important}\n';(R/'dist/chapters/p_recursion.css').write_text(css,encoding='utf-8')
specs=[];groups={}
def add(id,title,group=None,**spec):
 specs.append(dict(id=id,title=title,spec=spec))
 if group:groups.setdefault(group,[]).append(id)
add('fact-four','Factorial four: descent, saved continuations, and returns','stack',operation='factorial',n=4)
add('fact-zero','The factorial empty-product base','stack',operation='factorial',n=0)
add('around-three','Output before and after a child call','output',operation='around',n=3)
add('digits-738','Digit sum: 738 to 73 to 7','euclid',operation='digits',value=738)
add('gcd-main','Euclid: remainder descent from 1071 and 462','euclid',operation='gcd',a=1071,b=462)
add('gcd-reversed','Euclid when the first input is smaller','euclid',operation='gcd',a=6,b=35)
add('pal-even','A matching even-length byte palindrome','palindrome',operation='palindrome',text='abccba')
add('pal-mismatch','Short-circuit on the inner mismatch','palindrome',operation='palindrome',text='abca')
add('pal-empty','An empty content interval','palindrome',operation='palindrome',text='')
add('binary-seven','Unsuccessful binary search: three comparisons and an empty call','binary',operation='binary',target=8)
add('binary-success','Immediate midpoint success','binary',operation='binary',target=7)
add('power-thirteen','One stored half-result for exponent thirteen',None,operation='power',a=2,exponent=13)
add('fib-five','A full invocation tree for Fibonacci five','fibonacci',operation='fib',n=5)
add('fib-zero','Fibonacci zero: one invocation, no additions','fibonacci',operation='fib',n=0)
add('memo-six','Memo Fibonacci six: requests, completed entries, and returns','memo',operation='memo',n=6)
add('memo-one','A preseeded base cache hit','memo',operation='memo',n=1)
add('hanoi-three','Hanoi three: lift, transfer, lower, and settle','hanoi',operation='hanoi',n=3)
add('hanoi-empty','An empty Hanoi tower needs no move','hanoi',operation='hanoi',n=0)
add('subsets-three','Three position decisions with explicit restoration','subsets',operation='subsets',n=3)
add('subsets-empty','The single empty subset','subsets',operation='subsets',n=0)
add('stride-seven','Reverse-stride copy for seven positions',None,operation='stride',n=7)
add('koch-three','Koch geometry: four connected replacements per level','koch',operation='koch',n=3)
script="const fs=require('fs'),a=require('./dist/chapters/p_recursion.js');process.stdout.write(JSON.stringify(JSON.parse(fs.readFileSync(0,'utf8')).map(s=>a.makeModel(s.id,s.title,s.spec))));"
models=json.loads(subprocess.check_output(['node','-e',script],input=json.dumps(specs).encode(),cwd=R))
for m in models:
 for f in m['frames']:
  f['formulaHtml']=mathml.wrap_display(mathml.Parser(f.pop('formula')).seq());f['teaching']['checks']=[dict(mathHtml='<p>'+x['expression']+'</p>',result=x['result'])for x in f['teaching']['checks']]
save(R/'dist/chapters/p_recursion-models.json',dict(models=models,groups=groups));save(E/'models.json',dict(models=len(models),checkpoints=sum(len(m['frames'])for m in models),scope='Explicit recursive algorithms, traced C-like sequencing, zero-based counting conventions, actual frame/tree/cache/interval/Hanoi/Koch geometry; not an arbitrary C interpreter.'))
print('80 worked authored/reconstructed questions, one checked exam bridge,',len(models),'models,',sum(len(m['frames'])for m in models),'checkpoints')

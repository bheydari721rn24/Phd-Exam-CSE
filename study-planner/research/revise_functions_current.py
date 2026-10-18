"""Focused functions revision. No other chapter body or approval is rewritten."""
from pathlib import Path
from html.parser import HTMLParser
import ast,copy,hashlib,html,json,re,sys
from markdown_it import MarkdownIt

R=Path(__file__).resolve().parents[1]; B=R/'research'; D=R/'dist/chapters'
sys.path.insert(0,str(B/'exam-rewrite'))
import mathml
mathml.wrap_display=lambda s:s
md=MarkdownIt('commonmark',{'html':True}).enable('table')
def text(s):return mathml.markdown_math(s,md)
def save(p,data):p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
def e(s):return html.escape(str(s),quote=True)

class Sections(HTMLParser):
    def __init__(self,s):
        super().__init__(convert_charrefs=False);self.s=s;self.offsets=[0];self.stack=[];self.spans=[]
        for m in re.finditer('\n',s):self.offsets.append(m.end())
        self.feed(s)
    def pos(self):
        row,col=self.getpos();return self.offsets[row-1]+col
    def handle_starttag(self,t,a):
        if t=='section':self.stack.append((self.pos(),dict(a)))
    def handle_endtag(self,t):
        if t=='section':
            start,a=self.stack.pop()
            if 'data-source-id'in a:self.spans.append((start,self.pos()+len('</section>'),a['data-source-id']))

Q=json.loads((B/'p_functions-questions.json').read_text(encoding='utf8'))
answers={}
for name in ['p_functions-answer-rewrites.en.md','p_functions-answer-rewrites-37-89.en.md']:
    s=(B/'deep-library-revision'/name).read_text(encoding='utf8')
    for m in re.finditer(r'^## (PF\d+) \|[^\n]*\n([\s\S]*?)(?=^## PF\d+ \||\Z)',s,re.M):
        answers[m[1]]=m[2].strip().replace('**Full replacement solution.** ','')
assert set(answers)=={q['id'] for q in Q}
for q in Q:q['solution']=answers[q['id']]
save(B/'p_functions-questions.json',Q)

A=json.loads((B/'p_functions-authentic.json').read_text(encoding='utf8'))
A[0]['options'][3]='`if(n<0)return; b[i+1]=a[n]; store(n-2,i+2);`'
A[0]['solution']=r'''After t completed writes, the source and destination indices in option 1 satisfy $n=N-1-2t$ and $i=t$. Initially t is zero, exactly matching store(N-1,0). One write copies the required source element into the next contiguous destination, and the recursive call decreases the source index by two while increasing the destination index by one. This establishes the same invariant at the next call.

The guard is tested before reading a[n]. A write occurs precisely when $N-1-2t\ge0$, giving $\lceil N/2\rceil$ writes. For N = 7 and a = [10,20,30,40,50,60,70], valid source indices are 6,4,2,0 and the destination becomes [70,50,30,10]. The next call has n = -2 and returns without reading an invalid element. For N = 6, indices 5,3,1 produce [60,40,20]. Empty input stops immediately at n = -1.

Option 2 begins at destination index one. Option 3 writes destination positions zero,two,four,..., leaving gaps. Option 4 also uses source stride two, but writes destination positions one,three,five,... . It therefore both skips b[0] and leaves gaps. The earlier claim that option 4 uses source stride one was a transcription error; the rendered original was rechecked on 18 October 2026. Correct option: 1, independently derived rather than verified against an official key.

Each nonterminal call performs its write before calling the next procedure. Unwinding creates no new writes. There are $\lceil N/2\rceil+1$ invocations including the terminal guard call. The syntax is legacy integer pseudocode; a real C implementation still requires appropriate types, valid storage and a nonoverflowing index contract. This is an explicit bridge revisit, not a newly discovered unique functions question.'''
A[0]['verification']='Original PDF page 34 visually rechecked and enlarged on 18 October 2026. All source strides are n-2. Option 4 destination indices are 1,3,5,... . Independently derived option 1; official key unverified.'
A[1]['options'][0]='A descending block, then the median m, then an ascending block.'
A[1]['solution']=r'''The printed base condition is length(A) at most one. Both an empty array and a singleton are already descending, so they return immediately without creating recursive children. A root visual inspection of the enlarged original confirms the less-than-or-equal sign; it must not be transcribed as a strict less-than sign.

For a larger array of distinct values, assume by strong induction that the two smaller recursive calls return their inputs in descending order. Every element in R exceeds m, and every element in L is below m. Therefore the returned greater block is descending internally, its last element exceeds m, and m exceeds the first element of the returned smaller block. The final smaller block is descending internally too. All internal and cross-block comparisons are descending, proving option 4.

For A = [7,2,5,1,6,3,4], the median is four. The greater input [7,5,6] returns [7,6,5], and the smaller input [2,1,3] returns [3,2,1]. Concatenating those results around four gives [7,6,5,4,3,2,1]. There are seven invocations for this example: the root, two three-element calls and four singleton calls. Maximum live depth is three including the root. Inventing empty recursive children for the singleton base would incorrectly change these counts to fifteen calls and depth four.

Median choice controls partition balance; R,m,L concatenation determines direction. Option 1 wrongly assigns different orientations to recursive outputs governed by the same algorithm. Option 2 ignores the ordering invariant. Option 3 would require the opposite L,m,R concatenation. No even-length numerical-median convention is needed for the odd-sized trace used here. The answer is independently derived, not an official-key assertion. This is a bridge revisit supporting recursive contracts and pending continuations.'''
A[1]['verification']='Root visually inspected complete PDF page 3 and enlarged base-case glyph on 18 October 2026: length(A) <= 1. Independently derived descending option 4; original seven-element trace has seven calls and depth three.'
save(B/'p_functions-authentic.json',A)

# Actual-input solution aids use inspectable steps, not unrelated scene aliases.
MODELS=json.loads((D/'problem-visual-models.json').read_text(encoding='utf8'))
NEW={};ASSOCIATIONS={}
def svg(title,columns,rows,selected=None):
    n=len(columns); cw=688/n; height=86+len(rows)*44
    out=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 {height}" role="img" aria-label="{e(title)}"><title>{e(title)}</title>'
    out+=f'<text x="380" y="27" text-anchor="middle" font-family="Source Sans 3" font-size="21">{e(title)}</text>'
    for j,c in enumerate(columns):out+=f'<text x="{36+(j+.5)*cw}" y="64" text-anchor="middle" font-family="Source Sans 3" font-size="18">{e(c)}</text>'
    for i,row in enumerate(rows):
        for j,c in enumerate(row):
            x=36+j*cw;y=79+i*44
            out+=f'<rect x="{x+2}" y="{y}" width="{cw-4}" height="40" rx="4" fill="'+('#e0f2eb'if i==selected else'#f3f6f8')+'"/>'
            out+=f'<text x="{x+cw/2}" y="{y+26}" text-anchor="middle" font-family="JetBrains Mono" font-size="17">{e(c)}</text>'
    return out+'</svg>'
def tablemodel(qid,title,columns,states,reading,kind='exact-state-table'):
    key='p_functions-review-'+qid;frames=[]
    for k,(rows,caption)in enumerate(states):
        frames.append({'html':svg(title,columns,rows,len(rows)-1),'caption':caption,'state':{'question':qid,'step':k,'rows':rows},'teaching':{'operation':caption,'why':reading,'reading':reading,'guide':[],'activeLine':None,'checks':[],'changes':[],'currentState':{'rows':rows},'initial':k==0,'mode':kind,'scope':'Actual stated question data; semantic objects and bindings, not physical machine addresses.'}})
    NEW[key]={'kind':kind,'reading':reading,'frames':frames,'scope':'Actual '+qid+' input. Playback is paused initially; the full written derivation remains the authoritative explanation.','audit':{'builder':'research/revise_functions_current.py','actualInput':True}}
    ASSOCIATIONS[qid]=key

def cumulative(qid,title,cols,rows,captions,reading,kind='exact-state-table'):
    tablemodel(qid,title,cols,[(rows[:k+1],captions[k])for k in range(len(rows))],reading,kind)

cumulative('MS_CS_1393_Q167','Reverse-stride copy: N = 7',['Source n','Destination i','Write / guard'],[[6,0,'b[0] = 70'],[4,1,'b[1] = 50'],[2,2,'b[2] = 30'],[0,3,'b[3] = 10'],[-2,4,'stop; no read']],['Start at the last source element.','Advance source by -2 and destination by +1.','Keep the destination contiguous.','Copy the last selected source value.','The negative guard precedes access; returns perform no writes.'],'Read the source and destination indices together. Every row is the actual N = 7 trace, including its terminal guard.','two-array-index-trace')
cumulative('Phd_CE_1405_Q9','SplitSort: returned blocks, not empty children',['Call input','Return value','Invocations'],[['[7] / [5]','[7] / [5]','two base calls'],['[7,5,6]','[7,6,5]','3 total here'],['[3] / [1]','[3] / [1]','two base calls'],['[2,1,3]','[3,2,1]','3 total here'],['[7,2,5,1,6,3,4]','[7,6,5,4,3,2,1]','7 total']],['Singletons satisfy the original base case.','Combine the returned greater and smaller singletons around six.','The smaller branch has its own singleton bases.','Combine around two with the same descending contract.','The root combines [7,6,5], four and [3,2,1].'],'These are bottom-up return checkpoints, not chronological creation of every call. No singleton creates empty children.','recursive-return-blocks')

for qid,start,alias in [('PF23',4,False),('PF24',4,True),('PF25',-2,False),('PF26',-2,True)]:
    v=7 if qid=='PF23'else 5;before=[start,start if alias else v];after1=[start+2,start+2 if alias else v];after2=[3*(start+2)]*2 if alias else[start+2,3*v]
    cumulative(qid,'Shared target'if alias else'Distinct targets',['Checkpoint','Read through p','Read through q'],[['entry',*before],['after *p += 2',*after1],['after *q *= 3',*after2]],['Establish whether p and q designate the same object.','Complete the first full statement.','The second read uses the updated object if aliased.'],'The same pointer spellings can designate one or two objects; the target identity decides the state space.','alias-target-transition')

cumulative('PF28','Pointer-to-pointer redirection',['Checkpoint','caller pointer r','a / b'],[['entry','&a','2 / 5'],['*slot = target','&b','2 / 5'],['*r += 4','&b','2 / 9']],['The parameter slot designates the caller pointer object.','Writing through slot redirects r rather than its old target.','The later dereference changes b.'],'Keep the pointer object r separate from both integer targets.','pointer-object-redirection')
cumulative('PF31','Two outputs alias one integer',['Statement','Target x','Surviving result'],[['entry','0','n copies 23; d copies 5'],['write quotient','4','quotient'],['write remainder','3','remainder only']],['Input values are copied before writes.','The first store writes four.','The second store overwrites that same object with three.'],'One scalar object cannot retain two different promised outputs simultaneously.','output-alias-overwrite')
cumulative('PF36','C17 permits two completed-body orders',['Argument order','left / right','result / counter'],[['left then right','1 / 2','-1 / 2'],['right then left','2 / 1','1 / 2']],['The first permitted execution supplies one to the left argument.','A separate alternative supplies one to the right argument.'],'Rows are alternative executions from a reset counter, not consecutive runs sharing state.','sequencing-alternatives')
cumulative('PF49','Greatest-divisor search: a = 12, b = 18',['Candidate d','Divides both?','Larger candidates'],[[12,'no','none initially'],[11,'no','12 excluded'],[10,'no','11..12 excluded'],[9,'no','10..12 excluded'],[8,'no','9..12 excluded'],[7,'no','8..12 excluded'],[6,'yes','7..12 excluded']],['Initialize at min(12,18).','Reject eleven.','Reject ten.','Nine does not divide twelve.','Eight does not divide both.','Reject seven.','Six divides both; the exclusion invariant proves greatestness.'],'Divisibility alone proves commonness; the excluded-larger-candidates invariant proves maximality.','maximality-invariant')

for qid,rows in {
 'PF64':[['entry','module x = 4','local x = 4'],['x += 3','module x = 4','local x = 7'],['return x * 2','module x = 4','y = 14']],
 'PF65':[['entry','x -> A [2]','a -> A'],['append(7)','x -> A [2,7]','a -> A'],['a = [99]','x -> A [2,7]','a -> B [99]'],['return a','x -> A [2,7]','y -> B [99]']],
 'PF66':[['entry','x -> A [1]','a -> A'],['append(5)','x -> A [1,5]','a -> A'],['return a','x -> A [1,5]','y -> A'],['y.append(9)','x -> A [1,5,9]','y -> A']],
 'PF67':[['entry','x -> A [2,3]','a -> A'],['b = list(a)','A [2,3]','b -> B [2,3]'],['b.append(8)','A [2,3]','B [2,3,8]'],['return b','x -> A','y -> B']],
 'PF68':[['definition','module k = 4','default = 4'],['k = 9','module k = 9','default = 4'],['f()','argument omitted','a = 4'],['f(k)','argument = 9','b = 9']],
 'PF69':[['definition','default D = []','no snapshots'],['f(2)','D = [2]','r1 -> R1 [2]'],['f(5)','D = [2,5]','r2 -> R2 [2,5]']],
 'PF70':[['f(1)','default D [1]','r1 [1]'],['f(7,[9])','explicit E [9,7]','r2 [9,7]'],['f(2)','default D [1,2]','r3 [1,2]']],
 'PF71':[['first omitted call','new A [1]','r1 -> A'],['second omitted call','new B [2]','r2 -> B'],['identity test','A and B distinct','r1 is r2: False']],
 'PF74':[['make(4)','a -> environment A','A.k = 4'],['make(9)','b -> environment B','B.k = 9'],['a(3)','3 + A.k','7'],['b(3)','3 + B.k','12']],
 'PF76':[['factory','retained n = 0','no return yet'],['first call','n = 2','return 2'],['second call','n = 4','return 4'],['third call','n = 6','return 6']],
 'PF77':[['create lambda 0','shared i = 0','not called yet'],['create lambda 1','shared i = 1','not called yet'],['create lambda 2','shared i = 2','not called yet'],['call saved functions','all read same i','[2,2,2]']],
 'PF78':[['create lambda 0','default (0,)','no free i lookup'],['create lambda 1','default (1,)','no free i lookup'],['create lambda 2','default (2,)','no free i lookup'],['call with no args','three saved defaults','[0,1,2]']],
 'PF79':[['counter reset','0','no arguments yet'],['left call','1','left = 1'],['right call','2','right = 2'],['subtract','counter = 2','result = -1']],
 'PF83':[['compose(square,plus2)','saved f = square','saved g = plus2'],['invoke lambda(3)','g(3) = 5','f still square'],['apply saved f','square(5)','return 25']],
 'PF85':[['factory calls','A = 0','B = 0'],['a() -> 1','A = 1','B = 0'],['a() -> 2','A = 2','B = 0'],['b() -> 1','A = 2','B = 1'],['a() -> 3','A = 3','B = 1']],
 'PF89':[['entry','a aliases x = 3','b copies 3'],['a += b','x = 6','b = 3'],['b += a','x = 6','b = 9'],['return void','x survives as 6','b lifetime ends']]
}.items():
    cumulative(qid,qid+': bindings and state',['Operation','Caller / shared state','Local / result'],rows,[str(row[0])+': '+str(row[1])+'; '+str(row[2])+'.'for row in rows],'Follow the named identity or binding. A local rebinding, shared-object mutation and retained environment update are distinct operations.','python-binding-trace'if 64<=int(qid[2:])<=85 else'reference-and-value')
cumulative('PF84','Persistent helper returns and caller total',['Call increment','saved / returned','caller sum'],[[1,1,1],[2,3,4],[3,6,10],[4,10,20]],['Add one to saved and accumulate its returned one.','Add two to saved; accumulate three rather than two.','The third return is six.','The persistent state is ten, while the sum of returns is twenty.'],'The two accumulators satisfy triangular and tetrahedral formulas respectively.','persistent-sum-recurrence')
def graph(title,names,objects,links):
    out=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 300" role="img" aria-label="{e(title)}"><title>{e(title)}</title><defs><marker id="pf-tip" markerWidth="7" markerHeight="6" refX="7" refY="3" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0L7 3L0 6Z" fill="#357d8b"/></marker></defs>'
    out+=f'<text x="380" y="28" text-anchor="middle" font-family="Source Sans 3" font-size="21">{e(title)}</text>'
    for i,label in enumerate(names):
        y=62+i*65;out+=f'<rect x="35" y="{y}" width="205" height="46" rx="6" fill="#edf4f8" stroke="#7b9da8"/><text x="137.5" y="{y+29}" text-anchor="middle" font-family="JetBrains Mono" font-size="18">{e(label)}</text>'
    for i,label in enumerate(objects):
        y=62+i*80;out+=f'<rect x="435" y="{y}" width="285" height="54" rx="6" fill="#e9f4ee" stroke="#7b9da8"/><text x="577.5" y="{y+33}" text-anchor="middle" font-family="JetBrains Mono" font-size="19">{e(label)}</text>'
    for a,b in links:
        y=85+a*65;v=89+b*80;out+=f'<path d="M240 {y} C320 {y},355 {v},435 {v}" fill="none" stroke="#357d8b" stroke-width="2" marker-end="url(#pf-tip)"/>'
    return out+'</svg>'

for qid in ['PF23','PF24','PF25','PF26']:
    m=NEW[ASSOCIATIONS[qid]];alias=qid in ['PF24','PF26']
    for f in m['frames']:
        row=f['state']['rows'][-1];p,q=row[1:]
        f['html']=graph(qid+': '+row[0],['parameter p','parameter q'],['a = '+str(p)]if alias else['a = '+str(p),'b = '+str(q)],[(0,0),(1,0 if alias else 1)])
for k,f in enumerate(NEW[ASSOCIATIONS['PF65']]['frames']):
    names=['module x','local a']if k<3 else['module x','module y']
    objects=['A = [2]']if k==0 else['A = [2,7]']if k==1 else['A = [2,7]','B = [99]']
    f['html']=graph('PF65: '+['Entry shares A','append mutates A','Local rebinding chooses B','Return supplies B'][k],names,objects,[(0,0),(1,0 if k<2 else 1)])
for k,f in enumerate(NEW[ASSOCIATIONS['PF74']]['frames']):
    f['html']=graph('PF74: '+['First retained environment','Two retained environments','a(3) returns 7','b(3) returns 12'][k],['function a']if k==0 else['function a','function b'],['environment A: k = 4']if k==0 else['environment A: k = 4','environment B: k = 9'],[(0,0)]if k==0 else[(0,0),(1,1)])

def arrays(k):
    source=[10,20,30,40,50,60,70];dest=[70,50,30,10];out='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 280" role="img" aria-label="Reverse stride actual arrays"><title>Reverse-stride source and contiguous destination</title><defs><marker id="pf-copy-tip" markerWidth="7" markerHeight="6" refX="7" refY="3" orient="auto"><path d="M0 0L7 3L0 6Z" fill="#357d8b"/></marker></defs>'
    out+='<text x="380" y="26" text-anchor="middle" font-family="Source Sans 3" font-size="21">MS Q167: source stride -2, destination stride +1</text>'
    for y,values in [(76,source),(195,dest)]:
        for j,v in enumerate(values):
            shown=y==76 or j<=k;active=(y==76 and j==6-2*k)or(y==195 and j==k)
            x=75+j*85;out+=f'<text x="{x+35}" y="{y-12}" text-anchor="middle" font-family="STIX Two Math" font-size="16">{j}</text><rect x="{x}" y="{y}" width="70" height="44" rx="5" fill="'+('#d9efe5'if active else'#f0f4f7')+f'" stroke="#7b9da8"/><text x="{x+35}" y="{y+28}" text-anchor="middle" font-family="STIX Two Math" font-size="22">{v if shown else "·"}</text>'
    if k<4:
        x=110+(6-2*k)*85;z=110+k*85;out+=f'<path d="M{x} 120 C{x} 150,{z} 150,{z} 195" fill="none" stroke="#357d8b" stroke-width="2" marker-end="url(#pf-copy-tip)"/>'
    else:out+='<text x="530" y="223" text-anchor="middle" font-family="JetBrains Mono" font-size="18">n = -2: stop</text>'
    return out+'</svg>'
for k,f in enumerate(NEW[ASSOCIATIONS['MS_CS_1393_Q167']]['frames']):f['html']=arrays(k)
MODELS.update(NEW);save(D/'problem-visual-models.json',MODELS)

def item(q,n,auth=False):
    provenance=e(q.get('origin',''))
    if auth:
        from urllib.parse import quote
        url='https://github.com/bheydari721rn24/Phd-Exam-CSE/blob/'+q['sourceCommit']+'/'+quote(q['repoPath'],safe='/')+'#page='+str(q['pdfPage'])
        provenance=f'<a href="{e(url)}">{e(q["booklet"].replace("_"," "))} · Q{q["qNumber"]} · PDF page {q["pdfPage"]}</a>. Explicit bridge revisit; independently derived, not an official key.'
    out=f'<section class="exam-question" data-kind="{"authentic"if auth else"original"}" data-source-id="{q["id"]}"><h3>Question {n}. {e(q["title"])}</h3><p class="exam-label">'+('Authentic bridge revisit · checked English adaptation'if auth else'Original/course-inspired problem · author-assessed '+q['difficulty'].lower())+'</p><p class="exam-provenance">'+provenance+'</p>'+text(q['stem'])
    if auth:out+='<div class="exam-options">'+''.join(f'<div class="exam-option"><b>{j}.</b><div>{text(v)}</div></div>'for j,v in enumerate(q['options'],1))+'</div>'
    out+='<details class="exam-solution"><summary>Read the complete derivation and reasoning</summary>'
    if auth:out+=f'<p><strong>Correct option: {q["answer"]}.</strong></p>'
    out+=text(q['solution'])
    if q['id']in ASSOCIATIONS:
        key=ASSOCIATIONS[q['id']];model=NEW[key]
        out+=f'<section class="problem-visual" data-problem-visual="{key}"><h4>Exact-input visual solution</h4><p>{e(model["reading"])}</p>{model["frames"][0]["html"]}<p>{e(model["frames"][0]["caption"])}</p></section>'
    return out+'</details></section>'

pagepath=D/'p_functions.html';page=pagepath.read_text(encoding='utf8')
spans=Sections(page).spans;assert len(spans)==91
records={q['id']:(q,n,n<=2)for n,q in enumerate(A+Q,1)}
for start,end,qid in sorted(spans,reverse=True):page=page[:start]+item(*records[qid])+page[end:]
page=page.replace('Student-approved chapter','Author-reviewed revision · awaiting student approval')
page=page.replace('</head>','<style>.chapter .formula-block{overflow-x:auto;max-width:100%}.chapter .formula-block math{max-width:none;white-space:nowrap}.problem-visual svg{max-width:760px;width:100%;height:auto}.exam-solution pre{overflow-x:auto}</style></head>')if'<style>.chapter .formula-block'not in page else page
page=re.sub(r'problem-visuals.js(?:\?[^"\s]*)?', 'problem-visuals.js?v=functions-review-20261018',page)
pagepath.write_text(page,encoding='utf8')
# Cache key only: the shared renderer and all pre-existing models are preserved.
p=D/'problem-visuals.js';s=p.read_text(encoding='utf8');s=re.sub(r'problem-visual-models.json\?[^\x27]*', 'problem-visual-models.json?v=functions-review-20261018',s);p.write_text(s,encoding='utf8')
save(B/'deep-library-revision/p_functions-answer-integration.json',{'status':'integrated_pending_browser_review','originalSolutions':89,'authenticBridgeSolutions':2,'exactInputVisualModels':len(NEW),'visualFrames':sum(len(m['frames'])for m in NEW.values()),'sourceCorrection':'MS CS 1393 Q167 option4 source stride -2. PhD <=1 base preserved after root enlarged-glyph inspection.','studentApproved':False,'questionSHA256':hashlib.sha256((B/'p_functions-questions.json').read_bytes()).hexdigest()})
print('Integrated 89 rewritten solutions, 2 checked bridge solutions,',len(NEW),'exact-input visual models.')

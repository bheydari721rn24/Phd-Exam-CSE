"""Integrate this chapter only; preserve other chapter bodies and models."""
from pathlib import Path
from html.parser import HTMLParser
import ast,html,json,re,sys,copy,shutil
from markdown_it import MarkdownIt
R=Path(__file__).resolve().parents[1];B=R/'research';E=B/'deep-library-revision';D=R/'dist/chapters';T=Path('C:/Users/bheydari/AppData/Local/Temp')
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
def text(s):return mathml.markdown_math(s,md)
def e(s):return html.escape(str(s),quote=True)
def save(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
for n in ast.parse((B/'revise_functions_current.py').read_text(encoding='utf8')).body:
    if isinstance(n,ast.ClassDef)and n.name=='Sections':exec(compile(ast.Module(body=[n],type_ignores=[]),'focused_sections','exec'))
    if isinstance(n,ast.FunctionDef)and n.name=='item':exec(compile(ast.Module(body=[n],type_ignores=[]),'focused_item','exec'))
answers={}
for p in sorted(E.glob('p_arrays-answer-rewrites-*.en.md')):
    for m in re.finditer(r'^## (PA\d+) \|[^\n]*\n([\s\S]*?)(?=^## PA\d+ \||\Z)',p.read_text(encoding='utf8'),re.M):
        s=m[2].strip();s=re.sub(r'^\*\*Stem clarification required\.\*\*[^\n]*\n\n','',s);answers[m[1]]=s
Q=json.loads((B/'p_arrays-questions.json').read_text(encoding='utf8'));assert set(answers)=={q['id']for q in Q}
for q in Q:q['solution']=answers[q['id']];q['difficulty']='Medium to hard'
Q[1]['stem']=Q[1]['stem'].replace('A matrix','A row-major matrix',1)
Q[4]['stem']=Q[4]['stem'].replace('A row-major array','A zero-based row-major array',1)
orientation=' Use the destination-to-source map (i+8) modulo twelve; distinguish it from original-to-destination movement.'
if orientation not in Q[38]['stem']:Q[38]['stem']+=orientation
Q[40]['title']='Direction of an in-place adjacent-difference transform'
Q[50]['stem']='For Python s="Aé", find len(s) and len(s.encode("utf-8")). In a C environment with eight-bit char bytes and UTF-8 execution encoding, how many char elements hold those UTF-8 bytes plus a final zero? Distinguish code points, encoded bytes and array capacity.'
Q[51]['stem']="In C17 consider:\n\n```c\nchar s[8] = {'a', 'b', 0, 'c'};\n```\n\nDetermine sizeof s, strlen(s), s[3], and whether later initialized entries extend the string beginning at s."
Q[53]['stem']="In C17 consider:\n\n```c\nchar a[] = \"cat\";\nconst char *p = \"cat\";\na[0] = 'b';\n```\n\nWhat changes? Why does casting away const not permit modifying the string literal?"
Q[66]['stem']='Assume new_bytes > 0. Explain the problem with p=realloc(p,new_bytes) when allocation failure is possible. What references remain valid after successful reallocation versus after failure?'
save(B/'p_arrays-questions.json',Q)
A=json.loads((B/'p_arrays-authentic.json').read_text(encoding='utf8'))
A[0]['solution']=r'''Let t count completed copies. At the beginning of a call, the required indices are $n=N-1-2t$ and $i=t$, while each already written destination $b[j]$ equals original source $a[N-1-2j]$ for $0\le j<t$. The initial call establishes this relation with an empty prefix. A nonnegative n permits exactly the next desired copy; decreasing n by two and increasing i by one preserves the invariant. The negative guard occurs before any invalid read.

For N=6 and a=[10,20,30,40,50,60], source indices 5,3,1 write [60,40,20] at consecutive destinations 0,1,2. The terminal call receives n=-1. For odd N=5, the selected indices are 4,2,0 and the terminal n is -2, so changing the guard to n<=0 would wrongly omit index zero. The general write count is $\lceil N/2\rceil$, with one additional guard-only invocation. No writes occur on unwinding.

All four original alternatives use the correct source stride minus two and the guard n<0. Option 2 starts at destination one; option 3 writes at zero,two,four,...; option 4 combines destination origin one and stride two. Only option 1 gives the required contiguous output. The independently derived answer is one, not a verified official key.

This is legacy integer pseudocode with globally available arrays. A real implementation needs a sufficiently large destination, valid indices and preservation of unread source values through separate storage or a proved overlap strategy. The mathematical empty extension copies nothing and makes one guard call, but is not an assertion that the original exam explicitly stipulated an empty input. This placement is an identified bridge revisit.'''
A[1]['stem']=r'''A contains n distinct finite values, with every permutation equally likely. The original mathematical pseudocode is:

```text
min = +infinity
for (i = 1; i <= n; i++)
    if (min > A[i])
        min = A[i]  // counted assignment
```

Y counts executions of the marked assignment. Which listed expression approximates its mean asymptotically? The original asks which expression is closer to the mean; this English adaptation makes its intended large-n comparison explicit.'''
A[1]['solution']=r'''Define $I_i=1$ when position i causes the marked assignment, and zero otherwise. This occurs exactly when that position contains the smallest of the first i distinct values. Under the stated uniform permutation model, each of those i positions is equally likely to contain that smallest value, giving $P(I_i=1)=1/i$.

The counted updates satisfy $Y=\sum_{i=1}^{n}I_i$. Linearity of expectation, without requiring independence, therefore gives

$$E[Y]=\sum_{i=1}^{n}\frac1i=H_n.$$

The exact expectation is a harmonic number. Integration of the decreasing function 1/x yields $\ln(n+1)\le H_n\le1+\ln n$, so option 2, ln n, is the intended asymptotic approximation. It is not an identity H_n=ln n and is not necessarily the numerically closest formula for every small n.

For n=3, all six permutations have eleven counted updates in total, giving exact mean 11/6. In the concrete order [5,2,4,1,3], the updates store five, two and one, so Y is three. The scan always makes n element comparisons, but its number of successful assignments varies from one in increasing order to n in decreasing order.

The infinity initialization ensures the first finite value is counted. Initializing instead from the first data element and scanning only the rest removes that update and changes the mean to H_n-1. Duplicates or a nonuniform permutation model require another probability proof. Option 1 misses the growing record count; option n treats every value as a new record; n ln n multiplies rather than sums the per-position probabilities. Both original loop endpoints and strict comparison were inspected on the scan; no official answer key is claimed.'''
for q in A:q.update(difficulty='Medium to hard',verification='Original complete PDF page and enlarged question inspected on 20 October 2026; source hashes match pinned revision. Independently derived key, not an official key.')
save(B/'p_arrays-authentic.json',A)

OLD=json.loads((D/'problem-visual-models.json').read_text(encoding='utf8'));MODELS=copy.deepcopy(OLD);NEW={};ASSOCIATIONS={}
def txt(x,y,s,size=20,font='STIX Two Math'):
    return f'<text x="{x}" y="{y}" text-anchor="middle" font-family="{font}" font-size="{size}">{e(s)}</text>'
def drawing(title,rows,mark=(),note='',arrows=()):
    h=100+len(rows)*104;out=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 {h}" role="img" aria-label="{e(title)}"><title>{e(title)}</title><defs><marker id="array-tip" markerWidth="7" markerHeight="6" refX="7" refY="3" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0L7 3L0 6Z" fill="#347f86"/></marker></defs>'+txt(380,27,title,21,'Source Sans 3')
    locations={}
    for r,(label,values)in enumerate(rows):
        top=77+r*104;out+=txt(380,top-20,label,18,'Source Sans 3');step=min(83,676/max(1,len(values)));start=380-len(values)*step/2
        for j,v in enumerate(values):
            x=start+j*step;w=step-5;locations[r,j]=(x+w/2,top,top+44)
            out+=f'<g data-entity="slot-{r}-{j}"><rect x="{x}" y="{top}" width="{w}" height="44" rx="5" fill="'+('#d9efe4'if(r,j)in mark else'#edf3f7')+f'" stroke="#88a7b0"/>'+txt(x+w/2,top+28,v,19 if len(str(v))<7 else 15)+ '</g>'+txt(x+w/2,top+66,j,15)
    for r,j,s,k in arrows:
        x,y,b=locations[r,j];u,v,w=locations[s,k];out+=f'<path data-arrow="copy" d="M{x} {b} C{x} {b+22},{u} {v-24},{u} {v}" fill="none" stroke="#347f86" stroke-width="2" marker-end="url(#array-tip)"/>'
    return out+txt(380,h-10,note,17,'Source Sans 3')+'</svg>'
def table(title,headers,rows):
    h=105+len(rows)*40;w=680/len(headers);out=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 {h}" role="img" aria-label="{e(title)}"><title>{e(title)}</title>'+txt(380,27,title,21,'Source Sans 3')
    for j,c in enumerate(headers):out+=txt(40+(j+.5)*w,64,c,18,'Source Sans 3')
    for i,row in enumerate(rows):
        for j,c in enumerate(row):x=40+j*w;y=79+i*40;out+=f'<rect x="{x+2}" y="{y}" width="{w-4}" height="36" rx="4" fill="#eef5f4"/>'+txt(x+w/2,y+24,c,17,'JetBrains Mono')
    return out+'</svg>'
def model(qid,kind,reading,states):
    key='p_arrays-review-'+qid;frames=[]
    for k,(state,svg,caption)in enumerate(states):
        frames.append({'html':svg,'state':state,'caption':caption,'teaching':{'operation':caption,'why':reading,'reading':reading,'currentState':state,'initial':k==0,'guide':[],'checks':[],'changes':[],'mode':kind}})
    NEW[key]={'kind':kind,'reading':reading,'frames':frames,'scope':'Exact '+qid+' data; diagrams illustrate the stated representation and do not establish physical C pointer provenance.','audit':{'actualInput':True,'builder':'research/revise_arrays_current.py'}};ASSOCIATIONS[qid]=key
def seq(qid,title,states,captions,kind='array-write-trace',logical=None):
    initial=states[0];frames=[]
    for k,a in enumerate(states):
        marks=[(1,j)for j,v in enumerate(a)if j>=len(states[max(0,k-1)])or v!=states[max(0,k-1)][j]]if k else[]
        state={'values':a,'initial':initial,'step':k}
        if logical is not None:state['logicalLength']=logical[k]
        note=('Logical length = '+str(logical[k]))if logical is not None else'Indices name fixed storage positions; values follow the stated writes.'
        frames.append((state,drawing(title,[('Initial state',initial),('Current',a)],marks,note),captions[k]))
    model(qid,kind,'Compare the initial state and the current state. The caption names the exact write or boundary decision.',frames)

seq('PA25','Boundary prefix construction',[[0],[0,3],[0,3,1],[0,3,1,6],[0,3,1,6,7],[0,3,1,6,7,3]],['P[0] is the empty-prefix boundary.','Read three.','Add minus two.','Add five.','Add one.','Add minus four; the last boundary is three.'],'boundary-prefix')
seq('PA26','Difference events, then prefix reconstruction',[[0,0,0,0,0,0],[0,4,0,0,-4,0],[0,4,-2,0,-4,2]],['Six boundary slots, five logical data values.','Start +4 at one, cancel at four.','Start -2 at two, cancel at five; reconstruct [0,4,2,2,-2].'],'difference-events')
for qid,forward in [('PA28',True),('PA29',False),('PA41',False)]:
    a=[3,5,9,10]if qid=='PA41'else[1,2,3,4,5];states=[a.copy()];caps=['Original values before any write.']
    for i in(range(1,len(a))if forward else range(len(a)-1,0,-1)):
        before=a[i];other=a[i-1];a[i]=before-other if qid=='PA41'else before+other;states.append(a.copy());caps.append(f'Index {i}: {before} '+('-'if qid=='PA41'else'+')+f' {other} = {a[i]}; predecessor is '+('already accumulated.'if forward else'still original.'))
    seq(qid,'Original-neighbor differences'if qid=='PA41'else('Increasing prefix updates'if forward else'Decreasing neighbor updates'),states,caps)
for qid,s,d,reverse in [('PA30',0,1,False),('PA31',0,1,True),('PA32',1,0,False)]:
    a=[2,4,6,8,10,12];states=[a.copy()];caps=['Initial backing array; source snapshot is preserved in the original row.']
    for t in(reversed(range(4))if reverse else range(4)):
        value=a[s+t];a[d+t]=value;states.append(a.copy());caps.append(f'Read current index {s+t} ({value}); write index {d+t}.')
    seq(qid,'Overlap '+('counterexample'if qid=='PA30'else'safe copying'),states,caps,'overlap-counterexample'if qid=='PA30'else'overlap-copy')
seq('PA35','Stable insertion at index two',[[3,6,9,12,'·','·'],[3,6,9,12,12,'·'],[3,6,9,9,12,'·'],[3,6,7,9,12,'·']],['Length four, capacity six.','Shift old index three right.','Shift old index two right.','Write seven; length is now five.'],logical=[4,4,4,5])
seq('PA36','Stable deletion at index one',[[3,6,9,12,15],[3,9,9,12,15],[3,9,12,12,15],[3,9,12,15,15]],['Delete six; preserve following order.','Copy index two to one.','Copy index three to two.','Copy index four to three; spare final slot is not logical output.'],logical=[5,5,5,4])
seq('PA37','Half-open segment reversal',[[0,1,2,3,4,5,6],[0,5,2,3,4,1,6],[0,5,4,3,2,1,6]],['Only indices one through five belong to the reversal.','Swap indices one and five.','Swap two and four; center three is unchanged.'])
seq('PA38','Three reversals implement rotation',[[0,1,2,3,4,5,6],[2,1,0,3,4,5,6],[2,1,0,6,5,4,3],[3,4,5,6,0,1,2]],['Split X=[0,1,2], Y=[3,4,5,6].','Reverse X.','Reverse Y.','Reverse the whole: block order is YX.'],'rotation-block-reversals')
a=[5,2,7,4,6,9,8];states=[a.copy()];lengths=[0];caps=['The retained prefix is initially empty.'];w=0
for i,v in enumerate(a.copy()):
    if v%2==0:a[w]=v;w+=1
    states.append(a.copy());lengths.append(w);caps.append(f'Read index {i}: '+('retain '+str(v)+' in output order.'if v%2==0 else'reject '+str(v)+'.'))
seq('PA40','Stable compaction retains even values',states,caps,'read-write-compaction',lengths)
seq('PA44','Fixed extended-slice slots',[[0,1,2,3,4,5],[0,9,2,8,4,7]],['Selected slots are one, three and five.','Replace those three slots in order; a two-item replacement would raise ValueError.'],'extended-slice')
seq('PA45','Slice replacement changes length',[[1,2,3,4,5],[1,8,9,5],[1,8,6,7,9,5]],['Original length five.','Replace indices one through three by two values.','Insert at current empty boundary two.'],'resizing-slice')
seq('PA48','Deletion under an advancing iterator',[[2,4,6,7],[4,6,7],[4,7]],['Next iterator position is zero.','Remove two; next iterator position one now holds six.','Remove six; next position two is beyond current length, so four is skipped.'],'iterator-mutation')

for qid,title,headers,rows,caps in [
 ('PA01','Normalize the declared lower bound',['Quantity','Calculation','Value'],[['element count','8 - (-3) + 1','12'],['index5 offset','5 - (-3)','8'],['index5 start','1600 + 4*8','1632'],['last byte','1600 + 48 - 1','1647']],['Count inclusive indices.','Normalize before scaling.','Convert the element offset to bytes.','Distinguish final byte from one-past1648.']),
 ('PA02','Row-major inverse: address4312',['Step','Result'],[['byte displacement','4312 - 4096 = 216'],['element offset','216 / 8 = 27'],['divide by7 columns','quotient3, remainder6'],['restore lower bounds','(2+3,-1+6) = (5,5)']],['Check address alignment.','Count elements rather than bytes.','Quotient gives row; remainder gives column.','Validate both recovered coordinates.']),
 ('PA06','Transpose changes row width',['Old offset','Source','New offset'],[[7,'(1,2)','2*2+1 = 5'],[9,'(1,4)','4*2+1 = 9']],['Decode with five columns, encode with two.','The final fixed position does not make the whole mapping identity.']),
 ('PA10','Jagged rows have repeated boundaries',['Row','Flat interval','Contents'],[[0,'[0,2)','offsets0,1'],[1,'[2,2)','empty'],[2,'[2,5)','offsets2,3,4'],[3,'[5,6)','offset5']],['First row has two values.','Repeated boundary records an empty row.','Offset two belongs here, at column zero.','Offset five belongs here; six is one-past.']),
 ('PA23','Strict record-minimum updates',['Read value','Current minimum','Updates'],[[5,5,1],[5,5,1],[2,2,2],[2,2,2],[7,2,2],[1,1,3],[1,1,3]],['Infinity makes the first value an update.','Equality is not a strict decrease.','Two is a new record.','A tie does not update.','Seven exceeds the minimum.','One is a new record.','The first tied minimum position is retained.']),
 ('PA43','Normalize negative-step slices',['Slice','Index progression','Result'],[['[::-1]','6,5,4,3,2,1,0','reverse'],['[:-1:-1]','start6, stop6','empty'],['[5:0:-2]','5,3,1','[5,3,1]']],['Omitted stop is before-first.','Explicit -1 normalizes to index six.','Stop zero is excluded.']),
 ('PA52','First zero ends the selected string',['Index','char value','Role'],[[0,"'a'",'string'],[1,"'b'",'string'],[2,'0','terminator'],[3,"'c'",'outside first string'],['4..7','0','initialized capacity']],['First visible byte.','Second visible byte.','strlen stops with result two.','The array object continues beyond its first string.','Total capacity remains eight.']),
 ('PA62','Doubling: count copies and peak slots',['Expansion','Copies','Two live capacities'],[['1 to2',1,3],['2 to4',2,6],['4 to8',4,12],['8 to16',8,24]],['First full block is copied.','The next expansion copies two.','The next copies four.','Total copies15; new writes13; peak24.']),
 ('PA64','Additive growth copies an arithmetic series',['Expansion','Copied elements','Cumulative'],[['3 to6',3,3],['6 to9',6,9],['9 to12',9,18]],['The fourth append expands.','The seventh expands.','The tenth expands; length12 uses capacity12.']),
 ('PA65','Tripling trades reserved space for copy work',['Expansion','Copies','Cumulative'],[['1 to3',1,1],['3 to9',3,4],['9 to27',9,13]],['Copy one.','Copy three.','Final length10, capacity27, spare17.']),
 ('PA68','Expand first, then shift',['Operation','Writes','Cumulative'],[['expand8 to16',8,8],['shift suffix at2',6,14],['store inserted value',1,15]],['Copy the complete old live prefix.','Move six elements right in descending order.','New logical length9; peak slots24.']),
 ('PA69','Half-full shrinking oscillates',['Operation','Capacity','Copied values'],[['delete fifth',4,4],['append fifth',8,4],['repeat pair','4 then8','8 per pair']],['Immediate shrink copies four.','Immediate regrowth copies four again.','A lower shrink threshold separates opposite resizes.']),
 ('PA70','Cold one-line cache',['Traversal','Element reads','Line fills'],[['row-major',64,8],['column-major',64,64]],['One fill serves all eight entries in each row.','Every next row evicts the only retained cache line.']),
 ('PA74','Exact lower-triangle inverse',['Row','Start','Next start'],[[3,6,10],[4,10,15],[5,15,21]],['Seventeen is beyond this row.','Seventeen is still beyond this row.','15 <=17<21 gives row5 and column2.']),
 ('PA77','A fitting total can have an invalid partial sum',['Term','Mathematical total','int32 status'],[[2147483647,2147483647,'fits'],[1,2147483648,'exceeds maximum'],[-1,2147483647,'cannot undo prior UB']],['First sum is at the maximum.','The second addition is the unsafe operation.','This final value is a mathematical comparison, not a valid execution result.'])]:
    model(qid,'exact-derivation-table','Read the exact quantities and the named model; rows are derivation checkpoints, not assumed physical memory.',[({'rows':rows[:k+1],'step':k},table(title,headers,rows[:k+1]),caps[k])for k in range(len(rows))])

def objects(title,labels,targets,edges):
    h=max(215,80+len(labels)*54,80+len(targets)*68);out=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 {h}" role="img" aria-label="{e(title)}"><title>{e(title)}</title><defs><marker id="obj-tip" markerWidth="7" markerHeight="6" refX="7" refY="3" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0L7 3L0 6Z" fill="#347f86"/></marker></defs>'+txt(380,27,title,21,'Source Sans 3')
    for j,v in enumerate(labels):y=60+54*j;out+=f'<rect x="30" y="{y}" width="250" height="40" rx="5" fill="#edf3f7" stroke="#88a7b0"/>'+txt(155,y+26,v,18,'JetBrains Mono')
    for j,v in enumerate(targets):y=60+68*j;out+=f'<rect x="450" y="{y}" width="280" height="45" rx="5" fill="#e3f2e9" stroke="#88a7b0"/>'+txt(590,y+29,v,18,'JetBrains Mono')
    for a,b in edges:y=80+54*a;v=82.5+68*b;out+=f'<path data-arrow="reference" d="M280 {y} C345 {y},385 {v},450 {v}" stroke="#347f86" stroke-width="2" fill="none" marker-end="url(#obj-tip)"/>'
    return out+'</svg>'
model('PA46','two-level-object-sharing','The two outer lists are distinct; their slots can still refer to the same inner list.',[
    ({'a':['X','Y'],'b':['X','Y'],'X':[2],'Y':[5]},objects('Outer copy shares both inner lists',['a[0]','b[0]','a[1]','b[1]'],['X = [2]','Y = [5]'],[(0,0),(1,0),(2,1),(3,1)]),'Copy outer slots; no inner list was copied.'),
    ({'a':['X','Y'],'b':['X','Y'],'X':[2,7],'Y':[5]},objects('Inner append changes the shared target',['a[0]','b[0]','a[1]','b[1]'],['X = [2,7]','Y = [5]'],[(0,0),(1,0),(2,1),(3,1)]),'Append seven through b[0]; a[0] sees the same X.'),
    ({'a':['X','Y'],'b':['X','Z'],'X':[2,7],'Y':[5],'Z':[9]},objects('Only b[1] redirects to a new inner object',['a[0]','b[0]','a[1]','b[1]'],['X = [2,7]','Y = [5]','Z = [9]'],[(0,0),(1,0),(2,1),(3,2)]),'Replace one b slot; a[1] stays attached to Y.')])
model('PA47','repeated-row-sharing','Three outer slots can select one mutable row; a comprehension creates separate row objects.',[
    ({'rows':['R','R','R'],'R':[0,0,0,0]},objects('Repeated rows before mutation',['bad[0]','bad[1]','bad[2]'],['R = [0,0,0,0]'],[(0,0),(1,0),(2,0)]),'All three links designate the same row.'),
    ({'rows':['R','R','R'],'R':[0,0,9,0]},objects('One shared row is changed',['bad[0]','bad[1]','bad[2]'],['R = [0,0,9,0]'],[(0,0),(1,0),(2,0)]),'The write through the second link is visible through all links.'),
    ({'rows':[[0,0,0,0],[0,0,9,0],[0,0,0,0]]},objects('Independent comprehension rows',['good[0]','good[1]','good[2]'],['R0 = [0,0,0,0]','R1 = [0,0,9,0]','R2 = [0,0,0,0]'],[(0,0),(1,1),(2,2)]),'Only the distinct second row changes.')])
model('PA59','pointer-and-character-sentinels','The outer null pointer differs from each inner string zero.',[
    ({'argv':['prog','x','yz',None]},objects('argv contains pointers, not a flat text matrix',['argv[0]','argv[1]','argv[2]','argv[3] = null'],['p,r,o,g,0','x,0','y,z,0'],[(0,0),(1,1),(2,2)]),'Only the first three pointer slots have character-array targets.'),
    ({'argv2index1':'z','argv2index2':0,'argv3':None},drawing('The third argument has its own terminator',[('argv[2] character elements',['y','z','0'])],[(0,1),(0,2)],'argv[3] has no target; argv[3][0] is invalid.'),'Read z at index one and zero at index two, not through the null sentinel.')])
model('PA72','ring-buffer-layout','Follow logical offsets around fixed physical slots; the head does not move in this append-position query.',[
    ({'head':5,'indices':[5,6,0,1],'length':4},drawing('Ring capacity7: logical order is 5,6,0,1',[('Physical indices',['v2','v3','free','free','free','v0','v1'])],[(0,i)for i in[5,6,0,1]],'Next append is physical index2.'),'Wrap from slot six to zero without reordering physical storage.'),
    ({'head':5,'tail':2,'emptyFullNeedLength':True},table('Length distinguishes empty and full',['Length','Head','Tail'],[[0,5,5],[4,5,2],[7,5,5]]),'Head equals tail for both empty and full; the length resolves it.')])
seq('PA73','Rectangular transpose: 2x3 becomes 3x2',[[0,1,2,3,4,5],[0,3,1,4,2,5]],['Values are labeled by their original offsets.','Destination order is [0,3,1,4,2,5]; movement map is [0,2,4,1,3,5].'],'rectangular-transpose')
model('MS_CS_1393_Q167','reverse-stride-copy','Each write uses a source index decreasing by two and a contiguous destination index.',[
    ({'sourceIndex':5-2*k,'dest':k,'copied':[60,40,20][:k+1]},drawing('MS Q167: six source elements',[('Source',[10,20,30,40,50,60]),('Destination',[60,40,20][:k+1]+['·']*(2-k))],[(0,5-2*k),(1,k)],'The guard precedes source access.',[(0,5-2*k,1,k)]),f'Copy source index {5-2*k} into destination {k}.')for k in range(3)]+[
    ({'sourceIndex':-1,'dest':3,'copied':[60,40,20]},drawing('Terminal call performs no access',[('Destination',[60,40,20])],note='n=-1; return without reading or writing.'),'Three copies and one guard-only call complete the even-length trace.')])
model('Phd_CS_1404_Q72','record-minimum-scan','The source counts successful strict updates after infinity initialization, not every comparison.',[
    ({'read':i,'value':v,'minimum':min([5,2,4,1,3][:i+1]),'updates':sum([5,2,4,1,3][j]==min([5,2,4,1,3][:j+1])for j in range(i+1))},drawing('PhD Q72: one actual permutation',[('A in source scan order',[5,2,4,1,3])],[(0,i)],'New minimum = '+str(min([5,2,4,1,3][:i+1]))),f'Read position {i+1}: '+('strict update.'if v==min([5,2,4,1,3][:i+1])else'no update.'))for i,v in enumerate([5,2,4,1,3])])
MODELS.update(NEW);save(D/'problem-visual-models.json',MODELS)
pagepath=D/'p_arrays.html';page=pagepath.read_text(encoding='utf8');spans=Sections(page).spans;assert len(spans)==83
records={q['id']:(q,n,n<=2)for n,q in enumerate(A+Q,1)}
for a,b,qid in sorted(spans,reverse=True):page=page[:a]+item(*records[qid])+page[b:]
rules=(B/'p_arrays-review.en.md').read_text(encoding='utf8')
rules=rules.replace('52. A difference-array range update adds at its left boundary and subtracts at its right boundary. The signs follow from starting and ending the change.','52. For an n-entry difference array, an empty range update is a no-op, including [n:n). For a nonempty range, add at the left boundary and subtract at the right only when it is below n. A separately allocated n+1 sentinel representation has another valid boundary contract.')
rules=rules.replace('66. Rotation by k on positive length n has $\\gcd(n,k)$ cycles under the modular step map. Track the direction of value movement explicitly.','66. Rotation by k on positive length n has $\\gcd(n,k)$ cycles. For left rotation, new position i reads old (i+k) modulo n; an old value moves instead to (i-k) modulo n. The two maps are inverses, not interchangeable value-movement directions.')
(B/'p_arrays-review.en.md').write_text(rules,encoding='utf8')
blocks=[]
for b in rules.split('\n\n'):
    m=re.fullmatch(r'(\d+)\. ([\s\S]+)',b)
    if m:blocks.append('<section class="review-rule"><h4>Rule '+m[1]+'</h4>'+text(m[2])+'</section>')
assert len(blocks)==80;it=iter(blocks);page,n=re.subn(r'<section class="review-rule">[\s\S]*?</section>',lambda _:next(it),page);assert n==80
page=page.replace('Student-approved chapter','Author-reviewed revision · awaiting student approval')
page=page.replace('p_arrays.css"','p_arrays.css?v=review-20261020"');page=re.sub(r'problem-visuals.js(?:\?[^"\s]*)?','problem-visuals.js?v=arrays-review-20261020',page)
pagepath.write_text(page,encoding='utf8')
p=D/'problem-visuals.js';s=p.read_text(encoding='utf8');s=re.sub(r'problem-visual-models.json\?[^\x27]*','problem-visual-models.json?v=arrays-review-20261020',s);p.write_text(s,encoding='utf8')
save(E/'p_arrays-answer-integration.json',{'status':'integrated_pending_full_quality_gates','solutions':83,'rules':80,'actualInputQuestionModels':len(NEW),'frames':sum(len(x['frames'])for x in NEW.values()),'studentApproved':False})
print('Integrated 81 replacement answers, two authentic solutions, 80 rules and',len(NEW),'exact question aids.')

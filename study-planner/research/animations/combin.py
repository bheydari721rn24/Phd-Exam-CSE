from common import node,frame,scene

def strip(values,k):
 ns=[node('value'+str(j),str(key)+'\n'+str(value),90+115*j,120,w=106,h=65,size=19,tone='done' if j<k else 'active' if j==k else 'plain') for j,(key,value) in enumerate(values)]
 return ns+[node('token','step '+str(k),90+115*min(k,len(values)-1),260,w=100,h=42,size=19,tone='active')]
def add(id,title,desc,invariant,records):
 fs=[frame(strip(vals,k),caption,metrics,formula,snapshot=q) for k,(vals,caption,metrics,formula,q) in enumerate(records)]
 return scene('comb-'+id,title,desc,invariant,fs)

vals=[('AB',1),('C+D',1),('r',1),('Y',1),('Z',0)]
add('dag','Topological propagation through shared logic','Compute a shared internal product once, then distribute it to both outputs.','Inputs A=B=D=H=1 and C=E=0 remain fixed; only evaluated gates advance.',[(vals[:k+1],f'Evaluate gate {k+1} in topological order. Earlier internal values remain available, and an output is computed only after every predecessor value has been determined.',{'computed gates':k+1},'',dict(kind='dag',step=k+1,values=[1,1,1,1,0][:k+1])) for k in range(5)])
records=[]
for i in range(8):
 e,r1,r0=(i>>2)&1,(i>>1)&1,i&1;g1=e*r1;g0=e*(1-r1)*r0
 records.append(([('E',e),('R1',r1),('R0',r0),('G1',g1),('G0',g0),('V',g1|g0)],f'Input row {i} is evaluated independently of earlier rows. Enabled request one suppresses the lower grant; validity equals the OR of the exclusive grants.',{'row':i},'G_1=ER_1,\\quad G_0=E\\overline{R_1}R_0',dict(kind='priority',row=i,g1=g1,g0=g0)))
add('priority','All priority-controller obligations','Traverse every enabled, disabled and simultaneous-request case.','At most one grant is high; a grant exists exactly when enable and some request are high.',records)
records=[]
on=[1,2,3,5,7]
for s in range(4):
 pair=[int(2*s+c in on) for c in [0,1]];names=['0','C','not C','1'];name=names[2*pair[0]+pair[1]]
 records.append(([('AB',format(s,'02b')),('C=0',pair[0]),('C=1',pair[1]),('data',name)],f'Select pair {format(s,"02b")} fixes A and B while C takes both values. The ordered pair {pair} determines exactly one residual data function, not an arbitrary mux connection.',{'data pin':s},'',dict(kind='cofactor',select=s,pair=pair)))
add('cofactor','Cofactors determine mux data pins','Read pairs 01, 11, 01, 01 as C, one, C, C.','Each selected pair checks both possible residual C values in the declared binary order.',records)
records=[]
for i in range(8):
 bits=list(map(int,format(i,'03b')));p=sum(bits)%2;m=int(sum(bits)>=2)
 records.append(([('address',format(i,'03b')),('decoder',str(i)),('parity',p),('majority',m),('word',str(p)+str(m))],f'Address {i} activates exactly decoder row {i}. Parity and majority independently select their output bits, producing stored word {p}{m} in the declared output order.',{'stored bits':16},'',dict(kind='rom',row=i,p=p,m=m)))
add('rom','A shared decoder generates two outputs','Read all eight words of the parity/majority ROM.','The first word bit is odd parity; the second is majority; addresses retain ABC order.',records)
records=[]
for i in range(8):
 a,b,c=(i>>2)&1,(i>>1)&1,i&1;p=1-a*b;q=1-a*c;y=1-p*q
 records.append(([('ABC',format(i,'03b')),('not AB',p),('not AC',q),('NAND',y),('A(B+C)',a*(b|c))],f'At row {i}, the first-stage NAND gates complement AB and AC. The final NAND restores their OR, so both displayed implementations agree on this fully specified row.',{'row':i},'\\overline{\\overline{AB}\\overline{AC}}=AB+AC',dict(kind='nand',row=i,p=p,q=q,y=y)))
add('nand','Polarity-correct NAND mapping','Verify the three-gate mapping on every input row.','The NAND output equals A(B+C) without assuming NAND associativity.',records)
records=[]
for i in range(8):
 a,b,c=(i>>2)&1,(i>>1)&1,i&1;f=a*(b|c);g=(a*b)|c
 records.append(([('ABC',format(i,'03b')),('reference',f),('candidate',g),('miter',f^g)],f'Compare both circuits using the same row {i}. The miter is one precisely when the candidate loses the required A guard on an asserted C input.',{'discrepancy':f^g},'',dict(kind='miter',row=i,f=f,g=g)))
add('miter','Find all functional counterexamples','Compare A(B+C) with the incorrect AB+C implementation.','The miter is the XOR of complete corresponding outputs, not a visual comparison of schematics.',records)
records=[]
for i in [7,6,3,2,0]:
 a,b,c=(i>>2)&1,(i>>1)&1,i&1;t=a*b;y=t|c;fault=c;detect=y^fault
 records.append(([('ABC',format(i,'03b')),('AB',t),('correct',y),('stuck 0',fault),('detected',detect)],f'Row {i} separates activation from observation. The product fault is activated only when AB is one and reaches the output only when C does not mask the OR.',{'detected':detect},'',dict(kind='fault',row=i,t=t,y=y,fault=fault)))
add('fault','Activate and propagate a stuck-at fault','Contrast an activated-but-masked fault with the detecting row 110.','Detection requires both a wrong internal value and a changed observed output.',records)
records=[]
for w in [3,4,5,6]:
 x=(1<<w)-2;s=x-(1<<w);inv=((1<<w)-1)^x
 records.append(([('width',w),('pattern',format(x,'0'+str(w)+'b')),('unsigned',x),('signed',s),('bit NOT',inv),('logical NOT',0)],f'Width {w} changes the unsigned interpretation and complement range. The signed value remains minus two for these sign-extended patterns, while logical negation remains the Boolean zero.',{'width':w},'',dict(kind='word',w=w,x=x,signed=s,inv=inv)))
add('word','Width and signedness change numerical meaning','Follow sign-extended negative-two patterns through four widths.','The unsigned value is 2^w−2; bitwise complement is one; logical negation is zero.',records)
records=[]
for k,(name,solutions) in enumerate([('q = q',[0,1]),('q = not q',[]),('q = q AND 0',[0])]):
 records.append(([('equation',name),('fixed points',','.join(map(str,solutions)) or 'none')],f'Equation {name} has the listed Boolean fixed points after exhaustive substitution of zero and one. Feedback alone therefore does not determine one universal number of stable assignments.',{'solutions':len(solutions)},'',dict(kind='feedback',case=k,solutions=solutions)))
add('feedback','Feedback existence and uniqueness','Compare two, zero and one algebraic fixed point without assuming electrical convergence.','Each fixed point is checked against its own equation; Boolean uniqueness does not certify analog settling.',records)
records=[]
for k,(en,d,y) in enumerate([(1,0,0),(0,1,0),(1,1,1),(0,1,1)]):
 records.append(([('enable',en),('data',d),('retained Y',y),('history',1 if k<2 else 2)],f'Checkpoint {k+1} follows a conditional assignment with no disabled branch. The two disabled checkpoints have identical current inputs but retain different values established by their preceding enabled histories.',{'checkpoint':k+1},'',dict(kind='latch',en=en,d=d,y=y,step=k)))
add('latch','Missing assignment exposes hidden history','Follow two histories ending at en=0 and d=1.','An enabled assignment updates Y; a disabled execution retains Y in this explicitly stateful model.',records)
records=[]
for k,(name,times) in enumerate([('balanced',[1,11,12]),('chain',[1,2,11]),('early subtree',[1,2,11])]):
 records.append(([('organization',name),('first',times[0]),('second',times[1]),('output',times[2])],f'Organization {name} uses latest-arrival maxima at each unit-delay AND gate. The late input arrives at time ten, so giving it a final one-gate path can outperform a fully balanced topology.',{'output bound':times[-1]},'',dict(kind='arrival',case=k,times=times)))
add('arrival','Late input changes the best tree','Compare balanced and late-last structures for four AND inputs.','Each output time is a structural latest-arrival bound with explicitly placed late input.',records)
records=[]
for k,(name,lo,hi) in enumerate([('primary',0,0),('p=AB',1,3),('q=p+C',2,7),('Y=qD',1,9)]):
 records.append(([('net',name),('earliest',lo),('latest',hi)],f'For net {name}, compute contamination with predecessor minima and propagation with predecessor maxima. These independent structural bounds do not assert that every possible input transition reaches the output.',{'earliest':lo,'latest':hi},'',dict(kind='interval',step=k,lo=lo,hi=hi)))
add('interval','Different extrema for contamination and propagation','Compute the asymmetric interval through a three-gate network.','Bounds use delays (1,3), (2,4), (1,2) for AND, OR, AND respectively.',records)
records=[]
for k,a in enumerate([0,1,0,1]):
 records.append(([('A',a),('not A',1-a),('product',0),('structural path','present')],f'Stable input A={a} always gives product zero because its two branches are correlated complements. Structural connectivity does not provide independent side-input assignments or prove a stable output transition.',{'settled output':0},'A\\overline A=0',dict(kind='falsepath',a=a,y=0)))
add('falsepath','Reconvergence constrains sensitization','Toggle the primary input while evaluating only settled Boolean values.','Stable output remains zero; this model deliberately makes no physical glitch-freedom claim.',records)
records=[]
for k,(en,r1,r0) in enumerate([(0,1,1),(1,0,0),(1,0,1),(1,1,1)]):
 g1=en*r1;g0=en*(1-r1)*r0
 records.append(([('en_n',1-en),('R1',r1),('R0',r0),('G1_n',1-g1),('G0_n',1-g0)],f'Convert the active-low enable to logical enable before computing priority, then complement each observed grant. This row preserves disabled suppression and gives a low active grant only to the selected requester.',{'logical enable':en},'',dict(kind='active-low',en=en,r1=r1,r0=r0,outputs=[1-g1,1-g0])))
add('active-low','Transform both sides of a polarity interface','Observe disabled high grants and enabled low assertions without mixing input/output complements.','Active-low inputs transform arguments; active-low outputs transform results.',records)

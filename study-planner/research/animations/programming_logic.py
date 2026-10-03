"""Executable-state traces and deliberately bounded digital models."""
from common import *
from fractions import Fraction as F
from itertools import product

def assignments():
    for simultaneous in [False,True]:
        states=[(2,5),(5,2)] if simultaneous else [(2,5),(5,5),(5,5)]
        frames=[]
        for k,(x,y) in enumerate(states):
            frames.append(frame([node('x',f'x = {x}',190,110,w=170,tone='active'),node('y',f'y = {y}',570,110,w=170,tone='done' if k else 'plain')],'Read '+('both old values before updating either target' if simultaneous else 'the current value of the right-hand variable before this assignment')+'. Assignment changes the program store; it is not a symmetric equation that preserves both old values.',{'Step':k,'x':x,'y':y,'Semantics':'simultaneous' if simultaneous else 'sequential'},line=0 if simultaneous else min(k,1)))
        scene('assignment-simultaneous' if simultaneous else 'assignment-sequential','Simultaneous exchange' if simultaneous else 'Sequential assignment is not a swap','The initial store is x=2, y=5. Compare the final stores under the two explicitly different update rules.','A sequential assignment reads the current store; a simultaneous exchange reads both old values.',frames,['(x,y) <- (y,x)'] if simultaneous else ['x <- y','y <- x'])
    frames=[]
    for x in [0,2]:
        frames.append(frame([node('guard',f'x != 0: {x!=0}',190,100,w=260),node('rhs','10/x > 1' if x else 'not evaluated',570,100,w=265,tone='done' if x else 'warning')],'Evaluate the left operand of logical AND first. Short-circuit semantics skip the division when the left operand is false, so the zero input does not trigger division by zero.',{'x':x,'Right operand evaluated':bool(x),'Final condition':bool(x and 10/x>1)},line=0))
    scene('short-circuit','Short-circuit AND protects a partial operation','This model uses a left-to-right short-circuit logical operator. A non-short-circuit operator or reversed operand order changes the safety argument.','The division is evaluated only after the nonzero guard succeeds.',frames,['if x != 0 AND 10/x > 1: ...'])
    frames=[]
    for value in [7,8,15,16,17]:
        unsigned=value%16;signed=unsigned if unsigned<8 else unsigned-16
        frames.append(frame([node('source',str(value),140,110),node('bits',format(unsigned,'04b'),380,110,w=150),node('signed',str(signed),610,250,tone='warning' if signed!=value else 'done')],'Encode the integer modulo sixteen in four bits, then interpret the same bits under unsigned or two’s-complement rules. The bit pattern alone does not specify the numeric interpretation.',{'Input integer':value,'Unsigned interpretation':unsigned,'Signed interpretation':signed,'Width':4},formula=rf'{value}\bmod16={unsigned}',edges=[{'from':'source','to':'bits','directed':True},{'from':'bits','to':'signed','directed':True}]))
    scene('finite-representation','Finite-width values: bits and interpretations','This is an explicit four-bit mathematical encoding model, not permission to rely on undefined signed overflow in C.','Unsigned values range from zero to fifteen; signed values range from negative eight to seven.',frames)
    frames=[]
    for v,rounded in [(16777216,16777216),(16777217,16777216),(16777218,16777218),(16777219,16777220)]:
        frames.append(frame([node('exact',str(v),210,105,w=265),node('rounded',str(rounded),550,250,w=265,tone='warning' if v!=rounded else 'done')],'Round the exact positive integer to binary32 using round-to-nearest with ties to even. At this exponent, adjacent representable values are separated by two, so some neighboring integers collapse.',{'Exact integer':v,'Binary32 result':rounded,'Local spacing':2,'Rounding error':rounded-v},edges=[{'from':'exact','to':'rounded','directed':True}]))
    check('binary32 tie even',int(__import__('struct').unpack('f',__import__('struct').pack('f',16777217))[0])==16777216)
    scene('float-rounding','Floating-point spacing and ties to even','The finite example is IEEE binary32 at 2^24 with round-to-nearest, ties-to-even. It shows representational rounding, not a universal real-arithmetic rule.','The unit spacing doubles at the stated exponent; halfway values choose an even significand.',frames)

def control():
    for input in [-1,0,2]:
        frames=[];result='negative' if input<0 else 'zero' if input==0 else 'positive'
        for k in range(2 if input<0 else 3):
            nodes=[node('x',f'x = {input}',130,80),node('first','x < 0',380,80,w=150,tone='active' if k==0 else 'done'),node('second','x == 0',380,180,w=150,tone='active' if k==1 and input>=0 else 'plain'),node('out',result if k==(1 if input<0 else 2) else 'pending',630,270,w=180,tone='done')]
            frames.append(frame(nodes,'Inspect the next condition on the selected control-flow path. Once a branch is selected, the remaining alternatives are skipped rather than executed in sequence.',{'Input':input,'Selected branch':result,'Step':k},line=k))
        scene('branch-'+str(input).replace('-','m'),'Conditional path for '+str(input),'Compare three mutually exclusive paths through one if–else-if–else chain. Only the selected body executes.','Exactly one of the three sign cases is selected.',frames,['if x < 0: negative','else if x == 0: zero','else: positive'])
    frames=[];s=0
    for i in range(1,6):
        if i==3:action='continue: skip addition'
        elif i==5:action='break: leave loop'
        else:s+=i;action='add current i'
        frames.append(frame([node('i',f'i = {i}',170,100,w=170,tone='active'),node('sum',f'sum = {s}',550,100,w=180,tone='done'),node('transfer',action,380,260,w=360,tone='warning' if i in [3,5] else 'plain')],'Follow the '+action+' transition. Continue skips the remaining body but still reaches the for-loop update; break exits without executing that update.',{'Loop index':i,'Accumulated sum':s,'Transfer':action},line=1 if i==3 else 2 if i==5 else 3))
    check('continue break trace',s==7)
    scene('loop-transfers','Continue and break: different control-flow edges','The concrete for loop starts at one, skips three, and stops at five. Its output is seven; five is never added.','The sum contains only values added before the break, excluding continued iterations.',frames,['for i = 1,...,6','if i == 3: continue','if i == 5: break','sum += i'])
    frames=[]
    for k in range(10):
        v=k%8;frames.append(frame([node('value',f'x = {v}',100+v*80,150,tone='warning' if k>=8 else 'active')],'Increment the explicitly modeled three-bit unsigned counter and wrap modulo eight. A guard that accepts every represented value cannot force termination when the state repeats.',{'Iteration':k,'Counter':v,'Repeated state':k>=8},formula=r'x\leftarrow(x+1)\bmod8',counterexample=k>=8))
    scene('wraparound-loop','Wraparound counterexample to an unbounded ranking claim','The model deliberately uses modular unsigned arithmetic. An integer ranking proof cannot be transferred to it without accounting for wraparound.','The finite store repeats after eight increments, so this guard does not terminate the loop.',frames,['x = 0','while x <= 7: x = (x+1) mod 8'])

def number_codes():
    n=45;frames=[];digits=[]
    while n:
        q,r=divmod(n,2);digits.append(r);frames.append(frame([node('n',str(n),150,100),node('q',str(q),380,100),node('r',str(r),610,100,tone='active')]+[node('d'+str(j),v,100+j*90,265,tone='done') for j,v in enumerate(digits)],'Divide the current quotient by two and save its remainder. Remainders arrive least-significant first and must be reversed when writing the final positional numeral.',{'Current dividend':n,'Quotient':q,'Remainder':r,'Saved low-first bits':''.join(map(str,digits))},formula=rf'{n}=2\cdot{q}+{r}'));n=q
    check('base conversion',sum(v*2**j for j,v in enumerate(digits))==45)
    scene('base-conversion','Integer base conversion by repeated division','The example converts forty-five to binary. Every step uses a quotient–remainder identity with remainder zero or one.','The saved remainders encode the processed low-order bits.',frames)
    x=F(3,10);frames=[];bits=[];seen={}
    for k in range(8):
        before=x;twice=2*x;digit=twice.numerator//twice.denominator;x=twice-digit;bits.append(digit)
        frames.append(frame([node('fraction',str(before),170,100,w=170),node('twice',str(twice),380,100,w=170),node('rest',str(x),590,250,w=170,tone='active')],'Multiply the fractional remainder by two, emit the integer part, and retain the new fractional remainder. Repeated remainder states explain the recurring binary expansion.',{'Bit emitted':digit,'Bit number':k+1,'Remainder':str(x),'Prefix':''.join(map(str,bits))},formula=rf'2\cdot\frac{{{before.numerator}}}{{{before.denominator}}}={digit}+\frac{{{x.numerator}}}{{{x.denominator}}}'))
    scene('fraction-conversion','Recurring binary fractions: exact remainder dynamics','The fraction three tenths is tracked exactly with rational arithmetic. Displayed remainders are not floating-point approximations.','Each emitted bit and new remainder satisfy the exact doubling identity.',frames)
    frames=[]
    for n in range(8):
        g=n^(n>>1);changed=None if n==0 else (g^((n-1)^((n-1)>>1))).bit_count();check('Gray consecutive distance',changed in [None,1])
        frames.append(frame([node('binary',format(n,'03b'),210,105,w=210),node('gray',format(g,'03b'),550,250,w=210,tone='active')],'Convert the next binary index to reflected Gray code. Compare this codeword with the previous one; adjacent indices differ in exactly one Gray bit.',{'Index':n,'Binary':format(n,'03b'),'Gray':format(g,'03b'),'Changed Gray bits':'not applicable' if changed is None else changed},formula=r'g=n\oplus\lfloor n/2\rfloor',edges=[{'from':'binary','to':'gray','directed':True}]))
    scene('gray-code','Reflected Gray code: one-bit transitions','This finite three-bit sequence covers all eight codewords. One-bit adjacency is a coding property, not a promise that arbitrary asynchronous circuitry cannot glitch.','Consecutive reflected Gray codewords have Hamming distance one.',frames)
    # Hamming(7,4), even parity; original data 1,0,1,1.
    word=[0,0,1,0,0,1,1]
    for p in [1,2,4]:word[p-1]=sum(word[j-1] for j in range(1,8) if j&p and j!=p)%2
    bad=word[:];bad[4]^=1;syndrome=0;frames=[]
    frames.append(frame([node('b'+str(i),v,65+i*100,100,tone='plain') for i,v in enumerate(word)],'Construct the valid seven-bit word with even parity on each indexed parity-check subset. The data bits occupy positions three, five, six, and seven.',{'Codeword':''.join(map(str,word)),'Parity convention':'even'}))
    for p in [1,2,4]:
        s=sum(bad[j-1] for j in range(1,8) if j&p)%2;syndrome+=p*s
        frames.append(frame([node('b'+str(i),v,65+i*100,100,tone='active' if (i+1)&p else 'plain') for i,v in enumerate(bad)],'Check the indexed parity subset after a single flipped bit. A failed check contributes its positional weight to the syndrome, which identifies the corrupted position under the single-error assumption.',{'Check weight':p,'Parity result':s,'Accumulated syndrome':syndrome,'Flipped position':5},formula=rf's_{{{p}}}={s}'))
    check('Hamming syndrome',syndrome==5);bad[syndrome-1]^=1;check('Hamming correction',bad==word)
    frames.append(frame([node('b'+str(i),v,65+i*100,100,tone='done' if i==4 else 'plain') for i,v in enumerate(bad)],'Flip the position identified by the syndrome to restore the original codeword. The correction is justified only under the stated single-bit error model.',{'Syndrome':syndrome,'Corrected position':5,'Recovered original':True}))
    scene('hamming-code','Hamming(7,4): parity checks, syndrome and correction','One bit at position five is flipped. Plain Hamming(7,4) must not be described as reliably correcting two errors.','Even-parity subset checks locate a single-bit error through their weighted syndrome.',frames)

def circuits():
    frames=[]
    # Transport-delay model: x falls at zero, inverter 2, AND 1, OR 1.
    states=[(-1,1,0,1,0,1),(0,0,0,1,0,1),(1,0,0,0,0,1),(2,0,1,0,0,0),(3,0,1,0,1,0),(4,0,1,0,1,1)]
    for time,x,nx,a,b,f in states:
        ns=[node('x',f'x = {x}',90,80,w=110),node('inv',f'NOT x = {nx}',270,250,w=180,tone='active' if time==2 else 'plain'),node('a',f'x AND y = {a}',465,80,w=240),node('b',f'NOT x AND z = {b}',465,250,w=250),node('f',f'F = {f}',680,160,w=110,tone='warning' if f==0 else 'done')]
        frames.append(frame(ns,'Advance to the next scheduled gate event after x falls while y and z remain one. Unequal path delays briefly leave both product terms zero even though the ideal Boolean output remains one.',{'Time':time,'Inverter delay':2,'AND delay':1,'OR delay':1,'Actual output':f,'Ideal steady output':1},formula=r'F=xy+\overline{x}z',edges=[{'from':'x','to':'a','directed':True},{'from':'x','to':'inv','directed':True},{'from':'inv','to':'b','directed':True},{'from':'a','to':'f','directed':True},{'from':'b','to':'f','directed':True}],counterexample=f==0,snapshot={'time':time,'x':x,'notx':nx,'a':a,'b':b,'f':f}))
    scene('static-hazard','Static-one hazard: scheduled events on unequal paths','The model uses transport delay: inverter two time units, AND and OR one each. It is a logical timing model, not a transistor waveform or inertial-pulse model.','With y=z=1, the steady function is one; the unequal paths produce a low output from time two to four.',frames)
    frames=[]
    for time,x,nx,a,b,f in states:
        frames.append(frame([node('a',f'xy = {a}',170,85,w=170),node('b',f'NOT x z = {b}',170,180,w=220),node('c','yz = 1',170,275,w=170,tone='done'),node('f','F = 1',570,180,w=170,tone='done')],'Hold the added consensus product at one while the two original paths respond to the input transition. The redundant steady-state term bridges their timing gap without changing the truth table.',{'Time':time,'Consensus product':1,'Output with consensus':1},formula=r'xy+\overline{x}z+yz=xy+\overline{x}z',edges=[{'from':a,'to':'f','directed':True} for a in ['a','b','c']]))
    scene('hazard-consensus','Consensus term: bridge the static-one hazard','The consensus term is already stable because y and z do not change. This demonstrates this specific single-input transition, not arbitrary multiple-input hazard freedom.','The stable yz term keeps the OR input high throughout the delayed transition.',frames)
    frames=[]
    for a,b in product([0,1],repeat=2):
        pdn=bool(a and b);pun=not pdn;out=int(pun);check('CMOS NAND complement',pun!=pdn and out==1-(a&b))
        frames.append(frame([node('pa','pA: '+('OFF' if a else 'ON'),220,90,w=160,tone='plain' if a else 'done'),node('pb','pB: '+('OFF' if b else 'ON'),530,90,w=160,tone='plain' if b else 'done'),node('na','nA: '+('ON' if a else 'OFF'),380,210,w=160,tone='done' if a else 'plain'),node('nb','nB: '+('ON' if b else 'OFF'),380,290,w=160,tone='done' if b else 'plain')],'Evaluate the ideal switches in a CMOS NAND gate. The parallel pull-up network conducts when either input is zero; the series pull-down path requires both inputs to be one.',{'A':a,'B':b,'Pull-up path conducts':pun,'Pull-down path conducts':pdn,'Output':out},formula=r'Y=\overline{AB}',edges=[{'from':'na','to':'nb','tone':'active' if pdn else 'plain'}]))
    scene('cmos-nand','CMOS NAND: parallel pull-up and series pull-down','Transistors are modeled as ideal conducting or nonconducting switches under stable binary inputs. Rise times, capacitances and transient short-circuit currents require a richer physical model.','Exactly one stable conducting network connects the output to its intended rail.',frames)
    frames=[]
    for a,b in product([0,1],repeat=2):
        n=1-(a&b);q=1-(n&n)
        frames.append(frame([node('a',f'A = {a}',130,80),node('b',f'B = {b}',130,255),node('n',f'NAND = {n}',390,165,w=220),node('q',f'AND = {q}',640,165,w=170,tone='done')],'Compute the first NAND output and feed it to both inputs of a second NAND. The second gate inverts the intermediate signal, implementing AND using only NAND gates.',{'A':a,'B':b,'Intermediate':n,'Output':q},formula=r'AB=\overline{\overline{AB}}',edges=[{'from':'a','to':'n','directed':True},{'from':'b','to':'n','directed':True},{'from':'n','to':'q','directed':True}]))
    scene('nand-mapping','Technology mapping: build AND using only NAND','The truth-table trace covers all four stable inputs and explicitly shows the tied inputs of the inverter stage.','The two-stage NAND network computes the same stable Boolean function as AND.',frames)

assignments();control();number_codes();circuits()

"""Independent bounded semantic oracle; no C/C++ compiler is invoked."""
import contextlib
import hashlib
import io
import json
import math
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(r"C:/Users/bheydari/.codex/.chatgpt-projects/g-p-6ab41269e8bc8191af2b98ca68a67648/study-planner")
OUT = ROOT / 'research/deep-library-revision'
questions = json.loads((ROOT / 'research/p_functions-questions.json').read_text(encoding='utf-8'))
qmap = {q['id']: q for q in questions}
checks = []
def check(name, passed, evidence):
    checks.append(dict(name=name, passed=bool(passed), evidence=evidence))
    if not passed:
        raise AssertionError(name)

# Execute the actual stated blocks, not certificate substitutes. Required calls
# written in prose/comments are appended explicitly in the observer field.
observers = {
64: 'answer=[x,y]',
65: 'answer=[x,y,x is y]',
66: 'answer=[x,y,x is y]',
67: 'answer=[x,y,x is y]',
68: 'answer=[a,b]',
69: 'answer=[r1,r2]; identities={"snapshots_distinct":r1 is not r2,"default":f.__defaults__[0]}',
70: 'answer=[r1,r2,r3]; identities={"snapshots_pairwise_distinct":len({id(r1),id(r2),id(r3)})==3,"default":f.__defaults__[0]}',
71: 'answer=[r1,r2,r1 is r2]',
72: 'f()',
73: 'answer=[x,r]',
74: 'answer=[a(3),b(3)]; identities={"function_distinct":a is not b,"closure_cells_distinct":a.__closure__[0] is not b.__closure__[0]}',
75: 'answer=g()',
76: 'answer=[f(),f(),f()]',
77: 'functions=build(); answer=[f() for f in functions]; identities={"three_distinct_functions":len({id(f) for f in functions})==3,"shared_closure_cell":len({id(f.__closure__[0]) for f in functions})==1}',
78: 'functions=build(); answer=[f() for f in functions]; identities={"defaults":[f.__defaults__ for f in functions],"closures":[f.__closure__ for f in functions]}',
79: 'answer=[r,i]',
80: 'f(1,a=3)',
81: 'answer=f(1,c=7)',
82: 'answer=r',
83: 'answer=f(3)',
}
python_runs=[]
for n in range(64,84):
    q=qmap[f'PF{n}']
    block=re.search(r'~~~python\n(.*?)\n~~~',q['stem'],re.S).group(1)
    observer=observers[n]
    harness='''import contextlib,io,json
ns={}
buf=io.StringIO()
exception=None
with contextlib.redirect_stdout(buf):
 try:
  exec(BLOCK,ns)
  exec(OBSERVER,ns)
 except Exception as e:
  exception={"type":type(e).__name__,"message":str(e)}
print(json.dumps({"answer":ns.get("answer"),"stdout":buf.getvalue(),"exception":exception,"identities":ns.get("identities")},ensure_ascii=False))
'''.replace('BLOCK',repr(block)).replace('OBSERVER',repr(observer))
    proc=subprocess.run([sys.executable,'-I','-c',harness],capture_output=True,text=True,check=True)
    result=json.loads(proc.stdout)
    expected=q['certificate']['data']['answer']
    actual=result['exception']['type'] if result['exception'] else result['answer']
    check(q['id']+' actual stated Python',actual==expected,dict(actual=actual,expected=expected,stdout=result['stdout']))
    check(q['id']+' no unexpected printing',result['stdout']=='',result['stdout'])
    python_runs.append(dict(id=q['id'],source_kind='actual stated block plus explicitly requested call/observer',block=block,observer=observer,**result))

# PF85 has no executable block in its stem: reconstruction is labelled as such.
def make_counter():
    n=0
    def increment():
        nonlocal n
        n+=1
        return n
    return increment
a,b=make_counter(),make_counter()
pf85=[a(),a(),b(),a()]
check('PF85 labelled reconstruction',pf85==[1,2,1,3] and a.__closure__[0] is not b.__closure__[0],dict(returns=pf85,distinct_cells=a.__closure__[0] is not b.__closure__[0]))

gcd_cases=gcd_candidates=0
for a in range(1,101):
    for b in range(1,101):
        gcd_cases+=1
        d=min(a,b)
        while True:
            gcd_candidates+=1
            assert all(a%k or b%k for k in range(d+1,min(a,b)+1))
            if a%d==0 and b%d==0:
                assert d==math.gcd(a,b)
                break
            d-=1
check('PF49 descending divisor maximality',True,dict(input_pairs=gcd_cases,candidate_states=gcd_candidates,range='a,b=1..100',initialization='d=min(a,b)',decrement='only after non-common candidate'))

for n in range(101):
    total=0;k=1
    while k<=n:
        assert 1<=k<=n+1 and total==(k-1)*k//2
        total+=k;k+=1
    assert k==n+1 and total==n*(n+1)//2 and total<=5050 and k<=101
check('PF50 stated triangular contract',True,dict(cases=101,n_range=[0,100],maximum_total=5050,maximum_k=101))

for n in range(151):
    p=0
    for k in range(n):
        assert p==2**k-1
        p+=2**k
    assert p==2**n-1
check('PF51 unbounded geometric invariant',True,dict(cases=151,n_range=[0,150],machine_safety='not implied for a C implementation'))

# Explicit corrected binary power: square only if future exponent bits exist.
def guarded_power(x,y):
    r,b,e=1,x,y
    operations=[]
    while e>0:
        assert r*b**e==x**y
        if e%2:
            r*=b; operations.append(r)
        e//=2
        if e:
            b*=b; operations.append(b)
    return r,operations
power_cases=0; safe_cases=0
for x in range(-50,51):
    for y in range(16):
        r,ops=guarded_power(x,y)
        power_cases+=1
        assert r==x**y
        if -(2**31)<=r<=2**31-1:
            safe_cases+=1
            assert all(-(2**31)<=v<=2**31-1 for v in ops)
check('PF52 explicit guarded binary-power reconstruction',True,dict(cases=power_cases,final_int32_fit_cases=safe_cases,bounds='x=-50..50,y=0..15',zero_exponent='returns 1, including adopted 0**0 convention',scope='this explicit algorithm, not an unspecified correction'))
check('PF53 needless final square counterexample',50000<=2**31-1 and 50000**2>2**31-1,dict(final_power=50000,unused_square=50000**2,int32_max=2**31-1))

qr_cases=0
for n in range(101):
    for d in range(1,51):
        q,r=divmod(n,d);qr_cases+=1
        assert n==q*d+r and 0<=r<d
        for q2 in range(102):
            r2=n-q2*d
            assert not(0<=r2<d) or (q2,r2)==(q,r)
check('PF54 quotient remainder enumeration',True,dict(cases=qr_cases,alternative_q_tests=qr_cases*102,stated_example=divmod(47,6),limits='n=0..100,d=1..50; proof supplies universal positive-d argument'))

signed_cases=0
for n in range(-100,101):
    for d in list(range(-20,0))+list(range(1,21)):
        q=(abs(n)//abs(d))*(-1 if (n<0)!=(d<0) else 1)
        r=n-q*d;signed_cases+=1
        assert abs(r)<abs(d) and (r==0 or (r<0)==(n<0))
        if d>0:
            qe,re=(q-1,r+d) if r<0 else (q,r)
            assert 0<=re<d and n==qe*d+re
check('PF55 mathematical model of C signed quotient',True,dict(cases=signed_cases,stated_q=-4,stated_r=-3,scope='exact integer truncation model, no C execution; nonzero denominator and representable quotient required'))

interval_cases=0
for bits in range(4,17):
    lo,hi=-(2**(bits-1)),2**(bits-1)-1
    bound_lo=max(lo,-((-lo)//2)-3)
    bound_hi=min(hi,hi//2-3)
    for x in range(lo,hi+1):
        interval_cases+=1
        safe=lo<=x+3<=hi and lo<=2*(x+3)<=hi
        assert safe==(bound_lo<=x<=bound_hi)
lo,hi=-(2**31),2**31-1
lower,upper=-1073741827,1073741820
boundaries=[]
for x in [lower-1,lower,upper,upper+1]:
    boundaries.append(dict(x=x,first=x+3,second=2*(x+3),safe=lo<=x+3<=hi and lo<=2*(x+3)<=hi))
assert [b['safe'] for b in boundaries]==[False,True,True,False]
check('PF57 exact composite interval',True,dict(exhaustive_cases=interval_cases,two_complement_widths=[4,16],int32_boundaries=boundaries,portability='general interval must use actual INT_MIN/INT_MAX; int32 is an additional assumption'))

s=0; returns=[]
for m in range(1,101):
    y=5
    for _ in range(2):
        s+=1;y+=s
    returns.append(y)
    assert y==5+4*m-1 and s==2*m
check('PF59 stateful sequential callback',True,dict(cases=100,first_two_results=returns[:2],final_s=s,formula='mth apply(step,5) = 4m+4',scope='mathematical bounded trace, int safety separately required'))

copy_out=[]
for order in [('p','q'),('q','p')]:
    caller=4;locals_={'p':10,'q':20}
    for name in order:caller=locals_[name]
    copy_out.append(caller)
check('PF62 stipulated copy-out model',copy_out==[20,10],dict(orders=['p then q','q then p'],results=copy_out,scope='theoretical stipulated semantics, neither C nor C++ references'))
i=3
by_name=[i+1];i+=1;by_name.append(i+1)
i=3;p=i+1;by_value=[p];i+=1;by_value.append(p)
check('PF63 stipulated by-name model',by_name==[4,5] and by_value==[4,4],dict(by_name=by_name,by_value=by_value,caller_i=4,scope='body explicitly has permission to modify caller i'))

for n in range(301):
    persistent=total=0
    for d in range(1,n+1):
        persistent+=d;total+=persistent
        assert persistent==d*(d+1)//2
    assert total==n*(n+1)*(n+2)//6
check('PF84 persistent triangular returns',True,dict(cases=301,n_range=[0,300],n4=dict(returns=[1,3,6,10],sum=20),closed_form='n(n+1)(n+2)/6',machine_safety='intermediate counter, caller accumulator, and evaluated closed-form products require separate bounds'))

classifications={
'PF37':'C17 function executions ordered but order unspecified; commutative sum invariant 3, counter 2',
'PF38':'undefined behavior: unsequenced modifications, not two numerical outcomes',
'PF39':[0,1,2,-1],
'PF40':[1,8],
'PF41':{'integer_quotient':2,'double_return':2.0,'fractional_cast_before_division':2.25},
'PF42':'using result of non-void fallthrough is undefined, except initial-main rule not applicable',
'PF43':'mathematical terminating domain nonnegative integers; stated actual C multiply additionally bounded',
'PF44':{'function':[6,4],'macro':'undefined unsequenced writes'},
'PF45':{'r':4,'i':5,'reason':'conditional first operand before selected operand'},
'PF46':'fixed float parameter vs trailing variadic float-to-double promotion',
'PF47':{'stdout':'5\n8\n','return':8},
'PF48':'constant-one counterexample satisfies common-positive-divisor contract without maximality',
'PF56':'equal result relation does not imply equal effects or termination',
'PF58':{'at4':28,'formula':'9x-8'},
'PF60':[11,7],
'PF61':18,
'PF86':'dangling returned reference does not extend ordinary automatic-local lifetime',
'PF87':'parameter adjusted to int*; sizeof is pointer size, not array size',
'PF88':{'stateful_s':2,'pure_s':0},
'PF89':{'final_x':6,'local_b_before_return':9},
}
result={
 'status':'pass',
 'source_sha256':hashlib.sha256((ROOT/'research/p_functions-questions.json').read_bytes()).hexdigest(),
 'python_version':sys.version,
 'checks':checks,
 'check_count':len(checks),
 'actual_python_blocks':len(python_runs),
 'python_runs':python_runs,
 'manual_semantic_classifications':classifications,
 'limitations':['No C/C++ compilation or execution.','Finite enumerations do not replace proofs outside tested ranges.','PF85 and guarded-power implementation are explicitly reconstructed because full executable blocks are absent from those stems.','This oracle checks current question JSON; it does not certify later rewritten prose, visuals, or browser rendering.']
}
(OUT/'p_functions-remaining-oracle.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'status':result['status'],'check_count':len(checks),'actual_python_blocks':len(python_runs),'output':str(OUT/'p_functions-remaining-oracle.json')},indent=2))

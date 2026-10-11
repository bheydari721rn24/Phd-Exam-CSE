from pathlib import Path
from fractions import Fraction
import copy,json,math,sys
B=Path(__file__).resolve().parent;R=B.parent;sys.path.insert(0,str(B/'exam-rewrite'));import mathml
def make(id,title,description,samples,formula,caption):
    frames=[]
    for i,s in enumerate(samples):
        f=formula(s);c=caption(s)
        frames.append(dict(nodes=[],edges=[],snapshot=copy.deepcopy(s),caption=c,captionHtml='<p>'+c+'</p>',metrics={'Integer input':s['n'],'Displayed ordinate':s['ordinate']},formula=f,formulaHtml='<div class="formula-block">'+mathml.render(f,True)+'</div>',line=0,teaching=dict(operation='Evaluate the exact integer input and normalize',why=c,currentState=copy.deepcopy(s),initial=i==0,activeLine=0,checks=[],changes=[],mode='plot',reading='Saved points are finite illustrations. The written subsequence or envelope argument proves the infinite-tail statement.')))
    return dict(id=id,title=title,description=description,descriptionHtml='<p>'+description+'</p>',invariant='Each point belongs to the stated integer input and the specified normalized function; no continuous interpolation is claimed.',visual=dict(type='plot',claim='Question-specific discrete ratio or log-ratio with fixed, labeled axes.',revision='exact-asymptotic-examples-v1'),code=['Evaluate the chosen integer input, then the specified normalized quantity'],frames=frames)
scenes={}
rows=[dict(n=n,ordinate=str(Fraction(n*n if n%2 else n,n)),family='odd quadratic' if n%2 else 'even linear') for n in range(1,17)]
scenes['asym-parity-ratio']=make('asym-parity-ratio','Question 7: one upper envelope fails on odd inputs','The ratio to n is one on even inputs and n on odd inputs. These finite points illustrate the two unbounded subsequences analyzed in the solution.',rows,lambda s:rf'\frac{{f({s["n"]})}}{{{s["n"]}}}={s["ordinate"]}',lambda s:f'At integer n={s["n"]}, the {s["family"]} definition gives ratio {s["ordinate"]}. The even points stay at one; the odd points grow with the input.')
rows=[dict(n=n,ordinate=str(Fraction(2**(n.bit_length()-1),n)),power=2**(n.bit_length()-1)) for n in [1,2,3,4,7,8,15,16,31,32]]
scenes['asym-floor-ratio']=make('asym-floor-ratio','Question 46: binary blocks and a nonconvergent ratio','Every displayed ratio lies above one half and at most one. Block starts return to one; block ends approach one half. The exact subsequences in the solution establish nonconvergence.',rows,lambda s:rf'\frac{{2^{{\lfloor\log_2 {s["n"]}\rfloor}}}}{{{s["n"]}}}=\frac{{{s["power"]}}}{{{s["n"]}}}',lambda s:f'At integer n={s["n"]}, the largest power of two no greater than n is {s["power"]}. The exact normalized ratio is {s["ordinate"]}. Discrete jumps at block boundaries do not violate the tight linear envelopes.')
rows=[]
for k in range(4):
    for sign in [1,-1]:
        phase=(math.pi/2 if sign==1 else 3*math.pi/2)+2*math.pi*k;n=math.floor(math.exp(phase));t=math.log(n);e=math.sin(t);z=t*e
        assert e>=.5 if sign==1 else e<=-.5
        rows.append(dict(n=n,phase=phase,logn=t,exponent=e,ordinate=z,sign=sign))
scenes['asym-log-oscillation']=make('asym-log-oscillation','Question 45: integer subsequences in logarithmic coordinates','Horizontal coordinate is ln(n); vertical coordinate is ln(f(n)/n squared). Positive and negative sampled subsequences witness opposite directions. Floating values are display approximations; the solution proves the integer-subsequence claims analytically.',rows,lambda s:rf'\ln R({s["n"]})=\ln({s["n"]})\sin(\ln({s["n"]}))',lambda s:f'Round the exponential phase down to integer n={s["n"]}. Its logarithm is approximately {s["logn"]:.6f}, the sine exponent is {s["exponent"]:.6f}, and ln(R) is {s["ordinate"]:.6f}. This belongs to the '+('large-ratio subsequence, with exponent at least one half.' if s['sign']==1 else 'small-ratio subsequence, with exponent at most negative one half.'))
p=R/'dist/chapters/concept-animations.json';d=json.loads(p.read_text());d['scenes'].update(scenes);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:len(s['frames']) for k,s in scenes.items()}))

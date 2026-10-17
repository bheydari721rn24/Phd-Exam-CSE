"""Small mechanism-specific models with exact rational numerical certificates."""
from fractions import Fraction as F
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
def frac(x):return str(F(x))
def fit(ts,ys,ws=None):
 ts=list(map(F,ts));ys=list(map(F,ys));ws=list(map(F,ws or[1]*len(ts)))
 s=sum(ws);t=sum(w*x for w,x in zip(ws,ts));t2=sum(w*x*x for w,x in zip(ws,ts));y=sum(w*z for w,z in zip(ws,ys));ty=sum(w*x*z for w,x,z in zip(ws,ts,ys));det=s*t2-t*t
 assert det>0
 return[(t2*y-t*ty)/det,(s*ty-t*y)/det]
def line(ts,ys,ws=None,constant=False):
 ts=list(map(F,ts));ys=list(map(F,ys));ws=list(map(F,ws or[1]*len(ts)))
 mean=sum(w*y for w,y in zip(ws,ys))/sum(ws);c,d=([mean,F(0)]if constant else fit(ts,ys,ws))
 frames=[]
 for a,b,title,why in [(F(0),F(0),'Start with an explicit candidate','Zero is one feasible model; it is not assumed optimal.'),(sum(ys)/len(ys),F(0),'Fit an unweighted constant','This isolates the intercept before applying the stated weights and features.'),(c,d,'Solve the declared model','The final weighted column products vanish. The plotted errors are vertical, not perpendicular distances to the plotted line.')]:
  residual=[y-a-b*t for t,y in zip(ts,ys)];sse=sum(w*r*r for w,r in zip(ws,residual))
  frames.append(dict(kind='fit',t=list(map(float,ts)),y=list(map(float,ys)),w=list(map(float,ws)),c=float(a),d=float(b),exactC=frac(a),exactD=frac(b),sse=frac(sse),residual=list(map(frac,residual)),normal0=frac(sum(w*r for w,r in zip(ws,residual))),normal1=frac(sum(w*t*r for w,t,r in zip(ws,ts,residual))),constant=constant,title=title,why=why))
 return frames
models={
 'line':line([1,2,3],[1,2,2]),
 'weighted-constant':line([0,1,2],[0,2,4],[1,1,2],True),
 'weighted-line':line([0,1,2],[0,1,0],[1,2,1]),
}
models['deficient']=[dict(kind='coefficients',a=[1,2],rhs=4,point=list(map(float,p)),pointExact=list(map(frac,p)),target=None,sse='18',title=title,why='All three observed inputs equal two. Every displayed point gives the identical fitted constant four and squared residual eighteen. Only the final point also minimizes coefficient norm.')for p,title in[([F(4),F(0)],'One coefficient description'),([F(2),F(1)],'Move along the design nullspace'),([F(0),F(2)],'Another identical fit'),([F(4,5),F(8,5)],'Select the minimum-norm member')]]
models['constraint']=[dict(kind='coefficients',a=[1,1],rhs=1,point=p,pointExact=list(map(frac,p)),target=[3,0],sse=frac((3-F(p[0]))**2+F(p[1])**2),title=title,why='Every moving point satisfies the exact sum constraint. The optimum has residual (1,1), perpendicular to the feasible direction (1,−1).')for p,title in[([0,1],'A feasible starting coefficient'),([1,0],'Another feasible coefficient'),([2,-1],'The constrained closest point')]]
models['ridge']=[]
for lam in [F(0),F(1,4),F(1),F(4),F(16)]:
 x=F(3)/(1+lam);r=3-x
 models['ridge'].append(dict(kind='ridge',lam=float(lam),lambdaExact=frac(lam),x=float(x),xExact=frac(x),residualSSE=frac(r*r),coefficientSSE=frac(x*x),penalty=frac(lam*x*x),sse=frac(r*r+lam*x*x),title='Penalty λ = '+frac(lam),why='The plotted curve is the complete objective (3−x)² + λx². Its minimizer balances residual and coefficient costs; it is not an ordinary projection.'))
models['ridge-identity']=[]
for lam in [F(0),F(1,4),F(1),F(4),F(16)]:
 alpha=1/(1+lam);res=25*(1-alpha)**2;penalty=lam*25*alpha**2
 models['ridge-identity'].append(dict(kind='ridge-identity',lam=float(lam),lambdaExact=frac(lam),alpha=float(alpha),alphaExact=frac(alpha),xExact=[frac(3*alpha),frac(4*alpha)],residualSSE=frac(res),penalty=frac(penalty),sse=frac(res+penalty),title='Two-coordinate ridge: λ = '+frac(lam),why='This is Problem24: A is the two-by-two identity and b = (3,4). The curve restricts the complete objective to x = α(3,4); the full normal equations prove this direction contains the unique global minimizer.'))
models['householder']=[dict(kind='vectors',vectors=v,labels=names,title=title,why=why,sse='4/25')for v,names,title,why in[
 ([[3,4],[1,2]],['Design column v','Observed data b'],'Original observation coordinates','The column spans a line. Its coefficient is eleven twenty-fifths; its squared distance to the data is four twenty-fifths.'),
 ([[3,4],[8,4]],['Design column v','Reflector normal u'],'Construct the reflector normal','With α = −5, use u = v + 5e₁ = (8,4). The sign avoids cancellation in the leading coordinate.'),
 ([[-5,0],[-2.2,.4]],['Transformed column Hv','Transformed data Hb'],'Reflect both the design and the data','H is orthogonal. Both vectors must be transformed; their residual length is preserved.'),
 ([[-2.2,0],[-2.2,.4]],['Optimal transformed fit','Transformed data Hb'],'Separate fitted and residual coordinates','The first coordinate is fitted exactly. The vertical remaining coordinate is two-fifths, giving squared error four twenty-fifths.')]]
models['leverage']=[]
for omit,title in[(None,'Full three-point fit'),(1,'Delete the middle observation'),(0,'Delete the left observation')]:
 ts=[F(-1),F(0),F(1)];ys=[F(0),F(1),F(0)];keep=[i for i in range(3)if i!=omit];c,d=fit([ts[i]for i in keep],[ys[i]for i in keep]);res=[y-c-d*t for t,y in zip(ts,ys)]
 models['leverage'].append(dict(kind='fit',t=list(map(float,ts)),y=list(map(float,ys)),w=[1]*3,c=float(c),d=float(d),exactC=frac(c),exactD=frac(d),omit=omit,sse=frac(sum(res[i]**2 for i in keep)),residual=list(map(frac,res)),title=title,why='An outlined point was omitted from fitting but is still predicted. Its vertical error is a deleted-observation error, not its original training residual.'))
models['sensitivity']=[]
for ep in [F(1),F(1,10),F(1,100),F(1,1000)]:
 delta=F(1,100);x2=delta/ep;x1=1-x2
 models['sensitivity'].append(dict(kind='sensitivity',epsilon=frac(ep),x=[float(x1),float(x2)],xExact=[frac(x1),frac(x2)],delta='1/100',sse='1',title='Column separation ε = '+frac(ep),why='Only the second observed response changes by one-hundredth. Fitted change remains (0,1/100,0), while canceling coefficients can grow large as the columns become dependent.'))
models['discrete-noise']=[dict(kind='noise',errors=list(pair),point=[(pair[0]+pair[1])/2,(pair[0]-pair[1])/2],sse='0'if pair[0]==pair[1]else'2',title='Errors '+str(pair),why='Each of four outcomes has probability one-quarter. The coefficient error M and first residual D never are simultaneously zero; their product nevertheless always vanishes.')for pair in[(1,1),(1,-1),(-1,1),(-1,-1)]]
(R/'dist/chapters/l_leastsquares-models.json').write_text(json.dumps(models,indent=2)+'\n',encoding='utf8')
print({'models':len(models),'finiteCheckpoints':sum(map(len,models.values()))})

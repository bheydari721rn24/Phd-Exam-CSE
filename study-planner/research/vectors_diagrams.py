from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parent/'exam-rewrite'));import mathml
def plot(kind):
 xy=lambda v:(100+48*v[0],230-48*v[1])
 def arrow(a,b,color,id,dashed=False):
  x,y=xy(a);X,Y=xy(b);return f'<path d="M{x} {y}L{X} {Y}" fill="none" stroke="{color}" stroke-width="2.3" marker-end="url(#{kind}-{id})"'+(' stroke-dasharray="5 4"' if dashed else '')+'/>'
 def label(v,value,dx=0,dy=0):
  x,y=xy(v);return f'<text x="{x+dx}" y="{y+dy}" font-size="18" font-family="STIX Two Math,serif">{value}</text>'
 colors={'blue':'#277d9f','green':'#268466','orange':'#b77e25'}
 svg=f'<svg viewBox="0 0 760 330" role="img" aria-label="Exact coordinate vector construction: {kind}"><defs>'+''.join(f'<marker id="{kind}-{id}" markerWidth="7" markerHeight="6" refX="7" refY="3" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0L7 3L0 6Z" fill="{c}"/></marker>' for id,c in colors.items())+'</defs><path d="M60 230H370M100 258V45" fill="none" stroke="#a4b8c0" stroke-width="1"/>'
 svg+=label([0,0],'0',-20,22)
 for i in [1,2,3,4]:svg+=label([i,0],str(i),-5,22)
 if kind=='addition':
  svg+=arrow([0,0],[3,1],colors['blue'],'blue')+arrow([3,1],[4,3],colors['green'],'green')+arrow([0,0],[1,2],colors['green'],'green',True)+arrow([0,0],[4,3],colors['orange'],'orange')
  svg+=label([3,1],'u',5,22)+label([1,2],'v',-28,-8)+label([4,3],'u + v',12,-15)
  notes=['Blue: u = (3, 1)','Green: v = (1, 2), translated','Orange: total displacement (4, 3)'];formula=r'(3,1)+(1,2)=(4,3)'
  caption='The solid second vector begins exactly at the first endpoint. Its dashed copy has the same components at the origin. Both coordinate axes have the same unit scale; translation changes no vector.'
 else:
  x,b,p=([3,2],[1,0],[3,0]) if kind=='projection' else ([3,1],[1,2],[1,2]);r=[x[i]-p[i] for i in range(2)]
  svg+=arrow([-.3*b[0],-.3*b[1]],[1.5*b[0] if kind!='projection' else 5,1.5*b[1]],'#b2c3cb','green',True)
  svg+=arrow([0,0],x,colors['blue'],'blue')+arrow([0,0],p,colors['green'],'green')+arrow(p,x,colors['orange'],'orange')
  svg+=label(x,'x',14,-12)+label(p,'p',18,24)
  notes=[f'Blue: target x = {tuple(x)}',f'Green: foot p = {tuple(p)}',f'Orange: residual r = {tuple(r)}'];formula=(r'x=p+r,\quad (0,2)\cdot(1,0)=0' if kind=='projection' else r'p=(1,2),\quad r=(2,-1),\quad r\cdot b=0')
  caption=('Projection onto the horizontal line gives foot (3,0) and perpendicular residual (0,2). The vector sum reconstructs the target (3,2).' if kind=='projection' else 'Separate teaching example: target (3,1), nonunit direction (1,2), coefficient one, foot (1,2), residual (2,-1), and distance sqrt(5). The direction and residual are perpendicular in the equal-scale plot.')
 for i,n in enumerate(notes):svg+=f'<text x="415" y="105+{i*43}" font-size="18" font-family="Source Sans 3,sans-serif">{n}</text>'.replace(f'105+{i*43}',str(105+i*43))
 m=mathml.render(formula);svg+=f'<foreignObject x="40" y="277" width="680" height="45"><div xmlns="http://www.w3.org/1999/xhtml" style="height:100%;display:flex;align-items:center;justify-content:center;font:18px STIX Two Math,serif;overflow:hidden">{m}</div></foreignObject></svg>'
 return '<figure class="logic-diagram'+(' exam-figure' if kind=='nonunit' else '')+'">'+svg+'<figcaption>'+caption+'</figcaption></figure>'

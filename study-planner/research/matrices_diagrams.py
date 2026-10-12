from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parent/'exam-rewrite'));import mathml
def box(formula,x,y,w,h):return f'<foreignObject x="{x}" y="{y}" width="{w}" height="{h}"><div xmlns="http://www.w3.org/1999/xhtml" style="display:flex;align-items:center;justify-content:center;height:100%;font-family:STIX Two Math,serif;font-size:20px;line-height:1.2">'+mathml.render(formula,True)+'</div></foreignObject>'
def figure(kind):
 svg='<svg viewBox="0 0 760 280" role="img" aria-label="Verified matrix '+kind+' construction"><defs><marker id="matrix-static-'+kind+'" markerWidth="7" markerHeight="6" refX="7" refY="3" orient="auto"><path d="M0 0L7 3L0 6Z" fill="#577889"/></marker></defs>'
 if kind=='product':
  for x,label,formula in [(15,'A: 2 rows, 3 columns',r'\begin{pmatrix}1&-1&2\\0&3&1\end{pmatrix}'),(275,'B: 3 rows, 2 columns',r'\begin{pmatrix}2&0\\1&4\\-1&2\end{pmatrix}'),(535,'AB: 2 rows, 2 columns',r'\begin{pmatrix}-1&0\\2&14\end{pmatrix}')]:
   svg+=f'<text x="{x+100}" y="40" text-anchor="middle" font-size="17">{label}</text>'+box(formula,x,65,200,120)
  svg+='<text x="245" y="125" text-anchor="middle" font-size="24">×</text><text x="505" y="125" text-anchor="middle" font-size="24">=</text>'+box(r'(AB)_{12}=1\cdot0+(-1)\cdot4+2\cdot2=0',25,205,710,60)
  caption='Actual rectangular example: each entry sums over the shared three-coordinate index. The zero top-right result comes from cancellation, not zero factors.'
 else:
  for x,label,formula in [(20,'Input coordinates',r'x\in\mathbb R^p'),(295,'After B',r'Bx\in\mathbb R^n'),(570,'After A',r'A(Bx)\in\mathbb R^m')]:
   svg+=f'<rect x="{x}" y="70" width="170" height="105" rx="10" fill="#f3f8fa" stroke="#aac2cb"/><text x="{x+85}" y="45" text-anchor="middle" font-size="17">{label}</text>'+box(formula,x,80,170,85)
  for start,end,label in [(190,295,'B'),(465,570,'A')]:svg+=f'<path d="M{start} 122H{end}" stroke="#577889" fill="none" stroke-width="2" marker-end="url(#matrix-static-{kind})"/><text x="{(start+end)/2}" y="100" text-anchor="middle" font-size="20">{label}</text>'
  svg+=box(r'[AB]x=A(Bx),\quad B:\mathbb R^p\to\mathbb R^n,\quad A:\mathbb R^n\to\mathbb R^m',20,205,720,60)
  caption='Connected endpoints follow the actual map order: B first, A second. The written matrix product is AB; the intermediate coordinate dimension must match.'
 return '<figure class="matrix-figure">'+svg+'</svg><figcaption>'+caption+'</figcaption></figure>'

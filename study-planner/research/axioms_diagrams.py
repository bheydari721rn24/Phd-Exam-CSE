from loop_diagrams import mathbox
def coarsening(render):
 svg='<svg viewBox="0 0 760 310" role="img" aria-label="Four equally likely ordered two-toss outcomes induce three unequal head-count probabilities"><defs><marker id="axioms-coarse-arrow" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#346f86"/></marker></defs><text x="380" y="26" text-anchor="middle" font-size="18">Detailed outcomes are equally likely; reported counts need not be.</text>'
 xs=[110,290,470,650]
 for x,label in zip(xs,['HH','HT','TH','TT']):
  svg+=f'<rect x="{x-55}" y="55" width="110" height="78" rx="6" fill="#e6f1f5" stroke="#346f86"/><text x="{x}" y="80" text-anchor="middle" font-size="20">{label}</text>'+mathbox(render,r'\frac14',x-38,87,76,44)
 for x,z in zip(xs,[125,355,405,635]):svg+=f'<path d="M{x} 133C{x} 160 {z} 162 {z} 192" fill="none" stroke="#346f86" stroke-width="2" marker-end="url(#axioms-coarse-arrow)"/>'
 for x,count,mass in [(125,0,r'1/4'),(380,1,r'1/2'),(635,2,r'1/4')]:
  svg+=f'<rect x="{x-86}" y="192" width="172" height="85" rx="6" fill="#e4f1e9" stroke="#537d68"/><text x="{x}" y="219" text-anchor="middle" font-size="18">{count} '+('head' if count==1 else 'heads')+'</text>'+mathbox(render,mass,x-46,229,92,44)
 return '<figure class="logic-diagram">'+svg+'</svg><figcaption>Arrows connect each detailed outcome to its reported head count. The middle report receives two masses of one quarter; the outer reports receive one each. The reporting map aggregates the existing law and never assigns a new uniform law.</figcaption></figure>'
def atoms(render):
 svg='<svg viewBox="0 0 760 330" role="img" aria-label="A complete weighted two-event law with marginals three fifths and one half"><text x="380" y="26" text-anchor="middle" font-size="18">Four disjoint membership cells form one complete probability law</text>'
 for x,label in [(310,'B absent'),(530,'B present')]:svg+=f'<text x="{x}" y="68" text-anchor="middle" font-size="18">{label}</text>'
 for y,label in [(132,'A absent'),(230,'A present')]:svg+=f'<text x="113" y="{y}" text-anchor="middle" font-size="18">{label}</text>'
 for x,y,mass in [(223,88,r'\frac1{10}'),(443,88,r'\frac3{10}'),(223,186,r'\frac25'),(443,186,r'\frac15')]:
  svg+=f'<rect x="{x}" y="{y}" width="174" height="70" rx="6" fill="#e6f1f5" stroke="#346f86"/>'+mathbox(render,mass,x+30,y+11,114,48)
 svg+=mathbox(render,r'P(\text{exactly one})=\frac25+\frac3{10}=\frac7{10}',150,274,480,50)+'</svg>'
 return '<figure class="logic-diagram exam-figure">'+svg+'<figcaption>'+render(r'This example has $P(A)=3/5$, $P(B)=1/2$ and $P(A\cap B)=1/5$. The cells sum to one. Off-diagonal cells give exactly one; every cell except neither belongs to the union. Rectangle areas do not represent the unequal masses, which are written explicitly. No independence is assumed.')+'</figcaption></figure>'

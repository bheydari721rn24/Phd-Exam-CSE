import html
def mathbox(render,formula,x,y,w=220,h=35):
    m=render('$'+formula+'$').removeprefix('<p>').removesuffix('</p>\n')
    return f'<foreignObject x="{x}" y="{y}" width="{w}" height="{h}"><div xmlns="http://www.w3.org/1999/xhtml" style="font-size:20px;text-align:center;margin:0">{m}</div></foreignObject>'
def triangle(render):
    svg='<svg viewBox="0 0 760 300" role="img" aria-label="Exact strict triangular integer region at n=5, with ten admitted index pairs">'+mathbox(render,r'0\le j<i<5',240,8,280)
    for i in range(5):
        svg+=mathbox(render,str(i),150,62+38*i,40)
        for j in range(5):svg+=f'<rect x="{210+64*j}" y="{58+38*i}" width="54" height="30" rx="4" fill="'+('#b4d6c3' if j<i else '#f3f5f7')+'" stroke="#b8ccd7"/>'
    for j in range(5):svg+=mathbox(render,str(j),216+64*j,250,40)
    svg+='<text x="125" y="152" text-anchor="middle" font-size="18">i</text><text x="560" y="270" font-size="18">j</text>'+mathbox(render,r'B=\binom52=10',560,110,185,65)+'</svg>'
    return '<figure class="logic-diagram">'+svg+'<figcaption>Each green cell is one admitted pair. Gray cells fail the strict inequality, including the entire diagonal. This diagram counts body visits; it does not count header tests.</figcaption></figure>'
def schedules(render):
    svg='<svg viewBox="0 0 760 330" role="img" aria-label="Two exact row-frequency ledgers at numeric bound eight, geometric row work versus logarithmic row visits">'
    svg+='<text x="380" y="28" text-anchor="middle" font-size="18">Geometric outer values; body work equals the current value</text>'
    for i,v in enumerate([1,2,4,8]):
        x=100+140*i;svg+=f'<rect x="{x}" y="{120-7*v}" width="70" height="{7*v}" fill="#8db9cb"/>'+mathbox(render,str(v),x,128,70)
    svg+=mathbox(render,r'1+2+4+8=15',220,165,320)
    svg+='<text x="380" y="214" text-anchor="middle" font-size="18">Consecutive outer values; inner counter doubles up to each value</text>'
    for i,v in enumerate([1,2,2,3,3,3,3,4]):
        x=86+74*i;svg+=f'<rect x="{x}" y="{282-11*v}" width="48" height="{11*v}" fill="#aad0b9"/>'+mathbox(render,str(i+1),x,287,48)
    svg+='</svg>'
    return '<figure class="logic-diagram">'+svg+'<figcaption>At the same numeric bound eight, the first program has four outer visits and fifteen weighted body operations. The second has eight outer rows with lengths one, two, two, three, three, three, three and four, totaling twenty-one constant-cost bodies. Bar heights are exact row frequencies, not machine timings.</figcaption></figure>'

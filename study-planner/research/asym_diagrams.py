import math
def native(render,s,x,y,w,h):
    label=render('$'+s+'$').replace('<p>','<p style="margin:0;text-align:center">')
    return f'<foreignObject x="{x}" y="{y}" width="{w}" height="{h}"><div xmlns="http://www.w3.org/1999/xhtml" style="font-size:20px;line-height:1.3">{label}</div></foreignObject>'
def envelopes(render):
    s='<figure class="logic-diagram"><svg viewBox="0 0 760 360" role="img" aria-label="Exact normalized ratio three plus seven over n; lower envelope three, upper envelope four, and threshold seven"><path d="M70 285H645M70 285V40" fill="none" stroke="#41667d" stroke-width="2"/>'
    def point(n,r):return 70+55*n,285-23*r
    for r,color in [(3,'#268466'),(4,'#bc831c')]:
        x,y=point(0,r);s+=f'<path d="M{x} {y}H645" stroke="{color}" stroke-width="2" stroke-dasharray="6 4"/>'+native(render,str(r),650,y-17,60,34)
    x,_=point(7,0);s+=f'<path d="M{x} 45V285" stroke="#8a99a6" stroke-dasharray="5 5"/>'+native(render,'n_0=7',x-45,294,90,42)
    for n in range(1,11):
        x,y=point(n,3+7/n);s+=f'<circle cx="{x}" cy="{y}" r="5" fill="{"#268466" if n>=7 else "#b4425f"}"/>'
    s+=native(render,r'F(n)/n=3+7/n',190,15,380,45)+native(render,'n',670,266,35,35)
    return s+'</svg><figcaption>This quantitative example uses F(n)=3n+7. The lower envelope 3 holds globally; the upper envelope 4 holds exactly when n is at least 7. Individual integer points, rather than a smoothed curve, show the finite exceptions.</figcaption></figure>'
def hierarchy(render):
    s='<figure class="logic-diagram"><svg viewBox="0 0 760 200" role="img" aria-label="Strict fixed-parameter growth chain from logarithm to factorial"><defs><marker id="asym-chain-port" markerWidth="6" markerHeight="6" refX="6" refY="3" orient="auto"><path d="M0 0L6 3L0 6Z" fill="#41667d"/></marker></defs>'
    expressions=[r'\log n','n',r'n\log n','n^2','2^n','n!']
    for i,e in enumerate(expressions):
        x=15+125*i;s+=f'<rect x="{x}" y="45" width="100" height="65" rx="8" fill="#eef5fa" stroke="#adc3d3"/>'+native(render,e,x+4,63,92,43)
        if i<5:s+=f'<path d="M{x+100} 78H{x+125}" stroke="#41667d" stroke-width="2" marker-end="url(#asym-chain-port)"/>'
    s+=native(render,r'\frac{f_i(n)}{f_{i+1}(n)}\to0',220,135,320,45)
    return s+'</svg><figcaption>Read the six boxes from left to right. Each function is little-oh of its neighbor; the ratio under the row states the meaning of the ordering. This is a strict growth classification, not a prediction of finite hardware timings.</figcaption></figure>'

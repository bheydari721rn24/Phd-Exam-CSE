"""A leaf-depth witness matching the model chapter's actual four depths."""
import math

def representation(render):
    s='<figure class="logic-diagram model-diagram"><svg viewBox="0 0 900 340" role="img" aria-label="An abstract input is encoded into bits, packed or aligned into words, and processed using declared instructions"><defs><marker id="model-review-port" markerWidth="8" markerHeight="8" refX="8" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#426f8a"/></marker></defs>'
    for x,title,subtitle,color in [(25,'Abstract input','array, graph, integer','#edf3fa'),(256,'Encoding','explicit serialization','#f0f5e9'),(487,'Storage','word layout','#fcf2e9'),(718,'Execution','declared instructions','#f3edf9')]:
        s+=f'<rect x="{x}" y="30" width="160" height="82" rx="10" fill="{color}" stroke="#829db2"/><text x="{x+15}" y="64" font-size="19" style="font-family:Source Sans 3,sans-serif">{title}</text><text x="{x+15}" y="91" font-size="15" style="font-family:Source Sans 3,sans-serif">{subtitle}</text>'
    for a,z in [(185,256),(416,487),(647,718)]:s+=f'<path d="M{a} 71H{z}" stroke="#426f8a" stroke-width="2.2" marker-end="url(#model-review-port)"/>'
    rows=[r'For $n$ entries of $b$ bits each and word width $w$:',r'Payload size: $nb$ bits.',r'Separately aligned entries: $n\lceil b/w\rceil$ words.',r'Densely packed payload: $\lceil nb/w\rceil$ words before metadata.',r'One-word entries: $n$ entry reads for a complete scan.']
    for j,line in enumerate(rows):
        label=render(line).replace('<p>','<p style="margin:0">')
        s+=f'<foreignObject x="35" y="{135+37*j}" width="830" height="37"><div xmlns="http://www.w3.org/1999/xhtml" style="font-family:Source Sans 3,sans-serif;font-size:18px;line-height:1.4">{label}</div></foreignObject>'
    return s+'</svg><figcaption>Connected arrows separate input meaning, encoding, storage and operations. Separate entry alignment can use more words than dense packing; neither formula charges allocation, metadata or decoding automatically.</figcaption></figure>'
def depth_witness(render):
    points=[(350,45,'1',False),(120,130,r'\frac12',True),(480,130,r'\frac12',False),(360,220,r'\frac14',True),(620,220,r'\frac14',False),(550,310,r'\frac18',True),(710,310,r'\frac18',True)]
    edges=[(0,1),(0,2),(2,3),(2,4),(4,5),(4,6)]
    s='<figure class="logic-diagram question-specific-diagram"><svg viewBox="0 0 760 360" role="img" aria-label="A full binary tree with leaf depths one, two, three and three and respective masses one half, one quarter, one eighth and one eighth">'
    for a,b in edges:
        x,y,_,_=points[a];u,v,_,_=points[b];d=math.hypot(u-x,v-y);dx,dy=24*(u-x)/d,24*(v-y)/d;s+=f'<path d="M{x+dx} {y+dy}L{u-dx} {v-dy}" fill="none" stroke="#47768a" stroke-width="2"/>'
    for x,y,label,leaf in points:
        value=render('$'+label+'$').removeprefix('<p>').removesuffix('</p>\n');s+=f'<circle cx="{x}" cy="{y}" r="24" fill="{"#f8e9c6"if leaf else"#e3f1f6"}" stroke="#a2bac6"/><foreignObject x="{x-22}" y="{y-21}" width="44" height="42"><div xmlns="http://www.w3.org/1999/xhtml" style="height:100%;display:flex;align-items:center;justify-content:center;font-size:18px">{value}</div></foreignObject>'
    return s+'</svg><figcaption>Gold nodes are the four leaves. Only their masses are added: one half, one quarter and two eighths sum to one. Every blue internal node has two children, although the leaf depths differ.</figcaption></figure>'

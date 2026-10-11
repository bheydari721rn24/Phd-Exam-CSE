"""Exact illustrations for the particular induction questions that need them."""
import math
def leaf_mass(render):
    s='<figure class="logic-diagram question-specific-diagram"><svg viewBox="0 0 760 280" role="img" aria-label="A unary root leaves half the mass unused; a full tree with leaf depths one, two and two has total mass one">'
    def node(x,y,label):
        nonlocal s
        v=render('$'+label+'$').removeprefix('<p>').removesuffix('</p>\n')
        s+=f'<circle cx="{x}" cy="{y}" r="26" fill="#f2f8fa" stroke="#a2bac6"/><foreignObject x="{x-23}" y="{y-22}" width="46" height="44"><div xmlns="http://www.w3.org/1999/xhtml" style="height:100%;display:flex;align-items:center;justify-content:center;font-size:18px">{v}</div></foreignObject>'
    edges=[((160,70),(160,190)),((530,60),(420,160)),((530,60),(640,140)),((640,140),(585,230)),((640,140),(705,230))]
    for (x,y),(u,v)in edges:
        d=math.hypot(u-x,v-y);dx,dy=(u-x)*26/d,(v-y)*26/d
        s+=f'<path d="M{x+dx} {y+dy}L{u-dx} {v-dy}" fill="none" stroke="#47768a" stroke-width="2"/>'
    for x,y,label in [(160,70,'1'),(160,190,r'\frac12'),(530,60,'1'),(420,160,r'\frac12'),(640,140,r'\frac12'),(585,230,r'\frac14'),(705,230,r'\frac14')]:node(x,y,label)
    s+='<text x="160" y="25" text-anchor="middle" font-size="17">One child: half the mass used</text><text x="530" y="25" text-anchor="middle" font-size="17">Full tree: all the mass used</text></svg><figcaption>Circle labels show the mass available at that node. Only leaf masses are added: the left tree has one leaf of weight one half; the right has weights one half, one quarter and one quarter. An internal node’s mass is passed to its children and is not added again.</figcaption></figure>'
    return s
def full_shapes(render):
    nodes=[(190,55,False),(100,130,False),(280,130,False),(55,205,True),(145,205,True),(235,205,True),(325,205,True),(530,55,False),(450,115,True),(610,115,False),(530,175,True),(690,175,False),(650,235,True),(735,235,True)]
    edges=[(0,1),(0,2),(1,3),(1,4),(2,5),(2,6),(7,8),(7,9),(9,10),(9,11),(11,12),(11,13)]
    s='<figure class="logic-diagram question-specific-diagram"><svg viewBox="0 0 760 320" role="img" aria-label="Two full binary trees with three internal nodes and seven total nodes: perfect height two and comb height three">'
    for a,b in edges:
        x,y,_=nodes[a];u,v,_=nodes[b];d=math.hypot(u-x,v-y);dx,dy=(u-x)*14/d,(v-y)*14/d
        s+=f'<path d="M{x+dx} {y+dy}L{u-dx} {v-dy}" fill="none" stroke="#47768a" stroke-width="2"/>'
    for x,y,leaf in nodes:s+=f'<circle cx="{x}" cy="{y}" r="14" fill="'+('#f5e8cb'if leaf else'#e4f1f6')+'" stroke="#a2bac6"/>'
    for x,formula in [(20,r'I=3,\ N=7,\ h=2'),(400,r'I=3,\ N=7,\ h=3')]:
        v=render('$'+formula+'$').removeprefix('<p>').removesuffix('</p>\n')
        s+=f'<foreignObject x="{x}" y="267" width="340" height="40"><div xmlns="http://www.w3.org/1999/xhtml" style="text-align:center;font-size:18px">{v}</div></foreignObject>'
    s+='<text x="190" y="25" text-anchor="middle" font-size="17">Perfect full shape</text><text x="565" y="25" text-anchor="middle" font-size="17">Full comb shape</text></svg><figcaption>Blue circles are internal nodes; gold circles are leaves. Every blue node has two children in both trees. The different leaf depths and heights show why fullness does not fix balance, perfection or shape. Height counts edges on a longest root-leaf path.</figcaption></figure>'
    return s

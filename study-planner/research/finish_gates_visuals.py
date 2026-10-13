from pathlib import Path
import re,sys
B=Path(__file__).parent;R=B.parent;sys.path.insert(0,str(B/'exam-rewrite'));import mathml
def fo(x,y,w,h,formula):return f'<foreignObject x="{x}" y="{y}" width="{w}" height="{h}"><div xmlns="http://www.w3.org/1999/xhtml" style="font:20px &quot;STIX Two Math&quot;;text-align:center;line-height:1.2">'+mathml.render(formula,False)+'</div></foreignObject>'
def fig(id,desc,body,caption,height=300):return f'<figure class="gates-diagram deep-gates-figure"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 {height}" role="img" aria-labelledby="{id}"><title id="{id}">{desc}</title><g fill="none" stroke="#438297" stroke-width="1.7">'+body+'</g></svg><figcaption>'+caption+'</figcaption></figure>'
def nand(x,y,label):return f'<path d="M{x} {y}h25a25 25 0 0 1 0 50h-25Z" stroke="#28495b" fill="white"/><circle cx="{x+55}" cy="{y+25}" r="5" fill="white" stroke="#28495b"/>'+fo(x+5,y+10,40,34,label)
def label(x,y,v):return f'<text x="{x}" y="{y}" text-anchor="middle" fill="#28495b" stroke="none" font-family="Source Sans 3" font-size="17">{v}</text>'
p=R/'dist/chapters/g_gates.html';s=p.read_text()
# Replace mathematical formula labels in the six-symbol panel with native math.
a=s.index('data-schematic="gate-symbols"');a=s.rfind('<figure',0,a);z=s.index('</figure>',a)+9;v=s[a:z]
formulas=[r'xy',r'x+y',r'\neg(x+y)',r'\neg(xy)',r'x\oplus y',r'\neg(x\oplus y)'];matches=list(re.finditer(r'<text\b[^>]*y="(?:151|326)"[\s\S]*?</text>',v));assert len(matches)==6
for m,f in reversed(list(zip(matches,formulas))):
 x=float(re.search(r'x="([^"]+)"',m[0])[1]);y=float(re.search(r'y="([^"]+)"',m[0])[1]);v=v[:m.start()]+fo(x-90,y-25,180,48,f)+v[m.end():]
s=s[:a]+v+s[z:]
selector=nand(145,65,r'\neg s')+nand(350,120,'p')+nand(350,218,'q')+nand(560,164,'F')
selector+='<path d="M60 77H145M110 77V102H145M110 77V230H350M60 157H320V132H350M60 255H350M205 90H290V157H350M410 145H500V176H560M410 243H520V201H560M620 189H705"/><circle cx="110" cy="77" r="3" fill="#438297"/>'+fo(25,34,70,35,'s')+fo(20,115,85,35,'d_0')+fo(20,272,85,35,'d_1')+fo(640,208,85,35,'F')
selectorfig=fig('deep-gates-selector','Four NANDs implement a selector with a tied-input select inverter',selector,'The connected netlist computes F=(not s)d₀+s d₁. The marked junction fans out s; d₀ and d₁ are separate primary data wires. The two pins of the first NAND share the same s net. No propagation timing is asserted.',330)
a=s.index('data-schematic="nand-mux"');a=s.rfind('<figure',0,a);z=s.index('</figure>',a)+9;s=s[:a]+selectorfig+s[z:]
# Topology drawings accompany solved transfer problems where a net or RC path is essential.
three=nand(140,112,'t')+nand(350,112,'u')+nand(560,112,'F')+'<path d="M50 124H140M50 148H140M200 137H300V124H350M300 137V148H350M410 137H495V124H560M460 220H530V148H560M620 137H710"/><circle cx="300" cy="137" r="3" fill="#438297"/>'+fo(20,76,90,35,'x')+fo(20,166,90,35,'y')+fo(420,220,90,35,'z')+fo(270,70,120,40,r't=\neg(xy)')+fo(440,70,110,40,'u=xy')
f1=fig('deep-three-nand','The proved three-cell NAND construction',three,'Challenge 1: the middle tied-input NAND restores xy before the final NAND combines it with z. The diagram is the exact construction used in the lower-bound proof.')
rc='<path d="M40 95H115M185 95H340M410 95H690M260 95V157M560 95V157M260 173V240M560 173V240M248 240H272M548 240H572"/><rect x="115" y="84" width="70" height="22" fill="white"/><rect x="340" y="84" width="70" height="22" fill="white"/><path d="M240 157H280M240 173H280M540 157H580M540 173H580"/><circle cx="260" cy="95" r="3" fill="#438297"/><circle cx="560" cy="95" r="3" fill="#438297"/>'+fo(95,36,115,36,r'R_1=2\,\mathrm{k}\Omega')+fo(325,36,130,36,r'R_2=1\,\mathrm{k}\Omega')+fo(175,265,170,36,r'C_1=5\,\mathrm{fF}')+fo(420,265,260,36,r'C_2=4+6=10\,\mathrm{fF}')+label(685,76,'output')
f2=fig('deep-elmore-chain','The exact two-resistor two-node Elmore chain',rc,'Challenge 2: C₁ shares R₁ with the output path; C₂ shares R₁+R₂. Its output capacitor combines a 4 fF internal component and a 6 fF fixed load. The capacitor lower terminals reference ground.',330)
dag='<rect x="180" y="65" width="170" height="55" fill="#edf5f8"/><rect x="180" y="210" width="170" height="55" fill="#edf5f8"/><rect x="510" y="145" width="170" height="55" fill="#edf5f8"/><path d="M60 78H180M60 103H180M90 78V238H180M350 92H440V158H510M350 238H460V188H510M680 173H725"/><circle cx="90" cy="78" r="3" fill="#438297"/>'+label(265,100,'NAND u: [1,4] ns')+label(265,245,'NOT v: [2,6] ns')+label(595,177,'NOR F: [0.5,2] ns')+fo(20,30,140,38,r'x:[0,3]')+fo(15,125,140,38,r'y:[2,5]')
f4=fig('deep-early-late-dag','Shared x input and separate early and late timing bounds',dag,'Challenge 4: brackets on gate blocks are contamination/propagation delay bounds; brackets on sources are early/late arrivals. The x fanout is marked. The shared input creates reconvergence; the structural bounds need not be attained by a real sensitized transition.',310)
for n,fragment in [(1,f1),(2,f2),(4,f4)]:
 needle=f'<h3>Challenge {n}.';a=s.index(needle);z=s.index('</h3>',a)+5;s=s[:z]+fragment+s[z:]
s=s.replace('font-family="SourceSans3"','font-family="Source Sans 3"').replace('font-family="STIXTwoMath"','font-family="STIX Two Math"')
p.write_text(s,encoding='utf-8');print({'newTransferDiagrams':3,'rebuiltSelector':1,'nativePrimitiveFormulaLabels':6})

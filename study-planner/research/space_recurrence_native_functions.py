"""Separate named operators from arguments without changing mathematical grouping."""
from pathlib import Path
import re,xml.etree.ElementTree as ET
B=Path(__file__).parent;R=B.parent;NS='http://www.w3.org/1998/Math/MathML';ET.register_namespace('',NS)
names={'log','ln','sin','cos','exp','min','max','gcd','lcm','lim','det','rank','tr','ker','dim'}
def fix(m):
 root=ET.fromstring(m[0]);edits=0
 for parent in list(root.iter()):
  kids=list(parent)
  for i,child in enumerate(kids):
   name=child.tag.split('}')[-1];base=list(child)[0]if name in['msub','msup','msubsup','munder','mover','munderover']and list(child)else child
   if base.tag.split('}')[-1]=='mi'and base.get('mathvariant')=='normal'and base.text in names:
    siblings=list(parent);at=siblings.index(child)
    if at+1<len(siblings)and siblings[at+1].tag.split('}')[-1]=='mspace':continue
    if parent.tag.split('}')[-1]in ['msub','msup','msubsup','munder','mover','munderover']:continue
    parent.insert(at+1,ET.Element('{'+NS+'}mspace',{'width':'.14em'}));edits+=1
 return ET.tostring(root,encoding='unicode')if edits else m[0]
p=R/'dist/chapters/a_recurrence.html';s=p.read_text();s=re.sub(r'<math\b[\s\S]*?</math>',fix,s);p.write_text(s,encoding='utf8')
p=R/'dist/chapters/a_asym.html';s=p.read_text();a=s.index('data-source-id="MS_CE_1405_Q58"');a=s.rfind('<section',0,a);z=s.index('</details>',a);s=s[:a]+re.sub(r'<math\b[\s\S]*?</math>',fix,s[a:z])+s[z:];p.write_text(s,encoding='utf8')

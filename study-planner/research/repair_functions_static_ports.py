"""Attach the five retained static diagrams' arrows to their actual nodes."""
from pathlib import Path
import re,math,json,xml.etree.ElementTree as ET
B=Path(__file__).parent;R=B.parent;ET.register_namespace('','http://www.w3.org/2000/svg')
def local(t):return t.split('}')[-1]
def number(n,a):return float(n.attrib[a])
def center(n):
 return (number(n,'cx'),number(n,'cy'))if local(n.tag)=='circle'else(number(n,'x')+number(n,'width')/2,number(n,'y')+number(n,'height')/2)
def distance(n,p):
 x,y=center(n)
 if local(n.tag)=='circle':return abs(math.hypot(p[0]-x,p[1]-y)-number(n,'r'))
 w=number(n,'width')/2;h=number(n,'height')/2
 return math.hypot(max(abs(p[0]-x)-w,0),max(abs(p[1]-y)-h,0))if abs(p[0]-x)>w or abs(p[1]-y)>h else min(w-abs(p[0]-x),h-abs(p[1]-y))
def boundary(n,target):
 x,y=center(n);dx,dy=target[0]-x,target[1]-y
 if local(n.tag)=='circle':k=number(n,'r')/math.hypot(dx,dy)
 else:k=1/max(abs(dx)/(number(n,'width')/2),abs(dy)/(number(n,'height')/2))
 return [x+k*dx,y+k*dy]
records=[]
def repair(match):
 raw=match[0];a=raw.index('<svg');z=raw.index('</svg>',a)+6;svg=ET.fromstring(raw[a:z]);shapes=[n for n in svg.iter()if local(n.tag)in['circle','rect']]
 for marker in[n for n in svg.iter()if local(n.tag)=='marker']:
  attributes=dict(marker.attrib);marker.clear();marker.attrib.update(attributes);marker.attrib.update(viewBox='0 0 7 6',markerWidth='7',markerHeight='6',refX='7',refY='3',orient='auto',markerUnits='userSpaceOnUse');marker.append(ET.Element('path',{'d':'M0 0L7 3L0 6Z','fill':'#547e95'}))
 attached=[]
 for line in[n for n in svg.iter()if local(n.tag)=='line'and'marker-end'in n.attrib]:
  oldA=(number(line,'x1'),number(line,'y1'));oldB=(number(line,'x2'),number(line,'y2'));source=min(shapes,key=lambda n:distance(n,oldA));target=min(shapes,key=lambda n:distance(n,oldB));assert source is not target
  assert distance(source,oldA)<20 and distance(target,oldB)<20
  A=boundary(source,center(target));C=boundary(target,center(source));line.attrib.update(x1=str(A[0]),y1=str(A[1]),x2=str(C[0]),y2=str(C[1]),**{'stroke-width':'1.5','stroke-linecap':'round','data-static-ports':'attached'})
  attached.append(dict(sourceCenter=center(source),targetCenter=center(target),sourcePort=A,targetPort=C,sourceShape=local(source.tag),targetShape=local(target.tag)))
 for t in[n for n in svg.iter()if local(n.tag)=='text']:
  label=''.join(t.itertext());family='"Source Sans 3"'if re.search(r'[A-Za-z]{4}',label)else'"STIX Two Math"';t.attrib['style']='font-family:'+family+' !important'
  if svg.attrib.get('aria-label')=='A two-image idempotent function on four labeled points':
   if label.startswith('A two-image'):t.attrib.update(y='22',**{'font-size':'20'})
   elif label in['Inputs','Outputs in the same set']:t.attrib.update(y='55',**{'font-size':'18'})
   elif label=='Fixed image point':t.attrib.update(x='500',**{'text-anchor':'start','font-size':'17'})
   elif label.startswith('Every image point'):t.attrib['font-size']='18'
  if re.search(r'[A-Za-z]{4}',label)and t.text and re.search(r'\bf\b',t.text):
   parts=re.split(r'\b(f)\b',t.text);t.text=parts[0]
   for i in range(1,len(parts),2):span=ET.SubElement(t,'tspan',{'style':'font-family:"STIX Two Math" !important'});span.text=parts[i];span.tail=parts[i+1]
 records.append(dict(title=svg.attrib.get('aria-label'),attachedArrows=len(attached),ports=attached))
 return raw[:a]+ET.tostring(svg,encoding='unicode')+raw[z:]
p=R/'dist/chapters/d_functions.html';s=re.sub(r'<figure\b[\s\S]*?</figure>',repair,p.read_text(encoding='utf-8'));p.write_text(s,encoding='utf-8');assert len(records)==5
(B/'deep-library-revision/d_functions-static-ports.json').write_text(json.dumps(dict(status='geometry_rebuilt_pending_browser_check',diagrams=records),indent=2)+'\n',encoding='utf-8');print({'diagrams':len(records),'attachedArrows':sum(v['attachedArrows']for v in records)})

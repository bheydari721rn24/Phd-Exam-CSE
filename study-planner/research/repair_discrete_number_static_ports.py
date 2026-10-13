"""Preserve parallel edge lanes and snap only actual near-node endpoints."""
from pathlib import Path
import math,re,json,xml.etree.ElementTree as ET
B=Path(__file__).parent;R=B.parent;ET.register_namespace('','http://www.w3.org/2000/svg');records=[]
def tag(e):return e.tag.split('}')[-1]
def num(e,k):return float(e.attrib[k])
def snap(e,p):
 if tag(e)=='circle':
  x,y,r=num(e,'cx'),num(e,'cy'),num(e,'r');d=math.hypot(p[0]-x,p[1]-y);return[x+r,y]if d==0 else[x+r*(p[0]-x)/d,y+r*(p[1]-y)/d]
 x,y,w,h=[num(e,k)for k in['x','y','width','height']]
 candidates=[[x,min(max(p[1],y),y+h)],[x+w,min(max(p[1],y),y+h)],[min(max(p[0],x),x+w),y],[min(max(p[0],x),x+w),y+h]]
 return min(candidates,key=lambda q:math.dist(p,q))
def repair(match):
 raw=match[0];a=raw.index('<svg');z=raw.index('</svg>',a)+6;svg=ET.fromstring(raw[a:z]);shapes=[v for v in svg.iter()if tag(v)in['circle','rect']];ports=[]
 if 'nonunit power sequence' in svg.attrib.get('aria-label',''):
  # The transient is 1 -> 2 -> 4; the eventual period is the directed 4 <-> 8 cycle.
  ns='{http://www.w3.org/2000/svg}';defs=ET.Element(ns+'defs');marker=ET.SubElement(defs,ns+'marker',{'id':'number-transient-port','markerWidth':'7','markerHeight':'6','refX':'7','refY':'3','orient':'auto','markerUnits':'userSpaceOnUse'});ET.SubElement(marker,ns+'path',{'d':'M0 0L7 3L0 6Z','fill':'#547e95'});svg.insert(0,defs)
  for line in[v for v in svg.iter()if tag(v)=='line']:line.attrib['marker-end']='url(#number-transient-port)'
  curves=[v for v in svg.iter()if tag(v)=='path'and 'stroke'in v.attrib]
  delta=24/math.sqrt(2)
  for curve,points,cy in [(curves[0],[(425+delta,110-delta),(625-delta,110-delta)],45),(curves[1],[(625-delta,110+delta),(425+delta,110+delta)],165)]:
   P,Q=points;curve.attrib.update(d=f'M{P[0]} {P[1]} Q525 {cy} {Q[0]} {Q[1]}',**{'stroke-width':'1.5','marker-end':'url(#number-transient-port)','data-static-path-ports':','.join(map(str,P+Q))});ports.append(dict(sourcePort=P,targetPort=Q,kind='curve'))
 for marker in[v for v in svg.iter()if tag(v)=='marker']:
  attributes=dict(marker.attrib);marker.clear();marker.attrib.update(attributes);marker.attrib.update(viewBox='0 0 7 6',markerWidth='7',markerHeight='6',refX='7',refY='3',orient='auto',markerUnits='userSpaceOnUse');marker.append(ET.Element('path',{'d':'M0 0L7 3L0 6Z','fill':'#547e95'}))
 for line in[v for v in svg.iter()if tag(v)=='line']:
  if not shapes:continue
  P=[num(line,'x1'),num(line,'y1')];Q=[num(line,'x2'),num(line,'y2')]
  A=min(shapes,key=lambda v:math.dist(P,snap(v,P)));C=min(shapes,key=lambda v:math.dist(Q,snap(v,Q)))
  if A is C or max(math.dist(P,snap(A,P)),math.dist(Q,snap(C,Q)))>30:continue
  if 'divisibility lattice' in svg.attrib.get('aria-label','') and tag(A)==tag(C)=='circle':
   centerA=[num(A,'cx'),num(A,'cy')];centerC=[num(C,'cx'),num(C,'cy')];X=snap(A,centerC);Y=snap(C,centerA)
  else:X=snap(A,P);Y=snap(C,Q)
  line.attrib.update(x1=str(X[0]),y1=str(X[1]),x2=str(Y[0]),y2=str(Y[1]),**{'stroke-width':'1.5','stroke-linecap':'round','data-static-ports':'attached'})
  ports.append(dict(sourcePort=X,targetPort=Y))
 for text in[v for v in svg.iter()if tag(v)=='text']:
  label=''.join(text.itertext());text.attrib['style']='font-family:'+('"Source Sans 3"'if re.search('[A-Za-z]{4}',label)else'"STIX Two Math"')+' !important'
  if 'nonunit power sequence' in svg.attrib.get('aria-label','') and label.strip()in['→','←']:
   parent=next(p for p in svg.iter()if text in list(p));parent.remove(text)
  if re.fullmatch(r'(even|odd) k\s*[≥>]\s*\d+',label):
   attributes=dict(text.attrib);text.clear();text.attrib.update(attributes);word,mathpart=label.split(' ',1);text.text=word+' ';child=ET.SubElement(text,'{http://www.w3.org/2000/svg}tspan',{'style':'font-family:"STIX Two Math" !important'});child.text=mathpart
 records.append(dict(title=svg.attrib.get('aria-label'),ports=ports))
 result=raw[:a]+ET.tostring(svg,encoding='unicode')+raw[z:]
 return re.sub(r'(<figcaption>Figure )\d+',lambda m:m[1]+str(len(records)),result,count=1)
p=R/'dist/chapters/d_number.html';s=re.sub(r'<figure\b[\s\S]*?</figure>',repair,p.read_text(encoding='utf-8'));p.write_text(s,encoding='utf-8');assert len(records)>=4
(B/'deep-library-revision/d_number-static-ports.json').write_text(json.dumps(dict(status='rebuilt_pending_browser',diagrams=records),indent=2)+'\n',encoding='utf-8');print({'diagrams':len(records),'attachedArrows':sum(len(v['ports'])for v in records)})

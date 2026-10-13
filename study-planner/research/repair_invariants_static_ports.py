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
 if 'Primary coordinate first' in raw:
  boxes=[(35,75,'(2,0)'),(210,75,'(1,5)'),(385,75,'(1,4)'),(560,75,'(1,0)'),(210,213,'(0,M)'),(385,213,'(0,M−1)'),(560,213,'(0,0)')]
  prefix='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 330" role="img" aria-label="Lexicographic progress with attached reset and decrement arrows"><title>Lexicographic progress with attached reset and decrement arrows</title><defs><marker id="invariants-lex-port" markerWidth="7" markerHeight="6" refX="7" refY="3" orient="auto" markerUnits="userSpaceOnUse"><path d="M0 0L7 3L0 6Z" fill="#547e95"/></marker></defs><text x="350" y="25" text-anchor="middle" font-size="20">Primary coordinate first: rank = (y,x)</text>'
  nodes=''.join('<rect x="'+str(x)+'" y="'+str(y)+'" width="105" height="44" rx="10" fill="#edf5f9" stroke="#87adbf"/><text x="'+str(x+52.5)+'" y="'+str(y+28)+'" text-anchor="middle" font-size="19">'+value+'</text>'for x,y,value in boxes)
  arrows=''
  for src,dst,compressed,label in[(0,1,False,'reset'),(1,2,False,'one step'),(2,3,True,'repeat'),(4,5,False,'one step'),(5,6,True,'repeat')]:
   x,y,_=boxes[src];X,Y,_=boxes[dst];arrows+='<line x1="'+str(x+105)+'" y1="'+str(y+22)+'" x2="'+str(X)+'" y2="'+str(Y+22)+'" stroke="#547e95" stroke-width="1.5" marker-end="url(#invariants-lex-port)"'+(' stroke-dasharray="4 3"'if compressed else'')+' data-static-ports="attached"/><text x="'+str((x+105+X)/2)+'" y="'+str(y-8)+'" text-anchor="middle" font-size="14">'+label+'</text>'
  arrows+='<path d="M612.5 119 C612.5 175 262.5 157 262.5 213" fill="none" stroke="#547e95" stroke-width="1.5" marker-end="url(#invariants-lex-port)" data-attached-reset="true"/>'
  footer='<text x="350" y="285" text-anchor="middle" font-size="18">A reset lowers y; horizontal steps lower x.</text><text x="350" y="315" text-anchor="middle" font-size="17">Shown branch: M ≥ 1. A reset to M = 0 ends immediately.</text></svg>'
  svg=ET.fromstring(prefix+nodes+arrows+footer);shapes=[v for v in svg.iter()if tag(v)in['circle','rect']]
 for marker in[v for v in svg.iter()if tag(v)=='marker']:
  attributes=dict(marker.attrib);marker.clear();marker.attrib.update(attributes);marker.attrib.update(viewBox='0 0 7 6',markerWidth='7',markerHeight='6',refX='7',refY='3',orient='auto',markerUnits='userSpaceOnUse');marker.append(ET.Element('path',{'d':'M0 0L7 3L0 6Z','fill':'#547e95'}))
 for line in[v for v in svg.iter()if tag(v)=='line'and'marker-end'in v.attrib]:
  if not shapes:continue
  P=[num(line,'x1'),num(line,'y1')];Q=[num(line,'x2'),num(line,'y2')]
  A=min(shapes,key=lambda v:math.dist(P,snap(v,P)));C=min(shapes,key=lambda v:math.dist(Q,snap(v,Q)))
  if A is C or max(math.dist(P,snap(A,P)),math.dist(Q,snap(C,Q)))>20:continue
  X=snap(A,P);Y=snap(C,Q);line.attrib.update(x1=str(X[0]),y1=str(X[1]),x2=str(Y[0]),y2=str(Y[1]),**{'stroke-width':'1.5','stroke-linecap':'round','data-static-ports':'attached'})
  ports.append(dict(sourcePort=X,targetPort=Y))
 for text in[v for v in svg.iter()if tag(v)=='text']:
  label=''.join(text.itertext());text.attrib['style']='font-family:'+('"Source Sans 3"'if re.search('[A-Za-z]{4}',label)else'"STIX Two Math"')+' !important'
 records.append(dict(title=svg.attrib.get('aria-label'),ports=ports))
 result=raw[:a]+ET.tostring(svg,encoding='unicode')+raw[z:]
 return re.sub(r'(<figcaption>Figure )\d+',lambda m:m[1]+str(len(records)),result,count=1)
p=R/'dist/chapters/d_invariants.html';s=re.sub(r'<figure\b[\s\S]*?</figure>',repair,p.read_text(encoding='utf-8'));p.write_text(s,encoding='utf-8');assert len(records)==4
(B/'deep-library-revision/d_invariants-static-ports.json').write_text(json.dumps(dict(status='rebuilt_pending_browser',diagrams=records),indent=2)+'\n',encoding='utf-8');print({'diagrams':4,'attachedArrows':sum(len(v['ports'])for v in records)})

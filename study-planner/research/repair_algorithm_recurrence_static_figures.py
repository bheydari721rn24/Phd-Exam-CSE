from pathlib import Path
import re,math,json,sys,xml.etree.ElementTree as ET
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';sys.path.insert(0,str(B/'exam-rewrite'));import mathml;mathml.wrap_display=lambda s:s
p=R/'dist/chapters/a_recurrence.html';s=p.read_text();figures=re.findall(r'<figure\b[\s\S]*?</figure>',s);assert len(figures)==5;repairs=[]
for i,v in enumerate(figures,1):
 old=v
 if i==3:
  text=re.search(r'<svg\b[\s\S]*?</svg>',v)[0];root=ET.fromstring(text);circles=root.findall('circle');ports=[]
  defs=ET.Element('defs');marker=ET.SubElement(defs,'marker',dict(id='recurrence-static-tip',markerWidth='7',markerHeight='6',refX='7',refY='3',orient='auto',markerUnits='userSpaceOnUse'));ET.SubElement(marker,'path',dict(d='M0 0L7 3L0 6Z',fill='#547e95'));root.insert(1,defs)
  for line in root.findall('line'):
   x1,y1,x2,y2=[float(line.get(k))for k in ['x1','y1','x2','y2']]
   nearest=lambda x,y:min(circles,key=lambda c:math.hypot(x-float(c.get('cx')),y-float(c.get('cy'))))
   A=nearest(x1,y1);D=nearest(x2,y2);ax,ay,bx,by=[float(t.get(k))for t,k in[(A,'cx'),(A,'cy'),(D,'cx'),(D,'cy')]];dx,dy=bx-ax,by-ay;L=math.hypot(dx,dy);ra=float(A.get('r'));rb=float(D.get('r'));P=[ax+ra*dx/L,ay+ra*dy/L,bx-rb*dx/L,by-rb*dy/L]
   for k,z in zip(['x1','y1','x2','y2'],P):line.set(k,str(z))
   line.set('marker-end','url(#recurrence-static-tip)');line.set('data-recurrence-static-ports',','.join(map(str,P)));ports.append(P)
  v=v.replace(text,ET.tostring(root,encoding='unicode'));repairs.append(dict(figure=3,directedAttachedEdges=len(ports)))
 if i==5:
  title='Critical logarithmic toll at input eight';chunks=['<svg viewBox="0 0 700 365" role="img" aria-label="'+title+'"><title>'+title+'</title><text x="350" y="32" text-anchor="middle" font-size="22" font-family="Source Sans 3" fill="#16384d">'+title+'</text>']
  for y,label,formula in[(78,'Depth zero',r'1\cdot8\cdot3=24'),(133,'Depth one',r'2\cdot4\cdot2=16'),(188,'Depth two',r'4\cdot2\cdot1=8'),(243,'Terminal leaves',r'8\cdot1=8')]:
   chunks.append('<rect x="44" y="'+str(y-15)+'" width="612" height="46" rx="7" fill="#e8f0f5" stroke="#91abba"/><text x="139" y="'+str(y+14)+'" text-anchor="middle" font-size="17" font-family="Source Sans 3" fill="#16384d">'+label+'</text><foreignObject x="256" y="'+str(y-9)+'" width="374" height="38"><div xmlns="http://www.w3.org/1999/xhtml" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px">'+mathml.render(formula,True)+'</div></foreignObject>')
  chunks.append('<foreignObject x="44" y="306" width="612" height="45"><div xmlns="http://www.w3.org/1999/xhtml" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:22px">'+mathml.render(r'T(8)=24+16+8+8=56',True)+'</div></foreignObject></svg>');svg=re.search(r'<svg\b[\s\S]*?</svg>',v)[0];v=v.replace(svg,''.join(chunks))
  a=v.index('<figcaption>');z=v.index('</figcaption>',a);v=v[:a]+'<figcaption>The stated recurrence has local toll '+mathml.render(r'n\log_2n',False)+' and unit singleton cost. The three internal levels cost twenty-four, sixteen and eight, and the eight terminal leaves cost another eight. Their exact total is fifty-six. The decreasing logarithmic factor appears in each per-node toll; the complete lesson proves the general '+mathml.render(r'\Theta(n\log^2n)',False)+' order.'+v[z:]
 # Prose uses Source Sans; literal arithmetic fragments use the separate mathematical font.
 def typography(m):
  opening,body=m[1],m[2]
  body=re.sub(r'</?tspan\b[^>]*>','',body)
  opening=re.sub(r'\s(?:font-family|style)="[^"]*"','',opening)+" style=\"font-family:'Source Sans 3'!important\""
  if not re.search('[A-Za-z]',body):return opening.replace('Source Sans 3','STIX Two Math')+'>'+body+'</text>'
  body=re.sub(r'(?<![A-Za-z])(?:[qkhj]\b|[0-9]+(?:\.[0-9]+)?(?:\s*[×=−:/]\s*[0-9]+(?:\.[0-9]+)?)*|[×=−])',lambda q:'<tspan style="font-family:STIX Two Math!important">'+q[0]+'</tspan>',body)
  return opening+'>'+body+'</text>'
 v=re.sub(r'(<text\b[^>]*?)>([\s\S]*?)</text>',typography,v);v=v.replace(' font-family="Source Sans 3" font-family="STIX Two Math"',' font-family="STIX Two Math"')
 s=s.replace(old,v,1)
p.write_text(s,encoding='utf8');(E/'a_recurrence-static-ports.json').write_text(json.dumps(dict(status='rewritten_pending_rendered_checks',figures=5,repairs=repairs,directedAttachedConnections=8,proseFont='Source Sans 3',mathematicalFont='STIX Two Math',criticalFigureFormula=r'T(n)=2T(n/2)+n\log_2n',criticalFigureExactTotal=56),indent=2)+'\n',encoding='utf8')

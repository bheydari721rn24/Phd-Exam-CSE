from pathlib import Path
import re,json,math,html,sys
from xml.etree import ElementTree as ET
B=Path(__file__).parent;R=B.parent;E=B/'deep-library-revision';sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;p=R/'dist/chapters/a_divide.html';page=p.read_text();figs=re.findall(r'<figure\b[\s\S]*?</figure>',page);assert len(figs)==6;ports=[]
def native(formula,x,y,w,h,size=22):return '<foreignObject x="'+str(x)+'" y="'+str(y)+'" width="'+str(w)+'" height="'+str(h)+'"><div xmlns="http://www.w3.org/1999/xhtml" style="display:flex;align-items:center;justify-content:center;height:100%;font-size:'+str(size)+'px">'+mathml.render(formula,True)+'</div></foreignObject>'
for index,fig in enumerate(figs,1):
 old=fig;svg=re.search(r'<svg\b[\s\S]*?</svg>',fig)[0];root=ET.fromstring(svg);local=lambda e:e.tag.split('}')[-1];ns='{http://www.w3.org/2000/svg}'if root.tag.startswith('{')else'';rects=[e for e in root.iter()if local(e)=='rect']
 # Every existing directed dependency joins actual rectangle ports. The divider is not a dependency.
 if index in [2,4,5,6]:
  markerId='divide-static-tip-'+str(index);defs=ET.Element(ns+'defs');mark=ET.SubElement(defs,ns+'marker',dict(id=markerId,markerWidth='7',markerHeight='6',refX='7',refY='3',orient='auto',markerUnits='userSpaceOnUse'));ET.SubElement(mark,ns+'path',dict(d='M0 0L7 3L0 6Z',fill='#547e95'));root.insert(1,defs)
  def center(r):return(float(r.get('x'))+float(r.get('width'))/2,float(r.get('y'))+float(r.get('height'))/2)
  def distance(r,x,y):
   rx,ry,w,h=map(float,[r.get(k)for k in ['x','y','width','height']]);return max(rx-x,0,x-rx-w)**2+max(ry-y,0,y-ry-h)**2
  for line in [e for e in root.iter()if local(e)=='line']:
   x,y,u,v=map(float,[line.get(k)for k in ['x1','y1','x2','y2']]);A=min(rects,key=lambda r:distance(r,x,y));D=min(rects,key=lambda r:distance(r,u,v));ax,ay=center(A);bx,by=center(D);dx,dy=bx-ax,by-ay;assert A is not D
   a=min(float(A.get('width'))/2/abs(dx or 1e-30),float(A.get('height'))/2/abs(dy or 1e-30));b=min(float(D.get('width'))/2/abs(dx or 1e-30),float(D.get('height'))/2/abs(dy or 1e-30));P=[ax+a*dx,ay+a*dy,bx-b*dx,by-b*dy]
   for k,val in zip(['x1','y1','x2','y2'],P):line.set(k,str(val))
   line.set('stroke-width','1.5');line.set('marker-end','url(#'+markerId+')');line.set('data-divide-static-ports',','.join(map(str,P)));ports.append(dict(figure=index,ports=P))
 svg2=ET.tostring(root,encoding='unicode');svg2=svg2.replace('ns0:','').replace(':ns0','');fig=fig.replace(svg,svg2)
 # Native equations replace fragmented superscript/subscript text, retaining every mathematical claim.
 if index==4:
  texts=list(re.finditer(r'<text\b[^>]*>[\s\S]*?</text>',fig))
  replacements={1:native(r'z_2=x_Hy_H',20,76,200,68),2:native(r'z_0=x_Ly_L',250,76,200,68),3:native(r'z_d=(x_H-x_L)(y_H-y_L)',480,76,200,68,15),4:'',5:native(r'z_1=z_2+z_0-z_d',155,211,390,63),6:native(r'xy=z_2\,2^{2m}+z_1\,2^m+z_0',40,301,620,47)}
  for i in reversed(list(replacements)):m=texts[i];fig=fig[:m.start()]+replacements[i]+fig[m.end():]
 if index==5:
  texts=list(re.finditer(r'<text\b[^>]*>[\s\S]*?</text>',fig));replacements={1:native(r'E_j',30,91,160,58),2:native(r'O_j',30,236,160,58),3:native(r'\times\omega^j',275,236,140,58),4:native(r'E_j+\omega^jO_j',490,91,175,58,20),5:native(r'E_j-\omega^jO_j',490,236,175,58,20)}
  for i in reversed(list(replacements)):m=texts[i];fig=fig[:m.start()]+replacements[i]+fig[m.end():]
 def typography(m):
  opening,body=m[1],m[2];opening=re.sub(r'\s(?:font-family|style)="[^"]*"','',opening)+" style=\"font-family:'Source Sans 3'!important\"";body=re.sub(r'(?<![A-Za-z])(?:\d+(?:\.\d+)?|[δω]|[×=−+]|[mjN]\b)',lambda n:"<tspan style=\"font-family:'STIX Two Math'!important\">"+n[0]+'</tspan>',body);return opening+'>'+body+'</text>'
 fig=re.sub(r'(<text\b[^>]*?)>([\s\S]*?)</text>',typography,fig);page=page.replace(old,fig,1)
p.write_text(page,encoding='utf8');(E/'a_divide-static-ports.json').write_text(json.dumps(dict(status='repaired_pending_rendered_checks',staticFigures=6,attachedDirectedEdges=len(ports),ports=ports,proseFont='Source Sans 3',mathFont='STIX Two Math',nativeFormulaReplacements=11),indent=2)+'\n');print(len(ports),'attached directed static edges')

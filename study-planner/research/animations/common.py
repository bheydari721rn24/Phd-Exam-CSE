"""Authored immutable checkpoint data shared by the animated course models."""
from copy import deepcopy
SCENES={};CHECKS=[]
def check(label,condition):
    assert condition,label
    CHECKS.append(label)
def node(id,label,x,y,w=88,h=46,tone='plain',kind='card',**kw):
    return dict(id=str(id),label=str(label),x=float(x),y=float(y),w=w,h=h,tone=tone,kind=kind,**kw)
def frame(nodes,caption,metrics=None,formula='',line=0,edges=None,**kw):
    return deepcopy(dict(nodes=nodes,caption=caption,metrics=metrics or {},formula=formula,line=line,edges=edges or [],**kw))
def scene(id,title,description,invariant,frames,code=(),**kw):
    assert id not in SCENES and len(frames)>=2,(id,len(frames))
    for i,f in enumerate(frames):
        check(id+' unique entities '+str(i),len({n['id'] for n in f['nodes']})==len(f['nodes']))
        check(id+' bounded positions '+str(i),all(15<=n['x']<=745 and 20<=n['y']<=340 for n in f['nodes']))
        check(id+' complete explanation '+str(i),len(f['caption'].split())>=8)
    SCENES[id]=dict(id=id,title=title,description=description,invariant=invariant,frames=frames,code=list(code),**kw)
    return id
def array_nodes(values,y=95,prefix='r',tones=None,start=90,gap=92,labels=True):
    return [node(prefix+str(i),v,start+i*gap,y,tone=(tones or {}).get(i,'plain')) for i,v in enumerate(values)]
def cards(values,tones=None):
    return [node(str(i),v,140+(i%3)*240,80+(i//3)*90,w=205,h=62,tone=(tones or {}).get(i,'plain')) for i,v in enumerate(values)]

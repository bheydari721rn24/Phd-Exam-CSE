from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_i_uninformed_browser.py').read_text(encoding='utf-8').replace('i_uninformed','p_strings').replace('i-uninformed','p-strings').replace('SearchPlayers','StringPlayers').replace('SearchLab','StringLab').replace('us-','st-')
start=s.index(' for id,step,name in ');end=s.index(" capture('.hero'",start)
s=s[:start]+''' for id,step,name in [('scan-embedded',2,'scan.png'),('pad-copy',4,'padding.png'),('move-right',3,'overlap.png'),('match-worst',12,'matching.png'),('compact-main',5,'compaction.png'),('tokens-main',5,'tokens.png')]:
  js('StringPlayers.find(p=>p.model.id==='+json.dumps(id)+').show('+str(step)+')');capture('[data-st-model="'+id+'"]',name)
'''+s[end:]
s=s.replace('starvation-main','move-right').replace('bfs-main','scan-embedded').replace('p.show(0);p.host.querySelector("[data-next]").click()', 'p.show(1);p.host.querySelector("[data-next]").click()',1)
start=s.index(" report['labs']=[]");end=s.index(" cdp('Emulation.setDeviceMetricsOverride',dict(width=390",start)
s=s[:start]+''' report['labs']=[]
 for spec in [dict(operation='copy',source='abc',destination='',capacity=4),dict(operation='ncpy',source='ab',destination='xxxxxxxx',capacity=8,limit=5),dict(operation='append',source='XY',destination='orbit',capacity=10,limit=16),dict(operation='match',source='aa',destination='aaaa',capacity=5),dict(operation='move',source='',destination='abcd',capacity=8,**{'from':0,'to':1,'count':5}),dict(operation='compact',source='a',destination='banana',capacity=7),dict(operation='tokens',source=',',destination='a,,b,',capacity=6)]:
  obj=js('(()=>{const f=document.querySelector("#st-form"),spec='+json.dumps(spec)+';for(const [k,v]of Object.entries(spec))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));const bad=[];for(let i=0;i<StringLab.model.frames.length;i++){StringLab.show(i);bad.push(...DiagramLayout.audit(StringLab.host.querySelector("svg")));}return {error:document.querySelector("#st-error").textContent,result:StringLab.model.result,issues:bad};})()');assert not obj['error']and not obj['issues'],obj;report['labs'].append(obj)
 capture('#st-output .st-stage','editable-memory.png')
 for change in [dict(capacity=0),dict(capacity=17),dict(source='é'),dict(source='abcdefghijklmnop'),dict(destination='abcd',capacity=3),dict(operation='insert',source='',destination='ab',capacity=8,position=0)]:
  js('(()=>{window.oldLab=StringLab;const f=document.querySelector("#st-form"),base={operation:"copy",source:"abc",destination:"",capacity:8,limit:16,position:2,remove:1,from:0,to:1,count:3},change='+json.dumps(change)+';for(const[k,v]of Object.entries({...base,...change}))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('StringLab===oldLab && document.querySelector("#st-error").textContent.length>0')
 report['invalidPreservesPrevious']=6
'''+s[end:]
s=s.replace("['cards']==45","['cards']==46")
(B/'qa_p_strings_browser.py').write_text(s,encoding='utf-8')

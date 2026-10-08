from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_i_agents_browser.py').read_text().replace('i_agents','i_uninformed').replace('i-agents','i-uninformed').replace('AgentPlayers','SearchPlayers').replace('AgentLab','SearchLab').replace('ag-','us-').replace('#ag-','#us-').replace('==82','==81').replace('==44','==45')
a=s.index(' for id,step,name in ');b=s.index(" capture('.hero'",a)
s=s[:a]+''' for id,step,name in [('bfs-main',8,'bfs.png'),('ucs-main',11,'ucs.png'),('depth-alias-main',9,'depth-budget.png'),('counts-main',2,'counts.png'),('starvation-main',3,'cost-contour.png'),('grid-main',5,'grid.png'),('bidir-main',3,'bidirectional.png'),('segment-main',6,'segmentation.png')]:
  js('SearchPlayers.find(p=>p.model.id==='+json.dumps(id)+').show('+str(step)+')');capture('[data-us-model="'+id+'"]',name)
'''+s[b:]
s=s.replace('threshold-main','starvation-main').replace('vacuum-main','bfs-main')
a=s.index(" report['labs']=[]");b=s.index(" cdp('Emulation.setDeviceMetricsOverride',dict(width=390",a)
s=s[:a]+''' report['labs']=[]
 for alg,edges,limit in [('ucs','S A 4\\nS B 1\\nB A 1\\nA G 2\\nB G 8',4),('bfs','S G 9\\nS A 1\\nA G 1',4),('dfs','S A 1\\nS B 1\\nA G 1',4),('dls','S A 1\\nA B 1\\nB X 1\\nX G 1\\nS X 1',3),('ids','S A 1\\nA B 1\\nB G 1',3),('ucs','S A 0\\nA S 0\\nA G 2',4)]:
  obj=js('(()=>{const f=document.querySelector("#us-form");f.elements.algorithm.value='+json.dumps(alg)+';f.elements.edges.value='+json.dumps(edges)+';f.elements.limit.value='+str(limit)+';f.dispatchEvent(new Event("submit",{cancelable:true}));const bad=[];for(let i=0;i<SearchLab.model.frames.length;i++){SearchLab.show(i);bad.push(...DiagramLayout.audit(SearchLab.host.querySelector("svg")));}return {error:document.querySelector("#us-error").textContent,result:SearchLab.model.result,issues:bad};})()');assert not obj['error']and not obj['issues'],obj;report['labs'].append(obj)
 capture('#us-output .us-stage','editable-search.png')
 for field,value in [('edges','S G -1'),('edges','S G 1.5'),('edges','S G 10001'),('start','invalid name'),('goal','<bad>'),('limit','13')]:
  js('(()=>{window.oldLab=SearchLab;const f=document.querySelector("#us-form");f.elements.start.value="S";f.elements.goal.value="G";f.elements.edges.value="S G 2";f.elements.limit.value="4";f.elements['+json.dumps(field)+'].value='+json.dumps(value)+';f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('SearchLab===oldLab && document.querySelector("#us-error").textContent.length>0')
 report['invalidPreservesPrevious']=6
'''+s[b:]
(B/'qa_i_uninformed_browser.py').write_text(s,encoding='utf-8')

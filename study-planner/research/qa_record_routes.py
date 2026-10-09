"""Inspect the whole transit, not only the before/after endpoints."""
from pathlib import Path
R=Path(__file__).resolve().parents[1];source=(R/'research/qa_recent_simulations.py').read_text()
setup=source[:source.index(' for topic,globalname in TOPICS.items():')].replace("OUT=R/'research/recent-animation-redesign'","OUT=R/'research/player-behavior-repair'").replace("/'recent-simulation-qa'","/'record-route-qa'")
checks=r'''
 report={'status':'in_progress','models':[]}
 for topic in ['a_sort','a_select']:
  cdp('Emulation.setDeviceMetricsOverride',dict(width=1200,height=1000,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/{topic}.html'))
  for _ in range(200):
   if js('window.AdvancedSimulations?.players.length>5'):break
   time.sleep(.1)
  js('document.fonts.ready');js('AdvancedSimulations.players.forEach(p=>p.pause())')
  audit=js("""(()=>{const rows=[];for(const p of AdvancedSimulations.players){if(!p.model.frames.some(f=>f.svg))continue;const bad=[],steps=[];for(let i=1;i<p.model.frames.length;i++){p.show(i);if(!p.motionPairs)continue;steps.push(i);const slider=p.host.querySelector('.sim-motion-control input');for(const t of[0,.125,.25,.375,.5,.625,.75,.875,1]){slider.value=t*100;slider.dispatchEvent(new Event('input'));const svg=p.host.querySelector('.sim-stage svg'),boxes=[...svg.querySelectorAll('[data-entity]>rect')].filter(r=>getComputedStyle(r).visibility!=='hidden').map(r=>({...DiagramLayout.box(svg,r),entity:r.parentElement.dataset.entity}));for(const b of boxes){if(![b.x,b.y,b.w,b.h].every(Number.isFinite)||b.x<-.5||b.y<-.5||b.x+b.w>svg.viewBox.baseVal.width+.5||b.y+b.h>svg.viewBox.baseVal.height+.5)bad.push({frame:i,t,kind:'outside transit frame',entity:b.entity,b});}for(let a=0;a<boxes.length;a++)for(let b=a+1;b<boxes.length;b++){const A=boxes[a],B=boxes[b],x=Math.min(A.x+A.w,B.x+B.w)-Math.max(A.x,B.x),y=Math.min(A.y+A.h,B.y+B.h)-Math.max(A.y,B.y);if(x>2&&y>2)bad.push({frame:i,t,kind:'overlapping record bodies',entities:[A.entity,B.entity]});}}}p.show(0);rows.push({id:p.model.id,kind:p.model.kind,frames:p.model.frames.length,routedSteps:steps,issues:bad});}return rows;})()""")
  report['models']+=audit;print(topic,'routed steps',sum(len(r['routedSteps'])for r in audit),'issues',sum(len(r['issues'])for r in audit),flush=True)
  if topic=='a_sort':
   js("window.p=AdvancedSimulations.players.find(p=>p.model.kind==='bubble');p.host.scrollIntoView({block:'center'});window.i=p.model.frames.findIndex((f,i)=>i>0&&f.metrics.swaps>p.model.frames[i-1].metrics.swaps);p.show(i);const slider=p.host.querySelector('.sim-motion-control input');slider.value=50;slider.dispatchEvent(new Event('input'))");capture('.sim-redesign[data-frame="'+str(js('p.index'))+'"] .sim-shell','bubble-transit.png')
  else:
   js("window.p=AdvancedSimulations.players.find(p=>p.model.kind==='three-way-selection');p.show(5);p.host.scrollIntoView({block:'center'})");capture('.sim-redesign[data-frame="5"] .sim-shell','selection.png')
 report['status']='passed'if not any(r['issues']for r in report['models'])else'needs_repair'
finally:
 (OUT/'record-routes.json').write_text(json.dumps(report,indent=2)+'\n');server.shutdown();proc.terminate()
print(report['status'])
'''
exec(compile(setup+checks,str(__file__),'exec'))

"""Check live movement, exact fixed topology, compact layout and adjustable traces."""
from pathlib import Path
R=Path(__file__).resolve().parents[1]
source=(R/'research/qa_recent_simulations.py').read_text();setup=source[:source.index(' for topic,globalname in TOPICS.items():')].replace("OUT=R/'research/recent-animation-redesign'","OUT=R/'research/library-simulation-standard'").replace("/'recent-simulation-qa'","/'compact-library-qa'")
checks=r'''
 report={'status':'in_progress','chapters':{}}
 for topic in ['a_sort','p_recursion','p_arrays','p_functions','g_combin','g_kmap','a_arrays','s_discrete']:
  cdp('Emulation.setDeviceMetricsOverride',dict(width=1200,height=1000,deviceScaleFactor=1,mobile=False));cdp('Emulation.setEmulatedMedia',{'media':'screen','features':[{'name':'prefers-reduced-motion','value':'no-preference'}]});cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/{topic}.html'))
  for _ in range(200):
   if js('document.readyState==="complete"&&!!window.AdvancedSimulations'):break
   time.sleep(.1)
  js('document.fonts.ready');time.sleep(.3);js("Promise.all([...document.querySelectorAll('.concept-animation[data-scenes]')].map(h=>ConceptAnimations.ready(h)))")
  result={'errors':js('__errors')};report['chapters'][topic]=result
  js("window.p=AdvancedSimulations.players.find(p=>p.model.frames.length>3)")
  if topic=='a_sort':
   assert js('document.documentElement.dataset.sortLoaded')=='true'
   js("window.p=AdvancedSimulations.players.find(p=>p.model.kind==='merge'&&p.model.frames.some(f=>f.svg.includes('data-source-entity')))" )
  elif topic=='p_recursion':js("window.p=RecursionPlayers.find(p=>p.model.id==='hanoi-three')")
  elif topic in ['p_arrays','p_functions','g_combin','g_kmap']:
   js("document.querySelector('form').dispatchEvent(new Event('submit',{cancelable:true}));window.p=AdvancedSimulations.players.find(p=>p.model.id.includes('custom-'))")
  js('window.start=p.model.frames.findIndex((f,i)=>i>0&&f.svg?.includes("data-source-entity"));if(start<1)start=1;p.show(start-1);p.host.querySelector("[data-next]").click()');time.sleep(.2);js('p.pause();window.times=p.host.querySelector(".sim-stage").getAnimations({subtree:true}).map(a=>a.currentTime);window.progress=p.transition;window.drawing=p.host.querySelector(".sim-stage").innerHTML');time.sleep(.15)
  result['pause']=js('({motion:times.length,frozen:JSON.stringify(times)===JSON.stringify(p.host.querySelector(".sim-stage").getAnimations({subtree:true}).map(a=>a.currentTime)),geometryFrozen:p.transition===progress&&p.host.querySelector(".sim-stage").innerHTML===drawing})');assert result['pause']['motion']and result['pause']['frozen']and result['pause']['geometryFrozen'],(topic,result)
  js('p.host.querySelector("[data-play]").click()');time.sleep(.15);result['resumed']=js('p.transition>progress');assert result['resumed'];js('p.pause()')
  result['scrub']=js('(()=>{const q=p.host.querySelector(".sim-motion-control input");q.value=35;q.dispatchEvent(new Event("input"));return p.transition===.35&&!p.running;})()');assert result['scrub']
  result['zoom']=js('(()=>{const width=p.host.getBoundingClientRect().width;p.host.querySelector("[data-zoom]").click();const stage=p.host.querySelector(".sim-stage"),inside=stage.scrollWidth>stage.clientWidth&&p.host.getBoundingClientRect().width===width&&stage.clientHeight<=480;p.host.querySelector("[data-zoom]").click();return inside&&stage.dataset.zoomed==="false";})()');assert result['zoom']
  # Correct replacement and exact state from the legacy adjustable trace interface.
  formcount=js('document.querySelectorAll("form").length')
  if formcount:
   result['replacement']=js('(()=>{const f=document.querySelector("form");f.dispatchEvent(new Event("submit",{cancelable:true}));const n=AdvancedSimulations.players.length;f.dispatchEvent(new Event("submit",{cancelable:true}));return {stable:n===AdvancedSimulations.players.length,noDetachedPlayers:AdvancedSimulations.players.every(p=>p.host.isConnected)};})()')
   assert result['replacement']['stable']and result['replacement']['noDetachedPlayers'],(topic,result)
  if topic=='a_sort':
   js("window.heap=AdvancedSimulations.players.find(p=>p.model.kind==='heap');heap.show(1);heap.host.querySelector('[data-next]').click();heap.pause();")
   result['heapFixedShapes']=js('heap.motionPairs>=0&&[...heap.host.querySelectorAll(".sim-stage circle")].every(n=>!n.getAnimations().length)')
   result['copyRoutes']=js('p.dependencyFlows>0');assert result['copyRoutes']
  js('window.p=AdvancedSimulations.players.find(p=>p.model.frames.length>3);p.show(2);p.print()');cdp('Emulation.setEmulatedMedia',{'media':'print'});result['print']=js('({visible:getComputedStyle(p.host.querySelector(".sim-print")).display!=="none",shellHidden:getComputedStyle(p.host.querySelector(".sim-shell")).display==="none",idsUnique:(()=>{const ids=[...p.host.querySelectorAll(".sim-print [id]")].map(n=>n.id);return new Set(ids).size===ids.length;})()})');assert all(result['print'].values());cdp('Emulation.setEmulatedMedia',{'media':'screen','features':[{'name':'prefers-reduced-motion','value':'reduce'}]});time.sleep(.1);js('p.show(1);p.host.querySelector("[data-next]").click()');result['reducedMotion']=js('p.transition===1&&p.host.querySelector(".sim-stage").getAnimations({subtree:true}).length===0');assert result['reducedMotion']
  js('p.show(2);p.host.dataset.capture="current"');capture('[data-capture=current] .sim-shell',topic+'.png');result['errors']=js('__errors');assert not result['errors'];print(topic,'live replay / compact zoom / print passed',flush=True)
 report['status']='passed'
finally:
 (OUT/'interactions.json').write_text(json.dumps(report,indent=2)+'\n');server.shutdown();proc.terminate()
print(report['status'])
'''
exec(compile(setup+checks,str(__file__),'exec'))

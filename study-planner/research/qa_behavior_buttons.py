"""Use the visible controls; do not substitute pause() for the user's Pause button."""
from pathlib import Path
R=Path(__file__).resolve().parents[1]
source=(R/'research/qa_recent_simulations.py').read_text()
setup=source[:source.index(' for topic,globalname in TOPICS.items():')].replace("OUT=R/'research/recent-animation-redesign'","OUT=R/'research/player-behavior-repair'").replace("/'recent-simulation-qa'","/'player-behavior-buttons'")
checks=r'''
 report={'status':'in_progress','chapters':{}}
 for topic in ['a_sort','p_recursion','p_arrays','p_functions','g_combin','g_kmap','a_arrays','s_discrete','d_relations']:
  cdp('Emulation.setDeviceMetricsOverride',dict(width=1200,height=1000,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/{topic}.html'))
  for _ in range(200):
   if js('document.readyState==="complete"&&!!window.AdvancedSimulations&&AdvancedSimulations.players.length>0'):break
   time.sleep(.1)
  js('document.fonts.ready');js("Promise.all([...document.querySelectorAll('.concept-animation[data-scenes]')].map(h=>ConceptAnimations.ready(h)))")
  js('window.p=AdvancedSimulations.players.find(p=>p.model.frames.length>3&&p.host.querySelector(".sim-stage svg"));p.host.scrollIntoView({block:"center"});p.show(0)');time.sleep(.2)
  r={'errors':js('__errors')};report['chapters'][topic]=r
  js('p.host.querySelector("[data-next]").click()');time.sleep(.16)
  r['manualStepOffersPause']=js('p.transition<1&&p.host.querySelector("[data-play]").textContent==="Pause"');assert r['manualStepOffersPause'],(topic,r)
  js('p.host.querySelector("[data-play]").click();window.t=p.transition;window.markup=p.host.querySelector(".sim-stage").innerHTML');time.sleep(.16)
  r['visiblePauseActuallyFreezes']=js('!p.running&&p.transition===t&&p.host.querySelector(".sim-stage").innerHTML===markup&&p.host.querySelector("[data-play]").textContent==="Play"');assert r['visiblePauseActuallyFreezes'],(topic,r)
  js('p.host.querySelector("[data-play]").click()');time.sleep(.15);r['visibleResume']=js('p.transition>t');assert r['visibleResume'];js('p.host.querySelector("[data-play]").click()')
  js('p.show(3);p.host.querySelector("[data-prev]").click()');r['reverseOrigin']=js('p.index===2&&p.replayFrom===3');assert r['reverseOrigin'];time.sleep(.1);js('p.host.querySelector("[data-play]").click()')
  js('p.show(2);p.host.querySelector("[data-view=before]").click()');r['beforeState']=js('p.host.dataset.displayedFrame==="1"&&p.host.querySelector(".sim-caption").textContent===p.model.frames[1].caption&&p.teaching.root.querySelector("[data-detail=state] pre").textContent===JSON.stringify(AdvancedSimulations.state(p.model.frames[1]),null,2)');assert r['beforeState']
  js('p.host.querySelector("[data-view=after]").click();const slider=p.host.querySelector(".sim-motion-control input");slider.value=35;slider.dispatchEvent(new Event("input"));p.host.querySelector("[data-play]").click()');time.sleep(.16);r['resumeFromScrub']=js('p.transition>.35&&p.index===2');assert r['resumeFromScrub'];js('p.pause()')
  r['speedChangesMotion']=js('(()=>{const q=p.host.querySelector("[data-speed]");q.value=4400;q.dispatchEvent(new Event("change"));const a=p.host.querySelector(".sim-stage").getAnimations({subtree:true})[0];const ok=a?.playbackRate===.5;q.value=2200;q.dispatchEvent(new Event("change"));return ok;})()');assert r['speedChangesMotion'],(topic,r)
  js('p.show(p.model.frames.length-2);p.host.querySelector("[data-next]").click()');time.sleep(.15);js('p.host.querySelector("[data-play]").click();window.t=p.transition;p.host.querySelector("[data-play]").click()');time.sleep(.15);r['lastFrameResumeDoesNotRestart']=js('p.index===p.model.frames.length-1&&p.transition>t');assert r['lastFrameResumeDoesNotRestart'];js('p.pause()')
  js('p.show(2);p.print()');r['printIdsUniqueAcrossPlayer']=js('(()=>{const ids=[...p.host.querySelectorAll("[id]")].map(n=>n.id);return new Set(ids).size===ids.length;})()');assert r['printIdsUniqueAcrossPlayer'];js('p.clearPrint()')
  r['compactHeight']=js('p.host.querySelector(".sim-stage").clientHeight<=420');assert r['compactHeight']
  capture('.sim-redesign[data-frame="2"] .sim-shell',topic+'.png');r['errors']=js('__errors');assert not r['errors'];print(topic,'visible controls passed',flush=True)
 report['status']='passed'
finally:
 (OUT/'buttons.json').write_text(json.dumps(report,indent=2)+'\n');server.shutdown();proc.terminate()
print(report['status'])
'''
exec(compile(setup+checks,str(__file__),'exec'))

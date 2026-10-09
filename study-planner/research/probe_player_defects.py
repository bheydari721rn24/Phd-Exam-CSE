from pathlib import Path
R=Path(__file__).resolve().parents[1]
source=(R/'research/qa_recent_simulations.py').read_text()
setup=source[:source.index(' for topic,globalname in TOPICS.items():')].replace("OUT=R/'research/recent-animation-redesign'","OUT=R/'research/player-behavior-repair'").replace("/'recent-simulation-qa'","/'player-behavior-repair'")
checks=r'''
 OUT.mkdir(exist_ok=True)
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1200,height=1000,deviceScaleFactor=1,mobile=False))
 cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/p_recursion.html'))
 for _ in range(200):
  if js('window.RecursionPlayers?.length>0'):break
  time.sleep(.1)
 js('document.fonts.ready');js("window.p=RecursionPlayers.find(p=>p.model.id==='hanoi-three');p.host.scrollIntoView();p.show(0);p.host.querySelector('[data-next]').click()")
 time.sleep(.15)
 report={'manualMovement':js('({progress:p.transition,button:p.host.querySelector("[data-play]").textContent,running:p.running})')}
 js('p.host.querySelector("[data-play]").click()');time.sleep(.15)
 report['pauseButtonClick']=js('({progress:p.transition,button:p.host.querySelector("[data-play]").textContent,running:p.running})')
 js('p.pause();p.show(2);p.host.querySelector("[data-view=before]").click()')
 report['beforeView']=js('({caption:p.host.querySelector(".sim-caption").textContent,expectedCaption:p.model.frames[1].caption,state:p.teaching.root.querySelector("[data-detail=state] pre").textContent,expectedState:JSON.stringify(AdvancedSimulations.state(p.model.frames[1]),null,2)})')
 js('p.host.querySelector("[data-view=after]").click();p.print()')
 report['duplicatePrintIds']=js('(()=>{const ids=[...p.host.querySelectorAll("[id]")].map(n=>n.id);return ids.filter((id,i)=>ids.indexOf(id)!==i);})()')
 print(json.dumps(report),flush=True)
finally:
 (OUT/'defects-before.json').write_text(json.dumps(report,indent=2)+'\n');server.shutdown();proc.terminate()
'''
exec(compile(setup+checks,str(__file__),'exec'))

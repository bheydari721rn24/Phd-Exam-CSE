from pathlib import Path
R=Path(__file__).resolve().parents[1]
s=(R/'research/qa_recent_simulations.py').read_text();setup=s[:s.index(' for topic,globalname in TOPICS.items():')].replace("OUT=R/'research/recent-animation-redesign'","OUT=R/'research/library-simulation-standard'").replace("/'recent-simulation-qa'","/'compact-library-qa'")
checks=r'''
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1200,height=1000,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/l_vectors.html'))
 for _ in range(100):
  if js('document.readyState==="complete"&&!!window.ConceptAnimations'):break
  time.sleep(.1)
 js('document.fonts.ready');js("Promise.all([...document.querySelectorAll('.concept-animation[data-scenes]')].map(h=>ConceptAnimations.ready(h)))")
 report['labels']=js('({noStatisticalAlias:![...document.querySelectorAll(".sim-metric span")].some(n=>n.textContent.includes("Population variance")),variableV:[...document.querySelectorAll(".sim-metric span")].some(n=>n.textContent==="v"),mathFont:document.fonts.check("18px STIX Two Math"),errors:__errors})');assert report['labels']['noStatisticalAlias']and report['labels']['variableV']and not report['labels']['errors']
 js('window.p=AdvancedSimulations.players.find(p=>p.model.frames.length>2);p.show(2);p.host.dataset.capture="current"');capture('[data-capture=current] .sim-shell','contextual-l_vectors.png')
 report['status']='passed'
finally:
 (OUT/'contextual-readouts.json').write_text(json.dumps(report,indent=2)+'\n');server.shutdown();proc.terminate()
print(report['status'])
'''
exec(compile(setup+checks,str(__file__),'exec'))

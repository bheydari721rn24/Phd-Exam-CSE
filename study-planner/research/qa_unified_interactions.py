from pathlib import Path
R=Path(__file__).resolve().parents[1]
source=(R/'research/qa_recent_simulations.py').read_text();setup=source[:source.index(' for topic,globalname in TOPICS.items():')].replace("OUT=R/'research/recent-animation-redesign'","OUT=R/'research/library-simulation-standard'").replace("/'recent-simulation-qa'","/'compact-library-qa'")
checks=r'''
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1200,height=1000,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/a_sort.html'))
 for _ in range(100):
  if js('document.documentElement.dataset.sortLoaded'):break
  time.sleep(.1)
 print(js('({ready:document.documentElement.dataset.sortLoaded,hosts:document.querySelectorAll("[data-sort-model]").length,players:AdvancedSimulations.players.length,hero:document.querySelector(".hero").innerText})'),flush=True)
 report['status']='diagnostic'
finally:
 (OUT/'interactions.json').write_text(json.dumps(report,indent=2)+'\n');server.shutdown();proc.terminate()
'''
exec(compile(setup+checks,str(__file__),'exec'))

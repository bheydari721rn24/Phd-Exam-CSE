"""Focused keyboard, anchor, SVG namespace and print-media checks."""
from pathlib import Path
import ast,json
R=Path(__file__).resolve().parents[1]
source=(R/'research/qa_recent_simulations.py').read_text()
# Reuse only the browser setup and helper definitions, not the full sweep.
setup=source[:source.index(' for topic,globalname in TOPICS.items():')]
checks=r'''
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1440,height=1100,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/p_recursion.html#sim-hanoi-three'))
 for _ in range(100):
  if js('window.RecursionPlayers?.length'):break
  time.sleep(.1)
 js('document.fonts.ready');js('window.p=RecursionPlayers.find(p=>p.model.id==="hanoi-three");p.show(3);p.host.focus();p.host.dispatchEvent(new KeyboardEvent("keydown",{key:"ArrowRight",bubbles:true}))');assert js('p.index')==4
 js('p.host.dispatchEvent(new KeyboardEvent("keydown",{key:"Home",bubbles:true}))');assert js('p.index')==0
 js('p.host.dispatchEvent(new KeyboardEvent("keydown",{key:"End",bubbles:true}))');assert js('p.index===p.model.frames.length-1')
 report['keyboard']=True;report['anchor']=js('document.querySelector("#sim-hanoi-three")===p.host');assert report['anchor']
 js('p.show(7);p.host.querySelector("[data-view=compare]").click()');report['compareIDs']=js('(()=>{const ids=[...p.host.querySelectorAll(".sim-stage [id]")].map(n=>n.id);return new Set(ids).size===ids.length;})()');assert report['compareIDs']
 js('p.print()');cdp('Emulation.setEmulatedMedia',{'media':'print'});report['print']=js('({visible:getComputedStyle(p.host.querySelector(".sim-print")).display!=="none",shellHidden:getComputedStyle(p.host.querySelector(".sim-shell")).display==="none",marginLeft:getComputedStyle(p.host).marginLeft,idsUnique:(()=>{const ids=[...p.host.querySelectorAll(".sim-print [id]")].map(n=>n.id);return new Set(ids).size===ids.length;})()})');assert report['print']['visible']and report['print']['shellHidden']and report['print']['idsUnique']and report['print']['marginLeft']=='0px'
 cdp('Emulation.setEmulatedMedia',{'media':'screen'});cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/reviews/recent-simulation-redesign.html'))
 for _ in range(100):
  if js('[...document.links].filter(a=>a.hash.startsWith("#sim-")).length===251'):break
  time.sleep(.1)
 report['guideLinks']=js('[...document.links].filter(a=>a.hash.startsWith("#sim-")).length');assert report['guideLinks']==251
 report['runtimeErrors']=js('__errors');assert not report['runtimeErrors'];report['status']='passed'
finally:
 (R/'research/recent-animation-redesign/interactions.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');server.shutdown();proc.terminate()
print(json.dumps(report))
'''
exec(compile(setup+checks,str(__file__),'exec'))

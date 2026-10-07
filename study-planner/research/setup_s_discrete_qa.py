from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_s_descriptive_browser.py').read_text(encoding='utf-8')
s=s[:s.index(' # Every frame uses')].replace('s_descriptive','s_discrete').replace('s-descriptive','s-discrete').replace('StatisticsPlayers','DiscretePlayers').replace('stat-model','disc-model').replace('stat-print','disc-print').replace('==82','==83')
s+='''\n report['mappingPortsAndPadding']=js("""(()=>{const rows=[];for(const p of DiscretePlayers){if(!['weighted-fiber-map','many-to-one-transformation'].includes(p.model.kind))continue;for(let i=0;i<p.model.frames.length;i++){p.show(i);const svg=p.host.querySelector('svg'),boxes=[...svg.querySelectorAll('polygon')].map(e=>DiagramLayout.box(svg,e)).filter(b=>b.w>100&&b.h>40);for(const t of svg.querySelectorAll('text')){const a=DiagramLayout.box(svg,t),cx=a.x+a.w/2,cy=a.y+a.h/2,b=boxes.find(b=>cx>b.x&&cx<b.x+b.w&&cy>b.y&&cy<b.y+b.h);if(b){const pads=[a.x-b.x,b.x+b.w-a.x-a.w,a.y-b.y,b.y+b.h-a.y-a.h];if(Math.min(...pads)<6)rows.push({id:p.model.id,frame:i,text:t.textContent,pads});}}for(const path of svg.querySelectorAll('path')){const length=path.getTotalLength(),start=path.getPointAtLength(0),end=path.getPointAtLength(length);const source=boxes.find(b=>Math.abs(start.x-b.x-b.w)<.1&&start.y>=b.y&&start.y<=b.y+b.h),target=boxes.find(b=>Math.abs(end.x-b.x)<.1&&end.y>=b.y&&end.y<=b.y+b.h);if(!source||!target)rows.push({id:p.model.id,frame:i,kind:'connector endpoint'});}}p.show(0);}return rows;})()""");assert not report['mappingPortsAndPadding'],report['mappingPortsAndPadding']\n assert report['geometry']['models']==37 and report['geometry']['frames']==208\n'''
tail=r"""
 capture('.hero','title.png')
 capture('[data-source-id="s-discrete-original-30"]','question-convolution.png')
 capture('.review-rule','review-rule.png')
 for id,step,name in [('map-weighted',4,'mapping.png'),('cdf-three',3,'cdf.png'),('interval-three',3,'interval.png'),('square-five',5,'square.png'),('bin-four-quarter',4,'binomial.png'),('hyper-forced',3,'hypergeometric.png'),('cap-four',3,'stopping.png'),('max-four',2,'maximum.png'),('family-conditioning',2,'posterior.png')]:
  js('DiscretePlayers.find(p=>p.model.id==='+json.dumps(id)+').show('+str(step)+')');capture('[data-disc-model="'+id+'"]',name)
 js('window.p=DiscretePlayers.find(p=>p.model.id==="inverse-three");p.show(0);p.host.querySelector("[data-next]").click()');time.sleep(.1);js('p.pause();window.times=p.host.querySelector("svg").getAnimations({subtree:true}).map(a=>a.currentTime)');time.sleep(.1)
 report['pause']=js('({motions:times.length,frozen:JSON.stringify(times)===JSON.stringify(p.host.querySelector("svg").getAnimations({subtree:true}).map(a=>a.currentTime))})');assert report['pause']['motions']>0 and report['pause']['frozen']
 js('p.host.querySelector("[data-play]").click()');time.sleep(.1);report['resume']=js('p.host.querySelector("svg").getAnimations({subtree:true}).some(a=>a.currentTime>times[0])');assert report['resume'];js('p.pause();p.show(3);p.host.querySelector("[data-prev]").click()');assert js('p.index')==2
 js('p.host.querySelector("[data-seek]").value=4;p.host.querySelector("[data-seek]").dispatchEvent(new Event("input"))');assert js('p.index')==4
 js('p.host.querySelector("[data-reset]").click()');assert js('p.index')==0
 cdp('Emulation.setEmulatedMedia',{'features':[{'name':'prefers-reduced-motion','value':'reduce'}]});js('p.show(1);p.host.querySelector("[data-next]").click()');assert js('p.host.querySelector("svg").getAnimations({subtree:true}).length')==0;report['reducedMotion']=True
 js('p.print()');assert js('p.host.querySelectorAll(".disc-print figure").length')==js('p.model.frames.length');js('p.clearPrint()');report['printCheckpoints']=True
 fixtures=[('cdf','-2,1,4','.2,.5,.3',1,.25,4,.7),('interval','-2,1,4','.2,.5,.3',1,.25,4,[0,.3,.5,.8]),('quantile','-2,1,4','.2,.5,.3',1,.7,4,1),('square','-2,-1,0,1,2','.05,.1,.2,.25,.4',1,.7,4,[.2,.35,.45]),('binomial','-2,1,4','.2,.5,.3',4,.25,5,27/128),('geometric','-2,1,4','.2,.5,.3',4,.25,5,.75**8),('poisson','-2,1,4','.2,.5,.3',4,3,5,2.718281828459045**-3),('hypergeometric','-2,1,4','.2,.5,.3',8,4,3,[1/14,6/14,6/14,1/14])]
 report['labs']=[]
 for kind,v,mass,n,q,upper,expected in fixtures:
  val=js("(()=>{const f=document.querySelector('#disc-form');for(const [k,v] of Object.entries("+json.dumps(dict(kind=kind,values=v,masses=mass,n=str(n),p=str(q),upper=str(upper)))+"))f.elements[k].value=v;f.dispatchEvent(new Event('submit',{cancelable:true,bubbles:true}));const r=DiscreteLab.model.result,k="+json.dumps(kind)+";const result=k==='cdf'?r[1].after:k==='interval'?r.map(x=>x.p):k==='quantile'?r[0].x:k==='square'?r.map(x=>x.p):k==='binomial'?r[2].p:k==='geometric'?r.tail:k==='poisson'?r.law[0].p:r.map(x=>x.p);return {error:document.querySelector('#disc-error').textContent,result};})()")
  assert not val['error'],(kind,val)
  import math
  if isinstance(expected,list):assert all(math.isclose(a,b,abs_tol=1e-12) for a,b in zip(expected,val['result'])),(kind,val,expected)
  else:assert math.isclose(expected,val['result'],abs_tol=1e-12),(kind,val,expected)
  report['labs'].append(dict(mode=kind,**val))
 invalid=[{'kind':'cdf','masses':'.1,.1,.1'},{'kind':'cdf','values':'1,,2'},{'kind':'quantile','p':'0'},{'kind':'geometric','p':'0'},{'kind':'binomial','n':'2.5'},{'kind':'hypergeometric','n':'4','upper':'5','p':'2'}]
 for change in invalid:
  js('(()=>{window.previousModel=DiscreteLab;const f=document.querySelector("#disc-form");for(const [k,v] of Object.entries('+json.dumps(dict(kind='cdf',values='-2,1,4',masses='.2,.5,.3',n='4',p='.25',upper='5')|change)+'))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('DiscreteLab===previousModel && document.querySelector("#disc-error").textContent.length>0')
 report['invalidPreservesPrevious']=len(invalid)
 report['allModesGeometry']=js('DiagramLayout.audit(DiscreteLab.host.querySelector("svg"))');assert not report['allModesGeometry']
 cdp('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=1,mobile=True));report['mobileOverflow']=js('document.documentElement.scrollWidth>innerWidth+1');assert not report['mobileOverflow'];capture('[data-disc-model="cdf-three"]','mobile-cdf.png')
 cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Emulation.setEmulatedMedia',{'media':'print'});js('p.print()');report['printVisible']=js('getComputedStyle(p.host.querySelector(".disc-print")).display!=="none"');assert report['printVisible'];capture('[data-disc-model="inverse-three"]','print-inverse.png')
 report['runtimeErrors']=js('__errors');assert not report['runtimeErrors']
 cdp('Emulation.setEmulatedMedia',{'media':'screen'});cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/index.html#library'))
 for _ in range(100):
  if js('document.querySelector("#library a[href=\\"chapters/s_discrete.html\\"]")!==null'):break
  time.sleep(.1)
 report['library']=js('({cards:document.querySelectorAll(".library-card").length,visible:!document.querySelector("#view-lessons").hidden,current:document.querySelector("#library a[href=\\"chapters/s_discrete.html\\"]").textContent,errors:__errors})');assert report['library']['cards']==40 and report['library']['visible'] and not report['library']['errors']
 js('location.hash="week-3"');js('new Promise(r=>setTimeout(r,100))');report['weeklyChapterLink']=js('!document.querySelector("#view-weeks").hidden && document.querySelector("#week-detail a[href=\\"chapters/s_discrete.html\\"]")!==null');assert report['weeklyChapterLink']
 report['status']='passed'
 for name in ['title.png','mapping.png','cdf.png','square.png','hypergeometric.png','stopping.png','maximum.png','mobile-cdf.png']:
  shutil.copy2(OUT/name,R/'research/s_discrete-evidence'/name)
finally:
 (R/'research/s_discrete-evidence/browser.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');server.shutdown();proc.terminate()
print(json.dumps({k:v for k,v in report.items() if k not in ['geometry','labs']}))
"""
(B/'qa_s_discrete_browser.py').write_text(s+tail,encoding='utf-8')
print('Prepared real-browser checks.')

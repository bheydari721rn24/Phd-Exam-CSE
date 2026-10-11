from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_a_amortized_browser.py').read_text(encoding='utf-8').replace('a_amortized','s_variance').replace('a-amortized','s-variance').replace('AmortizedPlayers','VariancePlayers').replace('AmortizedLab','VarianceLab').replace('am-','sv-').replace('exsv-','exam-').replace('#am','#sv').replace('>20','>23').replace('==56','==57').replace('>398','>358')
lo=s.index(" for id,name in [");hi=s.index(" js('p.pause()",lo)
s=s[:lo]+""" for id,name in [('weighted-three','moments.png'),('joint-positive','covariance.png'),('two-group','mixture.png'),('psd-failure','matrix.png'),('walk-biased','walk.png'),('fixed-points','permutations.png')]:
  js('VariancePlayers.find(p=>p.model.id==='+json.dumps(id)+').show(VariancePlayers.find(p=>p.model.id==='+json.dumps(id)+').model.frames.length-1)');capture('[data-sv-model="'+id+'"]',name)
 js('window.p=VariancePlayers.find(p=>p.model.id==="linear-projection");p.show(1);p.host.querySelector("[data-next]").click()');time.sleep(.12)
 report['motion']=js('({pairs:p.motionPairs,progress:p.transition,clocks:p.host.querySelector("svg").getAnimations({subtree:true}).length})');assert report['motion']['pairs']>0 and 0<report['motion']['progress']<1
""" +s[hi:]
lo=s.index(" report['labs']=[]");hi=s.index(" cdp('Emulation.setDeviceMetricsOverride',dict(width=390",lo)
s=s[:lo]+""" report['labs']=[]
 for spec in [dict(kind='moments',x='-20,20',p='0.5,0.5',center='20'),dict(kind='moments',x='0',p='1',center=''),dict(kind='joint',x='-1,0,1',y='1,0,1',p='0.3333333333333333,0.3333333333333333,0.3333333333333333'),dict(kind='joint',x='-20,20',y='20,-20',p='0.5,0.5')]:
  obj=js('(()=>{const f=document.querySelector("#sv-form"),spec='+json.dumps(spec)+';for(const[k,v]of Object.entries({kind:"moments",x:"1,3,5",p:"0.25,0.25,0.5",y:"1,0,1",center:"",...spec}))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));const bad=[];for(let i=0;i<VarianceLab.model.frames.length;i++){VarianceLab.show(i);const svg=VarianceLab.host.querySelector("svg");bad.push(...DiagramLayout.audit(svg));for(const t of svg.querySelectorAll("text")){const b=t.getBBox();if(b.x<2||b.y<2||b.x+b.width>758||b.y+b.height>358)bad.push({kind:"text outside",text:t.textContent});}}return {kind:spec.kind,error:document.querySelector("#sv-error").textContent,result:VarianceLab.model.result,issues:bad};})()');assert not obj['error']and not obj['issues'],obj;report['labs'].append(obj)
 for change in [dict(x=''),dict(x='1,2,'),dict(x='21'),dict(p='0.2,0.2,0.2'),dict(p='0.25,-0.25,1'),dict(center='NaN'),dict(kind='joint',y='1,2'),dict(kind='joint',y='Infinity,1,2')]:
  js('(()=>{window.oldLab=VarianceLab;const f=document.querySelector("#sv-form"),base={kind:"moments",x:"1,3,5",p:"0.25,0.25,0.5",y:"1,0,1",center:""},change='+json.dumps(change)+';for(const[k,v]of Object.entries({...base,...change}))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('VarianceLab===oldLab && document.querySelector("#sv-error").textContent.length>0'),change
 report['invalidPreservesPrevious']=8
""" +s[hi:]
s=s.replace('[data-sv-model="queue-interleave"]','[data-sv-model="two-group"]').replace('mobile-queue.png','mobile-mixture.png')
s=s.replace(" js('window.p=VariancePlayers", """ js('VariancePlayers.find(p=>p.model.id==="walk-biased").show(50)');capture('[data-sv-model="walk-biased"]','walk-transfer.png')
 js('window.p=VariancePlayers""")
s=s.replace("dict(kind='joint',x='-20,20',y='20,-20',p='0.5,0.5')", "dict(kind='joint',x='-20,20',y='20,-20',p='0.5,0.5'),dict(kind='joint',x='1,1,1',y='2,2,2',p='0.25,0.25,0.5')")
(B/'qa_s_variance_browser.py').write_text(s,encoding='utf-8')
print('Variance-specific real-browser checks prepared.')

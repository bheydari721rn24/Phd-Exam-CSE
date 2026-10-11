"""Reuse the established Edge/CDP harness with this chapter's actual controls."""
from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_s_variance_browser.py').read_text(encoding='utf-8')
s=s.replace('s_variance','s_distributions').replace('s-variance','s-distributions').replace('VariancePlayers','DistributionPlayers').replace('VarianceLab','DistributionLab').replace('sv-','sd-')
s=s.replace("==87","==88").replace("==80","==84").replace(">23",">26").replace("==57","==58")
start=s.index(" for id,name in [");end=s.index("\n js('window.p=",start)
s=s[:start]+''' for id,name in [('binomial-eight','binomial.png'),('classification','classification.png'),('negative-two','waiting.png'),('finite-wait','finite-wait.png'),('poisson-splitting','splitting.png'),('poisson-approximation','approximation.png'),('censored','censoring.png'),('uniform-lattice','uniform.png')]:
  js('DistributionPlayers.find(p=>p.model.id==='+json.dumps(id)+').show(DistributionPlayers.find(p=>p.model.id==='+json.dumps(id)+').model.frames.length-1)');capture('[data-sd-model="'+id+'"]',name)
 js('DistributionPlayers.find(p=>p.model.id==="binomial-eight").show(16)');capture('[data-sd-model="binomial-eight"]','mass-transfer.png')
'''+s[end:]
s=s.replace('linear-projection','poisson-approximation')
start=s.index(" report['labs']=[]");end=s.index("\n cdp('Emulation.setDeviceMetricsOverride',dict(width=390",start)
s=s[:start]+''' report['labs']=[]
 for spec in [dict(kind='binomial',n='0',p='0'),dict(kind='binomial',n='12',p='1'),dict(kind='geometric',p='0.2',limit='12'),dict(kind='negative-binomial',r='6',p='0.5',limit='12'),dict(kind='hypergeometric',N='8',K='6',n='5'),dict(kind='poisson',lambdaValue='8',limit='12')]:
  obj=js('(()=>{const f=document.querySelector("#sd-form"),spec='+json.dumps(spec)+';for(const[k,v]of Object.entries({kind:"binomial",n:"6",p:"0.5",r:"2",N:"10",K:"4",lambda:"1",limit:"8",...spec}))if(k!=="lambdaValue")f.elements[k].value=v;if(spec.lambdaValue)f.elements.lambda.value=spec.lambdaValue;f.dispatchEvent(new Event("submit",{cancelable:true}));return {error:document.querySelector("#sd-error").textContent,result:DistributionLab.result,issues:DiagramLayout.audit(document.querySelector("#sd-output svg"))};})()');assert not obj['error']and not obj['issues'],obj;report['labs'].append(obj)
 for change in [dict(p='-0.1'),dict(n='1.5'),dict(n='13'),dict(kind='geometric',p='0'),dict(kind='negative-binomial',r='0'),dict(kind='hypergeometric',K='11'),dict(kind='poisson',lambdaValue='NaN'),dict(limit='')]:
  js('(()=>{window.oldLab=DistributionLab;const f=document.querySelector("#sd-form"),change='+json.dumps(change)+';for(const[k,v]of Object.entries({kind:"binomial",n:"6",p:"0.5",r:"2",N:"10",K:"4",lambda:"1",limit:"8",...change}))if(k!=="lambdaValue")f.elements[k].value=v;if(change.lambdaValue)f.elements.lambda.value=change.lambdaValue;f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('DistributionLab===oldLab && document.querySelector("#sd-error").textContent.length>0'),change
 report['invalidPreservesPrevious']=8
'''+s[end:]
s=s.replace('two-group','uniform-lattice').replace('mobile-mixture.png','mobile-uniform.png')
(B/'qa_s_distributions_browser.py').write_text(s,encoding='utf-8')
print('Prepared real-browser counts, every-frame geometry, editable inputs and player controls.')

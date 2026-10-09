"""Exercise all written chapters and every distinct used scientific trace in Edge."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
source=(R/'research/qa_recent_simulations.py').read_text()
setup=source[:source.index(' for topic,globalname in TOPICS.items():')]
setup=setup.replace("OUT=R/'research/recent-animation-redesign'","OUT=R/'research/library-simulation-standard'").replace("/'recent-simulation-qa'","/'unified-library-qa'")
checks=r'''
 report['uniqueModels']=[];seen=set();topics=sorted(p.stem for p in(R/'dist/chapters').glob('*.html'))
 import sys
 if '--resume'in sys.argv and(OUT/'browser.json').exists():
  previous=json.loads((OUT/'browser.json').read_text());report['chapters']={t:c for t,c in previous['chapters'].items()if 'controls'in c};report['uniqueModels']=[m for m in previous['uniqueModels']if not m['issues']and(m['key'].split(':')[0]in report['chapters']or m['key'].startswith(('concept:','problem:')))];seen={m['key']for m in report['uniqueModels']}
 audit="""(()=>{const p=window.auditPlayer,hash=JSON.stringify(p.model.frames),issues=[];let checks=0;for(let i=0;i<p.model.frames.length;i++){p.show(i);const svg=p.host.querySelector('.sim-stage svg');if(!svg){if(!p.host.querySelector('.sim-stage math'))issues.push({frame:i,kind:'missing scientific diagram or derivation'});checks++;continue;}if(p.host.dataset.frame!==String(i)||p.host.querySelector('[data-seek]').value!==String(i))issues.push({frame:i,kind:'wrong checkpoint'});if(!p.teaching.root.dataset.explanation)issues.push({frame:i,kind:'missing explanation'});if(p.host.querySelectorAll('.sim-timeline-list button').length!==p.model.frames.length)issues.push({frame:i,kind:'missing operation'});for(const t of svg.querySelectorAll('text')){const b=DiagramLayout.box(svg,t),v=svg.viewBox.baseVal;if(!Number.isFinite(b.x)||b.x<-1||b.y<-1||b.x+b.w>v.width+1||b.y+b.h>v.height+1)issues.push({frame:i,kind:'label outside drawing',text:t.textContent,bounds:b});}for(const issue of DiagramLayout.audit(svg))issues.push({frame:i,...issue});checks++;}p.show(0);if(hash!==JSON.stringify(p.model.frames))issues.push({kind:'scientific record mutation'});return {id:p.model.id,title:p.model.title,kind:p.model.kind,frames:p.model.frames.length,checked:checks,issues};})()"""
 for topic in topics:
  if topic in report['chapters']and not report['chapters'][topic].get('failedHosts')and not any(m['issues']for m in report['chapters'][topic]['models']):continue
  cdp('Emulation.setDeviceMetricsOverride',dict(width=1440,height=1100,deviceScaleFactor=1,mobile=False));cdp('Emulation.setEmulatedMedia',{'media':'screen','features':[{'name':'prefers-reduced-motion','value':'reduce'}]});cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/{topic}.html'))
  for _ in range(200):
   if js('document.readyState==="complete"&&!!window.AdvancedSimulations'):break
   time.sleep(.1)
  js('document.fonts.ready');time.sleep(.3)
  js("Promise.all([...document.querySelectorAll('.concept-animation[data-scenes]')].map(h=>ConceptAnimations.ready(h)))")
  js("document.querySelectorAll('details.exam-solution').forEach(d=>d.open=true)")
  js("Promise.all([...document.querySelectorAll('[data-problem-visual]')].map(h=>ProblemVisuals.ready(h)))")
  time.sleep(.2)
  # Explicitly exercise form-generated diagrams as well as stored ones.
  js('document.querySelectorAll("form").forEach(f=>f.dispatchEvent(new Event("submit",{cancelable:true})))')
  time.sleep(.1)
  result={'errors':js('__errors'),'players':js('AdvancedSimulations.players.length'),'conceptHosts':js('document.querySelectorAll(".concept-animation[data-scenes]").length'),'problemHosts':js('document.querySelectorAll("[data-problem-visual]").length'),'failedHosts':js('[...document.querySelectorAll("[data-loaded=error]")].map(h=>h.dataset.scenes??h.dataset.problemVisual??h.id)'),'models':[]};report['chapters'][topic]=result
  modelFile=R/f'dist/chapters/{topic}-models.json'
  if modelFile.exists():
   expected={m['id']for m in json.loads(modelFile.read_text())['models']};actual=set(js('AdvancedSimulations.players.map(p=>p.model.id)'));result['missingStoredModels']=sorted(expected-actual)
  else:result['missingStoredModels']=[]
  result['unloadedHosts']=js('[...document.querySelectorAll(".concept-animation[data-scenes],[data-problem-visual]")].filter(h=>h.dataset.loaded!=="true").map(h=>h.dataset.scenes??h.dataset.problemVisual)')
  result['compactWidth']=js('[...document.querySelectorAll(".sim-redesign")].every(h=>h.getBoundingClientRect().width<=h.parentElement.getBoundingClientRect().width+1)')
  rows=js('AdvancedSimulations.players.map((p,i)=>({i,id:p.model.id,kind:p.model.kind,concept:!!p.host.closest(".concept-animation")}))')
  for row in rows:
   if row['concept']:continue
   key=(topic if row['id']not in json.loads((R/'dist/chapters/problem-visual-models.json').read_text())else'problem')+':'+str(row['id'])
   if key in seen:continue
   seen.add(key);js('window.auditPlayer=AdvancedSimulations.players['+str(row['i'])+']');r=js(audit);r['key']=key;result['models'].append(r);report['uniqueModels'].append(r)
  # A scenario may be reused in several questions. Check its frames once globally,
  # but initialize and check the shared interface in every written chapter.
  choices=js('window.ConceptAnimations?ConceptAnimations.players.flatMap((p,i)=>p.scenes.map((s,j)=>({i,j,id:s.id}))):[]')
  for choice in choices:
   key='concept:'+choice['id']
   if key in seen:continue
   seen.add(key);js('window.wrapper=ConceptAnimations.players['+str(choice['i'])+'];wrapper.scene=wrapper.scenes['+str(choice['j'])+'];wrapper.show(0);window.auditPlayer=wrapper.api');r=js(audit);r['key']=key;result['models'].append(r);report['uniqueModels'].append(r)
  if js('window.ConceptAnimations'):
   js('ConceptAnimations.players.forEach(p=>{p.scene=p.scenes[0];p.show(0);})')
  result['controls']=js("""(()=>{const p=AdvancedSimulations.players.find(p=>p.model.frames.length>2),issues=[];if(!p)return {issue:'no multiple-state model'};const h=p.host;p.show(2);h.querySelector('[data-view=before]').click();if(!h.querySelector('.sim-stage svg'))issues.push('before');h.querySelector('[data-view=compare]').click();if(h.querySelectorAll('.sim-stage svg').length!==2)issues.push('compare');const ids=[...h.querySelectorAll('.sim-stage [id]')].map(n=>n.id);if(new Set(ids).size!==ids.length)issues.push('compare IDs');h.querySelector('[data-view=after]').click();h.querySelector('[data-prev]').click();if(p.index!==1)issues.push('previous');h.querySelector('[data-next]').click();if(p.index!==2)issues.push('next');h.querySelector('[data-seek]').value=1;h.querySelector('[data-seek]').dispatchEvent(new Event('input'));if(p.index!==1)issues.push('seek');h.querySelector('.sim-timeline-list button').click();if(p.index!==0)issues.push('timeline');h.querySelector('[data-reset]').click();if(p.index!==0)issues.push('reset');p.host.dispatchEvent(new KeyboardEvent('keydown',{key:'End',bubbles:true}));if(p.index!==p.model.frames.length-1)issues.push('keyboard');p.show(1);h.querySelector('[data-view=reference]').click();if(!h.querySelector('.sim-stage svg'))issues.push('reference');h.querySelector('[data-view=after]').click();p.print();if(h.querySelectorAll('.sim-print figure').length!==p.model.frames.length)issues.push('print trace');const all=[...h.querySelectorAll('.sim-print [id]')].map(n=>n.id);if(new Set(all).size!==all.length)issues.push('print IDs');p.clearPrint();return {issues,id:p.model.id,frames:p.model.frames.length};})()""")
  js('window.visual=AdvancedSimulations.players.find(p=>p.model.frames.length>2);visual.show(Math.min(3,visual.model.frames.length-1));visual.host.dataset.capture="current"')
  if topic in ['d_logic','d_counting','a_arrays','a_sort','a_stackqueue','g_gates','g_combin','g_kmap','l_gauss','l_vectors','s_conditional','p_functions','p_arrays','p_recursion']:
   capture('[data-capture=current] .sim-shell',topic+'.png')
  cdp('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=1,mobile=True));result['mobileOverflow']=js('document.documentElement.scrollWidth>innerWidth+1')
  result['simMobileOverflow']=js('[...document.querySelectorAll(".sim-shell")].some(n=>n.getBoundingClientRect().width>innerWidth)')
  if topic in ['d_logic','a_sort','g_combin','p_arrays']:capture('[data-capture=current] .sim-shell',topic+'-mobile.png')
  cdp('Emulation.setDeviceMetricsOverride',dict(width=1440,height=1100,deviceScaleFactor=1,mobile=False));js('document.documentElement.style.fontSize="200%"');result['enlargedOverflow']=js('document.documentElement.scrollWidth>innerWidth+1');js('document.documentElement.style.fontSize=""')
  result['underlined']=js('[...document.querySelectorAll(".sim-redesign a,.sim-redesign summary")].filter(n=>getComputedStyle(n).textDecorationLine.includes("underline")).length');result['errors']=js('__errors')
  result['initiallyPaused']=js('AdvancedSimulations.players.every(p=>!p.running)')
  (OUT/'browser.json').write_text(json.dumps(report,indent=2)+'\n');print(topic,result['players'],'instances;',len(result['models']),'new distinct models;',sum(len(m['issues'])for m in result['models']),'issues;',len(result['errors']),'errors;',result['mobileOverflow'],flush=True)
 report['status']='passed'if len(report['chapters'])==47 and all(c['players']and not(c['errors']or c['failedHosts']or c['missingStoredModels']or c['unloadedHosts']or not c['compactWidth']or c['controls'].get('issues')or c['controls'].get('issue')or c['mobileOverflow']or c['simMobileOverflow']or c['enlargedOverflow']or c['underlined'])for c in report['chapters'].values())and not any(m['issues']for m in report['uniqueModels'])else'needs_repair'
finally:
 (OUT/'browser.json').write_text(json.dumps(report,indent=2)+'\n');server.shutdown();proc.terminate()
print(json.dumps({'status':report['status'],'chapters':len(report['chapters']),'uniqueModels':len(report['uniqueModels']),'checkpoints':sum(m['frames']for m in report['uniqueModels'])}))
'''
exec(compile(setup+checks,str(__file__),'exec'))

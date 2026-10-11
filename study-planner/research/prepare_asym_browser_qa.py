from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_deep_model_browser.py').read_text().replace('a_model','a_asym').replace('deep-model-browser','deep-asym-browser').replace('==6','==7')
a=s.index(' for frame,name in');z=s.index(" report['staticDiagrams']",a)
s=s[:a]+''' report['controlChecks']=[]
 for sid,count in [('asym-parity-ratio',16),('asym-log-oscillation',8),('asym-floor-ratio',10)]:
  sel='.question-specific-animation[data-scenes="'+sid+'"]'
  row=js('(()=>{const h=document.querySelector('+json.dumps(sel)+'),c=ConceptAnimations.players.find(c=>h.contains(c.api.host)),w=c.api.host,checks=[];c.api.show(2);w.querySelector("[data-view=before]").click();checks.push(w.dataset.displayedFrame==="1");w.querySelector("[data-view=compare]").click();checks.push(w.querySelectorAll(".sim-compare svg").length===2);w.querySelector("[data-view=after]").click();w.querySelector("[data-next]").click();checks.push(c.api.index===3);w.querySelector("[data-prev]").click();checks.push(c.api.index===2);const seek=w.querySelector("[data-seek]");seek.value='+str(count-1)+';seek.dispatchEvent(new Event("input"));checks.push(c.api.index==='+str(count-1)+');w.querySelector("[data-reset]").click();checks.push(c.api.index===0);return {id:'+json.dumps(sid)+',checks};})()')
  report['controlChecks'].append(row);assert all(row['checks']),row
  for frame in [0,count//2,count-1]:
   js('(()=>{const h=document.querySelector('+json.dumps(sel)+');const c=ConceptAnimations.players.find(c=>c.api.host===h || h.contains(c.api.host));c.api.show('+str(frame)+');})()')
   capture(sel,sid+'-'+str(frame)+'.png')
'''+s[z:]
s=s.replace(" capture('.exam-question[data-deep-index=\"12\"] svg','question-12-depths.png')", " capture('.logic-diagram:nth-of-type(2)','strict-hierarchy.png')")
s=s.replace('[1,2,3,4,6,9,12,19,45,46]','[1,2,3,4,7,10,12,16,45,46]').replace('model-representation.png','ratio-envelopes.png').replace('model-animation.png','threshold-animation.png').replace('merge-mobile.png','parity-mobile.png')
(B/'qa_deep_asym_browser.py').write_text(s)

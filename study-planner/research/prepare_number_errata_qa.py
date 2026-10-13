from pathlib import Path
B=Path(__file__).parent
s=(B/'qa_final_invariants_browser.py').read_text();s=s[:s.index(" cdp('Page.enable')")];s=s.replace("'deep-invariants-browser'","'deep-number-errata-browser'").replace("'d_invariants'","'number-source-errata'")
s+=r'''
 cdp('Page.enable');report['pages']=[]
 for chapter in ['s_counting','d_counting','d_number']:
  cdp('Emulation.setDeviceMetricsOverride',dict(width=1360,height=1050,deviceScaleFactor=1,mobile=False));cdp('Page.navigate',dict(url='http://127.0.0.1:8771/chapters/'+chapter+'.html'))
  for _ in range(100):
   if js('document.readyState==="complete" && !!window.ConceptAnimations'):break
   time.sleep(.1)
  js('document.fonts.ready')
  selector='.exam-question[data-source-id="MS_CS_1405_Q129"]'
  js('document.querySelector('+json.dumps(selector)+').querySelector("details").open=true')
  body=js('document.querySelector('+json.dumps(selector)+').textContent')
  assert '40' in body and '96' in body and 'Correct option: 4' in body,(chapter,body)
  row=dict(chapter=chapter,total=40,result=96,option=4)
  if chapter!='d_counting':
   coef=js('document.querySelector(".exam-question[data-source-id=MS_CS_1405_Q125]").textContent')
   assert '15' in coef and '14' in coef
   row['coefficientInputExponent']=15
  if chapter=='s_counting':
   js('ConceptAnimations.ready(document.querySelector('+json.dumps(selector)+').querySelector(".concept-animation"))')
   row['frames']=js('(()=>{const c=ConceptAnimations.players.find(c=>c.scene.id==="counting-question-parity"),a=[];for(let i=0;i<c.scene.frames.length;i++){c.api.show(i);a.push({count:c.scene.frames[i].snapshot.prefix,text:c.api.host.textContent})}return a})()')
   assert [r['count']for r in row['frames']]==[20,40,59,78,96]
   js('(()=>{const c=ConceptAnimations.players.find(c=>c.scene.id==="counting-question-parity");c.api.show(4)})()')
   capture(selector+' .concept-animation','parity-final-desktop.png')
   row['play']=js('(async()=>{const c=ConceptAnimations.players.find(c=>c.scene.id==="counting-question-parity");c.api.show(0);const p=c.api.host.querySelector("[data-play]"),v=c.api.host.querySelector("[data-speed]");v.value="1400";v.dispatchEvent(new Event("change"));p.click();await new Promise(r=>setTimeout(r,1550));p.click();const i=c.api.index;await new Promise(r=>setTimeout(r,150));return{advanced:i>0,paused:i===c.api.index}})()');assert all(row['play'].values())
  capture(selector,chapter+'-corrected-desktop.png')
  for width in [768,390]:
   cdp('Emulation.setDeviceMetricsOverride',dict(width=width,height=950,deviceScaleFactor=1,mobile=width==390));js('new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
   assert js('document.documentElement.scrollWidth<=innerWidth+2'),(chapter,width)
   capture(selector,chapter+'-corrected-'+str(width)+'.png')
  report['pages'].append(row)
 report['status']='passed_current_corrected_pages_and_parity_playback';(R/'research/deep-library-revision/number-source-errata-browser.json').write_text(json.dumps(report,indent=2)+'\n');print({'status':report['status'],'pages':len(report['pages'])})
finally:
 proc.terminate()
 try:proc.wait(timeout=10)
 except subprocess.TimeoutExpired:proc.kill()
'''
(B/'qa_number_errata_browser.py').write_text(s,encoding='utf-8')

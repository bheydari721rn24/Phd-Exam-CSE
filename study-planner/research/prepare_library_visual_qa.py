from pathlib import Path
R=Path(__file__).resolve().parents[1];B=R/'research'
s=(B/'qa_subject_visuals.py').read_text(encoding='utf-8');s=s[:s.index(' for id,s in json.loads')]
s+=r'''
 report=dict(state='in_progress',scenes=[],chapters=[],errors=[]);previews={}
 for id,scene in json.loads((ROOT/'dist/chapters/concept-animations.json').read_text())['scenes'].items():
  row=js('(()=>{const p=reviewPlayer;p.pause();p.scene=reviewData.scenes['+json.dumps(id)+'];const bad=[];for(let i=0;i<p.scene.frames.length;i++){p.show(i,false);bad.push(...DiagramLayout.audit(p.canvas).map(x=>({...x,frame:i})));}return {id:p.scene.id,frames:p.scene.frames.length,bad};})()')
  report['scenes'].append(row)
  previews[id]=js('(()=>{reviewPlayer.show(0,false);return reviewPlayer.canvas.outerHTML;})()')
 # All precomputed checkpoint diagrams are also rendered and measured.
 for topic in ['d_counting','d_inclusion','d_pigeonhole','a_arrays']:
  row=js('(async()=>{const data=await(await fetch('+json.dumps(topic+'-models.json')+')).json(),h=document.createElement("div");document.querySelector("main").prepend(h);const rows=[];for(const m of data.models){const bad=[];for(let i=0;i<m.frames.length;i++){h.innerHTML=m.frames[i].svg;const svg=h.querySelector("svg");if('+json.dumps(topic)+'!=="a_arrays")DiagramLayout.finish(svg);bad.push(...DiagramLayout.audit(svg).map(x=>({...x,frame:i})));}rows.push({id:m.id,frames:m.frames.length,bad});}h.remove();return rows;})()')
  report['scenes'] += [dict(topicId=topic,**r) for r in row]
 report['state']='passed' if not any(r['bad'] for r in report['scenes']) else 'failed'
 (ROOT/'research/library-visual-question-review/animation-browser.json').write_text(json.dumps(report,indent=2)+'\n')
 (ROOT/'research/library-visual-question-review/scene-previews.json').write_text(json.dumps(previews,separators=(',',':'))+'\n')
 print(json.dumps(dict(state=report['state'],models=len(report['scenes']),frames=sum(r['frames'] for r in report['scenes']),bad=sum(len(r['bad']) for r in report['scenes']),examples=[r for r in report['scenes'] if r['bad']][:8])))
finally:
 proc.terminate();server.shutdown()
'''
(B/'qa_library_visuals.py').write_text(s,encoding='utf-8')
print('Prepared full-library measured animation audit')

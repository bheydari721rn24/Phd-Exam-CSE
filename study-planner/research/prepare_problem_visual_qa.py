from pathlib import Path
R=Path(__file__).resolve().parents[1]
source=(R/'research/qa_library_visuals.py').read_text()
prefix=source[:source.index(' # A dedicated test host')]
body=r'''
 js('(async()=>{window.problemModels=await (await fetch("problem-visual-models.json")).json();window.problemTest=document.createElement("div");problemTest.className="problem-stage";document.querySelector("main").prepend(problemTest);})()')
 report=dict(state='in_progress',models=[]);previews={}
 for id,model in json.loads((ROOT/'dist/chapters/problem-visual-models.json').read_text()).items():
  row=js('(()=>{const model=problemModels['+json.dumps(id)+'],bad=[];for(let i=0;i<model.frames.length;i++){problemTest.innerHTML=model.frames[i].html;for(const svg of problemTest.querySelectorAll("svg")){DiagramLayout.finish(svg,{arrows:false});bad.push(...DiagramLayout.audit(svg).map(x=>({...x,frame:i})));}}return {id:'+json.dumps(id)+',kind:model.kind,frames:model.frames.length,bad};})()')
  report['models'].append(row)
  previews[id]=js('(()=>{problemTest.innerHTML=problemModels['+json.dumps(id)+'].frames[0].html;for(const s of problemTest.querySelectorAll("svg"))DiagramLayout.finish(s,{arrows:false});return problemTest.innerHTML;})()')
 report['state']='passed' if not any(r['bad'] for r in report['models']) else 'failed'
 (ROOT/'research/library-visual-question-review/problem-browser.json').write_text(json.dumps(report,indent=2)+'\n')
 (ROOT/'research/library-visual-question-review/problem-previews.json').write_text(json.dumps(previews,separators=(',',':'))+'\n')
 print(json.dumps(dict(state=report['state'],models=len(report['models']),frames=sum(r['frames'] for r in report['models']),bad=sum(len(r['bad']) for r in report['models']),examples=[r for r in report['models'] if r['bad']][:12])))
finally:
 proc.terminate();server.shutdown()
'''
(R/'research/qa_problem_visuals.py').write_text(prefix+body)

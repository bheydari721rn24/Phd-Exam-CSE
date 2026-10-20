"""Inspect actual arrays problem models, editable traces and typography."""
from pathlib import Path
R=Path(__file__).resolve().parents[1]
t=(R/'research/qa_gauss_current_revision.py').read_text(encoding='utf8')
t=t.replace('Gaussian','Arrays').replace('gauss-current','arrays-current').replace('l_gauss.html','p_arrays.html').replace('==71','==83').replace('==33','==38')
t=t.replace("p.scene.id==='gauss-swap'","p.scene.id==='arr-overlap'")
a=t.index('    def mat(a):');z=t.index("    report['fonts']=",a)
lab=r'''
    report['labCases']=[];trace_checks=0
    cases=[[2],[1],[-20,20],[-2,0,3,4,5,6],[2,4,6,8,10,12],[5,3,1,-1,-3,-5]]
    cases += [[((i+3*k)%41)-20 for i in range(1+k%6)]for k in range(24)]
    for mode in ['prefix','right','bad','reverse','difference','compact']:
        for values in cases:
            js('document.getElementById("arrays-form").elements.mode.value='+json.dumps(mode)+';document.getElementById("arrays-form").elements.input.value='+json.dumps(','.join(map(str,values)))+';document.getElementById("arrays-form").dispatchEvent(new Event("input"))')
            d=js('({...document.getElementById("arrays-output").dataset})');assert d['valid']=='true'
            states=json.loads(d['states']);last=states[-1]
            if mode=='prefix':assert last['prefix']==[sum(values[:i])for i in range(len(values)+1)]
            elif mode=='right':assert last['values']==values[:1]+values[:-1]
            elif mode=='bad':assert last['values']==[values[0]]*len(values)
            elif mode=='reverse':assert last['values']==values[::-1]
            elif mode=='difference':assert last['values']==values[:1]+[values[i]-values[i-1]for i in range(1,len(values))]
            elif mode=='compact':
                kept=[v for v in values if v%2==0];assert last['values'][:last['write']]==kept and last['write']==len(kept)
            assert states[0]['input']==values
            trace_checks+=len(states);report['labCases'].append({'mode':mode,'input':values,'steps':len(states)})
    report['independentTraceChecks']=trace_checks
    for value in ['',',','1,2,3,4,5,6,7','1.5','x','21','-21','1,,2']:
        js('document.getElementById("arrays-form").elements.input.value='+json.dumps(value)+';document.getElementById("arrays-form").dispatchEvent(new Event("input"))')
        assert js('document.getElementById("arrays-output").dataset.valid')=='false'
        assert js('document.getElementById("arrays-player").hidden')
    report['invalidInputsRejected']=8
    js('document.getElementById("arrays-form").elements.mode.value="prefix";document.getElementById("arrays-form").elements.input.value="2,4,6";document.getElementById("arrays-form").dispatchEvent(new Event("input"))')
    report['staticFigures']=js("[...document.querySelectorAll('.arrays-diagram svg')].map(s=>({issues:DiagramLayout.audit(s)}))")
    assert all(not x['issues']for x in report['staticFigures'])
'''
t=t[:a]+lab+t[z:]
a=t.index("    capture('[data-source-id=");z=t.index("    js('document.querySelectorAll(\"details.exam-solution\")",a)
t=t[:a]+'''    capture('[data-source-id="PA46"] .problem-visual','nested-sharing.png');capture('[data-source-id="PA31"]','overlap-proof.png');capture('[data-source-id="PA66"]','allocation-promotions.png');capture('[data-source-id="PA27"]','rectangle-prefix.png')
'''+t[z:]
t=t.replace('passed_gauss_current_revision_browser_checks','passed_arrays_current_revision_browser_checks')
exec(compile(t,str(R/'research/qa_arrays_current_revision.generated.py'),'exec'))

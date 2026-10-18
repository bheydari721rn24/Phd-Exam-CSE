"""Exercise actual functions inputs and all current question frames in Edge."""
from pathlib import Path
R=Path(__file__).resolve().parents[1]
t=(R/'research/qa_gauss_current_revision.py').read_text(encoding='utf8')
t=t.replace('Gaussian','Functions').replace('gauss-current','functions-current').replace('l_gauss.html','p_functions.html').replace('==71','==91').replace('==33','==27')
t=t.replace("p.scene.id==='gauss-swap'","p.scene.id==='fn-alias'")
a=t.index('    def mat(a):');z=t.index("    report['fonts']=",a)
lab=r'''
    report['labCases']=[];trace_checks=0
    for mode in ['copy','pointer','alias','static','nested']:
        for u in range(-20,21):
            js('document.getElementById("functions-form").elements.mode.value='+json.dumps(mode)+';document.getElementById("functions-form").elements.input.value='+json.dumps(str(u))+';document.getElementById("functions-form").dispatchEvent(new Event("input"))')
            d=js('({...document.getElementById("functions-output").dataset})');assert d['valid']=='true'
            states=json.loads(d['states']);last=states[-1]
            if mode=='copy':assert last['caller']==u and last['value']==2*(u+3)
            elif mode=='pointer':assert last['caller']==2*u+3 and last['shared']==2*u+3 and last['value']=='void'
            elif mode=='alias':assert [s['shared']for s in states]==[u,u+2,3*(u+2)]
            elif mode=='static':assert [s['shared']for s in states]==[0,u,u,u,2*u,2*u,2*u,3*u,3*u] and last['value']==10+3*u
            elif mode=='nested':assert last['value']==12*u+5 and last['caller']==u
            trace_checks+=len(states)
            report['labCases'].append({'mode':mode,'input':u,'last':last})
    report['independentTraceChecks']=trace_checks
    bad=['-21','21','1.5','abc','','+2',' 2']
    for value in bad:
        js('document.getElementById("functions-form").elements.input.value='+json.dumps(value)+';document.getElementById("functions-form").dispatchEvent(new Event("input"))')
        assert js('document.getElementById("functions-output").dataset.valid')=='false'
        assert js('document.getElementById("functions-player").hidden')
    report['invalidInputsRejected']=len(bad)
    js('document.getElementById("functions-form").elements.mode.value="copy";document.getElementById("functions-form").elements.input.value="4";document.getElementById("functions-form").dispatchEvent(new Event("input"))')
'''
t=t[:a]+lab+t[z:]
a=t.index("    capture('[data-source-id=");z=t.index("    js('document.querySelectorAll(\"details.exam-solution\")",a)
t=t[:a]+'''    capture('[data-source-id="PF65"] .problem-visual','mutation-and-rebinding.png');capture('[data-source-id="MS_CS_1393_Q167"] .problem-visual','reverse-stride.png');capture('[data-source-id="PF84"]','persistent-sum-solution.png')
'''+t[z:]
t=t.replace('passed_gauss_current_revision_browser_checks','passed_functions_current_revision_browser_checks')
exec(compile(t,str(R/'research/qa_functions_current_revision.generated.py'),'exec'))

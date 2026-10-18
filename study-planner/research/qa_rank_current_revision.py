"""Use the established local-browser harness for the current rank chapter."""
from pathlib import Path
R=Path(__file__).resolve().parents[1]
template=(R/'research/qa_gauss_current_revision.py').read_text(encoding='utf8')
template=template.replace('Gaussian','Rank').replace('gauss','rank').replace('==71','==90').replace('==33','==27')
a=template.index('    def mat(a):');z=template.index("    report['fonts']=",a)
lab=r'''
    def mat(a):return S.Matrix([[S.Rational(x)for x in row]for row in a])
    report['labCases']=[];trace_checks=0;rng=random.Random(1406)
    cases=[(k,None)for k in['pivot','tall','wide','zero','fractions','exceptional']]
    cases += [('shape-'+str(m)+'x'+str(n),[[rng.randint(-3,3)for _ in range(n)]for _ in range(m)])for m in range(1,6)for n in range(1,6)]
    for label,values in cases:
        if values is None:js('document.querySelector("[data-rank-preset='+label+']").click()')
        else:js('document.getElementById("rank-form").elements.matrix.value='+json.dumps('\n'.join(' '.join(map(str,row))for row in values))+';document.getElementById("rank-form").dispatchEvent(new Event("input"))')
        d=js('({...document.getElementById("rank-output").dataset})');assert d['valid']=='true',d
        A=mat(json.loads(d['input']));rr,piv=A.rref();rank=A.rank()
        assert int(d['rank'])==rank and json.loads(d['pivots'])==list(piv)and mat(json.loads(d['rref']))==rr
        for key,M,dimension in[('null',A,A.cols-rank),('left',A.T,A.rows-rank)]:
            vectors=[S.Matrix([S.Rational(x)for x in v])for v in json.loads(d[key])]
            assert len(vectors)==dimension and all(M*v==S.zeros(M.rows,1)for v in vectors)
            assert not vectors or S.Matrix.hstack(*vectors).rank()==dimension
        assert json.loads(d['column'])==[list(map(str,A[:,j]))for j in piv]
        assert json.loads(d['row'])==[list(map(str,rr.row(i)))for i in range(rank)]
        for f in json.loads(d['trace']):
            B=mat(f['a']);assert B.rref()[0]==rr;trace_checks+=1
        js('document.querySelector("[data-rank-step=next]").click()');assert js('document.getElementById("rank-output").dataset.step')=='1'
        js('document.querySelector("[data-rank-step=back]").click()');assert js('document.getElementById("rank-output").dataset.step')=='0'
        js('document.querySelector("[data-rank-step=next]").click();document.querySelector("[data-rank-step=reset]").click()');assert js('document.getElementById("rank-output").dataset.step')=='0'
        report['labCases'].append({'id':label,'rank':rank,'nullity':A.cols-rank,'leftNullity':A.rows-rank})
    report['independentTraceChecks']=trace_checks
    bad=['1 2\n1 2 3','1/0 2','abc 2','0.5 1','100001 2','1 2 3 4 5 6','1\n1\n1\n1\n1\n1','']
    for value in bad:
        js('document.getElementById("rank-form").elements.matrix.value='+json.dumps(value)+';document.getElementById("rank-form").dispatchEvent(new Event("input"))')
        assert js('document.getElementById("rank-output").dataset.valid')=='false'
    report['invalidInputsRejected']=len(bad);js('document.querySelector("[data-rank-preset=pivot]").click()')
'''
template=template[:a]+lab+template[z:]
template=template.replace("ConceptAnimations.players.find(p=>p.scene.id==='rank-swap')","ConceptAnimations.players.find(p=>p.scene.id==='rank-pivots')")
a=template.index("    capture('[data-source-id=")
z=template.index("    js('document.querySelectorAll(\"details.exam-solution\")",a)
template=template[:a]+'''    capture('[data-source-id="LR24"]','left-inverse-family.png');capture('[data-source-id="LR03"] .problem-visual','four-space-reduction.png');capture('[data-source-id="Phd_CS_1404_Q30"]','norm-bound-proof.png')
'''+template[z:]
exec(compile(template,str(R/'research/qa_rank_current_revision.generated.py'),'exec'))

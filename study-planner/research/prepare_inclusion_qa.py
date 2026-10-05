from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_d_counting_browser.py').read_text().replace('d-counting','d-inclusion').replace('d_counting','d_inclusion').replace('counting','inclusion')
s=s.replace("==88","==82").replace("==15","==13").replace("==76","==56").replace('dc-gaps','di-rooks').replace('dc-periodic','di-cancel').replace('Permutations, Combinations, and Counting','Inclusion-Exclusion: Overlap, Exact Multiplicity, and Forbidden Configurations')
start=s.index('    for mode,n,k,expected in ');end=s.index('    # Fonts and scripts remain separate',start)
tests=r'''    for mode,n,m,cap,expected in [('sets',4,3,2,19),('maps',5,3,2,150),('maps',0,0,2,1),('maps',0,3,2,0),('permutations',5,3,2,64),('permutations',4,4,2,9),('caps',8,4,3,31),('caps',5,3,2,3)]:
        row=js(f"""(()=>{{const f=document.querySelector('#inclusion-form');f.elements.mode.value='{mode}';f.elements.n.value={n};f.elements.m.value={m};f.elements.cap.value={cap};f.elements.mode.dispatchEvent(new Event('change'));return {{mode:'{mode}',n:{n},m:{m},cap:{cap},count:Number(document.querySelector('#inclusion-output').dataset.count)}};}})()""")
        assert row['count']==expected,row;report['lab'].append(row);capture('#inclusion-lab','lab-'+mode+'.png')
    js('document.querySelector("#inclusion-form").elements.mode.value="permutations";document.querySelector("#inclusion-form").elements.n.value=2;document.querySelector("#inclusion-form").elements.m.value=3;document.querySelector("#inclusion-form").dispatchEvent(new Event("submit",{cancelable:true}))')
    report['labInvalidInput']=js('document.querySelector("#inclusion-output").textContent');assert 'cannot exceed' in report['labInvalidInput']
    report['invalidCalls']=js("""(()=>{const cases=[['maps',9,3,2,[]],['maps',3,5,2,[]],['caps',4,0,2,[]],['caps',4,3,6,[]],['permutations',2,3,2,[]],['sets',0,0,0,[1,2]],['sets',0,0,0,Array(8).fill(-1)]];return cases.map(c=>{try{InclusionLab.evaluate(...c);return false}catch(e){return true}})})()""");assert all(report['invalidCalls'])
    # Independent Python references were serialized before browser execution.
    import json as _json
    references=_json.loads((ROOT/'research/d_inclusion-lab-reference.json').read_text())
    report['labReferenceChecks']=js("""(()=>{const rows="""+_json.dumps(references)+""";return rows.map(r=>{const z=InclusionLab.evaluate(r.mode,r.n,r.m,r.cap,r.atoms);return {mode:r.mode,n:r.n,m:r.m,cap:r.cap,actual:z.count,expected:r.count};});})()""")
    assert all(x['actual']==x['expected'] for x in report['labReferenceChecks'])
    js('document.querySelector(\'[data-inclusion-model="di-cancel"] [data-seek]\').value=1;document.querySelector(\'[data-inclusion-model="di-cancel"] [data-seek]\').dispatchEvent(new Event("input"))');time.sleep(.5)
    js('document.querySelector(\'[data-inclusion-model="di-cancel"] [data-next]\').click()');report['realMotion']=js('document.querySelector(\'[data-inclusion-model="di-cancel"] .inclusion-stage\').getAnimations({subtree:true}).length');assert report['realMotion']>0
'''
s=s[:start]+tests+s[end:]
s=s.replace("assert report['print']['opened'] and report['print']['restored'] and report['print']['checkpoints']==56","assert report['print']['opened'] and report['print']['restored'] and report['print']['checkpoints']==56")
(B/'qa_d_inclusion_browser.py').write_text(s)
print('Prepared actual-browser audit for the sole new chapter.')

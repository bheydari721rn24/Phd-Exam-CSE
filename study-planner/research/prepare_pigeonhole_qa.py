from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_d_inclusion_browser.py').read_text().replace('d-inclusion','d-pigeonhole').replace('d_inclusion','d_pigeonhole').replace('inclusion','pigeonhole').replace('==13','==18').replace('==56','==78').replace('di-cancel','dp-placement').replace('di-rooks','dp-ramsey').replace('#allocations','#subsequences').replace('Inclusion-Exclusion: Overlap, Exact Multiplicity, and Forbidden Configurations','The Pigeonhole Principle: Sharp Guarantees, Hidden Classes, and Constructive Witnesses')
start=s.index('    for mode,n,m,cap,expected in');end=s.index('    # Fonts and scripts remain separate',start)
tests=r'''    references=json.loads((ROOT/'research/d_pigeonhole-lab-reference.json').read_text())
    report['labReferenceChecks']=js("""(()=>{const rows="""+json.dumps(references)+""";return rows.map(r=>{const z=PigeonholeLab.evaluate(r.mode,r.values,r.m,r.n,r.mask);return {mode:r.mode,actual:z.count,expected:r.count,actualLds:z.lds,expectedLds:r.lds};});})()""")
    assert all(x['actual']==x['expected'] and x.get('actualLds')==x.get('expectedLds') for x in report['labReferenceChecks'])
    for mode,values,m,n,mask,expected in [('occupancy','4,4,3,3,3',5,6,0,21),('prefix','3,4,2,7,1',5,6,0,1),('sequence','5,1,4,2,3',5,6,0,3),('graph','',5,5,665,0),('graph','',5,6,0,20)]:
        row=js(f"""(()=>{{const f=document.querySelector('#pigeonhole-form');f.elements.mode.value='{mode}';f.elements.mode.dispatchEvent(new Event('change'));f.elements.values.value='{values}';f.elements.m.value={m};f.elements.n.value={n};f.elements.mask.value={mask};f.dispatchEvent(new Event('submit',{{cancelable:true}}));return {{mode:'{mode}',count:Number(document.querySelector('#pigeonhole-output').dataset.count)}};}})()""")
        assert row['count']==expected,row;report['lab'].append(row);capture('#pigeonhole-lab','lab-'+mode+'.png')
    report['invalidCalls']=js("""(()=>{const cases=[['occupancy',[-1],5,6,0],['occupancy',[41],5,6,0],['prefix',[1],0,6,0],['prefix',[1.5],5,6,0],['sequence',Array(10).fill(1),5,6,0],['graph',[],5,5,1024],['graph',[],5,4,0]];return cases.map(c=>{try{PigeonholeLab.evaluate(...c);return false}catch(e){return true}})})()""");assert all(report['invalidCalls'])
    report['parserInvalid']=js("""(()=>{try{PigeonholeLab.parseList('1,,3');return false}catch(e){return true}})()""");assert report['parserInvalid']
    js('document.querySelector(\'[data-pigeonhole-model="dp-placement"] [data-seek]\').value=1;document.querySelector(\'[data-pigeonhole-model="dp-placement"] [data-seek]\').dispatchEvent(new Event("input"))');time.sleep(.5)
    js('document.querySelector(\'[data-pigeonhole-model="dp-placement"] [data-next]\').click()');report['realMotion']=js('document.querySelector(\'[data-pigeonhole-model="dp-placement"] .pigeonhole-stage\').getAnimations({subtree:true}).length');assert report['realMotion']>0
'''
s=s[:start]+tests+s[end:]
(B/'qa_d_pigeonhole_browser.py').write_text(s,encoding='utf-8')
print('Prepared real browser chapter QA.')

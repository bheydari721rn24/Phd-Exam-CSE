from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'research/check_site_en.py';s=p.read_text(encoding='utf-8').replace("assert boolean['status'] == 'draft'","assert boolean['status'] == 'ready'");s=s.replace('"g_number", "g_boolean")','"g_number", "g_boolean", "g_gates")')
marker="vector_html = (ROOT / 'chapters/l_vectors.html').read_text"
if "assert gates['status']" not in s:s=s.replace(marker,"gates = next(c for w in lessons for c in w['chapters'] if c['topicId'] == 'g_gates')\nassert gates['status'] == 'draft' and gates['url'] == 'chapters/g_gates.html'\n"+marker)
p.write_text(s,encoding='utf-8')
p=ROOT/'research/g_boolean-review.en.md';s=p.read_text(encoding='utf-8').replace('This is a completed English **review draft** awaiting explicit student approval.','The student approved this English chapter on 2026-10-02.');p.write_text(s,encoding='utf-8')
p=ROOT/'research/qa_proof_browser.py';s=p.read_text(encoding='utf-8').replace('"g_number", "g_boolean"}', '"g_number", "g_boolean", "g_gates"}')
marker='    if CHAPTER == "g_boolean":'
branch='''    if CHAPTER == "g_gates":
        for kind,n,count in [('AND',3,0),('NAND',3,4),('NOR',3,4),('XOR',4,0),('XNOR',3,8),('XNOR',4,0)]:
            js=f"document.getElementById('gate-kind').value={json.dumps(kind)};document.getElementById('gate-count').value='{n}';document.getElementById('gate-kind').dispatchEvent(new Event('change'));JSON.stringify({{count:document.querySelectorAll('#gate-table tbody tr').length,mismatch:document.getElementById('gate-status').dataset.mismatches}})"
            r=json.loads(cdp('Runtime.evaluate',{'expression':js,'returnByValue':True})['result']['value']);assert r=={'count':2**n,'mismatch':str(count)},r
        for inv,direct,comp,last,width in [(3,1,1,2,3),(0,1,1,0,0),(1,5,1,2,0),(0,0,0,0,0),(20,0,20,20,40)]:
            values={'haz-inv':inv,'haz-direct':direct,'haz-comp':comp,'haz-or':last}
            js=';'.join(f"document.getElementById('{k}').value='{v}'" for k,v in values.items())+";document.getElementById('haz-inv').dispatchEvent(new Event('input'));JSON.stringify({...document.getElementById('haz-status').dataset})"
            r=json.loads(cdp('Runtime.evaluate',{'expression':js,'returnByValue':True})['result']['value']);assert r=={'valid':'true','width':str(width)},r
        for value in ['', '-1','21']:
            js=f"document.getElementById('haz-inv').value={json.dumps(value)};document.getElementById('haz-inv').dispatchEvent(new Event('input'));JSON.stringify({{valid:document.getElementById('haz-status').dataset.valid,events:document.querySelectorAll('#haz-events tbody tr').length,shape:document.querySelector('#haz-wave').children.length}})"
            r=json.loads(cdp('Runtime.evaluate',{'expression':js,'returnByValue':True})['result']['value']);assert r=={'valid':'false','events':0,'shape':0},r
        cdp('Runtime.evaluate',{'expression':"document.getElementById('haz-inv').value=3;document.getElementById('haz-direct').value=1;document.getElementById('haz-comp').value=1;document.getElementById('haz-or').value=2;document.getElementById('haz-inv').dispatchEvent(new Event('input'))"})
        info=json.loads(cdp('Runtime.evaluate',{'expression':"""JSON.stringify({code:getComputedStyle(document.querySelector('pre code')).fontFamily,math:getComputedStyle(document.querySelector('math')).fontFamily,diagram:getComputedStyle(document.querySelector('svg .math-label')).fontFamily,mono:document.fonts.check('16px \\"JetBrains Mono\\"'),stix:document.fonts.check('16px \\"STIX Two Math\\"'),problems:[...document.querySelectorAll('h3')].filter(x=>x.textContent.startsWith('Problem ')).length})""",'returnByValue':True})['result']['value'])
        assert 'JetBrains Mono' in info['code'] and 'STIX Two Math' in info['math'] and 'STIX Two Math' in info['diagram'] and info['mono'] and info['stix'] and info['problems']==36,info
        for name,selector in [('laboratory','.gates-lab'),('problems','#worked-problems'),('review','#quick-reference'),('code','pre'),('diagram','.gates-diagram')]:
            cdp('Runtime.evaluate',{'expression':f"document.querySelector('{selector}').scrollIntoView({{block:'start'}})"});time.sleep(.2)
            (OUT/f'{name}-mobile-cdp.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
        print('Gate lab UI, invalid delay clearing, and chapter font checks passed.',info)
'''
if 'if CHAPTER == "g_gates":' not in s:s=s.replace(marker,branch+marker)
p.write_text(s,encoding='utf-8')
print('Gates static and browser QA prepared.')

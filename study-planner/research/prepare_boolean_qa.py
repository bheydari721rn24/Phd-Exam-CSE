from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'research/qa_proof_browser.py';s=p.read_text(encoding='utf-8')
s=s.replace('"g_number"}', '"g_number", "g_boolean"}')
marker='    if CHAPTER == "a_model":'
assert marker in s
branch='''    if CHAPTER == "g_boolean":
        cases=[('x | y','x ^ y','x',False,False,True,False),('x & y','x & y','x',True,False,True,False),('!x & y','!x & y','x',True,False,False,True),('x ^ y','x ^ y','x',True,False,False,False),('x','x','z',True,True,True,True),('1','1','x',True,True,True,True),('(x & y) | (!x & z) | (y & z)','(x & y) | (!x & z)','x',True,False,False,False)]
        for first,second,var,equivalent,independent,positive,negative in cases:
            js=f"document.getElementById('bool-first').value={json.dumps(first)};document.getElementById('bool-second').value={json.dumps(second)};document.getElementById('bool-variable').value={json.dumps(var)};document.getElementById('bool-first').dispatchEvent(new Event('input'));JSON.stringify({{status:{{...document.getElementById('bool-status').dataset}},kind:{{...document.getElementById('bool-classification').dataset}},rows:document.querySelectorAll('#bool-table tbody tr').length,cof:document.querySelectorAll('#bool-cofactors tbody tr').length}})"
            r=json.loads(cdp('Runtime.evaluate',{'expression':js,'returnByValue':True})['result']['value'])
            assert r['status']['valid']=='true' and r['status']['equivalent']==str(equivalent).lower(),r
            assert r['kind']=={'independent':str(independent).lower(),'positive':str(positive).lower(),'negative':str(negative).lower()},r
            assert r['rows']==8 and r['cof']==4,r
        for bad in ['', 'xy', '(x', '2']:
            js=f"document.getElementById('bool-first').value={json.dumps(bad)};document.getElementById('bool-first').dispatchEvent(new Event('input'));JSON.stringify({{valid:document.getElementById('bool-status').dataset.valid,rows:document.querySelectorAll('#bool-table tbody tr').length,cof:document.querySelectorAll('#bool-cofactors tbody tr').length}})"
            r=json.loads(cdp('Runtime.evaluate',{'expression':js,'returnByValue':True})['result']['value']);assert r=={'valid':'false','rows':0,'cof':0},r
        cdp('Runtime.evaluate',{'expression':"document.getElementById('bool-example').click()"})
        info=json.loads(cdp('Runtime.evaluate',{'expression':"""JSON.stringify({code:getComputedStyle(document.querySelector('pre code')).fontFamily,math:getComputedStyle(document.querySelector('math')).fontFamily,mono:document.fonts.check('16px \\"JetBrains Mono\\"'),stix:document.fonts.check('16px \\"STIX Two Math\\"'),problems:[...document.querySelectorAll('h3')].filter(x=>x.textContent.startsWith('Problem ')).length})""",'returnByValue':True})['result']['value'])
        assert 'JetBrains Mono' in info['code'] and 'STIX Two Math' in info['math'] and info['mono'] and info['stix'] and info['problems']==40,info
        assert 'STIX Two Math' in cdp('Runtime.evaluate',{'expression':"getComputedStyle(document.querySelector('svg .math-label')).fontFamily",'returnByValue':True})['result']['value']
        for name,selector in [('laboratory','.boolean-lab'),('problems','#worked-problems'),('review','#quick-reference'),('code','pre'),('diagram','.boolean-diagram')]:
            cdp('Runtime.evaluate',{'expression':f"document.querySelector('{selector}').scrollIntoView({{block:'start'}})"})
            time.sleep(.2)
            (OUT/f'{name}-mobile-cdp.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
        print('Boolean lab: seven valid cases, four invalid cases, example button, math/code fonts, and forty problems passed.',info)
'''
if 'if CHAPTER == "g_boolean":' not in s:s=s.replace(marker,branch+marker)
p.write_text(s,encoding='utf-8')
print('Browser QA extended for the Boolean chapter.')

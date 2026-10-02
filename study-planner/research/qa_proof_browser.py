"""Serve the static site and capture mobile/A4 QA with Edge DevTools."""

from __future__ import annotations

import base64
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import time

import requests
import websocket


ROOT = Path(__file__).resolve().parents[1]
EDGE = Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
CHAPTER = sys.argv[1] if len(sys.argv) > 1 else "d_proof"
assert CHAPTER in {"d_logic", "d_sets", "d_proof", "d_induction", "a_model", "a_asym", "a_loop", "s_axioms", "s_counting", "l_vectors", "l_matrices", "p_types", "p_flow", "g_number", "g_boolean"}
OUT = Path(tempfile.gettempdir()) / f"{CHAPTER}_qa"
OUT.mkdir(exist_ok=True)
server = ThreadingHTTPServer(("127.0.0.1", 0), partial(SimpleHTTPRequestHandler, directory=str(ROOT / "dist")))
threading.Thread(target=server.serve_forever, daemon=True).start()
profile = OUT / f"edge-cdp-{os.getpid()}"
process = subprocess.Popen([
    str(EDGE), "--headless=new", "--disable-gpu", "--no-first-run",
    "--remote-allow-origins=*", "--remote-debugging-port=0",
    f"--user-data-dir={profile}", "about:blank",
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

try:
    active = profile / "DevToolsActivePort"
    for _ in range(100):
        if active.is_file():
            break
        time.sleep(.1)
    assert active.is_file(), "Edge did not expose DevTools."
    port = int(active.read_text().splitlines()[0])
    pages = requests.get(f"http://127.0.0.1:{port}/json", timeout=5).json()
    page = next(item for item in pages if item["type"] == "page")
    ws = websocket.create_connection(page["webSocketDebuggerUrl"], timeout=20)
    seq = 0

    def cdp(method: str, params: dict | None = None) -> dict:
        global seq
        seq += 1
        ws.send(json.dumps({"id": seq, "method": method, "params": params or {}}))
        while True:
            response = json.loads(ws.recv())
            if response.get("id") == seq:
                assert "error" not in response, response
                return response.get("result", {})

    cdp("Page.enable")
    cdp("Emulation.setDeviceMetricsOverride", {
        "width": 390, "height": 844, "deviceScaleFactor": 1, "mobile": True,
    })
    cdp("Page.navigate", {"url": f"http://127.0.0.1:{server.server_port}/chapters/{CHAPTER}.html"})
    time.sleep(1.5)
    metrics = cdp("Runtime.evaluate", {"expression": """JSON.stringify({width:innerWidth,scroll:document.documentElement.scrollWidth,fontReady:document.fonts.status,bodyFont:getComputedStyle(document.body).fontFamily,headingFont:getComputedStyle(document.querySelector('.hero h1')).fontFamily,mathFont:getComputedStyle(document.querySelector('.formula-block')).fontFamily,formulaOverflow:Math.max(...[...document.querySelectorAll('.formula-block')].map(x=>x.scrollWidth-x.clientWidth)),problems:document.querySelectorAll('h3').length})""", "returnByValue": True})["result"]["value"]
    print(metrics)
    parsed = json.loads(metrics)
    if parsed["scroll"] > 390:
        offenders = cdp("Runtime.evaluate", {"expression": "JSON.stringify([...document.querySelectorAll('*')].filter(x=>x.getBoundingClientRect().right>392).slice(0,35).map(x=>({tag:x.tagName,cls:x.className?.baseVal??x.className,text:x.textContent.slice(0,90),right:Math.round(x.getBoundingClientRect().right)})))", "returnByValue": True})["result"]["value"]
        print(offenders.encode("ascii", "backslashreplace").decode("ascii"))
    if CHAPTER in {"a_model", "s_axioms", "s_counting", "l_vectors", "l_matrices", "p_types", "p_flow", "g_number", "g_boolean"}:
        overflow_items = cdp("Runtime.evaluate", {"expression": "JSON.stringify([...document.querySelectorAll('.formula-block')].filter(x=>x.scrollWidth>x.clientWidth).map(x=>({extra:x.scrollWidth-x.clientWidth,text:x.textContent.slice(0,110)})))", "returnByValue": True})["result"]["value"]
        print(overflow_items.encode("ascii", "backslashreplace").decode("ascii"))
    assert parsed["width"] == 390 and parsed["scroll"] == 390, "Mobile horizontal overflow."
    if CHAPTER in {"d_induction", "a_model", "a_asym", "a_loop", "s_axioms", "s_counting", "l_vectors", "l_matrices", "p_types", "p_flow", "g_number", "g_boolean"}:
        assert parsed["formulaOverflow"] == 0, "A mathematical display is clipped on mobile."
    shot = cdp("Page.captureScreenshot", {"format": "png", "captureBeyondViewport": False})["data"]
    (OUT / "mobile-cdp.png").write_bytes(base64.b64decode(shot))
    if CHAPTER in {"d_logic", "d_sets", "d_proof", "d_induction", "a_model", "a_asym", "a_loop", "s_axioms", "s_counting", "l_vectors", "l_matrices", "p_types", "p_flow", "g_number", "g_boolean"}:
        cdp("Runtime.evaluate", {"expression": "document.querySelector('math, .math-limits, .math-inline').scrollIntoView({block:'center'})" if CHAPTER not in {"s_counting", "l_vectors", "l_matrices", "p_types", "p_flow", "g_number", "g_boolean"} else "document.querySelector('math').scrollIntoView({block:'center'})"})
        time.sleep(.25)
        math_shot = cdp("Page.captureScreenshot", {"format": "png", "captureBeyondViewport": False})["data"]
        (OUT / "math-mobile-cdp.png").write_bytes(base64.b64decode(math_shot))
    if CHAPTER == "g_boolean":
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
        info=json.loads(cdp('Runtime.evaluate',{'expression':"""JSON.stringify({code:getComputedStyle(document.querySelector('pre code')).fontFamily,math:getComputedStyle(document.querySelector('math')).fontFamily,mono:document.fonts.check('16px \"JetBrains Mono\"'),stix:document.fonts.check('16px \"STIX Two Math\"'),problems:[...document.querySelectorAll('h3')].filter(x=>x.textContent.startsWith('Problem ')).length})""",'returnByValue':True})['result']['value'])
        assert 'JetBrains Mono' in info['code'] and 'STIX Two Math' in info['math'] and info['mono'] and info['stix'] and info['problems']==40,info
        assert 'STIX Two Math' in cdp('Runtime.evaluate',{'expression':"getComputedStyle(document.querySelector('svg .math-label')).fontFamily",'returnByValue':True})['result']['value']
        for name,selector in [('laboratory','.boolean-lab'),('problems','#worked-problems'),('review','#quick-reference'),('code','pre'),('diagram','.boolean-diagram')]:
            cdp('Runtime.evaluate',{'expression':f"document.querySelector('{selector}').scrollIntoView({{block:'start'}})"})
            time.sleep(.2)
            (OUT/f'{name}-mobile-cdp.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
        print('Boolean lab: seven valid cases, four invalid cases, example button, math/code fonts, and forty problems passed.',info)
    if CHAPTER == "a_model":
        diagram = cdp("Runtime.evaluate", {"expression": "JSON.stringify({container:document.querySelector('.model-diagram').clientWidth,content:document.querySelector('.model-diagram svg').clientWidth})", "returnByValue": True})["result"]["value"]
        print(diagram)
        assert json.loads(diagram)["content"] >= 700
        cdp("Runtime.evaluate", {"expression": "document.querySelector('.model-diagram').scrollIntoView({block:'center'})"})
        time.sleep(.25)
        diagram_shot = cdp("Page.captureScreenshot", {"format": "png", "captureBeyondViewport": False})["data"]
        (OUT / "diagram-mobile-cdp.png").write_bytes(base64.b64decode(diagram_shot))
    if CHAPTER == "s_axioms":
        expr = "JSON.stringify({valid:document.querySelector('#lab-result').dataset.valid,text:document.querySelector('#lab-result').textContent,cells:[...document.querySelectorAll('.lab-region .lab-math')].map(x=>x.textContent)})"
        lab = json.loads(cdp("Runtime.evaluate", {"expression": expr, "returnByValue": True})["result"]["value"])
        assert lab["valid"] == "true" and lab["cells"] == ["25%", "40%", "20%", "15%"], lab
        cdp("Runtime.evaluate", {"expression": "document.querySelector('#pq').value=5;document.querySelector('#pq').dispatchEvent(new Event('input'))"})
        lab = json.loads(cdp("Runtime.evaluate", {"expression": expr, "returnByValue": True})["result"]["value"])
        assert lab["valid"] == "false" and "negative mass of -5%" in lab["text"] and not lab["cells"], lab
        cdp("Runtime.evaluate", {"expression": "document.querySelector('#pq').value=25;document.querySelector('#pq').dispatchEvent(new Event('input'));document.querySelector('.probability-lab').scrollIntoView({block:'start'})"})
        time.sleep(.25)
        lab_shot = cdp("Page.captureScreenshot", {"format": "png", "captureBeyondViewport": False})["data"]
        (OUT / "laboratory-mobile-cdp.png").write_bytes(base64.b64decode(lab_shot))
        assert cdp("Runtime.evaluate", {"expression": "[...document.querySelectorAll('h3')].filter(x=>x.textContent.startsWith('Problem ')).length", "returnByValue": True})["result"]["value"] == 24
        print("Probability laboratory: valid initial law and invalid-overlap rejection passed.")
    if CHAPTER == "s_counting":
        expr = "JSON.stringify({mutual:document.querySelector('#parity-result').dataset.mutual,masses:[...document.querySelectorAll('#parity-masses tr')].map(x=>Number(x.dataset.mass)),text:document.querySelector('#parity-result').textContent})"
        for parameter in (100, 0, -100, 50):
            cdp("Runtime.evaluate", {"expression": f"document.querySelector('#parity').value={parameter};document.querySelector('#parity').dispatchEvent(new Event('input'))"})
            lab = json.loads(cdp("Runtime.evaluate", {"expression": expr, "returnByValue": True})["result"]["value"])
            assert lab["mutual"] == str(parameter == 0).lower(), lab
            assert len(lab["masses"]) == 8 and sum(lab["masses"]) == 1 and min(lab["masses"]) >= 0, lab
            for i in range(3):
                assert sum(p for k, p in enumerate(lab["masses"]) if (k >> i) & 1) == .5, lab
            for i, j in ((0, 1), (0, 2), (1, 2)):
                assert sum(p for k, p in enumerate(lab["masses"]) if ((k >> i)&1) and ((k >> j)&1)) == .25, lab
            assert lab["masses"][7] == (1-parameter/100)/8, lab
        cdp("Runtime.evaluate", {"expression": "document.querySelector('#parity').value=100;document.querySelector('#parity').dispatchEvent(new Event('input'));document.querySelector('.independence-lab').scrollIntoView({block:'start'})"})
        time.sleep(.25)
        lab_shot = cdp("Page.captureScreenshot", {"format": "png", "captureBeyondViewport": False})["data"]
        (OUT / "laboratory-mobile-cdp.png").write_bytes(base64.b64decode(lab_shot))
        assert cdp("Runtime.evaluate", {"expression": "[...document.querySelectorAll('h3')].filter(x=>x.textContent.startsWith('Problem ')).length", "returnByValue": True})["result"]["value"] == 34
        print("Independence laboratory: four parameter states, normalization, all marginals and pair joints, triple probability, and 34 problems passed.")
    if CHAPTER == 'g_number':
        cases=[(4,7,1,'add',8,-8,0,True),(4,15,1,'add',0,0,1,False),(4,8,8,'add',0,0,1,True),(4,7,8,'sub',15,-1,0,True),(4,0,0,'sub',0,0,1,False),(4,8,15,'sub',9,-7,0,False),(8,100,60,'add',160,-96,0,True),(16,65535,1,'add',0,0,1,False),(16,32767,1,'add',32768,-32768,0,True)]
        for n,a,b,op,word,signed,carry,overflow in cases:
            expression=f"document.getElementById('number-width').value={n};document.getElementById('number-a').value={a};document.getElementById('number-b').value={b};document.getElementById('number-operation').value='{op}';document.getElementById('number-operation').dispatchEvent(new Event('input'));JSON.stringify({{...document.getElementById('number-result').dataset}})"
            state=json.loads(cdp('Runtime.evaluate',{'expression':expression,'returnByValue':True})['result']['value'])
            assert state['valid']=='true' and int(state['word'])==word and int(state['signed'])==signed and int(state['carry'])==carry and state['overflow']==str(overflow).lower(),state
        for bad in ('', '-1', '1.5', '65536'):
            cdp('Runtime.evaluate',{'expression':f"document.getElementById('number-a').value='{bad}';document.getElementById('number-a').dispatchEvent(new Event('input'))"})
            assert cdp('Runtime.evaluate',{'expression':"document.getElementById('number-result').dataset.valid",'returnByValue':True})['result']['value']=='false'
        cdp('Runtime.evaluate',{'expression':"document.getElementById('number-width').value=4;document.getElementById('number-a').value=7;document.getElementById('number-b').value=1;document.getElementById('number-operation').value='add';document.getElementById('number-operation').dispatchEvent(new Event('input'))"})
        info=json.loads(cdp('Runtime.evaluate',{'expression':"JSON.stringify({math:getComputedStyle(document.querySelector('math')).fontFamily,code:getComputedStyle(document.querySelector('pre code')).fontFamily,diagram:getComputedStyle(document.querySelector('svg .math-label')).fontFamily,index:getComputedStyle(document.querySelector('sub')).fontFamily,underline:[...document.querySelectorAll('a')].some(x=>getComputedStyle(x).textDecorationLine.includes('underline')),problems:[...document.querySelectorAll('h3')].filter(x=>x.textContent.startsWith('Problem ')).length})",'returnByValue':True})['result']['value'])
        assert all('STIX Two Math' in info[k] for k in ('math','diagram','index')) and 'JetBrains Mono' in info['code'] and not info['underline'] and info['problems']==36,info
        font_loaded=cdp('Runtime.evaluate',{'expression':'''document.fonts.check('16px "JetBrains Mono"') && document.fonts.check('16px "STIX Two Math"')''','returnByValue':True})['result']['value']
        assert font_loaded, 'A bundled mathematical or code face did not load.'
        for name,selector in [('laboratory','.number-lab'),('problems','#worked-problems'),('review','#quick-reference'),('diagram','.number-diagram'),('gray','#gray'),('codes','#decimal')]:
            cdp('Runtime.evaluate',{'expression':f"document.querySelector('{selector}').scrollIntoView({{block:'start'}})"})
            time.sleep(.15)
            (OUT/f'{name}-mobile-cdp.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
        print('Number laboratory: nine arithmetic states, four invalid inputs, math/code/index/diagram fonts, links and 36 solutions passed.',info)
    if CHAPTER == 'p_flow':
        cases=[('for',5,0,'normal',5,4,6,5,5),('while',5,0,'normal',5,10,6,5,5),('do',0,0,'normal',1,0,1,1,1),('do',0,2,'normal',3,2,1,1,1),('bug',5,0,'cycle',0,0,1,1,0),('bug',5,1,'cycle',2,1,2,2,1),('break',8,0,'break',3,3,4,4,3),('break',3,0,'normal',3,3,4,3,3),('for',0,0,'normal',0,0,1,0,0),('for',4,6,'normal',6,0,1,0,0)]
        for mode,n,a,status,i,total,tests,entries,updates in cases:
            js=f"document.getElementById('flow-case').value='{mode}';document.getElementById('flow-limit').value={n};document.getElementById('flow-start').value={a};document.getElementById('flow-case').dispatchEvent(new Event('input'));document.getElementById('flow-end').click();JSON.stringify({{...document.getElementById('flow-state').dataset}})"
            state=json.loads(cdp('Runtime.evaluate',{'expression':js,'returnByValue':True})['result']['value'])
            assert state['status']==status and int(state['i'])==i and int(state['sum'])==total and int(state['tests'])==tests and int(state['entries'])==entries and int(state['updates'])==updates,state
        cdp('Runtime.evaluate',{'expression':"document.getElementById('flow-limit').value='';document.getElementById('flow-limit').dispatchEvent(new Event('input'))"})
        assert cdp('Runtime.evaluate',{'expression':"document.getElementById('flow-state').dataset.status",'returnByValue':True})['result']['value']=='invalid'
        cdp('Runtime.evaluate',{'expression':"document.getElementById('flow-case').value='for';document.getElementById('flow-limit').value=5;document.getElementById('flow-start').value=0;document.getElementById('flow-case').dispatchEvent(new Event('input'));document.getElementById('flow-next').click();document.getElementById('flow-prev').click()"})
        assert cdp('Runtime.evaluate',{'expression':"document.getElementById('flow-state').dataset.position",'returnByValue':True})['result']['value']=='0'
        info=json.loads(cdp('Runtime.evaluate',{'expression':"""JSON.stringify({code:getComputedStyle(document.querySelector('pre code')).fontFamily,math:getComputedStyle(document.querySelector('math')).fontFamily,mono:document.fonts.check('16px \"JetBrains Mono\"'),stix:document.fonts.check('16px \"STIX Two Math\"'),problems:[...document.querySelectorAll('h3')].filter(x=>x.textContent.startsWith('Problem ')).length})""",'returnByValue':True})['result']['value'])
        assert 'JetBrains Mono' in info['code'] and 'STIX Two Math' in info['math'] and info['mono'] and info['stix'] and info['problems']==36,info
        diagram_font=cdp('Runtime.evaluate',{'expression':"getComputedStyle(document.querySelector('svg .math-label')).fontFamily",'returnByValue':True})['result']['value']
        assert 'STIX Two Math' in diagram_font,diagram_font
        for name,selector in [('laboratory','.flow-lab'),('problems','#worked-problems'),('review','#quick-reference'),('code','pre'),('diagram','.flow-diagram')]:
            cdp('Runtime.evaluate',{'expression':f"document.querySelector('{selector}').scrollIntoView({{block:'start'}})"})
            time.sleep(.2)
            (OUT/f'{name}-mobile-cdp.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
        cdp('Runtime.evaluate',{'expression':"document.getElementById('flow-end').click()"})
        print('Flow laboratory: ten terminal states, invalid input, forward/back navigation, code/math fonts and 36 problems passed.',info)
    if CHAPTER == "p_types":
        cases=[('store',250,10,True,'4'),('store',255,255,True,'254'),('store',-1,10,False,''),('divide',-17,5,True,'-3'),('divide',17,-5,True,'-3'),('divide',8,0,False,''),('cast',9,4,True,'2'),('compare',-3,2,True,'0'),('guard',8,0,True,'0'),('guard',-2147483648,-1,False,''),('guard',8,-2,True,'0')]
        for mode,a,b,valid,value in cases:
            js=f"document.getElementById('type-case').value='{mode}';document.getElementById('type-a').value='{a}';document.getElementById('type-b').value='{b}';document.getElementById('type-case').dispatchEvent(new Event('input'));JSON.stringify({{valid:document.getElementById('type-result').dataset.valid,value:document.getElementById('type-result').dataset.value,text:document.getElementById('type-result').textContent}})"
            state=json.loads(cdp('Runtime.evaluate',{'expression':js,'returnByValue':True})['result']['value'])
            assert state['valid']==str(valid).lower() and state['value']==value,state
        cdp('Runtime.evaluate',{'expression':"document.getElementById('type-case').value='store';document.getElementById('type-a').value=250;document.getElementById('type-b').value=10;document.getElementById('type-case').dispatchEvent(new Event('input'))"})
        font_info=json.loads(cdp('Runtime.evaluate',{'expression':'''JSON.stringify({code:getComputedStyle(document.querySelector('pre code')).fontFamily,math:getComputedStyle(document.querySelector('math')).fontFamily,mono:document.fonts.check('16px "JetBrains Mono"'),stix:document.fonts.check('16px "STIX Two Math"'),problems:[...document.querySelectorAll('h3')].filter(x=>x.textContent.startsWith('Problem ')).length})''','returnByValue':True})['result']['value'])
        assert 'JetBrains Mono' in font_info['code'] and font_info['mono'] and font_info['stix'] and font_info['problems']==36,font_info
        for name,selector in [('laboratory','.types-lab'),('problems','#worked-problems'),('review','#quick-reference'),('code','pre')]:
            cdp('Runtime.evaluate',{'expression':f"document.querySelector('{selector}').scrollIntoView({{block:'start'}})"})
            time.sleep(.2)
            (OUT/f'{name}-mobile-cdp.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
        print('Typed-expression lab: eleven states, zero-divisor and minimum-quotient rejection, separate code/math fonts and 36 solutions passed.',font_info)
    if CHAPTER == "l_matrices":
        from math import sin, pi
        expression = "JSON.stringify({...document.querySelector('#matrix-result').dataset,text:document.querySelector('#matrix-result').textContent})"
        for angle, shear, x, y in ((90,100,100,100),(0,100,100,100),(180,100,100,100),(45,0,100,100),(-30,-150,-75,125),(90,100,0,0),(90,-200,150,-150),(146,75,100,0)):
            cdp("Runtime.evaluate", {"expression": f"document.querySelector('#matrix-angle').value={angle};document.querySelector('#matrix-shear').value={shear};document.querySelector('#matrix-x').value={x};document.querySelector('#matrix-y').value={y};document.querySelector('#matrix-angle').dispatchEvent(new Event('input'))"})
            lab = json.loads(cdp("Runtime.evaluate", {"expression":expression,"returnByValue":True})['result']['value'])
            expected=(shear/100*sin(angle*pi/180))**2*((x/100)**2+(y/100)**2)
            assert abs(float(lab['gap'])-expected)<1e-10,lab
            assert lab['commute']==str(shear==0 or angle in (0,180,-180)).lower(),lab
            first,second=json.loads(lab['first']),json.loads(lab['second'])
            assert abs(sum((a-b)**2 for a,b in zip(first,second))-expected)<1e-10,lab
            if angle==90 and shear==100 and x==y==100:
                assert all(abs(a-b)<1e-10 for a,b in zip(first,[-1,2])),lab
                assert all(abs(a-b)<1e-10 for a,b in zip(second,[0,1])),lab
        cdp("Runtime.evaluate", {"expression":"document.querySelector('#matrix-angle').value=90;document.querySelector('#matrix-shear').value=100;document.querySelector('#matrix-x').value=100;document.querySelector('#matrix-y').value=100;document.querySelector('#matrix-angle').dispatchEvent(new Event('input'))"})
        for name,selector in [('laboratory','.matrix-lab'),('problems','#worked-problems'),('review','#quick-reference'),('arrays','#blocks'),('code','#computation')]:
            cdp("Runtime.evaluate", {"expression":f"document.querySelector('{selector}').scrollIntoView({{block:'start'}})"})
            time.sleep(.15)
            (OUT/f'{name}-mobile-cdp.png').write_bytes(base64.b64decode(cdp('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})['data']))
        font_info=json.loads(cdp('Runtime.evaluate',{'expression':"JSON.stringify({math:getComputedStyle(document.querySelector('math')).fontFamily,cell:getComputedStyle(document.querySelector('mtd')).fontFamily,code:getComputedStyle(document.querySelector('pre')).fontFamily,arrays:document.querySelectorAll('mtable').length})",'returnByValue':True})['result']['value'])
        assert 'STIX Two Math' in font_info['math'] and 'STIX Two Math' in font_info['cell'],font_info
        assert font_info['arrays']>=70,font_info
        assert cdp('Runtime.evaluate',{'expression':"[...document.querySelectorAll('h3')].filter(x=>x.textContent.startsWith('Problem ')).length",'returnByValue':True})['result']['value']==36
        print('Matrix laboratory: eight states, both action orders, commutator identity, zero input, fonts and 36 solutions passed.',font_info)
    if CHAPTER == "l_vectors":
        expression = "JSON.stringify({...document.querySelector('#vector-result').dataset,text:document.querySelector('#vector-result').textContent})"
        for orientation, size, coefficient in ((0,100,300),(90,100,200),(180,100,-300),(30,50,150),(146,100,0),(30,0,500)):
            cdp("Runtime.evaluate", {"expression": f"document.querySelector('#vector-angle').value={orientation};document.querySelector('#vector-length').value={size};document.querySelector('#vector-candidate').value={coefficient};document.querySelector('#vector-angle').dispatchEvent(new Event('input'))"})
            lab = json.loads(cdp("Runtime.evaluate", {"expression": expression, "returnByValue": True})["result"]["value"])
            assert abs(float(lab['orthogonality'])) < 1e-10, lab
            assert abs(float(lab['actual'])-float(lab['minimum'])-float(lab['excess'])) < 1e-10, lab
            if size == 0:
                assert lab['valid'] == 'false' and float(lab['minimum']) == 13 and 'undefined' in lab['text'], lab
            if orientation in (0,90,180) and size:
                assert abs(float(lab['excess'])) < 1e-10, lab
        cdp("Runtime.evaluate", {"expression": "document.querySelector('#vector-angle').value=60;document.querySelector('#vector-length').value=100;document.querySelector('#vector-candidate').value=0;document.querySelector('#vector-angle').dispatchEvent(new Event('input'));document.querySelector('.vector-lab').scrollIntoView({block:'start'})"})
        time.sleep(.25)
        (OUT / "laboratory-mobile-cdp.png").write_bytes(base64.b64decode(cdp("Page.captureScreenshot", {"format":"png", "captureBeyondViewport":False})['data']))
        assert cdp("Runtime.evaluate", {"expression": "[...document.querySelectorAll('h3')].filter(x=>x.textContent.startsWith('Problem ')).length", "returnByValue":True})['result']['value'] == 34
        cdp("Runtime.evaluate", {"expression": "document.getElementById('worked-problems').scrollIntoView({block:'start'})"})
        (OUT / "problems-mobile-cdp.png").write_bytes(base64.b64decode(cdp("Page.captureScreenshot", {"format":"png", "captureBeyondViewport":False})['data']))
        cdp("Runtime.evaluate", {"expression": "document.getElementById('quick-reference').scrollIntoView({block:'start'})"})
        (OUT / "review-mobile-cdp.png").write_bytes(base64.b64decode(cdp("Page.captureScreenshot", {"format":"png", "captureBeyondViewport":False})['data']))
        print("Projection lab: six states including zero direction; residual orthogonality, minimum-plus-excess identity, and 34 worked problems passed.")
    cdp("Emulation.clearDeviceMetricsOverride")
    cdp("Emulation.setDeviceMetricsOverride", {
        "width": 1280, "height": 900, "deviceScaleFactor": 1, "mobile": False,
    })
    time.sleep(.5)
    cdp("Emulation.setEmulatedMedia", {"media": "print"})
    document = cdp("Page.printToPDF", {"printBackground": True, "preferCSSPageSize": True})["data"]
    (OUT / "print-cdp.pdf").write_bytes(base64.b64decode(document))
    cdp("Emulation.setEmulatedMedia", {"media": "screen"})
    cdp("Page.navigate", {"url": f"http://127.0.0.1:{server.server_port}/index.html#library"})
    time.sleep(1.0)
    library = cdp("Runtime.evaluate", {"expression": f"""JSON.stringify({{chapter:!!document.querySelector('a[href="chapters/{CHAPTER}.html"]'),setsReady:document.getElementById('library')?.textContent.includes('Sets and set operations')}})""", "returnByValue": True})["result"]["value"]
    print(library)
    assert json.loads(library)["chapter"] and json.loads(library)["setsReady"]
    if CHAPTER == 'p_types':
        title=cdp('Runtime.evaluate',{'expression':'''document.querySelector('#library article a[href="chapters/p_types.html"]').closest('article').querySelector('h3').textContent''','returnByValue':True})['result']['value']
        assert title == 'Data types, conversions, and operators',title
        print('New chapter library card has its complete title.')
    if CHAPTER == 'p_flow':
        title=cdp('Runtime.evaluate',{'expression':f"document.querySelector('#library article a[href={chr(34)}chapters/p_flow.html{chr(34)}]').closest('article').querySelector('h3').textContent",'returnByValue':True})['result']['value']
        assert title == 'Conditionals, loops, execution order',title
        print('Complete flow chapter title visible in library.')
    if CHAPTER == 'g_number':
        title=cdp('Runtime.evaluate',{'expression':f"document.querySelector('#library article a[href={chr(34)}chapters/g_number.html{chr(34)}]').closest('article').querySelector('h3').textContent",'returnByValue':True})['result']['value']
        assert title == 'Number bases and binary encoding',title
        print('Complete number chapter title visible in library.')
    ws.close()
finally:
    process.terminate()
    try:
        process.wait(timeout=8)
    except subprocess.TimeoutExpired:
        process.kill()
    server.shutdown()

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
assert CHAPTER in {"d_logic", "d_sets", "d_proof", "d_induction", "a_model", "a_asym", "a_loop", "s_axioms"}
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
    if CHAPTER in {"a_model", "s_axioms"}:
        overflow_items = cdp("Runtime.evaluate", {"expression": "JSON.stringify([...document.querySelectorAll('.formula-block')].filter(x=>x.scrollWidth>x.clientWidth).map(x=>({extra:x.scrollWidth-x.clientWidth,text:x.textContent.slice(0,110)})))", "returnByValue": True})["result"]["value"]
        print(overflow_items.encode("ascii", "backslashreplace").decode("ascii"))
    assert parsed["width"] == 390 and parsed["scroll"] == 390, "Mobile horizontal overflow."
    if CHAPTER in {"d_induction", "a_model", "a_asym", "a_loop", "s_axioms"}:
        assert parsed["formulaOverflow"] == 0, "A mathematical display is clipped on mobile."
    shot = cdp("Page.captureScreenshot", {"format": "png", "captureBeyondViewport": False})["data"]
    (OUT / "mobile-cdp.png").write_bytes(base64.b64decode(shot))
    if CHAPTER in {"d_logic", "d_sets", "d_proof", "d_induction", "a_model", "a_asym", "a_loop", "s_axioms"}:
        cdp("Runtime.evaluate", {"expression": "document.querySelector('.math-limits, .math-inline').scrollIntoView({block:'center'})"})
        time.sleep(.25)
        math_shot = cdp("Page.captureScreenshot", {"format": "png", "captureBeyondViewport": False})["data"]
        (OUT / "math-mobile-cdp.png").write_bytes(base64.b64decode(math_shot))
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
    ws.close()
finally:
    process.terminate()
    try:
        process.wait(timeout=8)
    except subprocess.TimeoutExpired:
        process.kill()
    server.shutdown()

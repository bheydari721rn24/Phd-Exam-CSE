"""Serve the static site and capture mobile/A4 QA with Edge DevTools."""

from __future__ import annotations

import base64
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import subprocess
import tempfile
import threading
import time

import requests
import websocket


ROOT = Path(__file__).resolve().parents[1]
EDGE = Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
OUT = Path(tempfile.gettempdir()) / "d_proof_qa"
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
    cdp("Page.navigate", {"url": f"http://127.0.0.1:{server.server_port}/chapters/d_proof.html"})
    time.sleep(1.5)
    metrics = cdp("Runtime.evaluate", {"expression": """JSON.stringify({width:innerWidth,scroll:document.documentElement.scrollWidth,fontReady:document.fonts.status,bodyFont:getComputedStyle(document.body).fontFamily,headingFont:getComputedStyle(document.querySelector('.hero h1')).fontFamily,mathFont:getComputedStyle(document.querySelector('.formula-block')).fontFamily,problems:document.querySelectorAll('h3').length})""", "returnByValue": True})["result"]["value"]
    print(metrics)
    parsed = json.loads(metrics)
    assert parsed["width"] == 390 and parsed["scroll"] == 390, "Mobile horizontal overflow."
    shot = cdp("Page.captureScreenshot", {"format": "png", "captureBeyondViewport": False})["data"]
    (OUT / "mobile-cdp.png").write_bytes(base64.b64decode(shot))
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
    library = cdp("Runtime.evaluate", {"expression": """JSON.stringify({proof:!!document.querySelector('a[href="chapters/d_proof.html"]'),setsReady:document.getElementById('library')?.textContent.includes('Sets and set operations')})""", "returnByValue": True})["result"]["value"]
    print(library)
    assert json.loads(library)["proof"] and json.loads(library)["setsReady"]
    ws.close()
finally:
    process.terminate()
    try:
        process.wait(timeout=8)
    except subprocess.TimeoutExpired:
        process.kill()
    server.shutdown()

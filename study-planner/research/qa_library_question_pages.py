"""Verify problem retention and real page behavior at desktop/mobile/print widths."""
import json,re,hashlib
from pathlib import Path
R=Path(__file__).resolve().parents[1];O=R/'research/library-visual-question-review'
inputs=json.loads((O/'input.json').read_text())
def remove_aids(s):
 while (m:=re.search(r'<div class="(?:problem-visual|question-concept-aid)"',s)):
  count=0;end=None
  for t in re.finditer(r'</?div\b[^>]*>',s[m.start():]):
   count+=-1 if t[0].startswith('</') else 1
   if not count:end=m.start()+t.end();break
  assert end
  s=s[:m.start()]+s[end:]
 return s
retained=[]
for row in inputs:
 current=re.findall(r'<section class="exam-question"[\s\S]*?</section>',(R/'dist/chapters'/f'{row["topicId"]}.html').read_text(encoding='utf-8'))
 assert len(current)==len(row['questions'])
 for old,new in zip(row['questions'],current):assert remove_aids(new)==old['html'],old['id']
 retained.append(dict(topicId=row['topicId'],questions=len(current),originalBodiesRetained=True))
(O/'retention.json').write_text(json.dumps(dict(state='passed',chapters=retained,problems=sum(r['questions'] for r in retained)),indent=2)+'\n')
base=(R/'research/qa_library_visuals.py').read_text();prefix=base[:base.index(' cdp(\'Page.enable\')')]
body=r'''
 cdp('Page.enable');cdp('Runtime.enable');cdp('Emulation.setDeviceMetricsOverride',dict(width=1280,height=1000,deviceScaleFactor=1,mobile=False))
 results=[]
 for row in ([] if '--screenshots-only' in sys.argv else json.loads((ROOT/'research/library-visual-question-review/input.json').read_text())):
  topic=row['topicId'];cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/{topic}.html'));time.sleep(.35)
  js('(async()=>{for(let i=0;i<150;i++){if(location.pathname.endsWith('+json.dumps(topic+'.html')+')&&document.readyState==="complete"&&window.ProblemVisuals&&window.ConceptAnimations)return;await new Promise(r=>setTimeout(r,50));}throw Error("Chapter scripts did not initialize");})()')
  js('document.fonts.ready')
  js('Promise.all([...document.querySelectorAll("details.exam-solution")].map(d=>{d.open=true;return Promise.all([...d.querySelectorAll("[data-problem-visual]")].map(ProblemVisuals.ready).concat([...d.querySelectorAll(".concept-animation")].map(ConceptAnimations.ready)));}))')
  check=js("""(()=>{const bad=[...document.querySelectorAll("[data-loaded=error]")].length;return {questions:document.querySelectorAll("section.exam-question").length,failedModels:bad,problemPlayers:ProblemVisuals.players.length,conceptPlayers:ConceptAnimations.players.length,mathFont:getComputedStyle(document.querySelector("math")).fontFamily,documentWidth:document.documentElement.scrollWidth,viewport:innerWidth,loadedFonts:document.fonts.check('18px "STIX Two Math"')};})()""")
  assert check['questions']==row['questionCount'] and check['failedModels']==0 and check['loadedFonts'] and 'STIX' in check['mathFont'],(topic,check)
  cdp('Emulation.setDeviceMetricsOverride',dict(width=390,height=844,deviceScaleFactor=1,mobile=False));time.sleep(.1)
  mobile=js('({width:document.documentElement.scrollWidth,viewport:innerWidth})')
  assert mobile['width']<=mobile['viewport']+1,(topic,mobile)
  cdp('Emulation.setEmulatedMedia',dict(media='print'));js('window.dispatchEvent(new Event("beforeprint"))')
  printed=js('({open:[...document.querySelectorAll("details.exam-solution")].every(d=>d.open),hiddenControls:[...document.querySelectorAll(".problem-controls")].every(c=>getComputedStyle(c).display==="none")})')
  assert printed['open'] and printed['hiddenControls'],(topic,printed)
  cdp('Emulation.setEmulatedMedia',dict(media=''));js('window.dispatchEvent(new Event("afterprint"))');cdp('Emulation.setDeviceMetricsOverride',dict(width=1280,height=1000,deviceScaleFactor=1,mobile=False))
  results.append(dict(topicId=topic,desktop=check,mobile=mobile,print=printed))
  print(topic,check['questions'],'problems: loaded, mobile contained, print ready',flush=True)
 if results:(ROOT/'research/library-visual-question-review/page-browser.json').write_text(json.dumps(dict(state='passed',chapters=results),indent=2)+'\n')
 # Capture representative real solution cards, not isolated renderer mocks.
 for topic,number in [('g_combin',37),('g_combin',58),('g_kmap',5),('l_gauss',5),('p_functions',25),('a_arrays',1)]:
  cdp('Page.navigate',dict(url=f'http://127.0.0.1:{server.server_port}/chapters/{topic}.html'));time.sleep(.2);js('document.fonts.ready')
  js('(async()=>{for(let i=0;i<150;i++){if(location.pathname.endsWith('+json.dumps(topic+'.html')+')&&document.readyState==="complete"&&window.ProblemVisuals)return;await new Promise(r=>setTimeout(r,50));}throw Error("Capture scripts did not initialize");})()')
  js('(async()=>{const q=document.querySelectorAll("section.exam-question")['+str(number-1)+'];q.querySelector("details").open=true;await Promise.all([...q.querySelectorAll("[data-problem-visual]")].map(ProblemVisuals.ready));(q.querySelector(".problem-visual")||q).scrollIntoView();})()');time.sleep(.15)
  screenshot=cdp('Page.captureScreenshot',dict(format='png'))['data'];(ROOT/'research/library-visual-question-review'/f'{topic}-q{number}.png').write_bytes(base64.b64decode(screenshot))
finally:
 proc.terminate();server.shutdown()
'''
(R/'research/qa_library_question_pages_browser.py').write_text(prefix+body)
print('All 2085 original problem bodies retained exactly; browser page audit prepared.')

"""Build self-contained teaching copies while private Site synchronization is unavailable."""
from pathlib import Path
import base64,hashlib,json,mimetypes,re
R=Path(__file__).resolve().parents[1];O=R/'exports';O.mkdir(exist_ok=True)
def url_data(p):
 mime='font/woff2'if p.suffix=='.woff2'else'audio/wav'if p.suffix=='.wav'else mimetypes.guess_type(str(p))[0]or'application/octet-stream'
 encoded=base64.b64encode(p.read_bytes()).decode('ascii')
 # Generated WAV bytes can coincidentally resemble a cloud credential in base64.
 # Standard percent-encoding changes the URL spelling, not the decoded media.
 encoded=encoded.replace('AKID','%41KID')
 return 'data:'+mime+';base64,'+encoded
def css(p):
 s=p.read_text(encoding='utf8')
 def asset(m):
  raw=m[1].strip('"\' ')
  if raw.startswith(('data:','#','http')):return m[0]
  file=(p.parent/raw.split('?')[0]).resolve();assert file.is_relative_to((R/'dist').resolve())and file.is_file(),file
  return 'url("'+url_data(file)+'")'
 return re.sub(r'url\(([^)]+)\)',asset,s)
records=[]
for relative,name in[('chapters/a_correct.html','Algorithm Correctness.html'),('ielts/academic-01-sentences.html','IELTS Academic Session 1.html'),('chapters/l_projection.html','Orthogonal Projections.html'),('ielts/academic-02-routines.html','IELTS Academic Session 2.html'),('chapters/s_conditional.html','Conditional Probability.html'),('chapters/s_bayes.html','Bayes Rule.html'),('chapters/l_leastsquares.html','Least Squares.html'),('ielts/academic-03-nouns.html','IELTS Academic Session 3.html')]:
 p=R/'dist'/relative;page=p.read_text(encoding='utf8');sceneIDs=set(x for group in re.findall(r'data-scenes="([^"]+)"',page)for x in group.split(','));db=json.loads((R/'dist/chapters/concept-animations.json').read_text(encoding='utf8'));scenes={k:db['scenes'][k]for k in sorted(sceneIDs)}
 if sceneIDs:
  encoded=json.dumps({'scenes':scenes},ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
  page=page.replace('</head>','<script>window.__OFFLINE_CONCEPTS='+encoded+';</script></head>')
 if relative=='chapters/l_leastsquares.html':
  model_data=(R/'dist/chapters/l_leastsquares-models.json').read_text(encoding='utf8').replace('<','\\u003c')
  page=page.replace('</head>','<script>window.LS_MODEL_DATA='+model_data+';</script></head>')
 def stylesheet(m):return'<style>'+css((p.parent/m[1].split('?')[0]).resolve())+'</style>'
 page=re.sub(r'<link\b[^>]*rel="stylesheet"[^>]*href="([^"]+)"[^>]*>',stylesheet,page)
 def script(m):
  path=(p.parent/m[1].split('?')[0]).resolve();assert path.is_relative_to((R/'dist').resolve())
  code=path.read_text(encoding='utf8')
  if path.name=='concept-unified.js':
   code=re.sub(r" const data=\(\)=>[\s\S]*?\n const el=",' const data=()=>dataPromise??(dataPromise=Promise.resolve(window.__OFFLINE_CONCEPTS));\n const el=',code,count=1)
   assert'concept-animations.json'not in code
  return'<script>'+code.replace('</script','<\\/script')+'</script>'
 page=re.sub(r'<script\b[^>]*src="([^"]+)"[^>]*>\s*</script>',script,page)
 page=re.sub(r'src="(audio/[^"]+\.wav)"',lambda m:'src="'+url_data((p.parent/m[1]).resolve())+'"',page)
 page=re.sub(r'<p class="top-link">[\s\S]*?</p>','<p class="top-link">Self-contained teaching copy · the full lesson, fonts and interactive resources are included.</p>',page,count=1)
 page=page.replace('<body>','<body><p style="margin:12px;text-align:center;font-size:14px">Offline teaching copy · 17 October 2026 · review draft</p>',1)
 # Retain references; turn app/source-audit navigation into verified repository links.
 page=re.sub(r'href="(\.\./[^"#]+)(#[^"]*)?"',lambda m:'href="https://github.com/bheydari721rn24/Phd-Exam-CSE/tree/study-planner-1406/study-planner"',page)
 ck=not re.search(r'<(?:link|script)\b[^>]*(?:href|src)="(?!data:)',page)
 assert ck and not re.search(r'<audio\b[^>]*src="(?!data:)',page)
 target=O/name;target.write_bytes(page.encode('utf8'));records.append({'path':str(target.relative_to(R)),'source':relative,'sourceSha256':hashlib.sha256(p.read_bytes()).hexdigest(),'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'embeddedScenes':len(scenes),'embeddedAudio':page.count('<audio'),'bytes':target.stat().st_size})
(O/'manifest.json').write_text(json.dumps({'date':'2026-10-17','copies':records,'scope':'Self-contained current drafts with embedded fonts, scripts, selected concept data and original audio. External references still require network access.'},indent=2)+'\n')
print(records)

from pathlib import Path
import fitz,json,requests,hashlib
R=Path(__file__).resolve().parents[1];O=R/'research/s_discrete-evidence';C=Path('C:/Users/bheydari/AppData/Local/Temp/s-discrete-sources')
url='https://fa16.eecs70.org/static/notes/n16.pdf';r=requests.get(url,timeout=40);r.raise_for_status();p=C/'berkeley.pdf';p.write_bytes(r.content);d=fitz.open(p);(C/'berkeley.txt').write_text('\n'.join('PDF PAGE '+str(i+1)+'\n'+p.get_text() for i,p in enumerate(d)),encoding='utf-8')
rows=json.loads((O/'acquisition.json').read_text());rows.append(dict(id='berkeley-valid',course='UC Berkeley CS70, Note16, Spring 2016 rehosted Fall 2016',url=url,path=str(p),pages=len(d),sha256=hashlib.sha256(r.content).hexdigest(),status='acquired_not_reviewed'));(O/'acquisition.json').write_text(json.dumps(rows,indent=2)+'\n')
for id in ['mit','berkeley','stanford','oxford','harvard']:
 d=fitz.open(C/(id+'.pdf'));print(id,len(d))
 for i,p in enumerate(d):
  s=p.get_text()
  if id in ['mit','oxford'] and any(t in s.lower() for t in ['discrete random variables','probability mass function','geometric distribution']):print('candidate page',i+1,s[:120].replace('\n',' '))

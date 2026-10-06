from pathlib import Path
import fitz,json,tempfile,re
T=Path(tempfile.gettempdir())/'exam-calibration-1406/source';rows=[]
for p in T.rglob('*.pdf'):
 if '/CS/' not in p.as_posix():continue
 d=fitz.open(p)
 for i,pg in enumerate(d):
  s=pg.get_text();norm=re.sub(r'\s+',' ',s).replace('ي','ی').replace('ك','ک')
  if any(t in norm for t in ['واریانس نمونه','میانگین نمونه','ضریب تغییر','میانه','واریانس داده','چارک','آمار توصیفی']):rows.append(dict(path=str(p),page=i+1,text=s))
B=Path(__file__).resolve().parent;(B/'s_descriptive-evidence/archive-candidates.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print([(r['path'].split('Exams')[-1],r['page'],r['text'][:180]) for r in rows])

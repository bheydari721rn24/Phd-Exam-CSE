from pathlib import Path
import json,re,hashlib
B=Path(__file__).resolve().parent;R=B.parent
report=[]
for name in ['exam-calibration/actual-items.json','a_sort-authentic.json']:
 p=B/name;a=json.loads(p.read_text(encoding='utf-8'))
 q=next(x for x in a if x['id']=='Phd_CE_1405_Q16');q['options']=['16','14','12','10'];q['answer']=1
 q['solution']=q['solution'].replace('sixteen.','sixteen, so the original booklet answer is option 1.')
 q['translationStatus']='Rechecked visually against the full original PDF page on 2026-10-06; repaired option ordering.'
 p.write_text(json.dumps(a,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
for p in (R/'dist/chapters').glob('*.html'):
 s=p.read_text(encoding='utf-8');needle='data-source-id="Phd_CE_1405_Q16"'
 if needle not in s:continue
 start=s.rfind('<section',0,s.index(needle));end=s.index('<details',start)
 old=s[start:end];op=old.index('<div class="exam-options">');tail=old[op:]
 values=re.findall(r'(<div class="exam-option">[\s\S]*?<b>)(\d+)([\s\S]*?<div>)([\s\S]*?)(</div></div>)',tail)
 assert len(values)==4,(p,tail[:500])
 newtail=tail
 for v in values:
  value={'1':'16','2':'14','3':'12','4':'10'}[v[1]]
  newtail=newtail.replace(''.join(v),v[0]+v[1]+v[2]+'<p>'+value+'</p>'+v[4])
 s=s[:start]+old[:op]+newtail+s[end:]
 endq=s.find('data-source-id=',start+len(needle)+40);endq=len(s) if endq<0 else s.rfind('<section',0,endq)
 part=s[start:endq]
 part=re.sub(r'(Correct option:\s*)(?:<[^>]+>)*2',r'\g<1>1',part)
 part=part.replace('Correct option: 2.','Correct option: 1.')
 s=s[:start]+part+s[endq:]
 oldhash=hashlib.sha256(p.read_bytes()).hexdigest();p.write_text(s,encoding='utf-8')
 report.append(dict(file=p.name,beforeSha256=oldhash,afterSha256=hashlib.sha256(p.read_bytes()).hexdigest(),change='Only Q16 option ordering and correct option index; mathematical solution and all other questions preserved.'))
(B/'a_sort-provenance-correction.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print('Corrected original booklet option order in',len(report),'previous chapter occurrences.')

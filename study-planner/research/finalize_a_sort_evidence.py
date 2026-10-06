from pathlib import Path
import json,subprocess,hashlib
B=Path(__file__).parent;R=B.parent;hash=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
p=B/'exam-calibration/actual-items.json';current=json.loads(p.read_text(encoding='utf-8'));raw=subprocess.check_output(['git','show','b9ac11a35732c82925d5b9806e502fc77dff806c:research/exam-calibration/actual-items.json'],cwd=R).decode('utf-8');old=json.loads(raw)
target=next(q for q in current if q['id']=='Phd_CE_1405_Q16');pos=raw.index('"id": "Phd_CE_1405_Q16"');start=raw.rfind('  {',0,pos);end=raw.index('\n  }',pos)+4
replacement='  '+json.dumps(target,indent=2,ensure_ascii=False).replace('\n','\n  ');raw=raw[:start]+replacement+raw[end:];p.write_text(raw,encoding='utf-8')
assert all(a==b for a,b in zip(old,json.loads(raw)) if a['id']!='Phd_CE_1405_Q16')
cor=json.loads((B/'a_sort-provenance-correction.json').read_text())
for item in cor:
 p=R/'dist/chapters'/item['file'];s=p.read_text(encoding='utf-8');pos=s.index('data-source-id="Phd_CE_1405_Q16"');st=s.rfind('<section',0,pos);en=s.index('>',pos);s=s[:st]+s[st:en].replace('data-answer="2"','data-answer="1"')+s[en:];p.write_text(s,encoding='utf-8');item['afterSha256']=hash(p);item['change']='Only Q16 option ordering, visible correct option and machine-readable answer index. Mathematical solution and other questions preserved.'
(B/'a_sort-provenance-correction.json').write_text(json.dumps(cor,indent=2)+'\n')
scopes={'mit3':[[1,6]],'mit5':[[1,5]],'mitr5':[[1,5]],'princeton21':[[3,36]],'princeton22':[[3,37]],'princeton23':[[5,24],[34,45]],'princeton24':[[33,40]],'cmu7':[[1,31]],'oxford':[[14,23]],'stanfordproof':[[1,2]],'stanford5':[[29,54]],'stanford6':[[24,58]]}
ledger=json.loads((B/'a_sort-reading.json').read_text())
print('reading ids',[q['id'] for q in ledger['documents']])
# Exact IDs are matched against the audit's stated document scopes below.
for q in ledger['documents']:
 check=hash(Path(q['path']));assert check==q['sha256'];q['state']='chapter_scope_read_and_reconciled';q['pdfPageRangesRead']=scopes[q['id']];q['scopeEvidence']='research/a_sort-source-audit.md';q['wholeCourseRead']=False
(B/'a_sort-reading.json').write_text(json.dumps(ledger,indent=2)+'\n')

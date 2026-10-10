from pathlib import Path
import json,hashlib,fitz
B=Path(__file__).resolve().parent;E=B/'d_recurrence-evidence'
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
sources=[]
for name,p,scope in [('MIT',Path('C:/Users/bheydari/AppData/Local/Temp/phd-correctness-sources/mit-mcs.pdf'),'PDF 876–891, Chapter 21'),('Berkeley Thursday',Path('C:/Users/bheydari/AppData/Local/Temp/d-recurrence-sources/berkeley-thursday.pdf'),'Both pages; page two visually inspected'),('Berkeley Friday',Path('C:/Users/bheydari/AppData/Local/Temp/d-recurrence-sources/berkeley-friday.pdf'),'Both pages')]:
 sources.append(dict(name=name,sha256=hashlib.sha256(p.read_bytes()).hexdigest(),pdfPages=len(fitz.open(p)),scope=scope))
sources += [dict(name='Oxford',scope='Chapter 5, printed 57–70, one-based PDF 67–80; web PDF text',hash=None),dict(name='Cornell',scope='One-based PDF 31–35; actual web PDF definitions, proofs and repeated-root paragraph',hash=None)]
save(E/'reading.json',dict(coreUniversities=['MIT','Oxford','Cornell','Berkeley'],sources=sources,candidateAudit='research/d_recurrence-source-audit.md',limits='Bounded written candidate pool; exact scopes rather than entire-course claims. No native hash for failed Oxford/Cornell downloads.'))
p=B/'g_mux-publication-pending.json';x=json.loads(p.read_text());x['uploadAttempts']=2;x['reason']='Two native private publication attempts failed at the OpenAI archive upload service, including upload-finalization failure on the second attempt. No deployment or saved-version identifier was returned.';save(p,x)
q=json.loads((B/'exam-calibration/actual-items.json').read_text());chosen=[dict(x)for x in q if x['id']in['MS_CS_1405_Q130','Phd_CS_1404_Q28','Phd_CS_1404_Q71']]
for x in chosen:
 p=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')/x['repoPath'];assert hashlib.sha256(p.read_bytes()).hexdigest()==x['sourceSha256'];d=fitz.open(p);d[x['pdfPage']-1].get_pixmap(matrix=fitz.Matrix(1.4,1.4)).save(str(E/(x['id']+'.png')));x['topics']=list(set(x['topics']+['d_recurrence']));x['translationStatus']='Revisited chapter bridge; original PDF page rendered again in d_recurrence evidence.'
save(B/'d_recurrence-authentic.json',chosen)
print('Recorded four actual university readings; rendered three original exam pages with source hashes verified.')

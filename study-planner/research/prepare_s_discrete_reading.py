from pathlib import Path
import fitz,json,hashlib
R=Path(__file__).resolve().parents[1];O=R/'research/s_discrete-evidence';C=Path('C:/Users/bheydari/AppData/Local/Temp/s-discrete-sources');A=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')
acq=json.loads((O/'acquisition.json').read_text());records=[]
scopes={'mit':(28,39,'Full Class 4 discrete-variable reading: mappings, PMF/CDF, Bernoulli, binomial, zero-based geometric, uniform and sum example.'),'berkeley-valid':(1,5,'Note16 definitions, fiber partition, permutation example and binomial/packet model. Expectation remainder excluded.'),'stanford':(1,124,'Full textual Lecture6 plus inspected formula figures; progressive duplicate slides recognized. Finite sample frequencies distinguished from unknown population law.'),'oxford':(18,21,'Chapter2 definitions through classical distributions and normalization exercise2.5; expectation section on final page only screened.' )}
for id,(lo,hi,scope) in scopes.items():
 row=next(x for x in acq if x['id']==id);records.append({**row,'status':'reviewed_bounded_scope','reviewScope':scope,'pdfPages':[lo,hi]})
records.append(dict(id='harvard-web',course='Harvard Statistics110, Joe Blitzstein, Strategic Practice4, 2011',url='https://stat110.hsites.harvard.edu/sites/g/files/omnuum10111/files/stat110/files/strategic_practice_and_homework_4.pdf',status='reviewed_bounded_web_scope',pdfPages=[1,4],reviewScope='Section1 problems1–3 and their page4 solutions via web PDF extraction. Same law versus equality, cyclic shift and positive-based geometric CDF. Direct acquisition403; no full downloaded-file review claimed.'))
(O/'reading.json').write_text(json.dumps(dict(selectedCoreUniversities=['Oxford','MIT','UC Berkeley','Stanford'],additionalReviewedUniversity='Harvard',candidatePoolUniversities=7,records=records,limits='A bounded located pool; not all courses in existence. CMU syllabus and ETH2019 index screened, not lecture reviews.'),indent=2)+'\n')
for id,page,name in [('mit',32,'mit-cdf.png'),('stanford',77,'stanford-binomial.png'),('oxford',20,'oxford-conventions.png')]:
 d=fitz.open(C/(id+'.pdf'));d[page-1].get_pixmap(matrix=fitz.Matrix(1.6,1.6)).save(C/name)
for rel,page,name in [('Exams/MS/CE/1405/Q135A-Arshad1405-[www.konkur.in].pdf',8,'ms-ce-1405-p8.png'),('Exams/Phd/CS/1404/Q892A-PHD1404-[www.konkur.in].pdf',15,'phd-cs-1404-p15.png')]:
 d=fitz.open(A/rel);d[page-1].get_pixmap(matrix=fitz.Matrix(1.8,1.8)).save(C/name)
print('Bounded four-course reading ledger and source-page images prepared.')

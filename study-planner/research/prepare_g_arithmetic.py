"""Build provenance-preserving question records and executable circuit checkpoints."""
from pathlib import Path
import json,re,subprocess,hashlib
B=Path(__file__).resolve().parent;R=B.parent
def save(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
parts=re.split(r'^### (\d+)\. (.+)$',(B/'g_arithmetic-problems.en.md').read_text(encoding='utf-8'),flags=re.M)
qs=[]
visuals={1:'full-basic',3:'full-basic',6:'ripple-chain',7:'ripple-chain',12:'prefix-chain',14:'prefix-chain',16:'prefix-chain',19:'select-eight',23:'nand-borrow',25:'subtract-boundary',28:'ripple-chain',33:'subtract-overflow',38:'compare-msb',41:'bcd-twelve',42:'bcd-nineteen',43:'bcd-twelve',46:'csa-max',47:'csa-max',50:'multiply-143',51:'booth-signed',52:'booth-minimum',53:'booth-signed',54:'booth-signed',56:'divide-45',57:'divide-45',58:'divide-45',77:'bcd-nineteen',78:'nand-borrow',80:'subtract-boundary'}
for i in range(1,len(parts),3):
 n=int(parts[i]);title=parts[i+1];stem,solution=parts[i+2].strip().split('#### Solution',1)
 qs.append(dict(id=f'g_arithmetic_original_{n:02d}',title=title,stem=stem.strip(),solution=solution.strip(),origin='Original problem and independent derivation; reconstructed course patterns are identified in the solution.',**({'modelId':visuals[n]}if n in visuals else{})))
assert len(qs)==80 and len({q['id']for q in qs})==80
save(B/'g_arithmetic-questions.json',qs)
items=json.loads((B/'exam-calibration/actual-items.json').read_text(encoding='utf-8'))
auth=[dict(q)for q in items if q['id']in['Phd_CE_1405_Q31','Phd_CE_1405_Q23']]
assert len(auth)==2
for q in auth:
 q['modelId']='nand-borrow'if q['questionNumber']==23 else 'subtract-overflow'
 q['visualQualification']='Revisited authenticated bridge. The circuit uses the original topology with the stated sample input; the trace does not replace the general Boolean derivation.'if q['questionNumber']==23 else 'The diagram shows a related signed-overflow counterexample, not a separate trace of each answer choice. The solution evaluates every original option.'
save(B/'g_arithmetic-authentic.json',auth)
specs=[('booth-signed','Signed Booth rows: negative three times negative two',dict(operation='booth',n=4,a=13,b=14,c=0,z=0),'booth'),('booth-minimum','Booth at the minimum negative boundary',dict(operation='booth',n=4,a=8,b=15,c=0,z=0),'booth'),('full-basic','Full-adder gate dependencies',dict(operation='full',n=1,a=1,b=1,c=1,z=0),'full'),('ripple-chain','One generate followed by a carry chain',dict(operation='ripple',n=4,a=15,b=1,c=0,z=0),'ripple'),('prefix-chain','An eight-bit ordered prefix network',dict(operation='prefix',n=8,a=255,b=1,c=0,z=0),'prefix'),('select-eight','Eight-bit carry-select with a four/four split',dict(operation='select',n=8,a=127,b=1,c=0,z=0),'select'),('subtract-boundary','Subtraction, no-borrow and signed overflow',dict(operation='subtract',n=4,a=8,b=1,c=0,z=0),'subtract'),('subtract-overflow','Result sign corrected by overflow',dict(operation='subtract',n=4,a=7,b=15,c=0,z=0),'subtract'),('compare-msb','Most-significant differing bit decides',dict(operation='compare',n=4,a=10,b=9,c=0,z=0),'compare'),('bcd-twelve','Decimal carry without initial binary carry',dict(operation='bcd',n=4,a=7,b=5,c=0,z=0),'bcd'),('bcd-nineteen','Decimal carry without correction-adder carry',dict(operation='bcd',n=4,a=9,b=9,c=1,z=0),'bcd'),('csa-max','Three maximum four-bit rows',dict(operation='csa',n=4,a=15,b=15,c=0,z=15),'csa'),('multiply-143','Eleven times thirteen: weighted partial rows',dict(operation='multiply',n=4,a=11,b=13,c=0,z=0),'multiply'),('divide-45','Forty-five divided by five: prefix invariant',dict(operation='division',n=6,a=45,b=5,c=0,z=0),'division'),('nand-borrow','Original NAND network with x=0 and y=1',dict(operation='nand',n=1,a=0,b=1,c=0,z=0),'borrow')]
payload=json.dumps(specs)
script="const {makeModel}=require('./dist/chapters/g_arithmetic.js');const specs="+payload+";process.stdout.write(JSON.stringify(specs.map(x=>makeModel(x[0],x[1],x[2]))));"
models=json.loads(subprocess.check_output(['node','-e',script],cwd=R,text=True,encoding='utf-8'))
groups={}
for spec in specs:groups.setdefault(spec[3],[]).append(spec[0])
# The half-subtractor network supports the borrow section as well as its authentic problem.
groups['subtract']=['subtract-boundary','subtract-overflow','nand-borrow'];groups.pop('borrow')
save(R/'dist/chapters/g_arithmetic-models.json',dict(models=models,groups=groups))
reading=dict(topicId='g_arithmetic',actualWrittenCoreUniversities=['MIT','Stanford','Berkeley','ETH Zurich'],selectionAudit='research/g_arithmetic-source-audit.md',downloadManifests=['research/g_arithmetic-evidence/downloads.json','research/g_arithmetic-evidence/followup-downloads.json'],readScopes=dict(MIT='Complete public Lecture 8 written arithmetic annotations, read through web text',Stanford='PDF 147–149, 189–218, 229–232; 209–211 reread',Berkeley='All nine arithmetic PDF pages; diagrams on 4 and 7; all three HW10/11 pages',ETH='PDF 37–66, 71–72, 81–84; diagrams 48–49 and 82–83'),limits='Bounded documented accessible candidate pool, not exhaustive worldwide discovery. ETH supplemental written slides are identified as such.')
save(B/'g_arithmetic-evidence/reading.json',reading)
print(f'Prepared {len(qs)} original/reconstructed questions, {len(auth)} authentic bridges, {len(models)} models and {sum(len(m["frames"])for m in models)} stored checkpoints.')

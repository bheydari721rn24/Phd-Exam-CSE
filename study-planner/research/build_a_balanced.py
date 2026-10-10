from pathlib import Path
import json,re,subprocess,hashlib
B=Path(__file__).resolve().parent;R=B.parent;E=B/'a_balanced-evidence'
def save(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
specs=[]
def add(id,title,g,**s):specs.append((id,title,s,g))
add('minimum-eight','Exact minimum-node thresholds through height eight','minimum',operation='minimum',limit=8)
for id,keys in [('ll',[30,20,10]),('rr',[10,20,30]),('lr',[30,10,20]),('rl',[10,30,20])]:add('avl-'+id,'AVL '+id.upper()+': actual leaf attachment and primitive repair','insertion',operation='avl-insert',keys=keys)
add('middle-subtree','Question 15: transfer the real middle subtree 25','insertion',operation='avl-insert',keys=[50,20,70,10,30,25])
for id,keys,remove in [('delete-zero',[40,20,10,30,60],[60]),('delete-outer',[40,20,10,60],[60]),('delete-inner',[40,20,30,60],[60]),('delete-cascade',[50,20,10,30,40,80,60,70,90,85,100,110],[10]),('delete-successor',[40,20,60,10,30,50,70],[40])]:add(id,'AVL '+id.replace('-',' ')+': inspect true heights and return-root links','deletion',operation='avl-delete',initial='plain',keys=keys,remove=remove)
add('multiway-seven','Top-down 2–3–4: actual split and promotion boxes','multiway',operation='multiway',keys=[10,20,30,40,50,60,70])
for case,num in [('borrow',36),('merge',37),('borrow-left-target',73)]:add('multiway-'+case,'Question '+str(num)+': exact multiway '+case+' intervals','multiway',operation='multiway-repair',case=case)
add('red-cluster','General red-black versus completed 2–3 LLRB','encoding',operation='encoding')
for case in ['red-uncle','line','triangle']:add('classical-'+case,'Classical insertion: '+case+' case','classical',operation='classical-demo',case=case)
add('llrb-seven','Seven increasing keys: every LLRB rotation and flip','llrb-insert',operation='llrb-insert',keys=[10,20,30,40,50,60,70])
add('llrb-descending','Seven decreasing keys: a distinct normalized trace','llrb-insert',operation='llrb-insert',keys=[70,60,50,40,30,20,10])
add('llrb-minimum','Remove 10 from the all-black seven-key tree','llrb-delete',operation='llrb-delete',keys=[10,20,30,40,50,60,70],remove=[10])
add('llrb-several','Prepared LLRB deletion of 10,40,70','llrb-delete',operation='llrb-delete',keys=[10,20,30,40,50,60,70],remove=[10,40,70])
add('zero-large','Question 62: correct equality repair in the larger counterexample','problem-only',operation='avl-delete',initial='plain',keys=[80,40,20,10,60,70,100,90],remove=[90])
add('compound-eight','Question 80: all three specified AVL updates','problem-only',operation='avl-updates',keys=[40,20,60,10,30,50,70,25,35],updates=[['delete',10],['delete',60],['insert',65]])
add('contract-inner','Question 70: the exact 50,10,30 LR example','problem-only',operation='avl-insert',keys=[50,10,30])
code="const{makeModel}=require('./dist/chapters/a_balanced.js');process.stdout.write(JSON.stringify("+json.dumps(specs)+".map(x=>makeModel(x[0],x[1],x[2]))));"
models=json.loads(subprocess.check_output(['node','-e',code],cwd=R,text=True,encoding='utf-8'));groups={}
for id,title,s,g in specs:groups.setdefault(g,[]).append(id)
save(R/'dist/chapters/a_balanced-models.json',dict(models=models,groups=groups))
parts=re.split(r'^### (\d+)\. (.+)$','\n\n'.join((B/f'a_balanced-problems{x}.en.md').read_text(encoding='utf-8')for x in['','-2','-3']),flags=re.M)
visuals={1:'minimum-eight',12:'avl-ll',13:'avl-ll',14:'avl-lr',15:'middle-subtree',17:'delete-zero',18:'delete-outer',19:'delete-inner',20:'delete-cascade',21:'delete-successor',34:'multiway-seven',38:'red-cluster',44:'classical-red-uncle',45:'classical-line',46:'classical-triangle',55:'llrb-seven',56:'llrb-minimum',57:'llrb-descending',62:'zero-large',70:'contract-inner',80:'compound-eight'}
# Q12's arbitrary opposite rotation is proved in text; do not attach an LL repair trace as its answer.
visuals.pop(12)
visuals.update({36:'multiway-borrow',37:'multiway-merge',73:'multiway-borrow-left-target'})
qs=[]
for i in range(1,len(parts),3):
 n=int(parts[i]);stem,solution=parts[i+2].strip().split('#### Solution',1)
 q=dict(id=f'a_balanced_original_{n:02d}',title=parts[i+1],stem=stem.strip(),solution=solution.strip(),origin='Independently authored mathematical/conceptual problem. Named course-pattern reconstructions use new data and complete original solutions.')
 if n in visuals:q.update(modelId=visuals[n],visualQualification='The checkpoint model uses the exact relevant keys and update rule. Read the written solution for the requested count, proof or comparison.')
 if n==1:q['visualQualification']='The model shows exact minimum thresholds through height eight, including the two thresholds used here. It does not construct a fifty-key witness.'
 if n==14:q['visualQualification']='This companion shows the LR member of the four exact three-key cases. All four case models appear in the main lesson; the solution distinguishes their primitive counts.'
 if n==62:q['visualQualification']='This model shows the correct single-rotation equality repair for the larger failure witness. The deliberately incorrect double branch is derived and rejected in the written solution.'
 qs.append(q)
assert len(qs)==80;save(B/'a_balanced-questions.json',qs)
manifest=json.loads((B/'exam-calibration/archive-manifest.json').read_text());files=manifest['files']
auth=[]
for id,path,page,num,title,stem,options,answer,solution in [
 ('MS_CE_1405_Q61','Exams/MS/CE/1405/Q135A-Arshad1405-[www.konkur.in].pdf',13,61,'Worst-case AVL insertion and deletion','An AVL tree supports insert(x) and delete(x), and remains AVL after every operation. What is the worst-case cost of each insertion and deletion?',['O(1)','O(n)','O(log n)','O(n log n)'],3,'The maintained AVL invariant implies logarithmic height from the exact minimum-node recurrence. Insertion searches one route, refreshes its ancestors and repairs one lowest site with at most two primitives. Deletion follows a search/successor-removal route and may repair multiple ancestors, but each visited ancestor costs constant local work and there are logarithmically many. Thus each operation has O(log n) worst-case cost under constant-cost comparisons and metadata: option 3. The differing rotation counts do not make their asymptotic route costs differ. This is an independently derived answer, not an official key.'),
 ('Phd_CE_1405_Q6','Exams/Phd/CE/1405/Q707A-phd1405-[www.konkur.in].pdf',2,6,'How many AVL shapes on keys 1,2,3?','How many AVL trees can be built using keys 1,2,3?',['1','2','6','C_3, where C_3 is the third Catalan number'],1,'If root is 1 or 3, the other two keys must lie in one child subtree of height one while the other child is empty with height minus one. The root difference is two, so those choices are invalid. Root 2 permits left leaf 1 and right leaf 3, giving the unique valid shape. Therefore the answer is one, option 1. Counting the six permutations or the five Catalan shapes ignores either output equivalence or the AVL invariant. A fixed increasing key set labels each ordered valid shape uniquely. This independently derived result is not an official key.')]:
 row=next(x for x in files if x['repoPath']==path);p=Path('C:/Users/bheydari/AppData/Local/Temp/exam-calibration-1406/source')/path;assert hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256']
 auth.append(dict(id=id,booklet=id.rsplit('_Q',1)[0],pdfPage=page,questionNumber=num,title=title,stem=stem,options=options,answer=answer,solution=solution,sourceCommit=manifest['commit'],repoPath=path,sourceSha256=row['sha256'],translationStatus='Exact original page rendered and visually read; checked English adaptation and independently derived answer.',answerProvenance='Independent solution, not an official key'))
save(B/'a_balanced-authentic.json',auth)
css=(R/'dist/chapters/a_bst.css').read_text(encoding='utf-8').replace('bt-','bl-')
css+='\n.bl-model svg .bl-prose{font-size:17px!important}.bl-model svg .bl-math{font-size:19px!important}.bl-model svg .bl-meta{font-size:15px!important}.bl-stage{max-height:420px}.bl-stage svg{width:760px;max-width:100%;height:auto}\n'
css+='\n.bl-model svg .bl-key-long{font-size:14px!important}.bl-model svg .bl-key-medium{font-size:16px!important}\n'
(R/'dist/chapters/a_balanced.css').write_text(css,encoding='utf-8')
print('Built 80 original/reconstructed questions, two authenticated exams and',len(models),'balanced-tree models /',sum(len(m['frames'])for m in models),'checkpoints.')

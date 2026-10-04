import json,shutil
from pathlib import Path
BASE=Path(__file__).resolve().parent;ROOT=BASE.parent
cache=Path('C:/Users/bheydari/AppData/Local/Temp/phd-rank-sources')
docs=json.loads((cache/'acquisition.json').read_text())
records=[]
specs=[
 ('oxford','Oxford','M1 Linear Algebra I, 2022; Andrew Wathen, course lecturer','https://courses.maths.ox.ac.uk/course/view.php?id=609','PDF pp. 42–51,57–61,68–69; all read','Primary proof source: dimension, rank–nullity, invertibility and rank factorization'),
 ('mit','MIT','18.700 Linear Algebra, Fall 2013; David Vogan','https://ocw.mit.edu/courses/18-700-linear-algebra-fall-2013/','PDF pp. 13–20; all read','Primary transformation and rectangular-inverse source'),
 ('stanford','Stanford','EE263, Autumn 2007–08; Stephen Boyd','https://web.stanford.edu/class/archive/ee/ee263/ee263.1082/','Lecture 3 slides 3–1 through 3–19; read','Primary measurement, ambiguity and inverse-direction source'),
 ('berkeley','UC Berkeley','Math 54, Spring 2018; Alexander Paulin','https://math.berkeley.edu/~apaulin/54_001(Spring2018).html','Rank and Nullity, both handwritten pages visually read','Primary exact pivot-column/kernel worked example'),
 ('cmu9','CMU','21-241 Matrix Algebra, Summer I 2014; William Gunther','https://www.math.cmu.edu/~wgunther/241/m14/index.html','Days 9,10,24: all ten pages read','Additional comparison and written prompt source; transcription slips corrected')]
for key,uni,course,url,scope,adv in specs:
 doc=next(x for x in docs if x['id']==key)
 records.append(dict(id=key+'-rank-written',subject='linear',university=uni,course=course,url=url,evidence=doc['url'],topics=['l_rank'],advantage=adv+'; '+scope,limit='Only the stated accessible written scope is counted; corrections and exclusions are in the chapter audit.',access='official_written_material',reviewLevel='reviewed_in_scope_written_sections'))
(BASE/'l_rank-reviewed-courses.json').write_text(json.dumps(records,indent=2)+'\n')
pub=ROOT/'dist/evidence/l_rank';pub.mkdir(parents=True,exist_ok=True)
(pub/'sources.json').write_text(json.dumps(dict(candidateCourses=5,primaryUniversities=['Oxford','MIT','Stanford','UC Berkeley'],additionalUniversity='CMU',documents=docs,readScopes={s[0]:s[4] for s in specs},limits='Bounded accessible written pool; no full-world, inaccessible homework or full-publication reproduction claim.'),indent=2)+'\n')

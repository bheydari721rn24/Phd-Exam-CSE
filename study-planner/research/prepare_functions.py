from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
base=ROOT/'research'
g=json.loads((base/'chapter-gate.json').read_text())
g.update(currentTopicId='d_functions',state='in_progress',approvedTopicId='d_relations',proposedNextTopicId=None,sourceAuditPath='research/d_functions-source-audit.md',qualityAuditPath='research/d_functions-quality-audit.md',activeWork='Writing and auditing the functions chapter after explicit approval of relations.',nextReview='Complete and deliver d_functions before awaiting explicit approval.')
(base/'chapter-gate.json').write_text(json.dumps(g,indent=2)+'\n')
p=base/'build_relations_chapter.py'
t=p.read_text(encoding='utf-8').replace('Review draft awaiting your approval','Student-approved chapter').replace("'status':'draft','url':'chapters/d_relations.html'","'status':'ready','url':'chapters/d_relations.html'")
p.write_text(t,encoding='utf-8')
p=base/'verify_d_relations_en.py';t=p.read_text().replace("assert 'awaiting your approval' in page","assert 'Student-approved chapter' in page");p.write_text(t,encoding='utf-8')
p=ROOT/'dist/chapters/d_relations.html';t=p.read_text(encoding='utf-8').replace('Review draft awaiting your approval','Student-approved chapter');p.write_text(t,encoding='utf-8')
p=ROOT/'dist/lessons.json';ls=json.loads(p.read_text());next(c for w in ls for c in w['chapters'] if c['topicId']=='d_relations')['status']='ready';p.write_text(json.dumps(ls,indent=2)+'\n')
# Reference downloads remain outside the source repository.
t=(base/'fetch_relations_sources.py').read_text()
t=t.replace('phd-relations-sources','phd-functions-sources').replace('d_relations-source-downloads','d_functions-source-downloads')
start=t.index('SOURCES={');end=t.index('def fetch',start)
t=t[:start]+'''SOURCES={
 'mit':'https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/efac321fdc8d0b27586ca35b04aab808_MIT6_042JF10_chap07.pdf',
 'stanford':'https://web.stanford.edu/class/archive/cs/cs103/cs103.1176/lectures/08/Small08.pdf',
 'stanford_ps3':'https://web.stanford.edu/class/archive/cs/cs103/cs103.1176/handouts/150%20Problem%20Set%203.pdf',
 'cambridge':'https://www.cl.cam.ac.uk/teaching/2003/DiscMaths/DiscMaths.pdf',
 'oxford':'https://www.cs.ox.ac.uk/andrew.ker/docs/discretemaths-lecture-notes-mt2010.pdf',
 'cmu_assignment':'https://www.math.cmu.edu/~sallison/concepts18/assignment5.pdf'}\n\n'''+t[end:]
(base/'fetch_functions_sources.py').write_text(t,encoding='utf-8')
print('Relations approved; functions is the sole active chapter.')

"""Preserve a partial arrays review and repair demonstrated boundary defects."""
from pathlib import Path
import hashlib,json,re,shutil,sys
from markdown_it import MarkdownIt
R=Path(__file__).resolve().parents[1];B=R/'research';E=B/'deep-library-revision';T=Path('C:/Users/bheydari/AppData/Local/Temp')
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
mathml.wrap_display=lambda s:s;md=MarkdownIt('commonmark',{'html':True}).enable('table')
def render(s):return mathml.markdown_math(s,md)
copies={
 'phd-arrays-layout-20261018/review.md':'p_arrays-layout-independent-review.en.md',
 'phd-arrays-layout-20261018/oracle-results.json':'p_arrays-layout-independent-checks.json',
 'arrays-source-refresh-20261018/source-refresh.en.md':'p_arrays-two-course-refresh.en.md',
 'arrays-source-refresh-20261018/acquisition.json':'p_arrays-two-course-acquisition.json',
 'arrays-source-refresh-20261018/mathematical-checks.json':'p_arrays-source-independent-checks.json'}
for a,b in copies.items():shutil.copyfile(T/a,E/b)
p=E/'p_arrays-answer-rewrites-01-12.en.md';s=p.read_text(encoding='utf8');ids=re.findall(r'^## (PA\d+) \|',s,re.M);assert ids==['PA'+str(i).zfill(2)for i in range(1,13)]
for display,inline in re.findall(r'\$\$([\s\S]*?)\$\$|\$([^$\n]+)\$',s):mathml.render(display or inline,bool(display))

old='The difference sequence satisfies $D[0]=A[0]$ and $D[i]=A[i]-A[i-1]$ for $i>0$. Adding c to $A[l:r)$ changes only D[l] by +c and, if r < n, D[r] by -c. An n+1 boundary array can retain a right-end sentinel. Reconstruct by a prefix accumulation. This inverse relation explains range updates; it is not merely a pair of memorized signs.'
new=r'''For positive length n, an n-entry difference sequence satisfies $D[0]=A[0]$ and $D[i]=A[i]-A[i-1]$ for $0<i<n$. For n equal to zero, the sequence is empty and neither index zero is read. A valid update on `A[l:r)` with l equal to r is a no-op, including the boundary case l = r = n. Otherwise $0\le l<r\le n$ proves that D[l] exists: add c there, and subtract c from D[r] only when r < n. These boundary changes reconstruct the intended range update by prefix accumulation. An explicitly allocated n+1 boundary representation can instead retain a right-end sentinel, but it is a different storage contract; an n-entry D has no element D[n].'''
p=B/'p_arrays.en.md';s=p.read_text(encoding='utf8');assert old in s;s=s.replace(old,new)
s=s.replace('realloc may move storage and invalidate earlier aliases; on failure the old allocation remains valid, so keep the old pointer until the result is known.','A successful realloc may move storage and invalidate earlier aliases. For a positive requested size, allocation failure leaves the old allocation valid, so retain its pointer until the result is known. Handle a requested size of zero separately: C17 zero-size behavior does not justify treating every null result as a failed positive-size request with the original block necessarily retained.')
p.write_text(s,encoding='utf8')
p=R/'dist/chapters/p_arrays.html';s=p.read_text(encoding='utf8');s,n=re.subn(r'<p>The difference sequence[\s\S]*?</p>',lambda _:render(new).strip(),s,count=1);assert n==1
s=s.replace('realloc may move storage and invalidate earlier aliases; on failure the old allocation remains valid, so keep the old pointer until the result is known.','A successful realloc may move storage and invalidate earlier aliases. For a positive requested size, allocation failure leaves the old allocation valid, so retain its pointer until the result is known. Handle zero-size requests separately under the C17 contract; a null result does not by itself establish a failed positive-size request.')
p.write_text(s,encoding='utf8')
# Bring stale editable source records into agreement with already-correct live pages.
for name in ['p_arrays-authentic.json','a_arrays-authentic.json','p_recursion-authentic.json']:
    p=B/name;data=json.loads(p.read_text(encoding='utf8'))
    q=next(q for q in data if q['id']=='MS_CS_1393_Q167');q['options'][3]=q['options'][3].replace('store(n-1,i+2)','store(n-2,i+2)');q['solution']=q['solution'].replace('and uses a source stride of one','and advances the destination by two, leaving gaps');q['verification']='Original PDF page 34 rechecked on 18 October 2026: all four source strides are -2. This editable record now agrees with the previously corrected live adaptation. Answer 1 remains independently derived.'
    p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
report={'status':'partial_arrays_review_not_complete','rewrittenManuscriptAnswers':12,'totalOriginalCourseInspiredAnswers':81,'remainingOriginalAnswers':69,'chapterReviewCountedComplete':False,'sourceRefreshUniversities':['Cambridge','CMU'],'freshAllSourceClaims':False,'completeCurrentSourcePool':6,'boundaryRepairs':['empty difference updates are no-ops; n=0 has no D[0]','positive-size realloc failure qualification'],'remaining':['PA13-PA81 individual derivations','four-primary-source synthesis and remaining scope refresh','both authentic archive placements','all decision rules and exact-input visuals','whole chapter browser gates'],'manuscriptSHA256':hashlib.sha256((E/'p_arrays-answer-rewrites-01-12.en.md').read_bytes()).hexdigest()}
(E/'p_arrays-review-start.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
p=B/'chapter-gate.json';g=json.loads(p.read_text(encoding='utf8'));g.update(currentDraftPath='research/deep-library-revision/p_arrays-answer-rewrites-01-12.en.md',currentDraftEvidence='research/deep-library-revision/p_arrays-review-start.json',currentReadingEvidence='research/deep-library-revision/p_arrays-two-course-refresh.en.md',currentReviewedAnswerBlocks=12,currentIndividualReviewComplete=False);p.write_text(json.dumps(g,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print('Preserved 12 full arrays derivations; repaired two concrete lesson boundaries; full arrays review remains incomplete.')

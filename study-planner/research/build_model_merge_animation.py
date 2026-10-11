"""Exact comparison events for the authentic eight-key merge-sort question."""
from pathlib import Path
import copy,json,sys
B=Path(__file__).resolve().parent;R=B.parent
sys.path.insert(0,str(B/'exam-rewrite'));import mathml
frames=[];total=0
def event(stage,L,Rr,i,j,out,chosen,finished=False):
    caption=('The complete sorted merge output includes the tail copied after one input emptied. This checkpoint adds no key comparison.'if finished else f'In {stage}, compare the highlighted fronts {L[i]} and {Rr[j]}, then emit {chosen}. Dimmed keys were consumed earlier in this merge; the output row is shown after this comparison.')
    formula=f'C={total}'
    frames.append(dict(nodes=[],edges=[],snapshot=dict(stage=stage,left=L,right=Rr,i=i,j=j,output=out,chosen=chosen,finished=finished,total=total),caption=caption,captionHtml='<p>'+caption+'</p>',metrics={'Total key comparisons':total,'Current merge output keys':len(out)},formula=formula,formulaHtml='<div class="formula-block">'+mathml.render(formula,True)+'</div>',line=1 if finished else 0,teaching=dict(operation='Copy the unconsumed tail'if finished else'Compare the two nonempty front keys and emit the smaller',why=caption,currentState=dict(totalComparisons=total,output=out),initial=not frames,activeLine=1 if finished else 0,checks=[],changes=[],mode='array',reading='The input rows highlight the fronts immediately before this event; the output row contains the prefix immediately after it. Each event charges one key comparison. Tail copying charges none.')))
    frames[-1]=copy.deepcopy(frames[-1])
def sort(A):
    global total
    if len(A)==1:return A
    m=len(A)//2;L=sort(A[:m]);Rr=sort(A[m:]);i=j=0;out=[];stage=f'Merge {L} with {Rr}'
    while i<len(L)and j<len(Rr):
        chosen=L[i]if L[i]<Rr[j]else Rr[j];out.append(chosen);total+=1;event(stage,L,Rr,i,j,out,chosen)
        if chosen==L[i]:i+=1
        else:j+=1
    out+=L[i:]+Rr[j:]
    event('Complete eight-key result'if len(A)==8 else'Tail copy: '+stage,L,Rr,i,j,out,None,True)
    return out
result=sort([12,7,5,9,3,8,2,6]);assert total==16 and result==[2,3,5,6,7,8,9,12]
description='This exact trace follows the authentic eight-key input. Checkpoints distinguish the 16 charged front-pair comparisons from seven tail-copy events, each of which adds zero key comparisons.'
scene=dict(id='model-merge-exact',title='Authentic eight-key merge sort: all 16 comparisons',description=description,descriptionHtml='<p>'+description+'</p>',invariant='Each merge output is a sorted prefix of its two inputs. The comparison counter changes only while both fronts exist.',visual=dict(type='array',claim='Exact original input, consumed positions, compared fronts and emitted prefixes.',revision='exact-authentic-merge-v1'),code=['Compare nonempty fronts and emit the smaller','Copy the remaining tail without comparing keys'],frames=frames)
p=R/'dist/chapters/concept-animations.json';d=json.loads(p.read_text());d['scenes'][scene['id']]=scene;p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(frames=len(frames),comparisons=total,result=result)))

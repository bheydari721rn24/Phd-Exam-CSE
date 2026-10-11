from pathlib import Path
import copy,json,sys
B=Path(__file__).resolve().parent;R=B.parent;sys.path.insert(0,str(B/'exam-rewrite'));import mathml
def frame(state,formula,caption,initial):
    return dict(nodes=[],edges=[],snapshot=copy.deepcopy(state),caption=caption,captionHtml='<p>'+caption+'</p>',metrics={},formula=formula,formulaHtml='<div class="formula-block">'+mathml.render(formula,True)+'</div>',line=0,teaching=dict(operation='Inspect the actual predicate and exact operation ledger',why=caption,currentState=copy.deepcopy(state),initial=initial,activeLine=0,checks=[],changes=[],reading='Read the axis labels and saved integer state. The finite trace illustrates the exact predicate; the written identities and uniform bounds establish general claims.'))
def scene(id,title,description,frames):
    return dict(id=id,title=title,description=description,descriptionHtml='<p>'+description+'</p>',invariant='Each displayed count equals the number of successful events in the explicitly stated finite region or array prefix.',visual=dict(type='enumeration',claim='Exact question-specific integer grid or fixed-array state trace; not a generic growth picture.'),code=['Evaluate the exact stated predicate, then update its specified counter'],frames=frames)
scenes={};frames=[];total=0
for i in range(1,9):
    row=sum((i+j)%2==0 for j in range(1,i+1));total+=row
    state=dict(n=8,i=i,rowCount=row,total=total)
    frames.append(frame(state,rf'B({i})={total}',f'Row i={i} tests {i} positions, keeps {row} same-parity positions, and brings the cumulative body count to {total}. Earlier rows remain visible; later rows are not yet visited.',i==1))
scenes['loop-question-parity']=scene('loop-question-parity','Question 9: the exact filtered triangle','Rows represent outer index i, columns represent inner index j. Green cells run the body; pink cells fail the parity filter. The diagonal is always kept, so the finite triangle does not split into equal halves.',frames)
frames=[];values=[8,3,7,2,6,1,5,4];smallest=None;updates=0
for i,key in enumerate(values,1):
    before=smallest;changed=before is None or key<before
    if changed:smallest=key;updates+=1
    state=dict(values=values,i=i,key=key,before='positive infinity' if before is None else before,after=smallest,update=changed,updates=updates,comparisons=i)
    frames.append(frame(state,rf'C={i},\quad U={updates},\quad m={smallest}',f'Compare key {key} at position {i} against the previous minimum {state["before"]}. The test is '+('true, so assign the new minimum.' if changed else 'false, so preserve the minimum.')+f' There have been {i} comparisons and {updates} successful updates.',i==1))
scenes['loop-question-minimum']=scene('loop-question-minimum','Question 11: fixed-array comparisons and updates','Each checkpoint compares exactly one supplied array key with the current minimum. The comparison counter increments on every key; the assignment counter increments only on a new record.',frames)
frames=[];total=0
for i in range(1,9):
    row=[sum(i*j*k<=8 for k in range(1,9)) for j in range(1,9)];count=sum(row);total+=count
    state=dict(n=8,i=i,rowCounts=row,layerCount=count,total=total)
    frames.append(frame(state,rf'A_{{{i}}}(8)={count},\quad P_{{{i}}}(8)={total}',f'Fix first factor i={i}. Exactly {count} positive pairs (j,k) in this layer satisfy i*j*k <= 8. Adding this layer gives cumulative count {total}. The full grid tests feasibility; gray cells are not part of the counted region.',i==1))
scenes['loop-question-product']=scene('loop-question-product','Question 45: product-constrained layers at n=8','For each fixed positive first factor i, rows are j and columns are k. Each green cell is one unique positive triple with product at most eight. The displayed finite layers complement the proof for arbitrary n.',frames)
p=R/'dist/chapters/concept-animations.json';d=json.loads(p.read_text());d['scenes'].update(scenes);p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:len(s['frames']) for k,s in scenes.items()}))

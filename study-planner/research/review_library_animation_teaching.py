"""Rebuild teaching metadata without changing mathematical checkpoint payloads."""
from pathlib import Path
import json, re, hashlib, copy
from fractions import Fraction
from collections import Counter
import sys
R=Path(__file__).resolve().parents[1];D=R/'dist/chapters';O=R/'research/library-animation-redesign';O.mkdir(exist_ok=True)
sys.path.insert(0,str(R/'research/exam-rewrite'))
from mathml import render
BASELINE='5e43af9577a09e425d09809a9d13449122e04ddb'

# These are reading contracts, not a single model imposed on different subjects.
POLICIES={
 'bars':('Follow complete tagged records. Slot indices are positions; tags are identities. A comparison never moves a record.', ['Locate the current scan, saved key or pair of heads.', 'Evaluate the displayed comparison before any movement.', 'Move the complete record along the stated route.', 'Check the sorted or classified region and preserved multiset.']),
 'search':('Read the half-open interval and the actual midpoint test. An empty interval is a completed search; a repeated nonempty interval is a progress failure.', ['Read lo and hi as boundaries, not both as included elements.', 'Compute the floor midpoint and inspect its key.', 'Discard only the side justified by sortedness.', 'Check that hi − lo decreases before the next iteration.']),
 'truth':('Read one complete valuation at a time. Both expressions use the same inputs. Different rows are independent cases, not physical signal transitions.', ['Fix the complete input valuation.', 'Evaluate the two displayed expressions under that valuation.', 'Compare their outputs.', 'Check all admitted valuations before claiming equivalence.']),
 'venn':('The universe and the four disjoint membership regions stay fixed. Each step classifies one element using the exact set predicate.', ['Read membership in A and B for the selected element.', 'Apply the operation’s Boolean membership rule.', 'Include the element if and only if that rule succeeds.', 'Keep complements relative to the stated universe.']),
 'graph':('Arrow direction expresses the declared relation or mapping. A new edge, witness or emitted vertex must satisfy its stated prerequisite.', ['Read the vertex types and arrow direction.', 'Inspect the selected path, fiber or prerequisite.', 'Add only the edge, witness or output justified by this step.', 'Check the mapping or reachability claim stated below.']),
 'geometry':('The axes, origin and units define the geometry. Moving points retain their identities. Read the exact endpoint equation separately from interpolated construction motion.', ['Identify the origin, axes and current geometric objects.', 'Follow the specified translation, rotation or component construction.', 'Read the exact resulting coordinates or scalar quantity.', 'Check the stated orthogonality, span or mapping relation.']),
 'matrices':('Rows, columns and blocks retain their mathematical roles. Changed entries are exact checkpoint values; they are never interpolated as fractional algorithm states.', ['Identify the matrix dimensions, coefficient field and current operation.', 'Inspect the entries or rows used by that operation.', 'Apply the exact arithmetic to the marked destination.', 'Check the displayed equality, equivalence or rank restriction.']),
 'array':('Physical slots stay fixed. Read/write indices, logical length and object identity have separate meanings. A copy changes a destination value, not the identity of the source slot.', ['Locate the source, destination and valid storage boundaries.', 'Read the source before overwriting any value still needed.', 'Apply the stated copy, shift, swap or address calculation.', 'Check the logical result against the original input contract.']),
 'memory':('A name, its stored value and its designated object are different entities. The active statement reads the current store; a reference may share a live target.', ['Identify the active frame or current statement.', 'Read the needed values or addresses from the correct environment.', 'Apply the assignment, call, return or control-flow transfer.', 'Inspect which objects changed and which bindings stayed fixed.']),
 'derivation':('Each checkpoint is a justified algebraic or logical step. Read assumptions before using a cancellation, substitution or contradiction.', ['State the current assumptions and exact claim.', 'Identify the rule authorizing the next transformation.', 'Apply that rule without changing its variable convention.', 'Check the resulting expression and any exceptional case.']),
 'numeric':('Use the stated radix, word width, coefficient domain and rounding rule. Exact arithmetic and a finite representation must not be confused.', ['Read the original inputs and numerical representation.', 'Identify the current quotient, remainder, bit, carry or accumulator.', 'Apply the stated exact operation or explicit rounding rule.', 'Check the conservation equation and termination condition.']),
 'probability':('Areas and weights represent probability mass under the specified model. Conditioning retains mass and then normalizes; it does not make unequal atoms equiprobable.', ['Identify the original atoms, weights and observation protocol.', 'Retain or reweight exactly the states allowed by the observation.', 'Normalize using the same positive denominator for all retained states.', 'Check the target event, dependence assumption and total mass.']),
 'plot':('Axes and scales are fixed across this scenario. Marks are exact saved samples; connecting segments are visual orientation unless a continuous model is explicitly defined.', ['Read the horizontal parameter and vertical quantity.', 'Locate the current exact sample on the fixed scale.', 'Compare it with the preceding sample using the displayed formula.', 'Keep a finite observation separate from a general theorem.']),
 'tree':('Follow parent/child dependencies and distinguish a pending call from a completed return. Node labels state size or work, not interchangeable quantities.', ['Read the current call, level or dependency node.', 'Check the smaller subproblem or required child results.', 'Expand, combine or return according to the stated contract.', 'Account for the exact toll and completed dependency.']),
 'enumeration':('Every counted object follows the stated ordering, repetition and feasibility rules. A canonical representative prevents counting one unordered object repeatedly.', ['Read whether order and repetition are allowed.', 'Construct the current admitted object.', 'Check feasibility and canonical representation.', 'Count that distinct object exactly once.']),
 'tiles':('New tiles or coins show the added row, border or smaller established construction. The finite picture illustrates the induction step; it does not replace its proof.', ['Identify the established smaller construction.', 'Locate the new row, border or coin added by this step.', 'Compute the exact increment.', 'Check that the new total satisfies the claimed formula.']),
 'kmap':('Gray order defines adjacency, including wraparound. Required cells, optional cells, selected cubes and selection variables remain distinct.', ['Read the ON, OFF and don’t-care obligations.', 'Inspect the proposed cube, merge or prime-chart selection.', 'Check legality and required coverage before cost.', 'Compare product and literal costs only among feasible covers.']),
 'waveform':('Signals are binary between scheduled events. The moving cursor denotes time; it does not interpolate a logic value between zero and one.', ['Read the declared delays and initial settled state.', 'Locate the next scheduled event time.', 'Update only signals whose events occur at that time.', 'Compare the output pulse with the steady Boolean function.']),
 'circuit':('Connections are electrical topology, not decorative arrows. Wire colors denote known logic levels; unknown gates remain unevaluated until their prerequisites are available.', ['Read input polarities and fixed gate ports.', 'Inspect the current gate, valuation or scheduled event.', 'Apply the declared gate function or delay model.', 'Check the output, fault witness or timing restriction.']),
 'cmos':('The pull-up and pull-down topologies stay fixed. Green channels conduct; an input change switches channel state without moving a transistor.', ['Read both input values.', 'Determine which pMOS and nMOS channels conduct.', 'Trace a complete path to the relevant supply rail.', 'Check the stable output and the complementary network.']),
}

MODE_GUIDES={
 'order':['Identify the end at which insertion is allowed.', 'Locate the next removable item under the stated LIFO or FIFO rule.', 'Perform one public operation.', 'Compare the resulting logical order with the storage representation.'],
 'ring':['Read front, count and physical capacity.', 'Compute the insertion or removal position modulo capacity.', 'Check the full or empty guard before touching storage.', 'Update the boundary and count, then read the logical FIFO order.'],
 'two':['Push enqueued items onto the input stack.', 'Inspect the output stack before removal.', 'Transfer the entire input stack only when the output stack is empty.', 'Remove its top and account for the transfer cost and potential.'],
 'two-bad':['Read the queue order promised before the transfer.', 'Follow the deliberately incorrect transfer into a nonempty output stack.', 'Locate the older item buried by the new transfer.', 'Compare the next removal with the FIFO contract.'],
 'postfix':['Read the next operand or operator token.', 'Push an operand; for a binary operator pop the right operand before the left.', 'Compute left operator right using the stated exact arithmetic.', 'Push the result and check the remaining operand stack.'],
 'infix':['Read the next token and the operator-stack top.', 'Apply the stated precedence and associativity rule.', 'Emit only the operators justified by that rule.', 'Handle parentheses as boundaries and drain the remaining operators.'],
 'brackets':['Read the next opening or closing delimiter.', 'Push an opener or compare a closer with the stack top.', 'Reject a mismatched or unmatched closer immediately.', 'Accept a complete input only when the delimiter stack is empty.'],
 'monostack':['Read the current index and the required comparison direction.', 'Apply the explicitly stated equality rule.', 'Pop precisely the candidates invalidated or resolved by the current value.', 'Retain indices when the required answer is a position or distance.'],
 'histogram':['Read the bar height and its index.', 'Apply the stated stack tie rule and identify bars whose right boundary is known.', 'For each resolved bar compute its width from the remaining left boundary.', 'Use the terminal sentinel to resolve bars still pending.'],
 'window':['Advance the right boundary and remove expired indices.', 'Remove candidates dominated under the stated value and tie rule.', 'Retain a deque of eligible candidate indices.', 'Read the current answer at the front only after enforcing the window boundaries.'],
 'permutation':['Read the next required output.', 'Push unused increasing inputs until that output is available.', 'Pop only a matching stack top.', 'Treat an unreachable required output as an impossibility witness.'],
 'catalan':['Read push and pop events as up and down steps.', 'Track stack height after each event.', 'Reject a prefix with negative height.', 'A completed balanced history ends at height zero.'],
 'aggregate':['Read the operand order and the associative combine function.', 'Update stored aggregates without commuting operands.', 'Combine the front and back summaries in logical order.', 'Compare the result with the aggregate of the complete logical sequence.'],
 'restore':['Locate the protected bottom or front part of the structure.', 'Move only the permitted items to the temporary structure.', 'Perform the required observation or insertion.', 'Restore the original logical order using the stated sequence of operations.'],
 'recursive':['Read the active call frame and suspended continuation.', 'Follow the descent without merging distinct parameter objects.', 'Compute the base return value.', 'Resume each suspended caller once in reverse call order.'],
 'linked':['Identify live nodes and head/tail references.', 'Save each successor needed after a write.', 'Reconnect declared ports using the stated operation.', 'Check reachability and the final head/tail contract.'],
 'shared':['Read both stack boundaries and the common allocation.', 'Inspect the gap between the occupied regions.', 'Insert only when the next position is within that gap.', 'Update the appropriate top while preserving the other stack.'],
 'deque':['Read the front and back ends of the logical sequence.', 'Choose the end specified by the operation.', 'Insert or remove only at that end.', 'Check the resulting order and any capacity guard.'],
 'josephus':['Read the live circular order and current count origin.', 'Count the specified number of live items.', 'Remove the selected item and move the origin as stated.', 'Repeat on the remaining circle until the stated stopping condition.'],
}

def dump(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def signature(v):return hashlib.sha256(json.dumps(v,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
def mathematical(v):
 if isinstance(v,dict):return {k:mathematical(x) for k,x in v.items() if k not in ('teaching','teachingPolicy')}
 if isinstance(v,list):return [mathematical(x) for x in v]
 return v
def delta(a,b,path=''):
 if a==b:return []
 if isinstance(a,dict) and isinstance(b,dict):
  return [x for k in sorted(set(a)|set(b)) for x in delta(a.get(k),b.get(k),path+'.'+k if path else k)]
 if isinstance(a,list) and isinstance(b,list) and len(a)==len(b):
  return [x for i,(aa,bb) in enumerate(zip(a,b)) for x in delta(aa,bb,path+'['+str(i)+']')]
 return [dict(field=path or 'state',before=a,after=b)]
def state(f):
 if f.get('snapshot') is not None:v=copy.deepcopy(f['snapshot'])
 elif f.get('state') is not None:v=copy.deepcopy(f['state'])
 elif f.get('rows'):v={r['name']:r.get('values',r.get('cells')) for r in f['rows']}
 elif f.get('nodes'):v={n['id']:n['label'] for n in f['nodes'] if n.get('label')}
 else:v={k:x for k,x in f.items() if k not in ('svg','html','formulaHtml','caption','captionHtml','teaching')}
 if f.get('metrics'):v={**v,'counters':f['metrics']}
 return v
def exact_check(id,f,prev):
 s=f.get('snapshot') or {};out=[]
 def add(expr,result):out.append(dict(mathHtml=render(expr),result=str(result),expression=expr))
 if 'inputs' in s and 'left' in s and 'right' in s:add(str(s['left'])+'='+str(s['right']),s['left']==s['right'])
 if id.startswith('set-') and s.get('inspected'):
  v=s['inspected'][-1];a=v in s['A'];b=v in s['B'];rule={'set-union':a or b,'set-intersection':a and b,'set-difference':a and not b,'set-symmetric':a!=b,'set-complement':not a,'set-set-demorgan':not(a or b)}[id]
  add(str(v)+r'\in R',rule)
  assert (v in s['result'])==rule,(id,v)
 if id in ('lower-bound','search-stall') and f.get('line')==1:
  mid=(s['lo']+s['hi'])//2;add(str(s['array'][mid])+'<'+str(s['target']),s['array'][mid]<s['target'])
 if id in ('partition3','partition-skip') and f.get('line')==1:
  v=s['array'][s['i']][1];p=s['pivot'];add(str(v)+'<'+str(p),v<p);add(str(v)+'='+str(p),v==p);add(str(v)+'>'+str(p),v>p)
 if id in ('insertion','insertion-unstable') and f.get('line')==2:
  j=f['metrics']['Scan'];a=s['array'][j][1];b=s['saved'][1];eq=id.endswith('unstable');add(str(a)+(r'\ge ' if eq else '>')+str(b),a>=b if eq else a>b)
 if id=='merge' and f.get('line')==1:
  a=s['left'][s['i']][1];b=s['right'][s['j']][1];add(str(a)+r'\le '+str(b),a<=b)
 if id=='division':add(str(s['X'])+'='+str(s['q'])+r'\cdot '+str(s['Y'])+'+'+str(s['r']),s['X']==s['q']*s['Y']+s['r'])
 if id=='euclid':add(str(s['a'])+'='+str(s['A'])+r'\cdot('+str(s['x0'])+')+'+str(s['B'])+r'\cdot('+str(s['y0'])+')',s['a']==s['A']*s['x0']+s['B']*s['y0'])
 if id in ('power','modular-power'):
  a=s['r']*s['b']**s['e'];b=s['x']**s['y'];mod=s['M'];add('r b^e'+(r'\equiv x^y\pmod{'+str(mod)+'}' if mod else '=x^y'),a%mod==b%mod if mod else a==b)
 if id=='conditional-bridge':add(r'\text{path from s to t}',s['connected'])
 if id in ('arr-search',) and 'equal' in s:add(r'\text{inspected text key = pattern key}',s['equal'])
 if id=='km-petrick':add(r'\text{all selection clauses satisfied}',all(s['satisfied']))
 if id in ('km-corners','km-cycle','km-greedy','km-dc','km-hazard-cover'):
  add(r'\text{all required one cells covered}',set(s['on'])<=set(s['covered']))
 if id in ('comb-miter',):add(str(s['f'])+r'\oplus '+str(s['g']),s['f']^s['g'])
 if id=='comb-feedback':add(r'\text{number of Boolean fixed points}',len(s['solutions']))
 if id in ('bayes-normalize','conditional-atoms') and ('values' in s or 'masses' in s):
  vals=s.get('values',s.get('masses'));add(r'\sum_i w_i',str(sum(map(Fraction,vals))))
 return out

def family(kind):
 k=kind.lower()
 if k in ('canonical-truth-rows','truth-contract'):return 'truth'
 if k in ('choice-tree','binary-decision-tree'):return 'tree'
 if k in ('occupancy-bars','bin-occupancies','balanced-bin-witness','finite-stock-selection'):return 'enumeration'
 if any(w in k for w in ('gate','circuit','multiplex','carry','truth','and-trees')):return 'circuit'
 if any(w in k for w in ('matrix','row-reduction','coordinate')):return 'matrices'
 if any(w in k for w in ('probab','mass','event','bayes')):return 'probability'
 if any(w in k for w in ('karnaugh','rook','board')):return 'kmap'
 if any(w in k for w in ('array','storage','buffer','shift','linked','address','stack','queue','ring','deque','list','permutation','postfix','bracket','two','restore','shared','order','resize','batch')):return 'array'
 if any(w in k for w in ('bin','fiber','object','matching','chain','bipartite','graph','subsequence')):return 'graph'
 if any(w in k for w in ('occupancy','selection','rotation','choice','inventory','star','allocation','pair','compression')):return 'enumeration'
 return 'derivation'

def enrich(m,id,kind,scene=False):
 typ=kind if scene else family(kind);reading,guide=POLICIES[typ];frames=m['frames'];audit=[]
 if not scene:
  guide=MODE_GUIDES.get(kind,guide)
  if m.get('invariant'):reading=m['invariant']+' '+reading
 for i,f in enumerate(frames):
  current=state(f);prior=state(frames[i-1]) if i else None
  changes=delta(prior,current) if i else []
  code=m.get('code') or guide;line=f.get('line',0)
  op=code[min(line,len(code)-1)] if scene and m.get('code') else f['caption'].split('. ')[0].rstrip('.')+'.'
  checks=exact_check(id,f,frames[i-1] if i else None) if scene else []
  t=dict(operation=op,why=f['caption'],reading=reading,guide=code,activeLine=line if m.get('code') else None,checks=checks,changes=changes,currentState=current,initial=i==0,mode=typ,counterexample=bool(f.get('counterexample') or 'counterexample' in kind.lower()),scope=m.get('invariant',m.get('scope',m.get('invariantHtml',''))))
  f['teaching']=t;audit.append(dict(step=i,operation=op,checkCount=len(checks),changedFields=len(changes),counterexample=t['counterexample']))
 m['teachingPolicy']=dict(mode=typ,reading=reading,guide=guide)
 return dict(id=id,kind=kind,frames=len(frames),steps=audit,mathematicalPayloadRetained=True)

def main():
 files=['concept-animations.json','a_arrays-models.json','a_stackqueue-models.json','d_counting-models.json','d_inclusion-models.json','d_pigeonhole-models.json','problem-visual-models.json']
 rows=[];checks=0
 for name in files:
  p=D/name;data=json.loads(p.read_text(encoding='utf-8'));before=signature(mathematical(data));models=data['scenes'].items() if name=='concept-animations.json' else data.items() if name.startswith('problem-') else [(m['id'],m) for m in data['models']]
  rr=[]
  for id,m in models:
   rr.append(enrich(m,id,m['visual']['type'] if name=='concept-animations.json' else m['kind'],name=='concept-animations.json'))
  assert before==signature(mathematical(data)),name
  dump(p,data);rows.append(dict(file=name,models=len(rr),frames=sum(r['frames'] for r in rr),payloadSha256=before,modelsReviewed=rr));checks+=sum(s['checkCount'] for r in rr for s in r['steps'])
 chapters=[]
 for p in sorted(D.glob('*.html')):
  if not re.match(r'^[daslgp]_',p.stem):continue
  source=p.read_text(encoding='utf-8')
  # Stored baseline HTML is used for the final independent retention comparison.
  import subprocess
  baseline=subprocess.check_output(['git','show',BASELINE+':dist/chapters/'+p.name],cwd=R).decode('utf-8')
  (O/'baseline').mkdir(exist_ok=True);(O/'baseline'/p.name).write_text(baseline,encoding='utf-8')
  chapters.append(dict(topicId=p.stem,questions=len(re.findall(r'class="exam-question"',source)),players=len(re.findall(r'class="concept-animation"|data-(?:problem-visual|arrays-model|sq-model|counting-model|inclusion-model|pigeonhole-model|sort-model)=',source))))
 dump(O/'inventory.json',dict(state='in_progress',scope='Every existing chapter animation; no new chapter.',baselineCommit=BASELINE,chapters=chapters,files=rows,checksDerived=checks))
 print(json.dumps(dict(chapters=len(chapters),models=sum(x['models'] for x in rows),frames=sum(x['frames'] for x in rows),explicitChecks=checks)))
if __name__=='__main__':main()

from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1];B=R/'research';E=B/'a_hash-evidence'
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
p=R/'dist/chapters/a_hash.js';s=p.read_text(encoding='utf-8')
s=s.replace("const rect=(id", """function nativeFormula(z){if(!z.formula)return '';const n=v=>v<0?'<mo>−</mo><mn>'+(-v)+'</mn>':'<mn>'+v+'</mn>';let body='';
if(z.kind==='horner')body='<msub><mi>H</mi>'+n(z.extra.prefix)+'</msub><mo>=</mo><mo>(</mo>'+n(z.extra.base)+'<mo>·</mo>'+n(z.extra.previous)+'<mo>+</mo>'+n(z.key)+'<mo>)</mo><mo>mod</mo>'+n(z.capacity)+'<mo>=</mo>'+n(z.extra.value);
else if(z.kind==='shift'&&z.extra.distanceToHole!==undefined)body='<mi>D</mi><mo>(</mo><mi>h</mi><mo>,</mo><mi>u</mi><mo>)</mo><mo>=</mo>'+n(z.extra.distanceToHole)+'<mspace width="1em"/><mi>D</mi><mo>(</mo><mi>h</mi><mo>,</mo><mi>v</mi><mo>)</mo><mo>=</mo>'+n(z.extra.distanceToSlot);
else body='<mi>h</mi><mo>(</mo>'+n(z.key)+'<mo>)</mo><mo>=</mo>'+n(z.key)+'<mo>mod</mo>'+n(z.capacity)+'<mo>=</mo>'+n(mod(z.key,z.capacity));return '<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow>'+body+'</mrow></math>';}
const rect=(id""")
s=s.replace('formula:z.formula,duration:', 'formula:z.formula,formulaHtml:nativeFormula(z),duration:').replace('operation:z.action,why:',"operation:'Hash-table operation: '+z.action,why:")
p.write_text(s,encoding='utf-8')
p=B/'build_a_hash.py';s=p.read_text(encoding='utf-8');s=s.replace("If duplicate keys are legal,", "This construction assumes insertion appends to the list, so a stable arrival identifier gives the left-to-right tie order. If insertion instead chooses an arbitrary list position, additional order-maintenance machinery and its costs must be analyzed. If duplicate keys are legal,")
p.write_text(s,encoding='utf-8')
qs=json.loads((B/'a_hash-questions.json').read_text(encoding='utf-8'))
notes=[]
for i,q in enumerate(qs,1):
 notes.append(dict(question=q['id'],decision='specialized inspectable companion'if q.get('modelId')else'complete written derivation or finite counterexample',modelId=q.get('modelId'),scope=q.get('visualQualification'),reason='Exact routes and changing placement benefit from inspectable checkpoints.'if q.get('modelId')else'Primary reasoning is an algebraic expectation, arithmetic identity, proof, interface contract or design comparison. No unrelated decorative animation attached.'))
save(E/'problem-visual-decisions.json',notes)
save(E/'concept-inventory.json',dict(arithmetic=['horner'],bucketOrder=['chaining'],lookupAndClusters=['linear'],markerAndUpdateInvariants=['tombstone','update','reuse','all-markers'],backwardRepair=['shift','mixed-shift'],routeCoverage=['square','square-failure','alternating','triangular','double','double-failure'],capacityChange=['rebuild'],fixedSetPlacement=['perfect'],approximateFilter=['bloom'],candidatePlacement=['cuckoo','cuckoo-failure'],displacementExchange=['robin'],boundaries='Probabilistic formulas are derived in text and checked by independently enumerated finite spaces; deterministic drawings are not mislabeled random-distribution proofs.'))
print('Completed problem visual decisions, concept inventory and editable native formulas.')

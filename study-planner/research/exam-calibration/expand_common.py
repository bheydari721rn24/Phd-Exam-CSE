"""Original problem-family authoring with explicit variation and solution provenance."""
from pathlib import Path
from fractions import Fraction
import json,math
BASE=Path(__file__).resolve().parent
baseline=json.loads((BASE/'tripling-baseline.json').read_text())
actual=json.loads((BASE/'actual-items.json').read_text())
questions=[]
def S(s,**args):
 for k,v in args.items():s=s.replace('@'+k+'@',str(v))
 return s
def fm(n):
 if isinstance(n,Fraction):return '$'+(str(n.numerator) if n.denominator==1 else r'\frac{'+str(n.numerator)+'}{'+str(n.denominator)+'}')+'$'
 return '$'+str(n)+'$'
def add(t,key,title,stem,answer,wrong,solution,kind='calculation',level='Medium',audit=None):
 choices=[answer]+list(wrong);assert len(choices)==4 and len(set(choices))==4,(t,key,choices)
 shift=sum(map(ord,key))%4;choices=choices[shift:]+choices[:shift];correct=choices.index(answer)+1
 assert len(solution.split())>=45,(t,key,'short solution')
 refs=[a['id'] for a in actual if a['answer'] is not None and t in a['topics']]
 questions.append(dict(id=t+'-'+key,topic=t,title=title,stem=stem,options=choices,answer=correct,solution=solution,pattern='; '.join(refs[:2]),difficulty=level,kind='Original expanded examination problem',questionType=kind,family=key.rsplit('-',1)[0],audit=audit))
def number(t,key,title,stem,value,wrong,solution,kind='calculation',audit=None):
 add(t,key,title,stem,fm(value),[fm(x) for x in wrong],solution,kind,audit=audit)
def concept(t,key,title,stem,correct,wrong,solution):
 add(t,key,title,stem,correct,wrong,solution,'conceptual boundary',level='Hard' if key.endswith('-4') else 'Medium')
def save(name):
 assert len({q['id'] for q in questions})==len(questions)
 (BASE/name).write_text(json.dumps(questions,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
 print(name,len(questions))
def C(n,k):return math.comb(n,k) if 0<=k<=n else 0
def family(t,key,title,model,formula,wrong_formulas,calculate,errors,derive,boundary,boundary_wrong,boundary_reason,seeds=(5,8),domain='the positive-integer parameter domain, subject to the additional conditions stated above'):
 """Two exact instances, one generalization, one applicability/counterexample task.

 Variants are openly identified as members of a common family. Formula problems
 carry their model, substitution, derivation and the actual distractor results.
 """
 for i,n in enumerate(seeds,1):
  v=calculate(n); ws=[f(n) for f in errors]
  assert len(set([v]+ws))==4,(t,key,n,v,ws)
  stem=S(model,n=n)+' Calculate the requested quantity for '+S(r'$n=@n@$.',n=n)
  sol='**Step 1 — model and conditions.** '+derive+'\n\n**Step 2 — compute.** The general expression is '+formula+'. Substituting '+S(r'$n=@n@$',n=n)+' gives '+fm(v)+'. Keep the exact value until all constraints have been applied.\n\n**Step 3 — audit the alternatives.** The other listed values are '+', '.join(fm(x) for x in ws)+'. They are obtained from the three competing expressions '+', '.join(wrong_formulas)+', respectively. Those expressions discard or alter a condition in the model; the derivation above shows where the discrepancy enters. Recomputing the defining constraints, rather than selecting the numerically nearest option, determines the answer.'
  number(t,key+'-'+str(i),title+' — exact instance '+str(i),stem,v,ws,sol,audit=dict(family=key,n=n,expected=str(v)))
 concept(t,key+'-3',title+' — symbolic generalization',S(model,n='n')+' Which general expression gives the requested quantity for all parameters in '+domain+'?',formula,wrong_formulas,'**Derive before generalizing.** '+derive+' Therefore the expression is '+formula+'. The three alternatives '+', '.join(wrong_formulas)+' violate the counting, algebraic or model conditions identified in that derivation. The exact instances above are useful checks, but agreement at one special parameter does not establish a general identity. The quantifier in this question requires validity over the entire specified parameter domain.')
 concept(t,key+'-4',title+' — applicability and boundary',S(model,n='n')+' Which statement correctly identifies the scope or a failure of this method?',boundary,boundary_wrong,'**Check the hypothesis.** '+boundary_reason+'\n\n**Connect it to the calculation.** '+derive+' The valid statement is: '+boundary+' A formula can remain numerically correct in one exceptional case after its assumptions are removed, but that does not justify using it as a general rule. Distinguish the mathematical identity from the modeling assumptions that permit this identity to count or measure the requested objects.')

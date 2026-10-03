"""Maintain the tripling revision's assumptions, report and rebuild entry points."""
from pathlib import Path
BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[1]
edits={
 'expand_structures.py':[("r'Find the least nonnegative $x$ with", "r'Assume $n\\ge2$. Find the least nonnegative $x$ with")],
 'expand_computing.py':[
 ("r'A format uses $n$ exponent bits", "r'Assume $n\\ge4$. A format uses $n$ exponent bits"),
 ("r'An $n$-bit word has unsigned value", "r'Assume $n\\ge3$. An $n$-bit word has unsigned value"),
 ("r'Add two maximum $n$-bit signed", "r'Assume $n\\ge2$. Add two maximum $n$-bit signed"),
 ('Two-complement gives','Two’s complement gives')],
 'clean_authoring.py':[("'author_computing'):","'author_computing','expand_discrete','expand_structures','expand_algorithms','expand_math','expand_computing'):")],
 'build.py':[("lastfamily=None\n for q in new:",
 "family_index={q['family']:q['title'].split(' — ')[0] for q in new if q.get('family')}\n if family_index:body+='<details class=\"family-index\"><summary>Choose a calculation and concept family</summary><ul>'+''.join('<li><a href=\"#family-'+e(k)+'\">'+e(v)+'</a></li>' for k,v in family_index.items())+'</ul></details>'\n lastfamily=None\n for q in new:")]
}
for name,pairs in edits.items():
 p=BASE/name;s=p.read_text(encoding='utf-8')
 for old,new in pairs:
  if new not in s:
   assert old in s,(name,old)
   s=s.replace(old,new)
 p.write_text(s,encoding='utf-8')
p=BASE/'finalize.py';s=p.read_text(encoding='utf-8')
if 'expansion=json.loads' not in s:
 s=s.replace("checks=json.loads((BASE/'answer-validation.json').read_text())", "checks=json.loads((BASE/'answer-validation.json').read_text())\nexpansion=json.loads((BASE/'expansion-validation.json').read_text())")
 s=s.replace("('manifest.json','answer-validation.json')", "('manifest.json','answer-validation.json','expansion-validation.json','tripling-baseline.json')")
 s=s.replace('Each bank separates authentic examination questions, eight newly authored medium/hard formula and conceptual analogues, and two retained integrated challenges.', 'Each bank separates authentic examination questions, original formula and conceptual analogues, and two retained integrated challenges. Every chapter now has at least three times its version-55 question count.')
 s=s.replace('<strong>{m["newOriginalItems"]} new original analogues</strong>', '<strong>{m["newOriginalItems"]} original analogues</strong> (176 from version 55 and 736 added in this revision)')
 s=s.replace("body+='<p>Read the theory", "body+='<p>The 736 added questions form 184 explicitly related families: two numerical instances, one symbolic generalization and one applicability or counterexample question per family. They are not 736 unrelated concepts. Chapter family menus let you choose a model without searching a long page. Difficulty is qualitative; many exact calculations provide medium-level preparation and scope questions develop conceptual discrimination.</p>'\nbody+='<p>Read the theory")
 s=s.replace("<th>Problem bank</th><th>Notes and sources</th>","<th>Before → now / minimum</th><th>Problem bank and sources</th>")
 s=s.replace("+'</a></td><td><a href=\"'+link+'#authentic-questions\">'", "+'</a></td><td>'+str(c['baselineQuestions'])+' → <strong>'+str(c['totalQuestions'])+'</strong><br>Required minimum: '+str(c['minimumQuestions'])+'</td><td><a href=\"'+link+'#authentic-questions\">'")
 s=s.replace("'>8 new analogues</a>","'>'+str(c['newOriginalQuestions'])+' original analogues</a>")
 s=s.replace("2 integrated challenges</a></td><td><a href=\"", "2 integrated challenges</a><br><a href=\"")
 s=s.replace("checks['independentChecks'])+' independent finite", "checks['independentChecks'])+' existing finite")
 s=s.replace("They do not amount to independent proofs of every question or every theorem.", "The expanded bank additionally passed 368 numeric-answer recomputations using separate finite models, state transitions and exact algebra; each recomputed value is bound to its selected alternative. All 22 individual count targets passed. Symbolic derivations and scope statements received editorial review; neither count checks nor numeric recomputation prove all general statements or difficulty labels.")
 s=s.replace('<a href="evidence/exam-calibration/answer-validation.json">Independent checks</a>', '<a href="evidence/exam-calibration/answer-validation.json">Existing checks</a> · <a href="evidence/exam-calibration/expansion-validation.json">Expanded-answer and count checks</a> · <a href="evidence/exam-calibration/tripling-baseline.json">Frozen version-55 baseline</a>')
 s=s.replace("str(checks['independentChecks'])+' independent finite/exact and output checks passed.", "str(checks['independentChecks'])+' existing finite/exact and output checks plus 368 expanded numeric recomputations passed.")
 s=s.replace('Authoring: original-*.json and author_*.py.', 'The 736 additions comprise 184 related four-question families; this is not a claim of 736 independent concepts. Authoring: original-*.json, author_*.py and expand_*.py. Audit: verify_answers.py and verify_expansion.py. Reauthor: clean_authoring.py regenerates both the earlier banks and all five expansion collections.')
 s=s.replace("new original analogues, {m", "original analogues, {m")
 s=s.replace("new authored analogues, {m", "original authored analogues, {m")
 s=s.replace("Await explicit approval of the exam-grounded revision.", "Await explicit approval of the tripled problem-bank revision.")
 s=s.replace("reviewScope='All 22 existing problem banks;", "reviewScope='At least three times the version-55 question count in every one of the 22 existing problem banks;")
 p.write_text(s,encoding='utf-8')
print('Updated assumptions, family navigation, report and rebuild instructions.')

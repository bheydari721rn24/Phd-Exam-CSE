from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_deep_logic_browser.py').read_text()
s=s.replace('deep-logic-browser','deep-sets-browser').replace('d_logic','d_sets')
s=s.replace("==53","==46").replace("==12","==7")
a=s.index(" for kind in['imp'");b=s.index(' for n in[2,5,6,19,50,52,53]')
s=s[:a]+''' for value in range(8):
  a,b,c=(bool(value&4),bool(value&2),bool(value&1))
  code='(()=>{'+''.join('document.getElementById('+json.dumps(name)+').value='+json.dumps('1'if flag else'0')+';'for name,flag in zip(['in-a','in-b','in-c'],[a,b,c]))+'document.getElementById("in-a").dispatchEvent(new Event("change"));return [...document.querySelectorAll("#set-lab-output tbody tr")].map(r=>r.lastElementChild.textContent);})()'
  got=js(code);want=['Yes'if flag else'No'for flag in[a and(b or c),(a and b)or(a and c),a!=(b and c),(a!=b)and(a!=c)]]
  assert got==want,(value,got,want)
  assert js('document.querySelectorAll("#set-lab-output math").length')==4
  report['lab'].append({'membershipBits':value,'verifiedExpressions':4})
'''+s[b:]
s=s.replace('for n in[2,5,6,19,50,52,53]','for n in[3,5,6,21,27,32,44,45,46]')
s=s.replace("if width==390:capture('.exam-question[data-deep-index=\"2\"]','question-2-mobile.png');capture('.exam-question[data-deep-index=\"5\"]','question-5-mobile.png')","if width==390:capture('.exam-question[data-deep-index=\"3\"]','question-3-mobile.png');capture('.exam-question[data-deep-index=\"21\"]','question-21-mobile.png')")
s=s.replace(" report['lab']=[]"," capture('.concept-animation','set-animation.png')\n report['lab']=[]")
(B/'qa_deep_sets_browser.py').write_text(s)
print('Prepared sets-specific browser checks.')

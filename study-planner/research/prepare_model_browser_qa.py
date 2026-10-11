from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_deep_induction_browser.py').read_text().replace('d_induction','a_model').replace('deep-induction-browser','deep-model-browser').replace('==12','==6')
a=s.index(' for host,key,name in');z=s.index(" report['staticDiagrams']",a)
s=s[:a]+''' for frame,name in [(0,'merge-first.png'),(15,'merge-middle.png'),(22,'merge-final.png')]:
  js('(()=>{const h=document.querySelector(".question-specific-animation");const c=ConceptAnimations.players.find(c=>c.api.host===h || h.contains(c.api.host));c.api.show('+str(frame)+');})()')
  capture('.question-specific-animation',name)
'''+s[z:]
a=s.index(" capture('.question-specific-diagram'");z=s.index(' for n in[',a)
s=s[:a]+''' capture('.exam-question[data-deep-index="12"] svg','question-12-depths.png')
'''+s[z:]
s=s.replace('[2,3,4,6,9,17,28,36,45,46]','[1,2,3,4,6,9,12,19,45,46]').replace('induction-animation.png','model-animation.png').replace('induction-dependency.png','model-representation.png')
s=s.replace("if width==390:capture('.exam-question[data-deep-index=\"3\"]','question-3-mobile.png');capture('.exam-question[data-deep-index=\"6\"]','question-6-mobile.png')", "if width==390:capture('.exam-question[data-deep-index=\"3\"]','question-3-mobile.png');capture('.exam-question[data-deep-index=\"6\"]','question-6-mobile.png');capture('.question-specific-animation','merge-mobile.png')")
(B/'qa_deep_model_browser.py').write_text(s)

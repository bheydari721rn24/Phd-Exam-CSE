from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_deep_proof_browser.py').read_text()
s=s.replace('deep-proof-browser','deep-induction-browser').replace('d_proof','d_induction').replace('==48','==46').replace('==8','==12')
s=s.replace('proof-animation.png','induction-animation.png').replace('proof-strategies.png','induction-dependency.png').replace('question-6-shift.png','question-3-mass.png')
s=s.replace('for n in[2,3,5,6,8,19,31,42,47,48]','for n in[2,3,4,6,9,17,28,36,45,46]')
s=s.replace('data-deep-index="8"','data-deep-index="6"').replace('question-8-mobile','question-6-mobile')
s=s.replace(" capture('.question-specific-diagram','question-3-mass.png')"," capture('.question-specific-diagram','question-3-mass.png')\n capture('.exam-question[data-deep-index=\"28\"] svg','question-28-shapes.png')\n capture('.question-specific-animation','question-46-reachability.png')")
(B/'qa_deep_induction_browser.py').write_text(s)
print('Prepared induction-specific browser checks.')

"""Adapt the chapter checks to the proof bank; there is no Boolean set lab here."""
from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_deep_sets_browser.py').read_text()
s=s.replace('deep-sets-browser','deep-proof-browser').replace('d_sets','d_proof')
s=s.replace('==46','==48').replace('==7','==8')
a=s.index(" report['lab']=[]");z=s.index(' for n in[3,5,6,21,27,32,44,45,46]')
s=s[:a]+" capture('.logic-diagram','proof-strategies.png')\n"+s[z:]
s=s.replace('set-animation.png','proof-animation.png').replace('for n in[3,5,6,21,27,32,44,45,46]','for n in[2,3,5,6,8,19,31,42,47,48]')
s=s.replace('question-21-mobile','question-8-mobile').replace('data-deep-index="21"','data-deep-index="8"')
s=s.replace(" capture('.logic-diagram','proof-strategies.png')",''' report['staticDiagrams']=js("""(()=>[...document.querySelectorAll('.logic-diagram svg')].map(svg=>{const v=svg.viewBox.baseVal;return{label:svg.getAttribute('aria-label'),outside:[...svg.querySelectorAll('text')].filter(t=>{const b=t.getBBox();return b.x<v.x||b.y<v.y||b.x+b.width>v.x+v.width||b.y+b.height>v.y+v.height;}).map(t=>t.textContent)}}))()""")
 assert all(not s['outside']for s in report['staticDiagrams']),report['staticDiagrams']
 capture('.logic-diagram','proof-strategies.png')
 capture('.question-specific-diagram','question-6-shift.png')''')
(B/'qa_deep_proof_browser.py').write_text(s)
print('Prepared proof-specific browser checks.')

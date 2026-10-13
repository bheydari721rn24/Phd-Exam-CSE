from pathlib import Path
import json,re
B=Path(__file__).parent;R=B.parent;s=(B/'qa_final_functions_browser.py').read_text(encoding='utf-8')
page=(R/'dist/chapters/d_invariants.html').read_text(encoding='utf-8');models=json.loads((R/'dist/chapters/concept-animations.json').read_text(encoding='utf-8'))['scenes']
hosts=re.findall(r'<section[^>]*class="concept-animation[^>]*data-scenes="([^"]+)"',page);ids=[id for group in hosts for id in group.split(',')];frames=sum(len(models[id]['frames'])for id in ids)
s=s.replace('deep-functions-browser','deep-invariants-browser').replace("'topicId':'d_functions'","'topicId':'d_invariants'").replace('/chapters/d_functions.html','/chapters/d_invariants.html')
s=s.replace("['questions']==47", "['questions']==46").replace("['solutions']==47","['solutions']==46").replace("['tutorials']==42","['tutorials']==49")
s=s.replace("len(report['models'])==48", "len(report['models'])=="+str(len(ids))).replace("len(report['frameRendering'])==758","len(report['frameRendering'])=="+str(frames))
s=s.replace("len(report['controls'])==46","len(report['controls'])=="+str(len(hosts))).replace("range(0,46,5)","range(0,"+str(len(hosts))+",5)").replace("len(report['playback'])==46","len(report['playback'])=="+str(len(hosts)))
selectors=sum(len(group.split(','))for group in hosts if ','in group)
s=s.replace("len(report['selection'])==4","len(report['selection'])=="+str(selectors))
s=s.replace('for n in[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,22,23,26,30,31,34,35,38,39,42,43,46,47]:','for n in[1,2,3,4,5,6,7,8,9,10,11,12,13,14,17,18,21,22,25,26,29,30,33,34,37,38,41,42,45,46]:')
a=s.index(" report['functionLab']=[]");z=s.index(" for i in range(len(report['staticDiagrams'])):",a)
lab=r'''
 report['invariantsLab']=[]
 def flags():return js("({...document.getElementById('invariant-output').dataset})")
 assert flags()=={'safe':'true','preserved':'false','terminates':'true'},flags()
 for name,expected in [('noninductive',('true','false','true')),('inductive',('true','true','false')),('unsafe',('false','false','true')),('chain',('true','true','true')),('cycle',('true','true','false')),('badrank',('true','true','true'))]:
  js('document.querySelector("[data-preset='+name+']").click()');actual=flags();assert tuple(actual[k]for k in('safe','preserved','terminates'))==expected,(name,actual);report['invariantsLab'].append(dict(preset=name,flags=actual))
 assert 'Invalid on reachable edges' in js("document.getElementById('invariant-output').textContent")
 js('document.querySelector("[data-preset=chain]").click();document.querySelector(\'[data-member="0"]\').click()');assert flags()['safe']=='false';assert 'initial state 0 is excluded'in js("document.getElementById('invariant-output').textContent");report['invariantsLab'].append(dict(case='exclude initial state',flags=flags()))
 js('document.querySelector("[data-preset=chain]").click();document.querySelector(\'[data-edge="0,0"]\').click()');assert flags()['terminates']=='false';report['invariantsLab'].append(dict(case='add reachable self-loop',flags=flags()))
 js('document.querySelector("[data-preset=chain]").click();const r=document.querySelector(\'[data-rank="0"]\');r.value="-1";r.dispatchEvent(new Event("change",{bubbles:true}));');assert js('document.querySelector(\'[data-rank="0"]\').validity.customError');report['invalidRankInput']=True
 js('document.querySelector("[data-preset=noninductive]").click()')
'''
s=s[:a]+lab+s[z:]
s=s.replace('data-functions-static-index','data-invariants-static-index')
# Questions four and six include real formulas and a mathematical solution.
s=s.replace("d_functions-browser.json","d_invariants-browser.json")
(B/'qa_final_invariants_browser.py').write_text(s,encoding='utf-8')
print({'players':len(hosts),'scenarios':len(ids),'frames':frames,'selectorEvents':selectors})

from pathlib import Path
B=Path(__file__).parent;s=(B/'qa_final_invariants_browser.py').read_text()
s=s.replace('deep-invariants-browser','deep-discrete-number-browser').replace('d_invariants','d_number').replace("==46 and report['counts']['solutions']==46","==47 and report['counts']['solutions']==47").replace("['tutorials']==49","['tutorials']==40")
s=s.replace("assert len(report['models'])==53 and", "assert len(report['models'])>=41 and")
s=s.replace("assert len(report['frameRendering'])==419 and", "assert len(report['frameRendering'])==sum(r['frames']for r in report['models']) and")
s=s.replace("assert len(report['controls'])==45 and", "assert len(report['controls'])==61 and")
s=s.replace("assert len(report['selection'])==16 and", "assert len(report['selection'])>=16 and")
s=s.replace('range(0,45,5)','range(0,61,5)').replace("assert len(report['playback'])==45 and","assert len(report['playback'])==61 and")
s=s.replace('for n in[1,2,3,4,5,6,7,8,9,10,11,12,13,14,17,18,21,22,25,26,29,30,33,34,37,38,41,42,45,46]:','for n in[1,2,3,4,5,6,7,8,9,10,11,12,13,14,18,22,26,30,34,38,42,46,47]:')
a=s.index(" report['invariantsLab']=[]");z=s.index(" for i in range(len(report['staticDiagrams'])):",a)
lab=r'''
 report['numberLab']=[]
 def flags():return js("({...document.getElementById('number-output').dataset})")
 for name,count,g,inverse in [('unit',1,1,'5'),('many',4,4,'none'),('none',0,4,'none'),('zero',6,6,'none'),('negative',1,1,'2')]:
  js('document.querySelector("[data-preset='+name+']").click()');actual=flags();assert actual==dict(count=str(count),gcd=str(g),inverse=inverse),(name,actual);assert js('document.querySelectorAll(".map-cell.solution").length')==count;report['numberLab'].append(dict(preset=name,flags=actual))
 for a,b,m,count,g,inverse in [(12,18,30,6,6,'none'),(0,1,1,1,1,'0'),(6,8,14,2,2,'none')]:
  js('document.getElementById("number-a").value='+str(a)+';document.getElementById("number-b").value='+str(b)+';document.getElementById("number-m").value='+str(m)+';document.getElementById("number-form").dispatchEvent(new Event("submit",{cancelable:true}))');actual=flags();assert actual==dict(count=str(count),gcd=str(g),inverse=inverse),(a,b,m,actual);report['numberLab'].append(dict(input=[a,b,m],flags=actual))
 js('document.getElementById("number-m").value=61;document.getElementById("number-m").dispatchEvent(new Event("change"))');assert js('document.getElementById("number-m").validity.rangeOverflow');report['invalidModulusInput']=True
 js('document.querySelector("[data-preset=many]").click();document.getElementById("number-a").value="";document.getElementById("number-a").dispatchEvent(new Event("change"))');assert js('document.getElementById("number-a").validity.valueMissing');report['missingCoefficientInput']=True
 js('document.querySelector("[data-preset=many]").click()')
'''
s=s[:a]+lab+s[z:];s=s.replace("['solutions']==46","['solutions']==47")
(B/'qa_final_discrete_number_browser.py').write_text(s,encoding='utf-8')

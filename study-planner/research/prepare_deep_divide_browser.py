from pathlib import Path
B=Path(__file__).parent;s=(B/'qa_final_algorithm_recurrence_browser.py').read_text().replace('a_recurrence','a_divide').replace('deep-algorithm-recurrence-browser','deep-divide-browser')
s=s.replace("==53","==46").replace("==40","==48").replace("len(report['selection'])>=16","len(report['selection'])>=0")
s=s.replace('1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,20,24,28,32,36,40,44,48,52,53','1,2,3,4,5,6,7,8,9,10,11,12,13,17,21,25,29,33,37,41,45,46')
a=s.index(" report['recurrenceLab']=[]");z=s.index(" for i in range(len(report['staticDiagrams']))",a)
s=s[:a]+''' report['summaryLab']=[]
 for name,expected in [('crossing',9),('negative',-2),('left',9),('ties',2)]:
  js('document.querySelector('+json.dumps('[data-preset='+name+']')+').click()');actual=js('({...document.getElementById("subarray-output").dataset})');assert int(actual['best'])==expected and actual['verified']=='true',(name,actual);report['summaryLab'].append(dict(preset=name,flags=actual))
 js('document.getElementById("subarray-input").value="3,-6,5,-5,1,6,-2";document.getElementById("subarray-split").value=5;document.getElementById("subarray-form").dispatchEvent(new Event("submit",{cancelable:true}))');actual=js('({...document.getElementById("subarray-output").dataset})');assert actual['best']=='7'and actual['start']=='2'and actual['end']=='6';report['summaryLab'].append(dict(preset='earliest-crossing-tie',flags=actual))
 js('document.querySelector("[data-preset=crossing]").click()')
'''+s[z:]
(B/'qa_deep_divide_browser.py').write_text(s,encoding='utf8');print('Browser check prepared')

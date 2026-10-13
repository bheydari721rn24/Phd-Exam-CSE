from pathlib import Path
B=Path(__file__).parent;s=(B/'qa_final_discrete_number_browser.py').read_text()
s=s.replace('deep-discrete-number-browser','deep-algorithm-recurrence-browser').replace('d_number','a_recurrence').replace('==47','==53').replace('>=41','>=46')
s=s.replace(" report['controls']=js("," report['playerCount']=js('ConceptAnimations.players.length');report['controls']=js(")
s=s.replace('==61',"==report['playerCount']").replace('range(0,61,5)',"range(0,report['playerCount'],5)")
a=s.index(" report['numberLab']=[]");z=s.index(' for i in range(len(report',a)
s=s[:a]+''' report['recurrenceLab']=[]
 for name,expected in [('leaves',496),('balanced',80),('root',496),('chain',7),('base',144)]:
  js('document.querySelector('+json.dumps('[data-preset='+name+']')+').click()');actual=js('({...document.getElementById("recurrence-output").dataset})');assert int(actual['total'])==expected and actual['total']==actual['levelTotal'],(name,actual);report['recurrenceLab'].append(dict(preset=name,flags=actual))
 js('document.getElementById("recurrence-h").value=0;document.getElementById("recurrence-base").value=20;document.getElementById("recurrence-form").dispatchEvent(new Event("submit",{cancelable:true}))');actual=js('({...document.getElementById("recurrence-output").dataset})');assert actual['total']=='20';report['recurrenceLab'].append(dict(preset='zero-depth-base-twenty',flags=actual))
 js('document.querySelector("[data-preset=balanced]").click()')
''' +s[z:]
s=s.replace("assert len(report['staticDiagrams'])>=4","assert len(report['staticDiagrams'])>=3")
s=s.replace('n in[1,2,3,4,5,6,7,8,9,10,11,12,13,14,18,22,26,30,34,38,42,46,47]','n in[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,20,24,28,32,36,40,44,48,52,53]')
(B/'qa_final_algorithm_recurrence_browser.py').write_text(s,encoding='utf8');print('Prepared full browser inspection.')

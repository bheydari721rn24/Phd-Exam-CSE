from pathlib import Path
B=Path(__file__).parent;s=(B/'qa_final_boolean_browser.py').read_text().replace('deep-boolean-browser','deep-gates-browser').replace('g_boolean','g_gates')
s=s.replace('==53','==46').replace('==40','==36').replace('range(0,40,5)','range(0,36,5)').replace('==150','==311')
s=s.replace('for n in[1,2,3,4,5,6,7,9,10,12,13,15,28,44,52,53]:','for n in[1,2,3,4,5,6,7,8,9,10,11,12,13,14,25,29,33,37,38,41,45,46]:')
a=s.index(" capture('.boolean-diagram:");z=s.index(" report['responsive']=",a)
replacement=r'''
 report['gateLab']=[]
 for kind,n in [('AND',4),('NAND',3),('NOR',3),('XOR',4),('XNOR',3),('XNOR',4)]:
  row=js('document.getElementById("gate-kind").value='+json.dumps(kind)+';document.getElementById("gate-count").value='+str(n)+';document.getElementById("gate-kind").dispatchEvent(new Event("change"));({rows:document.querySelectorAll("#gate-table tbody tr").length,mismatches:Number(document.getElementById("gate-status").dataset.mismatches)})');assert row['rows']==2**n;report['gateLab'].append(dict(kind=kind,n=n,**row))
 assert report['gateLab'][0]['mismatches']==0 and report['gateLab'][1]['mismatches']>0 and report['gateLab'][2]['mismatches']>0 and report['gateLab'][3]['mismatches']==0 and report['gateLab'][4]['mismatches']>0 and report['gateLab'][5]['mismatches']==0,report['gateLab']
 report['hazardLab']=[]
 for values,expected in [([3,1,1,2],3),([0,5,1,1],0),([0,0,0,0],0),([.5,1,.75,2],.25)]:
  code=';'.join('document.getElementById('+json.dumps(id)+').value='+json.dumps(str(value))for id,value in zip(['haz-inv','haz-direct','haz-comp','haz-or'],values))+';document.getElementById("haz-inv").dispatchEvent(new Event("input"));({...document.getElementById("haz-status").dataset})';row=js(code);assert row['valid']=='true'and float(row['width'])==expected;report['hazardLab'].append(row)
 report['invalidLab']=[]
 for bad in['','-1','21']:
  row=js('document.getElementById("haz-inv").value='+json.dumps(bad)+';document.getElementById("haz-inv").dispatchEvent(new Event("input"));({valid:document.getElementById("haz-status").dataset.valid,rows:document.querySelectorAll("#haz-events tbody tr").length,paths:document.querySelectorAll("#haz-wave path").length})');assert row==dict(valid='false',rows=0,paths=0),row;report['invalidLab'].append(row)
 js('document.getElementById("haz-inv").value="3";document.getElementById("haz-inv").dispatchEvent(new Event("input"))')
 for i in range(len(report['staticDiagrams'])):
  js('[...document.querySelectorAll("figure svg")]['+str(i)+'].closest("figure").setAttribute("data-gates-static-index","'+str(i)+'")');capture('[data-gates-static-index="'+str(i)+'"]',f'static-{i+1}.png')
'''
s=s[:a]+replacement+s[z:];s=s.replace("assert len(report['staticDiagrams'])==4 and", "assert len(report['staticDiagrams'])>=4 and").replace("len(report['selection'])==4","len(report['selection'])==11")
(B/'qa_final_gates_browser.py').write_text(s,encoding='utf-8')

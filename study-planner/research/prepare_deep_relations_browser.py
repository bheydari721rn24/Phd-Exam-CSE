from pathlib import Path
B=Path(__file__).parent;s=(B/'qa_final_gates_browser.py').read_text().replace('deep-gates-browser','deep-relations-browser').replace('g_gates','d_relations')
s=s.replace('==46','==45').replace("['tutorials']==36","['tutorials']==46").replace('==36','==44').replace('range(0,36,5)','range(0,44,5)').replace("len(report['models'])==42","len(report['models'])==49").replace('==311','==235').replace("len(report['selection'])==11","len(report['selection'])==9")
s=s.replace('for n in[1,2,3,4,5,6,7,8,9,10,11,12,13,14,25,29,33,37,38,41,45,46]:','for n in[1,2,3,4,5,6,7,8,9,10,11,12,13,16,17,20,24,28,32,36,37,40,44,45]:')
s=s.replace("capture('#quick-reference'","capture('#review'")
a=s.index(" report['gateLab']=");z=s.index(" report['responsive']=",a)
replacement=r'''
 report['relationLab']=[]
 for name,counts in [('chain',[6,10,16]),('cycle',[9,10,10]),('empty',[0,4,4])]:
  js('document.getElementById("lab-'+name+'").click()')
  row=js('({input:[...document.querySelectorAll("#lab-input button")].filter(b=>b.getAttribute("aria-pressed")==="true").length,closures:[...document.querySelectorAll("#lab-closures table")].map(t=>[...t.querySelectorAll("td span")].reduce((sum,v)=>sum+Number(v.textContent),0)),stage:document.getElementById("lab-stage").textContent})');assert row['closures']==counts and row['stage'].startswith('Stage 0'),row;report['relationLab'].append(dict(inputCase=name,**row))
  for k in range(4):js('document.getElementById("lab-next").click()')
  row=js('({stage:document.getElementById("lab-stage").textContent,disabled:document.getElementById("lab-next").disabled,count:[...document.querySelectorAll("#lab-stage-matrix td span")].reduce((sum,v)=>sum+Number(v.textContent),0)})');assert row['stage'].startswith('Stage 4')and row['disabled']and row['count']==counts[0],row;report['relationLab'].append(row)
 row=js('document.querySelectorAll("#lab-input button")[0].click();({stage:document.getElementById("lab-stage").textContent,disabled:document.getElementById("lab-next").disabled,count:[...document.querySelectorAll("#lab-closures table")][0].querySelectorAll("td span").length})');assert row['stage'].startswith('Stage 0')and not row['disabled']and row['count']==16,row;report['relationLab'].append(row)
 js('document.getElementById("lab-chain").click()')
 for i in range(len(report['staticDiagrams'])):
  js('[...document.querySelectorAll("figure svg")]['+str(i)+'].closest("figure").setAttribute("data-relations-static-index","'+str(i)+'")');capture('[data-relations-static-index="'+str(i)+'"]',f'static-{i+1}.png')
 for n in[4,6,7,8,9,10]:
  sel='h3';js('(()=>{const title=[...document.querySelectorAll("h3")].find(h=>h.textContent.startsWith("Challenge '+str(n)+'.")),h=title.nextElementSibling,c=ConceptAnimations.players.find(c=>h.contains(c.api.host));c.api.show(c.api.model.frames.length-1);h.setAttribute("data-capture-challenge","'+str(n)+'");})()');capture('[data-capture-challenge="'+str(n)+'"]',f'challenge-{n}-final.png')
'''
s=s[:a]+replacement+s[z:]
s=s.replace('startsWith("Problem ")','startsWith("Tutorial ")')
s=s.replace(" js('document.fonts.ready');", " assert js('!!window.ConceptAnimations'), 'Chapter or renderer did not load'\n js('document.fonts.ready');")
# No old lab or inherited playback evidence is reused for this new chapter.
a=s.index(" if '--layout-only'");z=s.index("  report['playback']=[]",a);s=s[:a]+" report['playback']=[]\n"+s[z+len("  report['playback']=[]\n"):]
begin=s.index("  for start in range(0,44,5):");end=s.index(" for n in[",begin);block=s[begin:end];s=s[:begin]+'\n'.join(line[1:]if line.startswith(' ')else line for line in block.split('\n'))+s[end:]
(B/'qa_final_relations_browser.py').write_text(s,encoding='utf-8')

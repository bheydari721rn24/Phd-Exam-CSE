from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_g_mux_browser.py').read_text(encoding='utf-8').replace('g_mux','d_recurrence').replace('g-mux','d-recurrence').replace('MuxPlayers','RecurrencePlayers').replace('MuxLab','RecurrenceLab').replace('.mx-','.rc-').replace('#mx-','#rc-').replace('data-mx-','data-rc-')
s=s.replace("questions']==82","questions']==83").replace("players']>17","players']>14").replace('>998','>758').replace("cards']==49","cards']==50")
start=s.index(' for id,step,name in');end=s.index(" capture('.hero'",start)
s=s[:start]+" for id,step,name in [('all-domino-eight',20,'tiling.png'),('ternary-forbidden',3,'automaton.png'),('derangement-cases',5,'cycles.png'),('ferrers-seven',3,'ferrers.png'),('ferrers-conjugate',1,'conjugation.png'),('reflection-six',1,'reflection.png'),('first-return-three',4,'catalan.png'),('weighted-forcing',4,'forcing.png'),('companion-state',4,'matrix.png')]:\n  js('RecurrencePlayers.find(p=>p.model.id==='+json.dumps(id)+').show('+str(step)+')');capture('[data-rc-model=\"'+id+'\"]',name)\n"+s[end:]
s=s.replace('d_recurrence_original_80','d_recurrence_original_34').replace('tree-eight','all-domino-eight').replace('mux-basic','ternary-forbidden').replace('mobile-full-adder.png','mobile-automaton.png')
start=s.index(" report['labs']=[]");end=s.index(" cdp('Emulation.setDeviceMetricsOverride',dict(width=390",start)
specs=[dict(operation='unrolling',n=5,p=0,a0=9),dict(operation='unrolling',n=8,p=-3,a0=1),dict(operation='tiling',n=6),dict(operation='resonance',n=8),dict(operation='automaton',n=6),dict(operation='derangements',n=8),dict(operation='partitions',n=8),dict(operation='ferrers',n=8),dict(operation='catalan',n=4),dict(operation='modular',n=8,modulus=6),dict(operation='matrix',n=8)]
s=s[:start]+''' report['labs']=[]
 for spec in '''+repr(specs)+''':
  obj=js('(()=>{const f=document.querySelector("#rc-form"),base={operation:"unrolling",n:5,p:2,a0:0,modulus:3},spec='+json.dumps(spec)+';for(const[k,v]of Object.entries({...base,...spec}))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));const bad=[];for(let i=0;i<RecurrenceLab.model.frames.length;i++){RecurrenceLab.show(i);bad.push(...DiagramLayout.audit(RecurrenceLab.host.querySelector("svg")));}return {error:document.querySelector("#rc-error").textContent,result:RecurrenceLab.model.result,issues:bad};})()');assert not obj['error']and not obj['issues'],obj;report['labs'].append(obj)
 for change in [dict(n=0),dict(n=9),dict(p=5),dict(a0=11),dict(modulus=1),dict(operation='catalan',n=5),dict(operation='ferrers',n=2)]:
  js('(()=>{window.oldLab=RecurrenceLab;const f=document.querySelector("#rc-form"),base={operation:"unrolling",n:5,p:2,a0:0,modulus:3},change='+json.dumps(change)+';for(const[k,v]of Object.entries({...base,...change}))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('RecurrenceLab===oldLab && document.querySelector("#rc-error").textContent.length>0')
 report['invalidPreservesPrevious']=7
'''+s[end:]
s=s.replace('week-3','week-4')
(B/'qa_d_recurrence_browser.py').write_text(s,encoding='utf-8')
print('Prepared exact rendered-font, every-checkpoint, controls, editable model and library QA.')

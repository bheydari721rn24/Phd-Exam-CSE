from pathlib import Path
B=Path(__file__).resolve().parent
s=(B/'qa_p_strings_browser.py').read_text(encoding='utf-8').replace('p_strings','p_recursion').replace('p-strings','p-recursion').replace('StringPlayers','RecursionPlayers').replace('StringLab','RecursionLab').replace('st-','rc-').replace('==46','==47')
a=s.index(" for id,step,name in");b=s.index(" capture('.hero'",a)
s=s[:a]+" for id,step,name in [('fact-four',3,'frames.png'),('fib-five',12,'tree.png'),('memo-six',20,'cache.png'),('hanoi-three',8,'pegs.png'),('subsets-three',13,'choices.png'),('koch-three',3,'geometry.png')]:\n  js('RecursionPlayers.find(p=>p.model.id==='+json.dumps(id)+').show('+str(step)+')');capture('[data-rc-model=\"'+id+'\"]',name)\n"+s[b:]
s=s.replace('p-strings-original-80','p-recursion-original-80').replace('move-right','hanoi-three').replace('p.show(1);p.host','p.show(5);p.host').replace('scan-embedded','fact-four')
a=s.index(" report['labs']=[]");b=s.index(" cdp('Emulation.setDeviceMetricsOverride',dict(width=390",a)
s=s[:a]+''' report['labs']=[]
 for spec in [dict(operation='factorial',n=4),dict(operation='fib',n=5),dict(operation='memo',n=6),dict(operation='hanoi',n=3),dict(operation='subsets',n=3),dict(operation='palindrome',text='abca'),dict(operation='power',a=2,exponent=13),dict(operation='koch',n=3)]:
  obj=js('(()=>{const f=document.querySelector("#rc-form"),spec='+json.dumps(spec)+';for(const [k,v]of Object.entries(spec))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));const bad=[];for(let i=0;i<RecursionLab.model.frames.length;i++){RecursionLab.show(i);bad.push(...DiagramLayout.audit(RecursionLab.host.querySelector("svg")));}return {error:document.querySelector("#rc-error").textContent,result:RecursionLab.model.result,issues:bad};})()');assert not obj['error']and not obj['issues'],obj;report['labs'].append(obj)
 capture('#rc-output .rc-stage','editable-recursion.png')
 for change in [dict(n=-1),dict(n=9),dict(operation='fib',n=6),dict(operation='hanoi',n=5),dict(operation='palindrome',text='é'),dict(operation='power',a=4)]:
  js('(()=>{window.oldLab=RecursionLab;const f=document.querySelector("#rc-form"),base={operation:"factorial",n:3,a:2,b:462,exponent:13,value:738,text:"abccba",target:8},change='+json.dumps(change)+';for(const[k,v]of Object.entries({...base,...change}))f.elements[k].value=v;f.dispatchEvent(new Event("submit",{cancelable:true}));})()');assert js('RecursionLab===oldLab && document.querySelector("#rc-error").textContent.length>0')
 report['invalidPreservesPrevious']=6
'''+s[b:]
(B/'qa_p_recursion_browser.py').write_text(s,encoding='utf-8')

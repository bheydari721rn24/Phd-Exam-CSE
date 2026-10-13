from pathlib import Path
B=Path(__file__).parent;s=(B/'qa_final_relations_browser.py').read_text();prefix=s[:s.index(" report['counts']=")]
body=r'''
 for n,k in[(36,0),(17,1),(44,2),(2,2)]:
  sel=f'.exam-question[data-deep-index="{n}"] .concept-animation';js('(()=>{const h=document.querySelector('+json.dumps(sel)+'),c=ConceptAnimations.players.find(c=>h.contains(c.api.host));c.api.show('+str(k)+');h.setAttribute("data-layout-capture","yes");})()');capture(sel,f'inspection-q{n}.png')
  row=js("""(()=>{const svg=document.querySelector('[data-layout-capture=yes] svg'),rows=[];for(const t of svg.querySelectorAll('text'))for(const m of svg.querySelectorAll('foreignObject math')){const a=t.getBoundingClientRect(),b=m.getBoundingClientRect();if(Math.min(a.right,b.right)-Math.max(a.left,b.left)>1&&Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top)>1)rows.push({text:t.textContent,tx:t.getAttribute('x'),ty:t.getAttribute('y'),label:m.getAttribute('aria-label'),textBox:[a.left,a.top,a.width,a.height],mathBox:[b.left,b.top,b.width,b.height],fo:m.closest('foreignObject').outerHTML.slice(0,400)});}document.querySelector('[data-layout-capture=yes]').removeAttribute('data-layout-capture');return rows;})()""");print(n,json.dumps(row),flush=True)
finally:
 proc.terminate()
'''
(B/'inspect_relations_layout_run.py').write_text(prefix+body,encoding='utf-8')

from pathlib import Path
B=Path(__file__).parent;D=B.parent/'dist/chapters'
s=(D/'a_stackqueue.js').read_text(encoding='utf-8');s=s[:s.index(' function formula(')]
s=s.replace('sq-','sort-').replace('sqModel','sortModel').replace('data-sq','data-sort').replace("function finish(svg){if(svg)window.DiagramLayout?.finish(svg,{arrows:false,labels:true});}","function finish(svg){}").replace("r.values.length?r.values.join(', '):'empty'","r.cells.length?r.cells.map(x=>x?x.key+'['+x.id+']':'hole').join(', '):'empty'")
(D/'a_sort.js').write_text(s+(B/'a_sort_lab.js').read_text(encoding='utf-8'),encoding='utf-8')
s=(D/'a_stackqueue.css').read_text(encoding='utf-8').replace('sq-','sort-')
s+='\n.sort-key{font-family:"STIX Two Math",serif!important;font-size:22px}.sort-id{font-family:"Source Sans 3",sans-serif!important;font-size:13px}.sort-label{font-family:"Source Sans 3",sans-serif!important;font-size:17px}.sort-meta{font-size:15px}.sort-index{font-size:13px}.sort-stage svg{max-height:none}.sort-stage svg text{font-weight:400}#sort-form input[name=values]{width:260px;max-width:100%}.sort-print-trace .sort-key{font-size:22px}.sort-print-trace .sort-label{font-size:17px}\n'
(D/'a_sort.css').write_text(s,encoding='utf-8')

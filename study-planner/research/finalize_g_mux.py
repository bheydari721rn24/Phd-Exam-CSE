from pathlib import Path
import json,subprocess,re,hashlib
B=Path(__file__).resolve().parent;R=B.parent;E=B/'g_mux-evidence'
# Replace stale inherited log wording, without altering chapter output.
p=B/'build_g_mux.py';s=p.read_text(encoding='utf-8').replace("print('Built 82 problems, 80 rules, 16 models,'","print('Built 82 problems, 80 rules, 17 models,'");p.write_text(s,encoding='utf-8')
p=B/'prepare_g_mux_qa.py';s=p.read_text(encoding='utf-8');s=s.replace("[('authentic-nor',2,'cascade.png')","[('decoder-gates',2,'decoder-gates.png'),('authentic-nor',2,'cascade.png')")
s=s.replace("(B/'qa_g_mux_browser.py').write_text", "s=s.replace(\"report['runtimeErrors']=js('__errors');\",\"assert not js('document.querySelector(\\\".lesson\\\").textContent.includes(\\\"undefined\\\")');report['runtimeErrors']=js('__errors');\")\n(B/'qa_g_mux_browser.py').write_text")
p.write_text(s,encoding='utf-8')
subprocess.run(['python','-X','utf8',str(B/'prepare_g_mux_qa.py')],cwd=R,check=True)
print('Final rendering and interaction evidence prepared.')

from pathlib import Path
import ast,json,re,sys
B=Path(__file__).parent;R=B.parent
ns={};tree=ast.parse((B/'deep_revision_inventory.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef,ast.ClassDef))],type_ignores=[]),'read_helpers','exec'),ns)
auth={q['id']:q for q in json.loads((B/'exam-calibration/actual-items.json').read_text())}
original={q['title']:q for f in (B/'exam-calibration').glob('original-*.json')for q in json.loads(f.read_text())if q.get('topic')=='d_number'};ids={q['id']:q for q in original.values()if q.get('id')};rows=[]
for i,(_,_,attrs,q)in enumerate(ns['questions']((R/'dist/chapters/d_number.html').read_text()),1):
 title=ns['plain'](re.search(r'<h3[^>]*>([\s\S]*?)</h3>',q)[1]);c=auth.get(attrs.get('data-source-id'))or ids.get(attrs.get('data-source-id'))or original.get(re.sub(r'^Question \d+\. ','',title));end=q.find('<details');end=end if end>=0 else q.index('<p><strong>Correct option:')
 rows.append(dict(index=i,title=title,stem=c['stem']if c else ns['plain'](q[:end]),options=c['options']if c else[],answer=c['answer']if c else int(re.search(r'Correct option:\s*(\d+)',ns['plain'](q))[1]),sourceId=attrs.get('data-source-id'),canonical=c))
if __name__=='__main__':
 a=int(sys.argv[1])if len(sys.argv)>1 else 1;b=int(sys.argv[2])if len(sys.argv)>2 else len(rows)
 for r in rows[a-1:b]:print(json.dumps({k:v for k,v in r.items()if k!='canonical'},ensure_ascii=False))

"""Repair the observed four-row load-cell padding without changing other models."""
from pathlib import Path
import ast,html,json,re,sympy as S
R=Path(__file__).resolve().parents[1];p=R/'dist/chapters/problem-visual-models.json'
source=R/'research/deep-library-revision/l_gauss-problem-visual-rebuild.py'
scope={'S':S,'html':html,'re':re}
for node in ast.parse(source.read_text(encoding='utf8')).body:
    if isinstance(node,ast.FunctionDef)and node.name in ['plain','txt','cell','matrix','figure']:
        exec(compile(ast.Module(body=[node],type_ignores=[]),str(source),'exec'),scope)
data=json.loads(p.read_text(encoding='utf8'));entry=data['l_gauss-q11'];matrix=scope['matrix'];figure=scope['figure']
for frame in entry['frames']:
    current=S.Matrix(frame['matrix']);n=current.cols-1
    out=figure('Actual augmented system: LG09',[('[coefficients | load]',current,n)],['Amber cells are the transformed load, not coefficient variables.','Coefficient pivots determine free coordinates; a contradictory load decides consistency.'])
    out=out.replace(matrix(380,91,current,'[coefficients | load]',n,min(52,260/current.cols)),matrix(380,73,current,'[coefficients | load]',n,min(52,260/current.cols),40))
    frame['html']=out
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print({'model':'l_gauss-q11','frames':len(entry['frames']),'rowHeight':40,'top':73,'numericValuesChanged':False})

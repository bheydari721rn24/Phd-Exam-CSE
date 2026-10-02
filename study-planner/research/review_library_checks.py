"""Run existing independent mathematical/lab checks and retain exact results."""
from pathlib import Path
import json,subprocess,sys,time
ROOT=Path(__file__).resolve().parents[1];rows=[]
for p in sorted((ROOT/'research').glob('verify*')):
 if p.suffix not in {'.py','.js','.cjs'}:continue
 command=[sys.executable,'-X','utf8',str(p)] if p.suffix=='.py' else ['node',str(p)]
 start=time.monotonic();r=subprocess.run(command,cwd=ROOT,capture_output=True,text=True,encoding='utf-8',timeout=180)
 rows.append({'check':p.name,'exitCode':r.returncode,'seconds':round(time.monotonic()-start,2),'output':(r.stdout+r.stderr)[-6000:]});print(p.name,r.returncode,flush=True)
 (ROOT/'research/library-review-checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
assert all(x['exitCode']==0 for x in rows), 'Review check failures must be resolved.'

"""Mirror the exact changed chapter files, preserving unrelated mirror changes."""
from pathlib import Path
import subprocess,shutil,sys
ROOT=Path(__file__).resolve().parents[1]
MIRROR=Path('C:/Users/bheydari/AppData/Local/Temp/phd-exam-1406-analysis/repo')
baseline=sys.argv[1]
def git(*args,cwd=ROOT):
 return subprocess.check_output(['git',*args],cwd=cwd,text=True,encoding='utf-8').strip()
assert git('branch','--show-current',cwd=MIRROR)=='study-planner-1406'
paths=git('diff','--name-only',baseline,'HEAD').splitlines()
assert paths and not any(Path(p).is_absolute() or '..' in Path(p).parts for p in paths)
for relative in paths:
 source=ROOT/relative;target=MIRROR/'study-planner'/relative
 assert source.is_file(),f'Deletion requires separate review: {relative}'
 assert target.resolve().is_relative_to((MIRROR/'study-planner').resolve())
 target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
stage=['study-planner/'+p.replace('\\','/') for p in paths]
subprocess.run(['git','add','--sparse','--',*stage],cwd=MIRROR,check=True)
subprocess.run(['git','diff','--cached','--check'],cwd=MIRROR,check=True)
subprocess.run(['git','commit','-m','Complete final review of sixteen English chapters and figures'],cwd=MIRROR,check=True)
subprocess.run(['git','push','origin','study-planner-1406'],cwd=MIRROR,check=True)
print(f'Mirrored {len(paths)} exact changed files; commit '+git('rev-parse','--short','HEAD',cwd=MIRROR))

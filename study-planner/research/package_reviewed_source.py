"""Package immutable committed static blobs after the bundled source push."""
from pathlib import Path
import sys,subprocess,tarfile,io,hashlib,json
R=Path(__file__).resolve().parents[1];sha=sys.argv[1];archive=Path(sys.argv[2])
assert len(sha)==40 and archive.is_absolute() and not archive.exists(), 'Preserve earlier archives; choose an unused immutable destination.'
files=subprocess.check_output(['git','ls-tree','-r','--name-only',sha,'--','.openai/hosting.json','dist'],cwd=R,text=True).splitlines()
assert '.openai/hosting.json'in files and 'dist/index.html'in files
with tarfile.open(archive,'w:gz')as t:
 for path in files:
  data=subprocess.check_output(['git','show',sha+':'+path],cwd=R);actual=(R/path).read_bytes();assert actual==data or actual.replace(b'\r\n',b'\n')==data,path
  info=tarfile.TarInfo(path);info.size=len(data);info.mode=0o644;t.addfile(info,io.BytesIO(data))
with tarfile.open(archive,'r:gz')as t:
 for q in t:assert t.extractfile(q).read()==subprocess.check_output(['git','show',sha+':'+q.name],cwd=R)
print(json.dumps(dict(sourceCommit=sha,archive=str(archive),archiveEntries=len(files),archiveSha256=hashlib.sha256(archive.read_bytes()).hexdigest())))

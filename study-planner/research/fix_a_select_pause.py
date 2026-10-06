from pathlib import Path
p=Path(__file__).resolve().parents[1]/'dist/chapters/teaching-transitions.js'
s=p.read_text(encoding='utf-8')
old="stage.getAnimations({subtree:true}).forEach(a=>a.pause());"
new="stage.getAnimations({subtree:true}).forEach(a=>{const t=a.currentTime;a.pause();if(t!==null)a.currentTime=t;});"
assert s.count(old)==1
p.write_text(s.replace(old,new),encoding='utf-8')

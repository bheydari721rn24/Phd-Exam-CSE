from pathlib import Path
import json
B=Path(__file__).parent;R=B.parent
for name in ['a_sort-quality-audit.md']:
 p=B/name;s=p.read_text(encoding='utf-8').replace('1,186','1,194').replace('1,242','1,250').replace('2,736','2,744');p.write_text(s,encoding='utf-8')
p=B/'chapter-gate.json';g=json.loads(p.read_text());g['delivery']['checkpoints']=1194;p.write_text(json.dumps(g,indent=2)+'\n')
p=R/'WEEKLY_DELIVERY.md';s=p.read_text(encoding='utf-8').replace('1,186 stored checkpoints','1,194 stored checkpoints');p.write_text(s,encoding='utf-8')
p=B/'a_sort-publication.json';a=json.loads(p.read_text());a['visualRevision']=dict(state='pending',date='2026-10-06',previousPublishedVersion=71,models=45,checkpoints=1194,comparedSteps=402);p.write_text(json.dumps(a,indent=2)+'\n')
# Final playback check, including actual motion pause.
p=B/'a_sort_browser_body.py.txt';s=p.read_text(encoding='utf-8');anchor=' old=js('
extra=''' report['motionPause']=js("(()=>{const p=SortingChapter.players.find(x=>x.model.id==='concept-3'),el=document.querySelector('[data-sort-model=concept-3]');p.draw(2);p.draw(3,true);el.querySelector('[data-play]').click();el.querySelector('[data-play]').click();const animations=el.querySelector('.sort-stage').getAnimations({subtree:true});const r={count:animations.length,paused:animations.every(a=>a.playState==='paused')};p.draw(0);return r;})()");assert report['motionPause']['count']>0 and report['motionPause']['paused']
'''
assert s.count(anchor)==1;s=s.replace(anchor,extra+anchor,1);p.write_text(s,encoding='utf-8')

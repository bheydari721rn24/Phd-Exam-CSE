"""Recheck the full library after actual-user-control failures were identified."""
from pathlib import Path
R=Path(__file__).resolve().parents[1]
s=(R/'research/qa_unified_library.py').read_text(encoding='utf-8')
s=s.replace("OUT=R/'research/library-simulation-standard'","OUT=R/'research/player-behavior-repair'")
s=s.replace("/'unified-library-qa'","/'player-behavior-library-qa'")
a="const svg=p.host.querySelector('.sim-stage svg');if(!svg)"
b="""const svg=p.host.querySelector('.sim-stage svg');const shownState=p.teaching.root.querySelector('[data-detail=state] pre')?.textContent;if(shownState!==JSON.stringify(AdvancedSimulations.state(p.model.frames[i]),null,2))issues.push({frame:i,kind:'state panel does not match exact checkpoint'});if(i>0){p.host.querySelector('[data-view=before]').click();if(p.host.querySelector('.sim-caption').textContent!==p.model.frames[i-1].caption||p.teaching.root.querySelector('[data-detail=state] pre')?.textContent!==JSON.stringify(AdvancedSimulations.state(p.model.frames[i-1]),null,2))issues.push({frame:i,kind:'previous drawing and explanation disagree'});p.host.querySelector('[data-view=after]').click();}if(svg){const ids=[...svg.querySelectorAll('[id]')].map(n=>n.id);if(new Set(ids).size!==ids.length)issues.push({frame:i,kind:'duplicate drawing IDs'});}if(!svg)"""
assert a in s;s=s.replace(a,b)
# Existing reference layout checks must inspect the inserted result, not a detached
# element that was replaced by the previous-state check.
s=s.replace("const svg=p.host.querySelector('.sim-stage svg');const shownState", "let svg=p.host.querySelector('.sim-stage svg');const shownState")
s=s.replace("p.host.querySelector('[data-view=after]').click();}if(svg)", "p.host.querySelector('[data-view=after]').click();svg=p.host.querySelector('.sim-stage svg');}if(svg)")
s=s.replace("const all=[...h.querySelectorAll('.sim-print [id]')].map(n=>n.id)","const all=[...h.querySelectorAll('[id]')].map(n=>n.id)")
out=R/'research/player-behavior-repair';out.mkdir(exist_ok=True)
exec(compile(s,str(__file__),'exec'))

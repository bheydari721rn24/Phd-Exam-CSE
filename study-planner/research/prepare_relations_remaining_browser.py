from pathlib import Path
import json,hashlib
B=Path(__file__).parent;E=B/'deep-library-revision';saved=E/'d_relations-browser-controls-before-lab-fix.json';old=(E/'d_relations-browser.json').read_bytes();report=json.loads(old)
assert len(report['controls'])==len(report['playback'])==44 and all(all(v['checks'])for v in report['controls'])and all(v['advanced']and v['paused']for v in report['playback'])
assert len(report['models'])==49 and len(report['frameRendering'])==235 and all(not r['issues']for r in report['frameRendering'])and all(not r['issues']for r in report['models'])
saved.write_bytes(old)
assets={str(p.relative_to(B.parent)):hashlib.sha256(p.read_bytes()).hexdigest()for p in [B.parent/'dist/chapters/d_relations.html',B.parent/'dist/chapters/concept-animations.json',B.parent/'dist/chapters/semantic-diagrams.js']}
report['assetHashesAtSegmentHandoff']=assets
(E/'d_relations-browser-segment-handoff.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
s=(B/'qa_final_relations_browser.py').read_text();prefix=s[:s.index(" report['counts']=")];tail=s[s.index(" report['relationLab']="):]
middle=" report=json.loads((R/'research/deep-library-revision/d_relations-browser-segment-handoff.json').read_text())\n import hashlib\n assert all(hashlib.sha256((R/path).read_bytes()).hexdigest()==sha for path,sha in report['assetHashesAtSegmentHandoff'].items())\n report['playbackEvidenceReused']='The preceding segment actually advanced and paused all 44 players and checked all 235 scenario frames. A QA-only selector quoting error occurred afterward. The immutable raw control-pass report is retained; chapter, model and renderer hashes are unchanged. This run completes the remaining lab, screenshots, responsive and print checks.'\n"
(B/'qa_remaining_relations_browser.py').write_text(prefix+middle+tail,encoding='utf-8')

from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1];E=R/'research/deep-library-revision';p=E/'a_correct-browser.json';d=json.loads(p.read_text())
assert len(d['controls'])==54 and all(all(x[k]for k in['next','back','seek','reset'])for x in d['controls'])
assert d['playPause']and all(x['started']and x['advanced']and x['stopped']for x in d['playPause'])
d.update(status='passed_controls_and_playback_only',scope='All 54 question players: next/back/seek/reset; every multiple-frame question player actually played, advanced and paused. The later responsive audit found long inline math escaping on mobile and is not passed by this record.',modelDataSha256=hashlib.sha256((R/'dist/chapters/concept-animations.json').read_bytes()).hexdigest(),playerScriptSha256=hashlib.sha256((R/'dist/chapters/concept-unified.js').read_bytes()).hexdigest(),rendererSha256=hashlib.sha256((R/'dist/chapters/semantic-diagrams.js').read_bytes()).hexdigest())
(E/'a_correct-controls-browser.json').write_text(json.dumps(d,indent=2)+'\n');print({'controlPlayers':len(d['controls']),'playbackPlayers':len(d['playPause'])})

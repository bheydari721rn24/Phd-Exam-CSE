"""Record verified content and the actual publication transport blocker."""
import json
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[1]
folder = root / 'research/player-behavior-repair'
receipt = {
    'status': 'pending_upload',
    'recordedAt': datetime.now(timezone.utc).isoformat(),
    'projectId': 'appgprj_6ab5666f72b081918286c6b371c1eb1b',
    'sourceContentCommit': 'd8c9309a915f4fed4a58a9cd5a9624a71b0e56d4',
    'sourcePushVerified': True,
    'githubBranch': 'study-planner-1406',
    'githubContentCommit': 'e2dc17d',
    'archive': 'C:/Users/bheydari/AppData/Local/Temp/simulation-behavior-corrections.tar.gz',
    'archiveSha256': 'fa4685dc255bb2d3e6b1b1e3ed01f218899dca9d9f317fed4e0f80c2c0ebd679',
    'archiveFileCount': 410,
    'lastConfirmedOnlineVersion': 85,
    'errorEndpoint': 'https://chatgpt.com/backend-api/files',
    'error': 'Native archive upload failed to send OpenAI file request. No new version or deployment ID was returned. Version history was reconciled after failures.',
    'automaticPrivatePublicationAccepted': False,
    'verification': 'passed',
    'localPreview': 'http://127.0.0.1:8766/reviews/simulation-behavior-corrections.html',
    'localPreviewScope': 'Available while the local preview process remains running on this computer.',
}
(folder / 'publication-pending.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
manifest_path = folder / 'manifest.json'
manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
manifest.update(status='verified_publication_pending', publicationRecordPath='research/player-behavior-repair/publication-pending.json')
manifest_path.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
gate_path = root / 'research/chapter-gate.json'
gate = json.loads(gate_path.read_text(encoding='utf-8'))
gate.update(simulationBehaviorPublicationState='pending_upload', simulationBehaviorPublicationPath='research/player-behavior-repair/publication-pending.json', activeWork='All-library functional corrections verified and pushed to GitHub. Native archive upload is blocked by a file-service transport error; online version remains 85. Local preview available. No next chapter begun.')
gate_path.write_text(json.dumps(gate, indent=2) + '\n', encoding='utf-8')
for relative in ['research/player-behavior-repair/DELIVERY.en.md', 'WEEKLY_DELIVERY.md']:
    path = root / relative
    with path.open('a', encoding='utf-8') as stream:
        stream.write('\n\n## Publication transport blocker (2026-10-09)\n\nThe verified source was pushed; the GitHub content commit is `e2dc17d` on `study-planner-1406`. The native archive upload repeatedly failed at the OpenAI file service before saving a version. Reconciliation confirms that online version 85 still contains the previous content. The exact 410-file archive is retained unchanged for a later supported retry. A local preview is available at http://127.0.0.1:8766/reviews/simulation-behavior-corrections.html while its process is running. See `research/player-behavior-repair/publication-pending.json`. No new chapter was started.\n')
print('Recorded publication pending; preserved chapter approval gate and last online version.')

"""Record a failed publication without confusing GitHub storage with Site hosting."""
from pathlib import Path
import hashlib,json,subprocess
ROOT=Path(__file__).resolve().parents[1]
source='6948e13944366e9aa0fb6af01651b6b72f424342'
mirror=Path('C:/Users/bheydari/.codex/worktrees/phd-exam-cloud-20261017')
github='19dc9d0ba3cec529a0c9e680615b0f22f8cd51ee'
archive=Path('C:/Users/bheydari/AppData/Local/Temp/phd-study-20261017-gauss-complete.tar.gz')
def git(path,*args):
 return subprocess.check_output(['git',*args],cwd=path)
assert git(mirror,'ls-remote','origin','refs/heads/study-planner-1406').decode().split()[0]==github
changed=git(ROOT,'diff','--name-only','ed4a4c486cba3a388a32384faa68a916bfda9399',source).decode().splitlines()
for rel in changed:
 assert git(ROOT,'show',source+':'+rel)==git(mirror,'show',github+':study-planner/'+rel),rel
manifest=json.loads(git(mirror,'show',github+':study-planner/exports/manifest.json'))
print('Manifest schema',type(manifest).__name__)
sha=hashlib.sha256(archive.read_bytes()).hexdigest()
assert sha=='806a1cca13446222ddb1ecc5f625f93498ab3cd8783cad869a59761daf23b63c'
record={
 'date':'2026-10-17','status':'pending_upload_after_three_terminal_failures',
 'projectId':'appgprj_6ab5666f72b081918286c6b371c1eb1b','audience':'owner-private',
 'sourceCommit':source,'githubContentCommit':github,'githubBranch':'study-planner-1406',
 'githubVerification':{'changedCanonicalPaths':len(changed),'technicalChapterHtml':62,'offlineCopies':9,'method':'Canonical committed Git blobs compared; all nine committed offline hashes independently checked in preceding delivery step.'},
 'archive':str(archive),'archiveBytes':archive.stat().st_size,'archiveSha256':sha,
 'attempts':[
  {'attempt':1,'stage':'backend files request','result':'Failed before archive upload; no saved version returned.'},
  {'attempt':2,'stage':'OpenAI file blob upload','result':'Connection failed after 144085 ms','requestId':'ec43d6a5-fcd0-405d-8f23-2d1f48ebb836'},
  {'attempt':3,'stage':'OpenAI file blob upload','result':'Timeout after 300006 ms','requestId':'36910ba9-92c6-40bf-b497-6177df43516c'}],
 'reconciliation':{'latestSavedVersion':108,'versionId':'appgprj_6ab5666f72b081918286c6b371c1eb1b~appgver_a6dd94502d6481919b5beefa793a1404','sourceCommit':'a97cc196368bef29966074d8ce4c406089a33d20','deploymentId':'appgdep_6ad37bf384dc819191c95bbf96541b7b','newSavedVersionReturned':False},
 'availability':'Complete Gaussian review is stored locally, in GitHub and in the self-contained offline copy. The confirmed online version108 contains the earlier targeted erratum, not the complete review.',
 'studentApproved':False,
 'retry':'Reuse the immutable archive and exact pushed source; reconcile saved versions before another native upload. Preserve private audience.'}
path=ROOT/'research/l_gauss-complete-publication-20261017.json'
path.write_text(json.dumps(record,indent=2)+'\n',encoding='utf8')
for rel in ['research/chapter-gate.json','research/continuation-status-20261017.json']:
 p=ROOT/rel; data=json.loads(p.read_text(encoding='utf8'))
 if 'currentTopicId' in data:
  data['publicationState']='complete_gauss_revision_stored_github_site_upload_pending'
  data['currentChapterPublicationState']='complete_individual_review_github_and_offline_site_upload_pending'
  data['pendingCurrentRevisionPublication']='research/l_gauss-complete-publication-20261017.json'
  data['currentDraftPath']='research/i_games.en.md'
  data['currentDraftEvidence']='research/i_games-source-evaluation-start.json'
 else:
  data['sitePublication']='complete_gauss_revision_stored_github_site_upload_pending'
  data['publicationEvidence']='research/l_gauss-complete-publication-20261017.json'
  data['currentAnswerManuscript']='research/deep-library-revision/l_gauss-advanced-answer-expansions.en.md'
  data['currentAnswerManuscriptChecks']='research/deep-library-revision/l_gauss-current-mathematics.json'
 p.write_text(json.dumps(data,indent=2)+'\n',encoding='utf8')
with (ROOT/'WEEKLY_DELIVERY.md').open('a',encoding='utf8') as f:
 f.write('\n\n## Complete Gaussian review: cloud storage confirmed, Site upload pending\n\nGitHub content commit '+github+' stores the complete review; all64changed paths,62technical chapter HTML files and9offline hashes were verified. Three native Site upload attempts failed before returning a saved version. Reconciliation still shows version108, source a97cc196368bef29966074d8ce4c406089a33d20. The immutable22525478byte archive is retained; the complete review is available from GitHub and exports/Gaussian Elimination.html. No current Site publication is claimed. Exact receipt: research/l_gauss-complete-publication-20261017.json.\n')
print(json.dumps({'record':str(path),'verifiedPaths':len(changed),'archiveSha256':sha}))

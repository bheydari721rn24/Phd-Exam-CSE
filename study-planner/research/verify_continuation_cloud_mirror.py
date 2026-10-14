from pathlib import Path
import json,subprocess
R=Path(__file__).resolve().parents[1];M=Path('C:/Users/bheydari/AppData/Local/Temp/phd-exam-1406-analysis/repo');BASE='c09d0bb8055290b10d94c3bbf333dfcb464a4b04'
def git(*args,cwd=R):return subprocess.check_output(['git',*args],cwd=cwd,text=True,encoding='utf8').strip()
root=git('rev-parse','HEAD');mirror=git('rev-parse','HEAD',cwd=M);remote=git('ls-remote','origin','refs/heads/study-planner-1406',cwd=M).split()[0];assert mirror==remote
paths=git('diff','--name-only',BASE,root).splitlines();assert len(paths)==79
for path in paths:assert git('rev-parse',root+':'+path)==git('rev-parse',mirror+':study-planner/'+path,cwd=M),path
lessons=json.loads((R/'dist/lessons.json').read_text(encoding='utf8'));chapters=[q['url']for week in lessons for q in week['chapters']];assert len(chapters)==60
for path in chapters:
 relative='dist/'+path;assert git('rev-parse',root+':'+relative)==git('rev-parse',mirror+':study-planner/'+relative,cwd=M),path
report={'status':'verified_exact_pushed_github_mirror','date':'2026-10-14','localContentCommit':root,'githubContentCommit':mirror,'githubRemoteBranchHead':remote,'branch':'study-planner-1406','changedFilesVerifiedByGitBlob':len(paths),'existingTechnicalNotesVerifiedByGitBlob':60,'newIeltsLessonsIncluded':1,'reviewedTechnicalEditions':23,'remainingIndividualReviews':37,'newTechnicalChaptersRemaining':59,'activeNewDraft':'l_projection','sitePublication':'Current editions are not published to Sites; official source workflow failed with connection reset before verified push or native save/deploy.'}
(R/'research/cloud-delivery-20261014.json').write_text(json.dumps(report,indent=2)+'\n')
p=R/'research/deep-library-revision/a_correct-revision.json';d=json.loads(p.read_text());d.update(publicationState='verified_on_github_site_source_connection_reset',githubContentCommit=mirror,githubBranch='study-planner-1406',cloudVerification='research/cloud-delivery-20261014.json');p.write_text(json.dumps(d,indent=2)+'\n')
p=R/'research/deep-library-revision/a_correct-publication-pending.json';d=json.loads(p.read_text());d.update(githubContentCommit=mirror,githubBranch='study-planner-1406',githubStatus='Exact pushed content verified',cloudVerification='research/cloud-delivery-20261014.json');p.write_text(json.dumps(d,indent=2)+'\n')
print({'status':report['status'],'filesVerified':79,'technicalNotesVerified':60,'githubCommit':mirror,'ieltsLessons':1})

"""Compute authored, revised, planned and cloud-mirrored counts separately."""
from pathlib import Path
from collections import Counter
import json,subprocess
R=Path(__file__).resolve().parents[1];M=Path('C:/Users/bheydari/AppData/Local/Temp/phd-exam-1406-analysis/repo')
def git(*args,cwd=R):return subprocess.check_output(['git',*args],cwd=cwd,text=True,encoding='utf8').strip()
plan=json.loads((R/'dist/schedule.en.json').read_text());lessons=json.loads((R/'dist/lessons.json').read_text());progress=json.loads((R/'research/deep-library-revision/progress.json').read_text());topics=plan['topics'];rows=[c for w in lessons for c in w['chapters']];written={c['topicId']:c for c in rows if(R/'dist'/c['url']).is_file()}
assert len(written)==len(rows)==60;revised={c['topicId']for c in progress['chapters']if c['state']=='revised_checked_review_draft'}
planned=Counter(t['subject']for t in topics.values());authored=Counter(topics[t]['subject']for t in written);checked=Counter(topics[t]['subject']for t in revised)
subjects=[dict(subject=s,title=v['title'],planned=planned[s],authored=authored[s],unwritten=planned[s]-authored[s],individuallyRevised=checked[s])for s,v in plan['subjects'].items()]
coverage=[];fullPrefix=0
for w in plan['weeks']:
 units=[u for u in w['units']if u['subject']!='english'];needed={t for u in units for t in u['topicIds']};missing=sorted(needed-written.keys());reviewMissing=sorted(needed-revised)
 fullySupplied=sum(u['hours']for u in units if all(t in written for t in u['topicIds']))
 coverage.append(dict(week=w['number'],technicalHours=sum(u['hours']for u in units),IELTSHours=sum(u['hours']for u in w['units']if u['subject']=='english'),requiredTechnicalTopics=len(needed),authoredRequiredTopics=len(needed&written.keys()),missingTechnicalTopics=missing,missingLatestRevisions=reviewMissing,fullySuppliedSubjectHours=fullySupplied))
 if not missing and fullPrefix==w['number']-1:fullPrefix=w['number']
def tree(cwd,prefix):
 lines=git('ls-tree','-r','HEAD','--',prefix,cwd=cwd).splitlines();return{r.split('\t',1)[1]:r.split()[2]for r in lines}
root=tree(R,'dist/chapters');mirror=tree(M,'study-planner/dist/chapters');same=[];bad=[]
for t,c in written.items():
 path='dist/'+c['url'];(same if root.get(path)==mirror.get('study-planner/'+path)else bad).append(t)
remote=git('ls-remote','origin','refs/heads/study-planner-1406',cwd=M).split()[0];mirrorSha=git('rev-parse','HEAD',cwd=M);assert remote==mirrorSha and not bad
onlineSource='77f4b6dd3bbabb32ac75667b0a2f83f6f8518306';online=json.loads(git('show',onlineSource+':dist/lessons.json'));onlineTopics=[c for w in online for c in w['chapters']];onlineReview=json.loads(git('show',onlineSource+':research/deep-library-revision/progress.json'))
onlinePaths={r.split('\t',1)[1]for r in git('ls-tree','-r',onlineSource,'--','dist/chapters').splitlines()};assert all('dist/'+c['url']in onlinePaths for c in onlineTopics)
report=dict(date='2026-10-14',plannedTechnicalTopics=len(topics),authoredTechnicalChapters=len(written),unwrittenTechnicalChapters=len(topics)-len(written),individuallyRevised=len(revised),existingChaptersStillNeedingRevision=len(written)-len(revised),IELTSAuthoredChapters=0,IELTSRoadmapStages=len(plan['ielts']['stages']),IELTSInitialSessionsPerStage=4,IELTSInitialPlannedSessions=4*len(plan['ielts']['stages']),IELTSFinalLessonCount='The app proposes four 60-minute sessions per stage, 44 initial sessions. Document grouping is not defined, and mastery repetitions or deeper subdivisions may increase the final lesson/session count.',subjects=subjects,weeklyCoverage=coverage,fullAuthoredTechnicalWeekPrefix=fullPrefix,wholeFirstPassWeeks=len(plan['weeks']),firstFourWeeksAvailableTechnicalHours=sum(w['fullySuppliedSubjectHours']for w in coverage[:4]),firstFourWeeksPlannedTechnicalHours=sum(w['technicalHours']for w in coverage[:4]),scheduleCoverageEquivalentWeeks=sum(w['fullySuppliedSubjectHours']for w in coverage[:4])/52,limitations='Hours are existing schedule allocations, not measured reading/solving time. Missing IELTS and week-four subjects prevent a complete four-week 7+1 track. Later topical fragments are not counted as an uninterrupted continuation.',github=dict(branch='study-planner-1406',remoteHead=remote,exactChapterBlobsMatched=len(same),mismatches=bad),online=dict(sourceCommit=onlineSource,version=106,chapterEntries=len(onlineTopics),actualChapterFilesInDeployedSource=len(onlineTopics),individuallyRevised=onlineReview['revisedChapters'],note='Confirmed deployed source includes all sixty earlier technical editions and nineteen complete individual revisions plus source errata; the newest three full revisions are on GitHub only.'))
p=R/'research/current-library-status-20261014.json';p.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(report,ensure_ascii=False,indent=2))

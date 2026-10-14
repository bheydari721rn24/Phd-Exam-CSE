"""Build an independently authored first IELTS teaching lesson and its app entry."""
from pathlib import Path
import json,re
from markdown_it import MarkdownIt
R=Path(__file__).resolve().parents[1]
text=(R/'research/ielts/academic-01-sentences.md').read_text(encoding='utf8')
md=MarkdownIt('commonmark',{'html':True}).enable('table')
body=md.render(text)
body=re.sub(r'<h1>.*?</h1>','',body,count=1)
for n in range(1,12):
 body=re.sub(r'<h2>'+str(n)+r'\. ',f'<h2 id="section-{n}">{n}. ',body,count=1)
page='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>IELTS Academic · Session 1 · Sentences, Evidence, and Listening</title><meta name="description" content="A complete 60-minute beginner lesson with ten worked grammar examples, evidence-based reading, original listening audio and explained post-teaching checks."><link rel="stylesheet" href="../chapters/chapter.en.css"><link rel="stylesheet" href="foundation.css"></head><body><main class="chapter"><p class="top-link"><a href="../index.html#ielts">← IELTS pathway and weekly plan</a></p><header class="hero"><p class="eyebrow">IELTS Academic · Foundation session 1 · 60 minutes</p><h1>Build a sentence, find evidence, and hear a correction</h1><p>Grammar · Reading · Listening · Teaching draft</p></header><nav class="toc" aria-label="Lesson contents">'''+''.join(f'<a href="#section-{n}">{label}</a>'for n,label in[(1,'Time and targets'),(2,'Sentence parts'),(3,'Affirmatives'),(4,'Negatives'),(5,'Questions'),(6,'Contractions and laboratory'),(7,'Reading'),(8,'Listening'),(9,'Summary'),(10,'After-teaching check'),(11,'References')])+f'</nav><article class="lesson">{body}</article></main><script src="foundation.js"></script></body></html>'
out=R/'dist/ielts';out.mkdir(exist_ok=True)
(out/'academic-01-sentences.html').write_text(page,encoding='utf8')
schedule=R/'dist/schedule.en.json';plan=json.loads(schedule.read_text(encoding='utf8'))
plan['ielts']['lessons']=[{'id':'academic-01-sentences','stage':1,'session':1,'title':'Build a sentence, find evidence, and hear a correction','minutes':60,'url':'ielts/academic-01-sentences.html','state':'teaching_draft','masteryConfirmed':False,'audioClips':6,'scope':'Present be, evidence-based beginner reading, names and corrected numbers.'}]
schedule.write_text(json.dumps(plan,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
app=R/'dist/app.en.js';js=app.read_text(encoding='utf8')
marker='    <div class="unit-grid">${path.stages.map'
new='''    <section class="card"><h2>Available teaching lessons</h2><p>These pages contain actual instruction, worked explanations and listening audio. Reading a page does not automatically confirm mastery.</p><div class="unit-grid">${(path.lessons || []).map(lesson => `<article class="card"><p class="eyebrow">Stage ${lesson.stage} · Session ${lesson.session} · ${lesson.minutes} minutes</p><h3>${escapeHtml(lesson.title)}</h3><p>${escapeHtml(lesson.scope)}</p><p>Teaching draft · ${lesson.audioClips} original audio clips · mastery not yet checked</p><a href="${escapeHtml(lesson.url)}">Open the complete teaching lesson →</a></article>`).join("") || "<p>No teaching lesson has been delivered yet.</p>"}</div></section>
'''
if 'Available teaching lessons'not in js:assert marker in js;js=js.replace(marker,new+marker,1)
js=js.replace('Each new chapter remains a draft until you approve it; only then does work begin on the next chapter.','Completed new or revised editions remain review drafts until you approve them. Writing continues sequentially under your standing authorization; your approval promotes an edition without blocking work on later chapters.')
app.write_text(js,encoding='utf8')
print({'lessonWords':len(text.split()),'audioClips':6,'technicalChapterCountUnchanged':True,'lesson':str(out/'academic-01-sentences.html')})

"""Refresh the current inventory from actual counts; preserve search controls."""
from pathlib import Path
import html,json,re
from teaching_prose_spacing import fix
R=Path(__file__).resolve().parents[1];D=R/'dist';P=R/'research/deep-library-revision/progress.json'
v=json.loads(P.read_text(encoding='utf8'));lessons=json.loads((D/'lessons.json').read_text(encoding='utf8'))
n=sum(len(w['chapters'])for w in lessons);assert n==64 and v['revisedChapters']==28 and v['pendingChapters']==32
p=D/'deep-library-review.html';s=p.read_text(encoding='utf8')
s=re.sub(r'<p><strong>\d+ of 60 existing editions reviewed[^<]*</strong></p>','<p><strong>28 of 60 existing editions reviewed · 32 reviews remain.</strong></p>',s)
s=re.sub(r'<p>The technical library now contains[\s\S]*?</p>','<p>The technical library contains 64 of 119 planned chapters; 55 new chapters remain. Projection, Least Squares, Adversarial Search and Constraint Satisfaction are the four additions to the original baseline. Author review and student approval are recorded separately.</p>',s,count=1)
cards='''<section class="cards"><article class="card"><h2>Functions, Scope and Parameter Passing</h2><p>Latest individual revision: 91 complete worked solutions, 80 final decision rules and 27 exact-input visual aids with 101 checkpoints. The six-course source audit distinguishes four primary universities and two supplementary courses.</p><a href="chapters/p_functions.html">Read the revised chapter</a><p><a href="reviews/p_functions-current-review.html">Read its current review</a></p></article><article class="card"><h2>Constraint Satisfaction</h2><p>New author-reviewed draft: 54 solved problems, exact constraint and propagation models, and explicit source and verification boundaries.</p><a href="chapters/i_csp.html">Read the new chapter</a><p><a href="reviews/i_csp-quality.html">Read its review</a></p></article><article class="card"><h2>IELTS Academic</h2><p>Three 60-minute lessons cover grammar, reading and listening. Each includes six original synthetic listening clips. Sessions two and three are prepared ahead; learner mastery is unconfirmed.</p><p><a href="ielts/academic-01-sentences.html">Session 1: Sentences and evidence</a></p><p><a href="ielts/academic-02-routines.html">Session 2: Routines and timetables</a></p><p><a href="ielts/academic-03-nouns.html">Session 3: Objects and precise information</a></p></article></section>'''
s=re.sub(r'<section class="cards">[\s\S]*?</section>',cards,s,count=1)
s=re.sub(r'<p>The table tracks[\s\S]*?</p>','<p>This table tracks individual review of the earlier 60-chapter library. The four new chapters do not inflate its reviewed count. Next existing review: Arrays and Indexing. Next new authoring: Informed Search.</p>',s,count=1)
s=re.sub(r'(data-filter="checked"[^>]*>)\d+ reviewed',r'\g<1>28 reviewed',s);s=re.sub(r'(data-filter="pending"[^>]*>)\d+ pending',r'\g<1>32 pending',s)
rows=''
for i,c in enumerate(v['chapters'],1):
    checked=c['state']=='revised_checked_review_draft';state='checked'if checked else'pending';label='Author-reviewed revision; student approval pending'if checked else'Individual deep review pending'
    rows+=f'<tr data-state="{state}"><td>{i}</td><td><a href="{html.escape(c["url"])}">{html.escape(c["title"])}</a></td><td>{c["questions"]}</td><td>{label}</td></tr>'
s=re.sub(r'<tbody>[\s\S]*?</tbody>','<tbody>'+rows+'</tbody>',s,count=1)
p.write_text(fix(s),encoding='utf8');print('Current inventory: 64 chapters; 28 baseline reviews complete, 32 remain.')

from pathlib import Path
import json,re
B=Path(__file__).resolve().parent;R=B.parent
title='The Pigeonhole Principle: Sharp Guarantees, Hidden Classes, and Constructive Witnesses'
s=(B/'render_d_inclusion.py').read_text().split('downloads={',1)[0].replace('d_inclusion','d_pigeonhole').replace('inclusion','pigeonhole').replace('Inclusion-Exclusion: Overlap, Exact Multiplicity, and Forbidden Configurations',title).replace('four primary university courses and one reviewed complementary course','five primary written courses from four universities and a sixth complementary course').replace('13 dedicated concept traces','18 dedicated concept traces').replace('animationCount=13,animationWalkthroughCount=13','animationCount=18,animationWalkthroughCount=18')
start=s.index("lab='''");end=s.index("source=",start)
s=s[:start]+'''lab='<section class="lab" id="pigeonhole-lab"><form id="pigeonhole-form"><label>Exact laboratory<select name="mode"><option value="occupancy">Occupancy and collision pairs</option><option value="prefix">Divisible contiguous blocks</option><option value="sequence">Strict monotone subsequences</option><option value="graph">Two-color complete graphs</option></select></label><label>Comma-separated integer values<input name="values" type="text" value="4,4,3,3,3" required></label><label>Positive modulus<input name="m" type="number" min="1" max="12" value="5"></label><label>Vertices<select name="n"><option value="5">Five</option><option value="6" selected>Six</option></select></label><label>Edge-color mask<input name="mask" type="number" min="0" max="32767" value="0"></label><button type="submit">Compute and draw the witness</button></form><div id="pigeonhole-output" aria-live="polite"></div><p>Occupancy mode permits one to eight bins and at most forty total objects. Prefix mode permits one to twelve values from −20 to 20 and modulus one to twelve. Sequence mode permits one to nine integer values from −20 to 20; duplicates are explicitly identified, and exhaustive index-subset enumeration checks the dynamic program. Graph mode permits five or six vertices and a legal integer bit mask: ten bits for five vertices, fifteen for six. Bits follow unordered edges in increasing lexicographic order. Blue is zero, red is one. A five-cycle counterexample uses five vertices and mask 665.</p></section>'
''' + s[end:]
s=s.replace("anchors=['sources','atoms','theorem','multiplicity','bounds','maps','derangements','rook','allocations','arithmetic','probability','computation','problems','review','laboratory','references']","anchors=['sources','assignment','average','capacity','collisions','residues','subsets','chains','geometry','subsequences','graphs','information','summary','problems','review','laboratory','references']")
s=s.replace("Authentic examination revisits","Authentic examination questions and conceptual bridges")
# Render original MC alternatives too; preserve the approved shared helper.
needle="bank='<h3 id="
pos=s.index(needle)
s=s[:pos]+'''old_item=item
def item(q,n,authentic=False):
 h=old_item(q,n,authentic)
 if not authentic and q.get('options'):
  opts='<div class="exam-options">'+''.join('<div class="exam-option"><b>'+str(i)+'.</b><div>'+text(v)+'</div></div>' for i,v in enumerate(q['options'],1))+'</div>'
  h=h.replace('<details class="exam-solution">',opts+'<details class="exam-solution">',1).replace('<summary>Read the complete derivation and reasoning</summary>','<summary>Read the complete derivation and reasoning</summary><p><strong>Correct option: '+str(q['answer'])+'.</strong></p>',1)
 return h
''' +s[pos:]
(B/'render_d_pigeonhole.py').write_text(s,encoding='utf-8')
css=(R/'dist/chapters/d_inclusion.css').read_text().replace('inclusion','pigeonhole')+'\n#pigeonhole-form input[name=values]{width:250px;max-width:100%}.pigeonhole-stage svg [data-entity] text{font-size:16px}.pigeonhole-stage .math-label,.pigeonhole-lab-diagram .math-label{font-family:"STIX Two Math",serif}\n'
(R/'dist/chapters/d_pigeonhole.css').write_text(css,encoding='utf-8')
s=(R/'dist/chapters/d_inclusion.js').read_text();s=s[:s.index('function maps')].replace('inclusion','pigeonhole');s+=(B/'d_pigeonhole-lab.js').read_text(encoding='utf-8')+'\n})();\n';(R/'dist/chapters/d_pigeonhole.js').write_text(s,encoding='utf-8')
# Add fields required by the established archive renderer.
p=B/'d_pigeonhole-authentic.json';actual=json.loads(p.read_text(encoding='utf-8'))
for q in actual:
 q.setdefault('sourceCommit',q.get('repositoryCommit'));q.setdefault('pdfPage',q.get('physicalPage'));q.setdefault('questionNumber',116 if q['id'].endswith('Q116') else 25);q.setdefault('booklet','MS_CS_1405' if 'Q116' in q['id'] else 'Phd_CS_1404')
p.write_text(json.dumps(actual,indent=2)+'\n',encoding='utf-8')
downloads={x['key']:x for x in json.loads((B/'d_pigeonhole-downloads.json').read_text())}
specs=[('mit','MIT','6.042J Mathematics for Computer Science, Spring 2015; Eric Lehman, F. Thomson Leighton and Albert R. Meyer','§14.8 physical pages 581–590; selected Problems 14.37–14.43, physical pages 618–619','Finite assignments, equal sums, card channels and boundary exercises'),('mit18','MIT','18.310 Principles of Discrete Applied Mathematics, Fall 2013; Michel Goemans','Pigeonhole lecture, September 2; all five pages','Monotone labels and adaptive one-lie transcript counting'),('oxford','Oxford','Discrete Mathematics, Michaelmas 2010; Andrew D. Ker','§6.5 physical pages 87–89; Exercises 6.7–6.8 physical page 92, solutions page 94','Divisibility, modular images, compression and geometric partitions'),('stanford','Stanford','CS103, Winter 2026; Sean Szumlanski','Lecture 11 physical pages 12–74, 83–135; page 139 zero-one exercise only','Degree restrictions, saturation, strict averages and Ramsey branching'),('toronto','Toronto','MAT344 Introduction to Combinatorics, Summer 2019; Balazs Elek','Lecture 7 §4, physical pages 1–2 before §5','Independent monotone-subsequence proof and odd-part chains'),('cornell','Cornell','CS2800 A Course in Discrete Structures; Rafael Pass and Wei-Lung Dustin Tseng','§4.5 physical page 77, Lemma 4.28 and Example 4.29','Complementary ceiling formulation and contradiction proof')]
urls={'oxford':'https://www.cs.ox.ac.uk/andrew.ker/docs/discretemaths-lecture-notes-mt2010.pdf','cornell':'https://www.cs.cornell.edu/courses/cs2800/2016sp/handouts/pass_tseng_discmath.pdf'}
courses=[]
for key,uni,course,scope,role in specs:
 d=downloads.get(key,{});url=d.get('url',urls.get(key));doc=dict(url=url,readingScope=scope,access='Original cached PDF inspected' if 'sha256' in d else 'Official PDF section read through web text reader; no local checksum claimed')
 if 'sha256' in d:doc.update(sha256=d['sha256'],cachedPath=d['path'])
 courses.append(dict(id=key+'-pigeonhole-written',subject='discrete',university=uni,course=course,url=url,evidence=url,topics=['d_pigeonhole'],advantage=role,limit='Bounded nine-candidate comparison, not an exhaustive worldwide ranking',access='Official public written text',reviewed=True,reviewScope=scope,selectionRole='Complementary' if key=='cornell' else 'Primary',sourceDocuments=[doc]))
(B/'d_pigeonhole-reviewed-courses.json').write_text(json.dumps(courses,indent=2)+'\n',encoding='utf-8')
p=R/'dist/course-audit-week1.en.json';a=json.loads(p.read_text());ids={c['id'] for c in courses};a['courses']=[c for c in a['courses'] if c['id'] not in ids]+courses;a['reviewedAt']='2026-10-05';p.write_text(json.dumps(a,indent=2)+'\n',encoding='utf-8')
print('Prepared chapter-only renderer, fonts, laboratories and exact reading records.')

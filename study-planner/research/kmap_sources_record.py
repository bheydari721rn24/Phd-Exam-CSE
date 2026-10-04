"""Record a finite discoverable pool, actual reading, and source corrections."""
from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parent;R=B.parent;C=Path('C:/Users/bheydari/AppData/Local/Temp/phd-kmap-sources')
docs=json.loads((C/'acquisition.json').read_text());p=C/'columbia.pdf'
docs.append(dict(id='columbia',url='https://www.cs.columbia.edu/~cs6861/handouts/quine-mccluskey-handout.pdf',pages=15,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
specs=[('mit','MIT','6.004 Computation Structures, Spring 2017; Chris Terman','Lecture 4 written annotations, slides 1–4 and 10–20 in depth; slides 21–29 screened for implementation context','Primary: specification, SOP, implicants, care sets and hazard coverage',[5,4,4,3]),('cambridge','Cambridge','Digital Electronics, 2025–26; Ian J. Wassell','Combined slides 21–43 and Examples Paper 1, all three pages; POS slide 34 and exercise page 2 visually checked','Primary: canonical polarity, Gray maps, POS, don’t-cares and tabular simplification',[5,5,4,5]),('stanford','Stanford','EE108A, Winter 2008; Philip Levis; reader author William J. Dally, 2002–2006','Reader Chapter 6, PDF pages 83–105, all text and exercise families read','Primary: cubes, essential primes, nonunique covers, greedy counterexample and delay hazards',[5,5,5,5]),('cornell','Cornell','ECE2300 / ENGRD2300, Fall 2026; Christopher Batten','T03 Boolean Algebra, all 26 pages; revision 2026-09-08','Primary: algebra-to-map connection, stepwise grouping and abstraction',[5,4,4,4]),('columbia','Columbia','CSEE E6861, 2016; Steven Nowick','Handout 5, Quine–McCluskey, all 15 pages; three exact covering examples','Selected fifth complement: chart dominance, secondary essentials and Petrick’s method',[5,5,5,5])]
courses=[]
for key,uni,course,scope,role,scores in specs:
 linked=[d for d in docs if d['id'].startswith(key)]
 courses.append(dict(id=key+'-minimization-written',subject='logic',university=uni,course=course,url=linked[0]['url'],evidence=linked[0]['url'],topics=['g_kmap'],advantage=role+'; '+scope,limit='Accessible bounded pool; exact reading and source corrections are documented.',access='Official public written material',reviewed=True,reviewScope=scope,selectionRole=role,selectionScores=dict(zip(['writtenAccess','boundaryCoverage','semanticDepth','exerciseValue'],scores)),sourceDocuments=linked))
(B/'g_kmap-reviewed-courses.json').write_text(json.dumps(courses,indent=2)+'\n')
out=R/'dist/evidence/g_kmap';out.mkdir(parents=True,exist_ok=True)
(out/'sources.json').write_text(json.dumps(dict(state='reviewed',readingDate='2026-10-04',courses=courses,documents=docs,scope='Nine university candidates discovered/screened. Five courses actually read. Four complementary primary courses and a fifth advanced source selected; no worldwide exhaustive claim.'),indent=2)+'\n')
s='''# Logic minimization: source selection and reading audit

## Selection method and bounded pool

Nine university candidates were discovered or screened: MIT, Cambridge, Stanford, Cornell, Columbia, Berkeley, CMU, Michigan and Illinois. Five accessible written courses were actually read. Four primary courses supply complementary foundations; Columbia is necessary as a fifth source for exact cyclic covering and dominance. Comparative scores below are editorial judgments, not objective worldwide rankings. Course dates are explicitly identified, including archived Stanford material. No claim is made that every course worldwide has been read.

## Actual reading and contributions

'''
for c in courses:s+=f"### {c['university']} — {c['course']}\n\n{c['reviewScope']}. {c['selectionRole']}. Written access / boundary coverage / semantic depth / exercise value: "+' / '.join(map(str,c['selectionScores'].values()))+f".\n\n[Official written source]({c['url']}). Acquisition hashes are recorded in the evidence file.\n\n"
s+='''## Alternatives and access limits

Berkeley CS150 Spring 1998 lecture outline was screened; its body was not comprehensively read. CMU 18-240 Fall 1996 course index was screened but usable lecture bodies were not retrieved. Michigan EECS270 Spring 2023 homework index was found, but no full lecture body was read. Illinois ECE462 Fall 2020 index exposes QM and Petrick lectures, but bodies were not read because the selected Columbia text provides an explicit exact-cover treatment. These four alternatives are not counted as reviewed courses.

## Reconciliation and corrections

MIT’s “cannot expand any selected term” argument establishes prime status, not global cover optimality. This chapter proves the prime restriction under its stated cost, then solves the chart exactly. Stanford explicitly acknowledges that greedy covering can be nonminimum. The lesson distinguishes irredundancy, prime status, minimum term count and minimum literal count.

Stanford’s prime-number example includes index 1; modern mathematical primality excludes 1. Our prime-detector tasks use 2,3,5,7,11,13. The reader’s “conjunctive (sum-of-products)” figure caption is inconsistent with standard CNF/DNF terminology. The chapter uses canonical DNF for the minterm sum and canonical CNF for the maxterm product. The decimal example refers to three primes while listing four; independent enumeration controls our counts. Stanford’s OR(bit-pattern) maxterm convention differs from ordinary index numbering; the chapter consistently defines M_i as zero at input i.

Columbia places implicants in columns and minterms in rows; Cambridge uses the transpose. Our charts put primes in rows and ON minterms in columns. Dominance is therefore taught by explicit set inclusion, not memorized “delete the dominating row” wording. Cost must be no larger before replacing a candidate. Equal-cost dominance can discard alternative optimal covers; it preserves an optimal value, not necessarily every optimum. Secondary essentials depend on earlier pruning choices and are not necessarily essential in the original chart.

Don’t-care cells are permission to choose outputs under an external input contract. Pure DC cubes may be generated as intermediate QM objects, but do not become required coverage obligations. The hazard treatment is confined to two-level SOP/POS and single-input changes with stable other inputs. It does not promise immunity to all dynamic or multiple-input hazards. Care-set equivalence is weaker than equality on all Boolean rows.

## Questions, figures and archive provenance

All figures and animations are original. Relevant course exercise families—threshold voters, canonical polarity, prime/Fibonacci detectors, BCD, all minimum covers, chart reduction, tabular merging and hazards—are represented by independently worded extensions. The chapter does not republish complete copyrighted course problem sheets or Cornell figures. Source PDFs are cached privately; no originals enter the public artifact.

Three authentic questions are revisited: MSc CS 1405 Q99, PhD CS 1405 Q22, and MSc CE 1405 Q78. Each was checked against its rendered original PDF page at the pinned archive commit. This revisit corrects a prior shortened transcription of Q78 option 4: the original has five products, including both complemented-B/complemented-C and complemented-A/complemented-C. Its extra term violates specified zero row 4. Earlier approved banks are preserved; this chapter records the corrected original explicitly. Q78 is a convention-sensitive tutorial with no unqualified single correct answer. It is excluded from single-answer scoring; the chapter adds an explicitly costed original hazard problem. Answers are independently derived, not official keys. These are revisits, not newly unique archive items.

## Coverage boundary

The chapter covers canonical forms, indexing, cubes, Gray maps through six-variable layout, exact SOP/POS, DC contracts, QM, chart dominance, Petrick, proofs of minimality, hazard-constrained covering and multi-output sharing. Timing claims state a gate-delay model. Technology mapping, large-scale heuristic synthesis, sequential minimization and transistor-level effects are separate topics. Exhaustive small-instance tests and provenance checks support the authored artifact; they cannot certify every possible unseen examination question.
'''
(B/'g_kmap-source-audit.md').write_text(s,encoding='utf-8')
(B/'g_kmap-quality-audit.md').write_text('# Logic minimization: verification audit\n\nReview draft. Exact cost conventions, care-set contracts, indexing order, dominance direction and hazard assumptions are explicit. Independent validation and browser results are added after actual execution. No absolute correctness or examination-performance guarantee is claimed.\n',encoding='utf-8')
print('Recorded five genuinely reviewed written courses and bounded selection evidence.')

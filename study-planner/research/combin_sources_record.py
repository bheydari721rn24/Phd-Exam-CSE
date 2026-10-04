from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parent;R=B.parent
C=Path('C:/Users/bheydari/AppData/Local/Temp/phd-combin-sources');K=C.parent/'phd-kmap-sources'
specs=[
 ('mit','MIT','6.004 Computation Structures, Spring 2017; Chris Terman','https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/pages/c4/c4s1/',K/'mit.txt','Lecture 4 written annotations: specification and fan-in/tree passages, and slides 21–29 multiplexer/decoder/ROM annotations read in full. Earlier Boolean sections previously reviewed.','Specification completeness, arrival-sensitive tree choice, table-lookup universality',[5,5,5,4]),
 ('stanford','Stanford','EE108A, Winter 2008; Philip Levis; reader author William J. Dally','https://web.stanford.edu/class/archive/ee/ee108a/ee108a.1082/reader/ch1to12.pdf',K/'stanford.pdf','Chapter 6 PDF pages 83–105 previously read in full; pages 83–86 and 95–96 reread for acyclic composition and mapping.','Acyclic-closure proof and design procedure from a mathematical contract',[5,5,5,5]),
 ('cambridge','Cambridge','Digital Electronics, 2025–26; Ian J. Wassell','https://www.cl.cam.ac.uk/teaching/2526/DigElec/materials.html',K/'cambridge.pdf','Combined slides pages 55–70 read in full; page 57 visually checked against original PDF. Earlier pages 21–43 and Examples Paper 1 previously reviewed.','Multilevel factoring, shared expressions, block implementation tradeoffs',[5,5,4,4]),
 ('cornell','Cornell','ECE2300 / ENGRD2300, Fall 2026; Christopher Batten','https://www.csl.cornell.edu/courses/ece2300/handouts/ece2300-T02-comb-logic.pdf',C/'cornell.pdf','T02 Combinational Logic, all 34 PDF pages read; revision 2026-09-03-23-48.','Internal net derivation, multiple outputs, structural Verilog and interval timing',[5,5,5,5]),
 ('berkeley','Berkeley','CS150, Fall 2005; Randy H. Katz','https://people.eecs.berkeley.edu/~randy/Courses/CS150.F05/Lectures/02-CombLogic.pdf',C/'berkeley.pdf','Lecture 2, all 37 PDF pages / 73 slides read, especially 18–24, 52–58 and 63–72.','Explicit cost models, multi-output examples and polarity-preserving NAND/NOR mapping',[5,5,4,5])]
courses=[]
for key,u,course,url,path,scope,role,scores in specs:
 courses.append(dict(id=key+'-combin-design-written',subject='logic',university=u,course=course,url=url,evidence=url,topics=['g_combin'],advantage=role+'; '+scope,limit='Bounded accessible comparison, not a worldwide exhaustive ranking.',access='Official public written course material',reviewed=True,reviewScope=scope,selectionRole=role,selectionScores=dict(zip(['writtenAccess','boundaryCoverage','semanticDepth','exerciseValue'],scores)),sourceDocuments=[dict(url=url,sha256=hashlib.sha256(path.read_bytes()).hexdigest(),readingScope=scope)]))
(B/'g_combin-reviewed-courses.json').write_text(json.dumps(courses,indent=2)+'\n')
pub=R/'dist/evidence/g_combin';pub.mkdir(parents=True,exist_ok=True)
(pub/'sources.json').write_text(json.dumps(dict(readingDate='2026-10-04',state='reviewed',courses=courses,selection='Five complementary written courses selected from nine university candidates. All five selected bodies actually read within their recorded ranges. Comparative scores are editorial judgments.'),indent=2)+'\n')
s='''# Combinational circuit design: source and selection audit

## Bounded discovery and comparison

Nine university candidates were screened across this and the preceding logic research: MIT, Stanford, Cambridge, Cornell, Berkeley, Columbia, CMU, Michigan and Illinois. Five accessible written courses were actually read and selected for this boundary. MIT, Stanford, Cornell and Cambridge provide the four primary complementary treatments; Berkeley is included as a fifth source because its technology mapping and multi-output design examples strengthen the worked problems. This is a bounded documented selection, not a claim to have read every course worldwide or an objective worldwide ranking.

'''
for c in courses:s+='### '+c['university']+' — '+c['course']+'\n\n'+c['reviewScope']+' '+c['selectionRole']+'. Scores (access / coverage / semantic depth / exercises): '+' / '.join(map(str,c['selectionScores'].values()))+'.\n\n[Official written course]('+c['url']+').\n\n'
s+='''## Alternatives

Columbia's reviewed QM handout is strong for exact minimization but does not provide the present specification-to-netlist boundary; it stays attributed in the preceding chapter. CMU's public historical course index did not yield retrieved written bodies. Michigan's accessible homework index and Illinois's lecture index were screened but their bodies were not read. They are not counted as reviewed courses. The source cache is private. Course PDF originals and copyrighted diagrams are not republished.

## Reconciliation

The lesson consistently uses A as the most significant input bit unless another order is explicitly stated. Cornell's ordering in displayed structural examples and comments is not adopted without independent row evaluation. Stanford's prime-number example includes 1; this lesson uses the modern definition excluding 1. Acyclic composition is a sufficient structural guarantee of history-independent behavior; it is not a theorem that every algebraic feedback equation necessarily has multiple solutions.

Cambridge page 57 is visually checked: its seven-input expression factors as (a+b+c)(d+e)f+g. The claimed four-gate implementation assumes three-input OR/AND gates; using only two-input gates changes counts and depth. MIT's logarithmic tree depth is stated as a ceiling for non-power-of-two widths and assumes simultaneous input arrival; a late-arriving input can favor an unbalanced tree. Berkeley's historical transistor counts and cost approximations are not universal constants for every library.

Cornell's X simulation value is kept distinct from a specification don't-care. Structural minimum and maximum delay recurrences are conservative path bounds; a structural path is not necessarily sensitizable. ROM storage is treated as a fixed lookup function under asynchronous read assumptions, not every practical memory interface. Behavioral SystemVerilog examples are original constructions supported by explicit truth tables; this review uses independent mathematical models and does not claim HDL compilation or electrical simulation.

## Archive and original questions

PhD CE 1405 Q23 (PDF page 6) and MSc CE 1404 Q80 (PDF page 19) are authentic bridge revisits, visually checked this run against their pinned original PDF pages. Their diagrams are transcribed into explicit equations; answers are independently derived, not official answer keys. The original PDFs retain their archive SHA-256 provenance. Previously approved banks remain unchanged. Original questions extend reviewed course families with new truth functions, multiple outputs, cofactors, costs, fault witnesses, delay calculations and formal counterexamples. They are not verbatim republications of entire course problem sheets.

## Coverage boundary

The chapter treats functional specification, care sets, history independence, DAG evaluation and proof, shared multilevel logic, polarity mapping, cofactor-based construction, decoder/ROM universality, width and active-low interfaces, complete combinational assignments, equivalence miters, fault testing, structural timing, false paths and integrated controller design. Dedicated detailed adder/comparator, mux/encoder, timing and hazard chapters remain distinct. Finite exhaustive checks for authored small models do not certify every possible unseen examination question.
'''
(B/'g_combin-source-audit.md').write_text(s,encoding='utf-8')
(B/'g_combin-quality-audit.md').write_text('# Combinational circuit design: verification audit\n\nDraft in progress. Observed independent scientific and browser results will be added after execution. No absolute correctness or examination-performance guarantee is claimed.\n')
items=json.loads((B/'exam-calibration/actual-items.json').read_text());auth=[q for q in items if q['id'] in ['Phd_CE_1405_Q23','MS_CE_1404_Q80']]
assert len(auth)==2
for q in auth:q['qNumber']=q['questionNumber']
(B/'g_combin-authentic.json').write_text(json.dumps(auth,indent=2)+'\n')
print('Five reviewed written courses and two authentic PDF-checked bridge revisits recorded.')

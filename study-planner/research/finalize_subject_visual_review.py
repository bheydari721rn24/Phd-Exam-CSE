"""Publish observed revision evidence, refresh hashes and close the review gate."""
from pathlib import Path
import json,html,re,hashlib,subprocess,tempfile,shutil
from revise_visual_library import questions,question_reasoning
ROOT=Path(__file__).resolve().parents[1]
BASE='2418526b9d18fb9a0ced9dc412fc59345745c530'
def read(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def write(p,v):
    path=ROOT/p;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
def main():
    report=read('research/subject-visual-review.json');browser=read('research/subject-visual-browser-audit.json')
    assert len(browser['scenes'])==206 and not browser['errors']
    assert not any(s['failures'] for s in browser['scenes'])
    assert len(browser['mathematicalLayout'])==31 and browser['renderedCircuitTruthCases']==48
    figure_path=Path(tempfile.gettempdir())/'chapter-library-review/browser-review.json'
    figures=json.loads(figure_path.read_text(encoding='utf-8'));assert len(figures)==31
    assert all(not f['outside'] and not f['overlap'] for r in figures for f in r['figures'])
    assert all(r['printStyle']['diagramOverflow']==0 and r['mobile']['document']<=390 for r in figures)
    write('research/subject-library-browser-audit.json',figures)
    plan=read('dist/schedule.en.json');animation=read('research/animation-manifest.json')
    for row in report['chapters']:
        topic=row['topicId'];path=ROOT/f'dist/chapters/{topic}.html';after=path.read_text(encoding='utf-8')
        before=subprocess.check_output(['git','show',BASE+':dist/chapters/'+topic+'.html'],cwd=ROOT).decode('utf-8')
        assert [question_reasoning(q) for q in questions(before)]==[question_reasoning(q) for q in questions(after)],topic
        # Every pre-existing source expression must retain its literal TeX source.
        # Newly drawn SVGs can contain additional native formula labels; compare
        # the original written expressions separately from revised artwork.
        sources=lambda s:re.findall(r'<math\b[^>]*aria-label="([^"]*)"',re.sub(r'<svg\b[\s\S]*?</svg>','',s))
        assert sources(before)==sources(after),topic+' formula sources changed'
        row.update(state='awaiting_user_approval',htmlSha256=hashlib.sha256(path.read_bytes()).hexdigest(),reviewed=True)
    assert sum(r['questionCount'] for r in report['chapters'])==1747
    report.update(state='awaiting_user_approval',questionCount=1747,staticSchematicsRewritten=13,printableWalkthroughs=169,checkpointsRendered=1211,
      validation={'chapters':31,'scenarios':206,'checkpoints':1211,'sceneLabelBoundaryFindings':0,'figureLabelFindings':0,'mobileWidth':390,'mathematicalSourcesAndTokensPreserved':True,'renderedCircuitTruthCases':48,'serializedReferenceAssertions':read('research/animation-model-audit.json')['assertions']},
      proseReviewScope='Visual reading instructions and diagram captions rewritten; existing definitions, proofs, worked problems, source selections and examination rules retained. This delivery does not claim a fresh sentence-by-sentence rewrite of all prose.',
      approval='All revised visual layers remain pending explicit user approval. Historical chapter-content approvals are recorded separately.')
    write('research/subject-visual-review.json',report)
    for ar in animation['chapters']:
        ar['htmlSha256']=next(r['htmlSha256'] for r in report['chapters'] if r['topicId']==ar['topicId'])
        ar['visualRevisionState']='awaiting_user_approval'
    animation.update(visualReviewPath='research/subject-visual-review.json',state='subject_visual_revision_awaiting_user_approval')
    write('research/animation-manifest.json',animation)
    for name in ['research/exam-calibration/manifest.json','dist/evidence/exam-calibration/manifest.json']:
        m=read(name)
        for c in m['chapters']:c['htmlSha256']=hashlib.sha256((ROOT/f'dist/chapters/{c["topicId"]}.html').read_bytes()).hexdigest()
        write(name,m)
    lessons=read('dist/lessons.json')
    for w in lessons:
        for c in w['chapters']:
            if any(r['topicId']==c['topicId'] for r in report['chapters']):c['visualRevisionState']='awaiting_user_approval'
    write('dist/lessons.json',lessons)
    write('dist/evidence/subject-visual-review/review.json',report)
    write('dist/evidence/subject-visual-review/browser.json',browser)
    # Short visible report: subject filter and cards, with exact scope and evidence.
    names={'bars':'Record bars and moving indices','search':'Search intervals','venn':'Set regions','truth':'Truth tables','graph':'Graphs and relation arrows','tiles':'Constructive tiles','derivation':'Proof and arithmetic dependencies','tree':'Recursion and dependency trees','geometry':'Coordinate geometry','matrices':'Matrix transformations','enumeration':'Outcome enumeration','numeric':'Numeric representations','memory':'Frames, references and flow','array':'Indexed storage','probability':'Probability regions and distributions','plot':'Quantitative sample plots','cmos':'Transistor schematics','circuit':'Circuit schematics','waveform':'Timing waveforms','kmap':'Gray maps and covering charts'}
    cards=[]
    for r in report['chapters']:
        t=plan['topics'][r['topicId']];subject=plan['subjects'][t['subject']]['title'];title=t['title']
        cards.append('<section class="review-card" data-subject="'+html.escape(subject,quote=True)+'"><p class="eyebrow">'+html.escape(subject)+'</p><h2><a href="chapters/'+r['topicId']+'.html?v=67">'+html.escape(title)+'</a></h2><p>'+html.escape('; '.join(names[k] for k in r['visualTypes']))+'.</p><p>'+str(len(r['models']))+' models · '+str(r['questionCount'])+' worked question entries retained.</p><p><a href="chapters/'+r['topicId']+'.html?v=67#visual-reading-guide">Read the revised diagram guide →</a></p></section>')
    subjects=sorted({plan['subjects'][plan['topics'][r['topicId']]['subject']]['title'] for r in report['chapters']})
    options='<option value="">All subjects</option>'+''.join('<option>'+html.escape(s)+'</option>' for s in subjects)
    body='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Subject-specific visual revision</title><link rel="stylesheet" href="chapters/chapter.en.css?v=67"><style>.review-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,280px),1fr));gap:18px}.review-card{border:1px solid #d2e2e9;border-radius:12px;padding:20px;background:#fff}.review-card h2{margin:0!important;padding:0!important;border:0!important;font-size:1.5rem}.review-card p{margin:.7rem 0}.review-grid [hidden]{display:none}.review-filter{font:inherit;padding:9px;border:1px solid #bfd3de;border-radius:7px;margin:12px 0}.revision-note{padding:20px;background:#edf6f9;border-left:3px solid #297d91}</style></head><body><main class="chapter"><p class="top-link"><a href="index.html#library">← Chapter library</a></p><header class="hero"><p class="eyebrow">All 31 existing chapters · review draft</p><h1>Subject-specific diagrams and mathematical layout</h1><p>Twenty visual families replace the common card presentation. Circuit gates, transistor channels, memory references, matrices, probability regions and algorithm records now have distinct representations.</p></header><article class="lesson"><section class="revision-note"><h2>What this revision changes</h2><p>All 206 saved models use an explicit subject-specific visual contract. Thirteen static circuit figures were redrawn with named nets and gate or transistor symbols. The 169 embedded walkthroughs retain printable first-checkpoint diagrams. Every chapter includes a new guide to reading its diagrams.</p><p>Mathematical layout uses STIX Two Math, balanced fences, attached scripts and spaced matrix entries. Mobile line breaks preserve the order of mathematical leaves. Wide matrices and indivisible quantified scopes use a labeled, horizontally scrollable equation region rather than losing symbols.</p><p>The existing deep lessons, proofs, 1,747 worked question entries and cited course pool remain in place. Visual instructions and figure captions were rewritten. This is not a claim that every prose paragraph was reauthored or that university sources were newly searched worldwide.</p></section><h2>Verification performed</h2><p>All 1,211 checkpoints in 206 models rendered without missing or nonfinite data or text outside the SVG boundary. Static figures across all 31 chapters passed their label and print-width checks. At a 390-pixel viewport, every chapter preserved mathematical text and source expressions; required equation panning was labeled and accessible. Forty-eight rendered input cases matched independent circuit predicates and declared gate counts. The existing 5,266 serialized-state/reference checks also passed.</p><p>These are bounded mathematical teaching models. Boolean truth tables do not certify analog transistor behavior; joined plot samples are orientation guides, not exact continuous curves. Interpolated movement between checkpoints adds no new mathematical or electrical state. General claims still depend on the written proof and stated assumptions.</p><p><a href="evidence/subject-visual-review/review.json">Chapter revision record</a> · <a href="evidence/subject-visual-review/browser.json">Browser and formula evidence</a></p><h2>Review a chapter</h2><p>Choose a subject, open a chapter, and inspect its diagrams and formulas. This revision awaits your explicit approval before the next new chapter begins.</p><label for="review-subject">Subject</label> <select class="review-filter" id="review-subject">'''+options+'</select><div class="review-grid">'+''.join(cards)+'''</div></article></main><script>document.getElementById('review-subject').addEventListener('change',e=>document.querySelectorAll('.review-card').forEach(c=>c.hidden=!!e.target.value&&c.dataset.subject!==e.target.value));</script></body></html>'''
    (ROOT/'dist/subject-visual-review.html').write_text(body,encoding='utf-8')
    for f in ['dist/library-review.html','dist/animation-review.html']:
        p=ROOT/f;s=p.read_text(encoding='utf-8');s=re.sub(r'<!-- SUBJECT VISUAL REVIEW -->[\s\S]*?<!-- END SUBJECT VISUAL REVIEW -->','',s)
        notice='<!-- SUBJECT VISUAL REVIEW --><aside class="visual-reading-guide"><h2>Current revision awaits approval</h2><p>All 31 chapters have a revised visual and mathematical layer. Earlier approval statements below describe previous versions. <a href="subject-visual-review.html">Open the current chapter-by-chapter review →</a></p></aside><!-- END SUBJECT VISUAL REVIEW -->'
        s=re.sub(r'(<main\b[^>]*>)',lambda m:m[0]+notice,s,count=1);p.write_text(s,encoding='utf-8')
    p=ROOT/'dist/index.html';s=p.read_text(encoding='utf-8')
    s=re.sub(r'(<section\b[^>]*id="view-lessons"[^>]*><p class="card">)[\s\S]*?(</p>)',lambda m:m[1]+'The visual and mathematical revision of all 31 existing chapters is ready for review. <a href="subject-visual-review.html">Choose a subject and review the revised chapters →</a>'+m[2],s,count=1)
    p.write_text(s,encoding='utf-8')
    gate=read('research/chapter-gate.json');gate.update(state='awaiting_user_approval',nextTopicId=None,proposedNextTopicId=None,activeWork='Completed whole-library visual/math revision; awaiting explicit user review.',lastCompletedReview='All 31 chapters: 20 visual families, 13 rewritten static schematics, 206 models / 1211 checkpoints, mathematical layout and 1747 retained question entries. Scope and observed checks: research/subject-visual-review.json.',nextReview='Await approval of the whole-library revision. Do not start d_counting or quiz the user.',visualReviewPath='research/subject-visual-review.json')
    write('research/chapter-gate.json',gate)
    p=ROOT/'WEEKLY_DELIVERY.md';s=p.read_text(encoding='utf-8')
    marker='## Current authoritative handoff — subject-specific whole-library revision'
    if marker in s:s=s[:s.index(marker)]
    s+='\n'+marker+'''\n\n5 October 2026: The user rejected the shared simulation style, missing circuit schematics and disorganized formulas across all existing chapters. This instruction authorized revision of the full 31-chapter library; no new chapter was started. Earlier next-chapter instructions above are historical.\n\nThe delivered review draft is dist/subject-visual-review.html. All 206 models now dispatch through twenty explicit subject-specific families in semantic-diagrams.js. Thirteen static logic/circuit figures and 169 printable initial walkthroughs use the revised models. Corrected transistor connectivity, enable/polarity, priority validity, ring capacity, matrix transpose, coordinate scaling, probability conditioning, shared nets and circuit routing are included. Interactive remounting now disposes prior players and keyboard handlers instead of keeping stale laboratory states.\n\nEvery chapter receives visual reading instructions. Existing deep lessons, proofs, rules and all 1,747 question entries are retained; stems, solution reasoning and TeX sources are checked against the opening source SHA. This is not a claim that all prose was freshly reauthored. Sources were not re-searched worldwide during this visual revision. Mathematical layout preserves leaves and scope, restores canonical expressions for print, spaces matrix entries, and provides labeled internal mobile panning for indivisible expressions.\n\nObserved evidence: all 1,211 checkpoint renders / 206 models, all 31 chapter figure layouts and printable solutions, actual 390-pixel mathematical containment and leaf/source preservation, 48 rendered circuit input predicates / topology counts, and 5,266 serialized/reference assertions. Separate combinational checks passed 7,911 assertions and 96 input/variant comparisons. Finite models do not certify electrical behavior or unseen examination performance. See research/subject-visual-review.json, research/subject-visual-browser-audit.json and research/subject-library-browser-audit.json.\n\nThe gate is awaiting_user_approval for this whole-library revision. Historical chapter approvals remain recorded separately; revised visual layers are pending. Do not begin d_counting until the user approves continuation. Do not ask the user test questions before initial study. Study-progress storage and private PDFs are preserved.\n\nMaintenance: research/revise_visual_library.py assigns explicit contracts and canonical math; research/qa_subject_visuals.py renders models and checks mobile mathematical preservation; research/install_subject_figures.py installs printable SVGs and math-styled captions; research/finalize_subject_visual_review.py refreshes hashes, evidence, report and gate after observed QA. build_concept_animations.py retains reviewed visual contracts/previews and canonical math. Historical one-time patch scripts are migration provenance, not required maintenance commands. Publish the exact pushed source to the existing owner-private Site and mirror changed files only to GitHub branch study-planner-1406, preserving unrelated mirror deletions.\n'''
    p.write_text(s,encoding='utf-8')
    print(json.dumps(report['validation']))
if __name__=='__main__':main()

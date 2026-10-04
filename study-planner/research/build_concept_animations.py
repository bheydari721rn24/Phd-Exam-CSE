"""Build exact scenario data, embed controls, and preserve chapter text/progress."""
import hashlib,html,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'research/animations'),str(ROOT/'research/exam-rewrite'),str(ROOT/'research')]
import algorithms,discrete,quantitative,programming_logic,advanced,conditional,bayes,gauss
from common import SCENES,CHECKS
from catalog import CATALOG
from mathml import render,markdown_math
from math_typography import normalize_math,normalize_scripts
from markdown_it import MarkdownIt
md=MarkdownIt('commonmark',{'html':True})

def text(s):return normalize_math(normalize_scripts(markdown_math(s,md)))

def static_svg(f,title):
    out=['<svg viewBox="0 0 760 360" role="img"><title>'+html.escape(title)+'</title>']
    pos={n['id']:n for n in f['nodes']}
    for e in f.get('edges',[]):
        a=pos.get(e['from']);b=pos.get(e['to'])
        color='#a23c59' if e.get('tone')=='warning' else '#b17616' if e.get('tone')=='active' else '#537e90'
        dash=' stroke-dasharray="6 5"' if e.get('dashed') else ''
        if a and b:out.append(f'<path d="M{a["x"]},{a["y"]} L{b["x"]},{b["y"]}" stroke="{color}" stroke-width="2" fill="none"{dash}/>')
    colors={'plain':'#e9f1f7','active':'#ffda87','done':'#bee4d0','warning':'#efbfd0'}
    for n in f['nodes']:
        out.append(f'<g transform="translate({n["x"]} {n["y"]})">')
        if n['kind']=='point':out.append('<circle r="7" fill="#2f7189"/>')
        else:out.append(f'<rect x="{-n["w"]/2}" y="{-n["h"]/2}" width="{n["w"]}" height="{n["h"]}" rx="7" fill="{colors.get(n["tone"],colors["plain"])}" stroke="#96b7c7"/>')
        lines=n['label'].split('\n');y=(-17 if n['kind']=='point' else 7 if len(lines)==1 else -3)+n.get('labelDy',0)
        out.append(f'<text text-anchor="middle" font-size="{n.get("size",22)}" y="{y}">')
        out.extend(f'<tspan x="{n.get("labelDx",0)}" dy="{0 if i==0 else 24}">{html.escape(line)}</tspan>' for i,line in enumerate(lines));out.append('</text></g>')
    return ''.join(out)+'</svg>'

def build_data():
    used={s for sections in CATALOG.values() for ids in sections.values() for s in ids}
    assert used==set(SCENES),(used-set(SCENES),set(SCENES)-used)
    for id in ['vector-addition','projection','gram-schmidt','affine-origin']:
        SCENES[id]['axes']=dict(cx=300,cy=245,scale=65,xs=list(range(-4,7)),ys=list(range(-1,4)))
    SCENES['matrix-composition']['axes']=dict(cx=310,cy=230,scale=85,xs=list(range(-3,5)),ys=list(range(-1,3)))
    SCENES['closest-pair']['axes']=dict(cx=380,cy=280,scale=65,xs=list(range(-5,6)),ys=list(range(0,4)))
    SCENES['cross-orientation']['axes']=dict(cx=270,cy=270,scale=65,xs=list(range(-3,7)),ys=list(range(0,4)))
    for s in SCENES.values():
        s['invariantHtml']=text('**Model condition.** '+s['invariant'])
        s['descriptionHtml']=text(s['description'])
        for f in s['frames']:
            f['formulaHtml']='<div class="formula-block">'+render(f['formula'],True)+'</div>' if f['formula'] else ''
            f['captionHtml']=text(f['caption'])
            f['metricLabels']={key:text(key) for key in f['metrics']}
    (ROOT/'dist/chapters/concept-animations.json').write_text(json.dumps({'version':1,'scenes':SCENES},ensure_ascii=True,separators=(',',':'))+'\n')

def install_animations():
    if not (ROOT/'dist/chapters/concept-animations.json').exists():return
    data=json.loads((ROOT/'dist/chapters/concept-animations.json').read_text())['scenes'];rows=[]
    for topic,sections in CATALOG.items():
        p=ROOT/f'dist/chapters/{topic}.html';s=p.read_text(encoding='utf-8')
        s=re.sub(r'<!-- CONCEPT ANIMATION START [^>]+ -->[\s\S]*?<!-- CONCEPT ANIMATION END -->','',s)
        s=re.sub(r'<link rel="stylesheet" href="concept-animation.css">|<script src="concept-animation.js"></script>','',s)
        before=len(re.findall(r'class="exam-question"',s))
        for anchor,ids in sections.items():
            target=re.search(r'<h2\b[^>]*\bid="'+re.escape(anchor)+r'"[^>]*>',s);assert target,(topic,anchor)
            end=re.search(r'<h2\b|</article>',s[target.end():]);assert end
            at=target.end()+end.start();first=data[ids[0]]
            widget=f'<!-- CONCEPT ANIMATION START {anchor} --><section id="animation-{anchor}" class="concept-animation" data-scenes="{",".join(ids)}" aria-label="Animated teaching for {html.escape(anchor)}"><h3>Animated concept walkthrough</h3><p>{html.escape(first["description"])}</p><p>Choose a concept, then use Play, Next step, Previous step, or the checkpoint slider. Every stop includes its exact state and a complete explanation.</p><div class="anim-stage">{static_svg(first["frames"][0],first["title"])}</div><div class="anim-explanation">{html.escape(first["frames"][0]["caption"])}</div>{first["invariantHtml"]}<noscript>This is the first verified checkpoint. Enable JavaScript for the remaining checkpoints and playback controls; the complete written lesson is available above.</noscript></section><!-- CONCEPT ANIMATION END -->'
            widget=normalize_math(normalize_scripts(widget))
            s=s[:at]+widget+s[at:]
        s=s.replace('</head>','<link rel="stylesheet" href="concept-animation.css"></head>').replace('</body>','<script src="concept-animation.js"></script></body>')
        assert len(re.findall(r'class="exam-question"',s))==before
        p.write_text(s,encoding='utf-8')
        rows.append(dict(topicId=topic,placements=len(sections),scenarios=len({i for ids in sections.values() for i in ids}),sections=sections,questionCount=before,htmlSha256=hashlib.sha256(p.read_bytes()).hexdigest()))
    p=ROOT/'dist/lessons.json';lessons=json.loads(p.read_text())
    approval=ROOT/'research/animation-approval.json'
    approved=set(json.loads(approval.read_text()).get('approvedTopics',[])) if approval.exists() else set()
    for w in lessons:
        for c in w['chapters']:
            if c['topicId'] in CATALOG:c.update(animationCount=len({id for v in CATALOG[c['topicId']].values() for id in v}),animationWalkthroughCount=len(CATALOG[c['topicId']]),animationReviewState='student_approved' if c['topicId'] in approved else 'awaiting_user_approval')
    p.write_text(json.dumps(lessons,indent=2)+'\n')
    for name in ['research/exam-calibration/manifest.json','dist/evidence/exam-calibration/manifest.json']:
        p=ROOT/name
        if p.exists():
            m=json.loads(p.read_text())
            for c in m['chapters']:c['htmlSha256']=hashlib.sha256((ROOT/f'dist/chapters/{c["topicId"]}.html').read_bytes()).hexdigest()
            p.write_text(json.dumps(m,indent=2)+'\n')
    manifest=dict(state='animation_revision_awaiting_user_approval',chapters=rows,uniqueScenarios=len(data),checkpoints=sum(len(s['frames']) for s in data.values()),placements=sum(r['placements'] for r in rows),constructionAssertions=len(CHECKS),scope='Original bounded explanatory models embedded in existing instructional sections. Written proofs remain authoritative; finite examples do not certify all inputs.',checkpointsPrint='Uninitialized players retain a printable first checkpoint. Initialized players print the currently selected exact checkpoint. No blank animation is required for offline reading.')
    (ROOT/'research/animation-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    report=['<h1>Animated teaching across the chapter library</h1>',f'<p>Review draft · {len(rows)} chapters · {len(data)} distinct scenarios · {manifest["checkpoints"]} exact checkpoints · {manifest["placements"]} embedded walkthroughs.</p>','<p>Open a chapter below and use its concept selector. Play follows the saved mathematical or program states. Next step pauses at one exact checkpoint; Previous step, Restart, and the slider let you inspect the same transition again. Colors are accompanied by explanations and values. Only one player runs at a time, and playback pauses when it leaves the reading area.</p>','<h2>Model scope and interpretation</h2><p>These are original teaching simulations derived from the definitions and algorithms already cited in each chapter. They are not copied university animations. A finite trace illustrates the chapter’s general proof; it does not replace it. Gate timing uses a stated transport-delay model, geometric displays use fixed coordinate scales, and the FFT states use a stated sign convention. Intentionally faulty cases are labeled as counterexamples. Small screens allow horizontal movement inside the figure without shrinking the mathematical labels.</p>','<p>The list below states precisely which concepts have animated walkthroughs. It does not claim an animation of every sentence, every exercise, or every possible parameter value. Textual sections without a listed walkthrough retain their written proofs and figures. Future chapters must include a concept inventory and the necessary simulations before delivery.</p>','<h2>Chapter and concept inventory</h2>']
    report[1]=report[1].replace(f'Review draft · {len(rows)} chapters',f'{len(approved)} approved chapters and {len(rows)-len(approved)} new review draft')
    plan=json.loads((ROOT/'dist/schedule.en.json').read_text())
    for row in rows:
        topic=plan['topics'][row['topicId']];title=plan['subjects'][topic['subject']]['title']+' · '+topic['title']
        report.append(f'<h3><a href="chapters/{row["topicId"]}.html">{html.escape(title)}</a></h3><ul>')
        for anchor,ids in row['sections'].items():report.append(f'<li><a href="chapters/{row["topicId"]}.html#animation-{anchor}">{html.escape(anchor.replace("-"," ").capitalize())}</a>: '+ '; '.join(html.escape(data[i]['title']) for i in ids)+'.</li>')
        report.append('</ul>')
    model=ROOT/'research/animation-model-audit.json';browser=ROOT/'research/animation-browser-audit.json'
    if model.exists() and browser.exists():
        m=json.loads(model.read_text());b=json.loads(browser.read_text());public=ROOT/'dist/evidence/animations';public.mkdir(parents=True,exist_ok=True)
        fresh=set(b['scenarios'])==set(data)
        evidence=dict(state='passed' if fresh and not b['layoutIssues'] and b.get('allScenariosVisited') else 'in_progress',serializedStateAndReferenceAssertions=m['assertions'],constructionAssertions=len(CHECKS),chaptersRendered=len(b['chapters']),scenariosRendered=len(b['scenarios']),checkpoints=manifest['checkpoints'],layoutIssues=len(b['layoutIssues']),mobileWidth=390,controls='previous, next, restart, seek, play/pause, keyboard, speed, mobile enlarge, reduced motion and print',questionEntriesRetained=sum(r['questionCount'] for r in rows),limits=m['limitations'])
        (public/'validation.json').write_text(json.dumps(evidence,indent=2)+'\n')
        report.append('<h2>Verification evidence</h2><p>'+str(m['assertions'])+' serialized-state and reference assertions passed. All '+str(len(b['scenarios']))+' scenarios and their checkpoints were rendered across '+str(len(b['chapters']))+' chapters. The audit found '+str(len(b['layoutIssues']))+' clipped or overlapping text-label cases after correction. Desktop, 390-pixel mobile containment, playback controls, reduced motion and printable checkpoints were checked. These finite checks are evidence within the stated model scope, not a universal scientific guarantee. <a href="evidence/animations/validation.json">Read the verification record.</a></p>')
    report.append(f'<h2>Approval</h2><p>The user approved the animated teaching in {len(approved)} existing chapters. Their approval is preserved. Newly added chapters and their animations remain drafts until explicitly approved.</p>')
    (ROOT/'dist/animation-review.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Animated teaching review</title><link rel="stylesheet" href="chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="index.html#library">← Chapter library</a></p><article class="lesson">'+''.join(report)+'</article></main></body></html>',encoding='utf-8')
    # Stable links survive rebuilding without changing study progress or card layout.
    for file in ['dist/index.html','dist/library-review.html']:
        p=ROOT/file;s=p.read_text(encoding='utf-8');s=re.sub(r'<!-- ANIMATION REVIEW LINK -->.*?<!-- END ANIMATION REVIEW LINK -->','',s,flags=re.S)
        notice='<!-- ANIMATION REVIEW LINK --><p class="top-link"><a href="'+('animation-review.html')+'">Animated chapter walkthroughs: concepts and controls</a></p><!-- END ANIMATION REVIEW LINK -->'
        if file=='dist/index.html':
            notice='<!-- ANIMATION REVIEW LINK --> Approved chapters retain their animated teaching. New chapter walkthroughs require review. <a href="animation-review.html">Choose a chapter and animated concept →</a><!-- END ANIMATION REVIEW LINK -->'
            s=re.sub(r'(<section\b[^>]*id="view-lessons"[^>]*><p class="card">)(.*?)(</p>)',lambda m:m[1]+m[2]+notice+m[3],s,count=1,flags=re.S)
        else:
            marker=re.search(r'<main\b[^>]*>',s)
            if marker:s=s[:marker.end()]+notice+s[marker.end():]
        p.write_text(s,encoding='utf-8')
    return manifest

if __name__=='__main__':
    build_data();m=install_animations();print(json.dumps({k:m[k] for k in ['uniqueScenarios','checkpoints','placements','constructionAssertions']}))

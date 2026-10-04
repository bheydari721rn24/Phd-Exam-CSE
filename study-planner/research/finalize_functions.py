"""Record the independently verified sole chapter draft and approval boundary."""
import json, shutil
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent
v = json.loads((BASE / 'p_functions-validation.json').read_text())
b = json.loads((BASE / 'p_functions-browser-review.json').read_text())
a = json.loads((BASE / 'animation-browser-audit.json').read_text())
assert v['state'] == b['state'] == 'passed'
assert len(a['chapters']) == 28 and len(a['scenarios']) == 160 and not a['layoutIssues']
assert v['approvedQuestionsPreserved'] == 1407

from preserve_library_approval import preserve_approval
preserve_approval()
models = json.loads((ROOT / 'dist/chapters/concept-animations.json').read_text())['scenes']
assert len(models) == 160
assert sum(len(s['frames']) for s in models.values()) == 974

gate = json.loads((BASE / 'chapter-gate.json').read_text())
gate.update(
    state='awaiting_user_approval', currentTopicId='p_functions', nextTopicId=None,
    proposedNextTopicId='p_arrays', approvedTopicId='l_rank',
    activeWork='Functions, Variable Scope, and Parameter Passing is delivered as a review draft. Await explicit approval before writing the next chapter.',
    lastCompletedReview='p_functions: six genuinely reviewed written university courses, 91 fully solved problems (89 original/course-inspired and two authentic bridge revisits), 80 complete examination rules, seven figures, twelve exact animations/58 checkpoints and a five-model adjustable lab. Independent verification and desktop/mobile/print/motion audits passed. All 27 approved chapters and 1,407 earlier question entries are preserved.',
    nextReview='After explicit approval, follow Week 2 order to p_arrays. Do not author it while awaiting approval.')
(BASE / 'chapter-gate.json').write_text(json.dumps(gate, indent=2) + '\n')

pub = ROOT / 'dist/evidence/p_functions'
pub.mkdir(parents=True, exist_ok=True)
for path in Path(b['screenshots']).glob('p_functions-*.png'):
    shutil.copy2(path, pub / path.name)
record = dict(b)
record['screenshots'] = 'Created chapter screenshots saved beside this file.'
(pub / 'browser.json').write_text(json.dumps(record, indent=2) + '\n')

quality = BASE / 'p_functions-quality-audit.md'
observed = """
## Final observed verification

Independent verification passed 5,587 checks, including 21 actual Python executions and preservation of all 1,407 earlier approved question entries. The new draft contains 91 worked tasks, 80 rules and seven original figures. All twelve new animation models and their 58 checkpoints passed exact-state checks. The five-model laboratory passed all 205 accepted inputs and eight invalid-input cases, including exact transitions, controls and actual token motion.

Browser review passed desktop, 390-pixel mobile and print checks: all seven figures have no clipped or overlapping labels, all 91 solutions open for printing, mathematical and code fonts are loaded, and there is no page-width overflow or link underline. The final full animation review rendered 160 models across 28 chapters with no reported label-layout issues. Review evidence and screenshots are available in the public chapter evidence folder. These observed finite checks complement the chapter's arguments; they do not constitute a guarantee for every possible input or unseen examination question.
"""
text = quality.read_text(encoding='utf-8')
if '## Final observed verification' not in text:
    quality.write_text(text + observed, encoding='utf-8')

from markdown_it import MarkdownIt
audit = MarkdownIt('commonmark').render(quality.read_text(encoding='utf-8'))
(ROOT / 'dist/reviews/p_functions-quality.html').write_text(
    '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Functions chapter audit</title><link rel="stylesheet" href="../chapters/chapter.en.css"></head><body><main class="chapter"><p class="top-link"><a href="../chapters/p_functions.html">← Functions chapter</a></p><article class="lesson">' + audit + '</article></main></body></html>', encoding='utf-8')

handoff = """
## Current authoritative handoff — functions, scope and parameter passing

4 October 2026: The user explicitly approved l_rank in Site version 62 and authorized one next chapter. All 27 earlier chapters and their animations are approved. Earlier pending statements above are historical and superseded by this entry.

The sole new draft is p_functions, Week 2 Programming Fundamentals: Functions, Variable Scope, and Parameter Passing, at dist/chapters/p_functions.html. Four primary written courses from Cambridge, UC Berkeley, Harvard and CMU are synthesized with Stanford and MIT as two additional genuinely reviewed comparisons. Exact reading ranges, bounded discovery/selection criteria, language differences, source corrections and prompt inventory are recorded in research/p_functions-source-audit.md, research/p_functions-reviewed-courses.json and dist/evidence/p_functions/sources.json. No worldwide exhaustive-course claim is made.

The chapter contains detailed English instruction, 91 fully explained mathematical/conceptual problems, 80 complete summary/examination rules, seven SVG figures, twelve exact animations with 58 checkpoints and an adjustable five-model laboratory. Its two authentic archive items are explicit bridge revisits of MSc CS 1393 Q167 and PhD CE 1405 Q9; they are not claimed as new unique examination items or functions-specific archive questions. The library now contains 28 authored chapters, 1,498 question entries, 160 animated models and 974 checkpoints.

Independent verification passed 5,587 checks and 21 actual Python executions. All 1,407 earlier approved question entries were preserved. Browser review passed all seven figure layouts, all 91 printable solutions, dedicated prose/heading/math/code fonts, 390-pixel mobile containment, 205 valid laboratory input cases, eight invalid-input cases, controls, enlargement and actual motion. The final library animation review passed 160 scenarios across 28 chapters with zero label-layout findings. No local C/C++ compiler is available: C/C++ cases have explicit language-rule reasoning and independent finite models, not a compiled-execution claim. Finite checks do not guarantee unseen-question performance.

The gate is awaiting_user_approval, with proposed next topic p_arrays. p_functions remains a draft until explicit approval. Do not begin another chapter or quiz the user before they study.

Rebuild this chapter with research/author_functions_problems.py, research/functions_sources_record.py and research/build_functions_chapter.py. Verify with research/verify_p_functions_en.py, research/qa_functions_browser.py, research/verify_concept_animations.py, research/qa_animations_browser.py when model data change, and research/check_site_en.py. Preserve study-progress data, all approved content and private cached original PDFs. Publish exact pushed source to the existing owner-private Site and mirror only changed paths to GitHub branch study-planner-1406, preserving unrelated mirror changes.
"""
delivery = ROOT / 'WEEKLY_DELIVERY.md'
if '## Current authoritative handoff — functions, scope and parameter passing' not in delivery.read_text(encoding='utf-8'):
    with delivery.open('a', encoding='utf-8') as f:
        f.write(handoff)
print('Functions draft delivered; approval gate closed; 27 previous approvals preserved.')

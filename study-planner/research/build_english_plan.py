"""Build the English reading plan without altering the Persian archival input."""

from __future__ import annotations

import json
from pathlib import Path


DIST = Path(__file__).resolve().parents[1] / "dist"
LEGACY = Path(__file__).resolve().parent / "legacy-inputs"
raw = json.loads((LEGACY / "schedule.json").read_text(encoding="utf-8"))

TITLES = dict(
    line.split("|", 1)
    for line in """
d_logic|Propositions, predicates, and logical equivalence
d_sets|Sets and set operations
d_proof|Direct proof, contradiction, and counterexamples
d_induction|Ordinary and strong induction
d_relations|Relations, equivalence, and partial orders
d_functions|Functions, inverses, injectivity, and surjectivity
d_invariants|Invariants and recursive reasoning
d_number|Divisibility, modular arithmetic, and number theory
d_counting|Permutations, combinations, and counting
d_inclusion|Inclusion–exclusion
d_pigeonhole|The pigeonhole principle and applications
d_recurrence|Recurrences and introductory solution methods
d_generating|Generating functions and advanced counting
d_graph|Graphs, paths, connectivity, and degree
d_trees|Trees, spanning trees, and structural properties
d_dprob|Discrete probability and counting
p_rep|Representation of numbers, characters, and data
p_types|Data types, conversions, and operators
p_flow|Conditionals, loops, and execution order
p_functions|Functions, variable scope, and parameter passing
p_arrays|Arrays and indexing
p_strings|Strings and terminators
p_recursion|Recursive functions and the call stack
p_pointers|Pointers, aliasing, and address arithmetic
p_memory|Dynamic memory and object lifetime
p_structs|Structures, records, and data layout
p_bitwise|Bitwise operators and masks
p_trace|Code tracing, boundary errors, and undefined behavior
a_model|Computation model and input size
a_asym|Asymptotic notation and growth comparison
a_loop|Loop analysis and operation counting
a_recurrence|Algorithmic recurrences and solution theorems
a_divide|Divide and conquer: design and analysis
a_arrays|Arrays, linked lists, and operation costs
a_stackqueue|Stacks, queues, and applications
a_sort|Comparison and non-comparison sorting
a_select|Searching, selection, and order statistics
a_bst|Binary search trees and traversal
a_balanced|Balanced trees and height analysis
a_heap|Heaps and priority queues
a_hash|Hash tables, collisions, and expected analysis
a_amortized|Amortized analysis and dynamic resizing
a_graphrep|Graph representations and traversal costs
a_bfsdfs|Breadth-first and depth-first search
a_topological|Topological order and components
a_mst|Minimum spanning trees
a_shortest|Shortest paths and algorithm preconditions
a_greedy|Greedy design and correctness proofs
a_dp|Dynamic programming and state design
a_flow|Network flow and minimum cuts
a_lower|Lower bounds and hard problems
a_random|Randomized algorithms and expected analysis
a_string|Basic string-matching algorithms
a_correct|Invariants, correctness certificates, and method comparison
s_axioms|Sample spaces, events, and probability axioms
s_counting|Counting probabilities and independence
s_conditional|Conditional probability and total probability
s_bayes|Bayes' rule and base rates
s_descriptive|Data summaries and descriptive statistics
s_discrete|Discrete random variables and common distributions
s_expectation|Expectation and its linearity
s_variance|Variance, covariance, and correlation
s_distributions|Binomial, geometric, and Poisson distributions
s_continuous|Continuous variables, densities, and distributions
s_joint|Joint and marginal distributions
s_condexp|Conditional expectation and variable independence
s_transform|Transformations of random variables
s_llnclt|Law of large numbers and central limit theorem
s_sampling|Sampling and sampling distributions
s_estimation|Point estimation and confidence intervals
s_hypothesis|Hypothesis testing, errors, and p-values
s_regression|Introductory regression and correlation
s_markov|Introductory Markov chains
l_vectors|Vectors, inner products, and linear geometry
l_matrices|Matrices and matrix operations
l_gauss|Gaussian elimination and linear systems
l_rank|Rank, invertibility, and solution sets
l_det|Determinants and their properties
l_spaces|Vector spaces, subspaces, bases, and dimension
l_linear|Linear maps, kernels, and images
l_orthogonality|Orthogonality and orthogonal decompositions
l_projection|Orthogonal projections and projection matrices
l_leastsquares|Least squares and applications
l_eigen|Eigenvalues and eigenvectors
l_diagonal|Diagonalization and symmetric matrices
l_svd|Singular value decomposition: core connections
g_number|Number bases and binary encoding
g_boolean|Boolean algebra and truth tables
g_gates|Logic gates and function implementation
g_kmap|Minterms, maxterms, and simplification
g_combin|Combinational circuit design
g_arithmetic|Adders, comparators, and arithmetic circuits
g_mux|Multiplexers, encoders, and decoders
g_latch|Latches and sequential-circuit foundations
g_ff|Flip-flops and excitation tables
g_register|Registers and data transfer
g_counter|Counters and state sequences
g_fsm|Finite-state machines and design
g_timing|Timing, delay, and critical paths
g_hazards|Logic hazards and transient behavior
g_memory|Memory and programmable logic fundamentals
i_agents|Agents, environments, and problem definition
i_uninformed|Uninformed search and its measures
i_informed|Informed search and heuristics
i_optimality|Completeness, optimality, and heuristic consistency
i_games|Adversarial search and pruning
i_csp|Constraint-satisfaction problems and propagation
i_prop|Knowledge representation with propositional logic
i_fol|First-order logic and unification
i_inference|Inference and proof strategies
i_planning|Classical planning and state spaces
i_bayes|Probabilistic inference and Bayes' rule
i_bn|Bayesian networks and conditional independence
i_decision|Decision-making under uncertainty
i_learning|Supervised learning and generalization
i_classification|Classification and model evaluation
i_clustering|Introductory clustering
i_neural|Introductory neural networks
i_eval|Overfitting, metrics, and evaluation errors
""".strip().splitlines()
)

assert set(TITLES) == set(raw["topics"]), (set(TITLES) ^ set(raw["topics"]))

SUBJECTS = {
    "discrete": "Discrete Mathematics",
    "algorithms": "Data Structures and Algorithms",
    "probability": "Probability and Statistics",
    "linear": "Linear Algebra",
    "programming": "Programming Fundamentals",
    "logic": "Digital Logic",
    "ai": "Artificial Intelligence",
}

WEEK_LABELS = [
    ("Common foundations", "Establish the definitions and worked examples that later chapters assume."),
    ("Relations and recursion", "Connect relations and functions to recursion, conditional probability, and linear systems."),
    ("Counting and structures", "Develop counting methods, linear data structures, and the first AI search models."),
    ("Trees and heuristics", "Compare trees, heaps, and hashing while studying informed search and linear maps."),
    ("Graphs and constraints", "Study graph traversal alongside continuous probability, least squares, games, and constraints."),
    ("Paths and inference", "Connect shortest paths, spanning trees, conditional expectation, and knowledge representation."),
    ("Design and estimation", "Develop dynamic programming, network flow, statistical sampling, and AI planning."),
    ("Uncertainty", "Use probability and statistical estimation to study Bayesian networks and decisions."),
    ("Learning", "Connect introductory machine learning to regression, probability, and linear algebra."),
    ("Integration", "Bring together AI model evaluation and the core reasoning methods of the other subjects."),
    ("First-pass consolidation", "Resolve unclear definitions through worked examples and record topics needing another pass."),
]

STARTS = [
    "2026-10-03", "2026-10-10", "2026-10-17", "2026-10-24", "2026-10-31",
    "2026-11-07", "2026-11-14", "2026-11-21", "2026-11-28", "2026-12-05",
    "2026-12-12",
]

from datetime import date, timedelta

weeks = []
for index, old in enumerate(raw["weeks"]):
    start = date.fromisoformat(STARTS[index])
    end = start + timedelta(days=6)
    units = []
    for item in old["units"]:
        units.append({
            "subject": item["subject"],
            "hours": item["hours"],
            "topicIds": item["topicIds"],
        })
    weeks.append({
        "number": old["number"],
        "dateLabel": f"{start:%b %d}–{end:%b %d, %Y}",
        "shortLabel": WEEK_LABELS[index][0],
        "focus": WEEK_LABELS[index][1],
        "totalHours": old["totalHours"],
        "units": units,
    })

english = {
    "updatedLabel": "English edition · chapter quality review in progress",
    "method": "The first pass assigns 56 study hours per week across seven priority subjects, including four hours of English reading. This is a study schedule, not a production deadline for chapter notes. Past entrance-exam booklets are reserved for the final month.",
    "strategy": {
        "core": "First priority: discrete mathematics, programming fundamentals, data structures and algorithms, probability and statistics, linear algebra, digital logic, and artificial intelligence.",
        "support": "Programming and digital logic keep their own study hours. English reading runs in parallel.",
        "deferred": "Operating Systems and Computer Architecture are second priority; their scope will be chosen after the first pass from actual progress and remaining time.",
        "excluded": "Theory of Languages and Automata is excluded at the student's request.",
        "english": "Four of the 56 weekly hours are reserved for careful reading of technical English.",
        "reviewGate": "Revise study order when actual chapter progress shows a concrete need. Do not use entrance-exam booklets before the final month.",
    },
    "subjects": {key: {"title": value} for key, value in SUBJECTS.items()},
    "topics": {
        key: {"title": TITLES[key], "subject": value["subject"]}
        for key, value in raw["topics"].items()
    },
    "weeks": weeks,
    "sources": [
        source for source in raw["sources"]
        if "Exams/" not in source["url"]
        and "konkur" not in source["url"].lower()
        and "Past Exam" not in source["label"]
    ],
}

(DIST / "schedule.en.json").write_text(
    json.dumps(english, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

daily_original = json.loads((LEGACY / "week1-daily.json").read_text(encoding="utf-8"))
DAY_TASKS = [
    [
        "Read the definitions of propositions, truth tables, equivalence, and quantifiers; follow the worked derivations.",
        "Trace data types, value representations, and conversions in short instructional programs.",
        "Work through base conversion and signed-integer representation step by step.",
        "Read a short technical passage related to today's subjects and record each new term in context.",
    ],
    [
        "Review the advanced logic examples and distinguish equivalence from entailment.",
        "Read the definitions of sets, subsets, and basic set operations.",
        "Identify the input size, computation model, and primitive-operation cost in worked examples.",
        "Study sample spaces, events, and probability axioms through worked examples.",
        "Read one technical paragraph and note the exact meaning of its subject-specific terms.",
    ],
    [
        "Study complete examples of direct proof, contradiction, and contraposition.",
        "Compare formal asymptotic bounds and function growth using worked examples.",
        "Follow more involved examples of event union, intersection, and complement.",
        "Build vector operations and linear combinations from definitions and geometric examples.",
    ],
    [
        "Compare ordinary and strong induction, including the base case and induction hypothesis.",
        "Count iterations of simple and nested loops step by step.",
        "Review linear dependence and span through geometric and algebraic examples.",
        "Read a technical passage on induction or vectors sentence by sentence.",
    ],
    [
        "Analyze dependent and piecewise loops by exact iteration counts.",
        "Study addition and multiplication rules, permutations, and combinations with their preconditions.",
        "Work through matrix operations and the geometric meaning of matrix-vector multiplication.",
        "Read a technical paragraph on counting or matrices and paraphrase its main claim.",
    ],
    [
        "Connect exact loop counts to asymptotic bounds; review complete worked examples.",
        "Study restricted counting using complements and disjoint cases.",
        "Examine matrix multiplication, transposes, and invertibility in worked examples.",
        "Trace the path through conditionals in short programs.",
    ],
    [
        "Review multi-step counting examples from assumptions to complete solutions.",
        "Consolidate matrix multiplication and linear-transform interpretations.",
        "Trace loops and conditionals step by step in instructional programs.",
        "Derive basic Boolean laws from truth tables.",
        "Study basic gates and construct the truth table of a simple circuit.",
    ],
]

assert len(DAY_TASKS) == len(daily_original["days"])
day_names = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
daily = {
    "week": 1,
    "startDate": "2026-10-03",
    "endDate": "2026-10-09",
    "dailyHours": 8,
    "guidance": "Hours are net study time; take breaks separately. Read the lesson and its worked examples before attempting independent practice. Entrance-exam booklets are reserved for the final month. A chapter marked draft is not a finished lesson.",
    "days": [],
}
for index, original_day in enumerate(daily_original["days"]):
    assert len(DAY_TASKS[index]) == len(original_day["blocks"])
    day_date = date.fromisoformat("2026-10-03") + timedelta(days=index)
    blocks = []
    for old_block, task in zip(original_day["blocks"], DAY_TASKS[index]):
        block = {
            "hours": old_block["hours"],
            "task": task,
        }
        block["topicId" if "topicId" in old_block else "subject"] = old_block.get(
            "topicId", old_block.get("subject")
        )
        blocks.append(block)
    daily["days"].append({
        "name": day_names[index],
        "date": f"{day_date:%b %d}",
        "blocks": blocks,
    })
(DIST / "week1-daily.en.json").write_text(
    json.dumps(daily, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

course_register = json.loads((LEGACY / "course-audit-week1.json").read_text(encoding="utf-8"))
course_register["method"] = (
    "A course entry records a checked course page and topic match. It does not "
    "imply that every lecture or exercise was read. Chapter-level audits state "
    "which texts were actually studied and synthesized."
)
course_register["courses"].extend([
    {
        "id": "mit-6042j-2010-logic", "subject": "discrete", "university": "MIT",
        "course": "6.042J Mathematics for Computer Science — Leighton and van Dijk (2010)",
        "url": "https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/",
        "evidence": "https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/7853d585044ef21bce5f48ce5fc89d28_MIT6_042JF10_chap01.pdf",
        "topics": ["d_logic"], "advantage": "Foundational truth conditions and quantifier examples.",
        "limit": "Only Chapter 1 is counted for this chapter; one informal sentence has a connective typo.",
        "access": "chapter_pdf", "reviewLevel": "all_relevant_text_reviewed"
    },
    {
        "id": "stanford-cs103-2014-logic", "subject": "discrete", "university": "Stanford",
        "course": "CS103 Mathematical Foundations of Computing — Luca Trevisan (2014)",
        "url": "https://cs.stanford.edu/people/trevisan/cs103-14/",
        "evidence": "https://cs.stanford.edu/people/trevisan/cs103-14/lecture09.pdf",
        "topics": ["d_logic"], "advantage": "Exact syntax, equivalence, and free-variable scope examples.",
        "limit": "Informal use of 'sentence' is made precise in the chapter.",
        "access": "lecture_pdf", "reviewLevel": "all_relevant_text_reviewed"
    },
    {
        "id": "berkeley-cs70-2024-logic", "subject": "discrete", "university": "UC Berkeley",
        "course": "CS70 Discrete Mathematics and Probability Theory — Shahzar and Hongxun Wu (2024)",
        "url": "https://su24.eecs70.org/",
        "evidence": "https://su24.eecs70.org/assets/pdf/notes/n1.pdf",
        "topics": ["d_logic"], "advantage": "First-order examples and restricted quantification in a single note.",
        "limit": "Several informal explanations require formal cross-checking.",
        "access": "note_pdf", "reviewLevel": "all_relevant_text_reviewed"
    },
    {
        "id": "cmu-15311-2026-logic", "subject": "discrete", "university": "Carnegie Mellon",
        "course": "15-311 Logic and Mechanized Reasoning — Marijn J. H. Heule (2026)",
        "url": "https://www.cs.cmu.edu/~mheule/15311-s26/schedule.html",
        "evidence": "https://www.cs.cmu.edu/~mheule/15311-s26/slides/FOL.pdf",
        "topics": ["d_logic"], "advantage": "Detailed formal semantics, substitution, and infinite models.",
        "limit": "Animated slide frames and deliberately false prompts require the full decks.",
        "access": "slide_pdfs", "reviewLevel": "all_relevant_text_reviewed"
    },
    {
        "id": "cornell-cs2800-2017-logic", "subject": "discrete", "university": "Cornell",
        "course": "CS2800 Discrete Structures — Lecture 36 (2017)",
        "url": "https://www.cs.cornell.edu/courses/cs2800/2017fa/",
        "evidence": "https://www.cs.cornell.edu/courses/cs2800/2017fa/lectures/lec36-logic.html",
        "topics": ["d_logic"], "advantage": "Inductive semantics and the object-language/metalanguage distinction.",
        "limit": "The inspected lecture is supplementary; full course logic sequence was not reviewed.",
        "access": "lecture_text", "reviewLevel": "one_lecture_inspected"
    },
    {
        "id": "princeton-cos341-2002-logic", "subject": "discrete", "university": "Princeton",
        "course": "COS 341 Discrete Mathematics — Moses Charikar (2002)",
        "url": "https://www.cs.princeton.edu/courses/archive/fall02/cs341/",
        "evidence": "https://www.cs.princeton.edu/courses/archive/fall02/cs341/lec2.pdf",
        "topics": ["d_logic"], "advantage": "A freely accessible slide deck on propositional logic and quantifiers.",
        "limit": "Lecture 2 was screened; the complete relevant course sequence was not reviewed.",
        "access": "lecture_pdf", "reviewLevel": "one_lecture_screened"
    },
    {
        "id": "illinois-cs173-2024-logic", "subject": "discrete", "university": "Illinois",
        "course": "CS173 Discrete Structures — Logic 1 (Fall 2024)",
        "url": "https://courses.grainger.illinois.edu/cs173/fa2024/ALL-lectures/lectures.html",
        "evidence": "https://courses.grainger.illinois.edu/CS173/fa2024/ALL-lectures/Lectures/logic1.html",
        "topics": ["d_logic"], "advantage": "Accessible written lecture treatment of foundational logic.",
        "limit": "The complete multi-lecture logic sequence was not reviewed.",
        "access": "lecture_text", "reviewLevel": "one_lecture_screened"
    },
    {
        "id": "oxford-logic-proof-2023", "subject": "discrete", "university": "Oxford",
        "course": "Logic and Proof (2022–2023)",
        "url": "https://www.cs.ox.ac.uk/teaching/courses/2022-2023/logicandproof/",
        "evidence": "https://www.cs.ox.ac.uk/teaching/courses/2022-2023/logicandproof/",
        "topics": ["d_logic"], "advantage": "Broad syllabus covering syntax, SAT, normal forms, and first-order structures.",
        "limit": "The public syllabus is not a verified complete lecture text and does not count toward synthesis.",
        "access": "syllabus", "reviewLevel": "syllabus_only"
    },
    {
        "id": "eth-discrete-2026", "subject": "discrete", "university": "ETH Zurich",
        "course": "Discrete Mathematics (2026)",
        "url": "https://www.vvz.ethz.ch/Vorlesungsverzeichnis/lerneinheit.view?ansicht=KATALOGDATEN&lang=en&lerneinheitId=204115&semkez=2026W",
        "evidence": "https://www.vvz.ethz.ch/Vorlesungsverzeichnis/lerneinheit.view?ansicht=KATALOGDATEN&lang=en&lerneinheitId=204115&semkez=2026W",
        "topics": ["d_logic"], "advantage": "A possible additional course for future comparison.",
        "limit": "Only the catalogue and a separate open book were located; their direct linkage was not established.",
        "access": "catalogue", "reviewLevel": "catalogue_only"
    }
])
(DIST / "course-audit-week1.en.json").write_text(
    json.dumps(course_register, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(f"Built English plan: {len(english['topics'])} topics, {len(weeks)} weeks")

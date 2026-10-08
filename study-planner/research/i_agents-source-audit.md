# Intelligent agents: written-source selection and reading audit

Reviewed 8 October 2026. Selection is chapter-specific and limited to the accessible pool below. It is not a claim to have inspected every university course worldwide. A catalogue or a course title does not count as a reviewed lecture.

## Four core courses from four universities

| University and course | Instructor / author and material actually read | Selection reason |
|---|---|---|
| UC Berkeley, CS 188, Fall 2023 | Igor Mordatch and Peyrin Kao; Note 1 by Nikhil Sharma, PDF pages 1–2, complete text | Concise definitions of rationality and task environments, checked against the more explicit distinctions below. |
| Carnegie Mellon, 15-281, Fall 2023 | Vincent Conitzer and Aditi Raghunathan; Introduction lecture, 51 PDF pages, complete extracted text; Lecture 1 activity solutions, both pages | Agent implementation, performance criteria and constrained state counting. The lecture credits Berkeley; shared provenance is disclosed rather than counted as four independent discoveries. |
| University of Edinburgh, INF2D | 2025-path written Lecture 1, all 37 pages; Lecture 2, all 31 pages of extracted text | Architecture, environment distinctions, problem representation and state-versus-node separation. Current course page lists Wenda Li, Nadin Kokciyan and organiser Craig Innes; the 2025 PDF does not identify an individual lecturer. |
| Stanford, CS221, Summer 2012–2013 | Chris Piech; Markov Decisions written handout, all sections; linked course page verifies instructor and term | Mathematical bridge from deterministic transitions to probability distributions, sequential utility and policy representation. The advanced MDP solution algorithms belong to a later chapter. |

## Compared candidates and supplementary material

1. MIT 6.034, Spring 2005, Leslie Kaelbling and Tomás Lozano-Pérez: Introduction transcript, all five pages. This particular file mostly describes organisation and the online tutor. It is accessible, but has less chapter-specific mathematical content than the selected fourth course; it is not counted as a core agent lecture.
2. Stanford CS221, Spring 2017–2018, Dorsa Sadigh: course catalogue and reading policy screened. Lecture text was not obtained from its calendar; do not substitute this term for Piech's verified handout.
3. Oxford Artificial Intelligence, Hilary 2026, Sara Bernardini: public syllabus screened. This confirms scope, not a reading of protected lectures; excluded from the core count.
4. Michael Wooldridge, *An Introduction to Multiagent Systems*, second-edition Lecture 2, all 71 extracted PDF pages read. Oxford hosts the author's slides, which retain a Liverpool URL. Treat this as supplementary author material, not evidence of a particular Oxford taught course. Formal runs, history dependence, bounded implementability and achievement/maintenance distinctions were compared with the chapter's independent constructions.

## Corrections and qualifications

- Berkeley Note 1, PDF page 2: static is described as not changing as the agent acts. The operational test is change during deliberation without a new agent action. Agent-caused changes are compatible with a static environment.
- Berkeley Note 1, PDF page 1: partial observability does not logically force memory or planning in every task. A common optimal action for all aliased histories permits a rational reflex agent. The chapter proves the finite-action intersection criterion.
- CMU lecture PDF page 42 uses “PEAS” while mixing state-space components with task descriptors. This chapter retains the standard Performance, Environment, Actuators, Sensors expansion and separately defines a search problem.
- CMU elevator activity permits 22 or 21 states depending on a door constraint. Our reconstruction explicitly states legal configurations and counts them; it does not silently choose an interpretation.
- Edinburgh Lecture 1, PDF page 18, contrasts utility with agents having a single goal. Goal-based systems can have conjunctions or multiple goals; utility adds graded preferences and tradeoffs, not merely a second goal.
- Stanford handout calls the Markov assumption “wrong” and presents discrete states / known start as MDP assumptions. These describe its introductory modelling setting. Markov models can be exact with a sufficient state; MDPs also have continuous-state variants and initial distributions. Our chapter states its finite model explicitly.
- Wooldridge's slides use “discrete” with finite percept/action sets. Countably infinite sets can also be discrete. Finiteness and discreteness are separated here.

## Coverage and evidence limits

Web retrieval supplied full extracted text for the cited documents. Local HTTPS downloads failed with a connection-refused error; document byte hashes are therefore not claimed. Some third-party slide pictures were not retrievable as images. No unseen diagram is described as visually checked, and no source diagram is reproduced. All chapter graphics are independently authored exact examples, inspected in the local browser. The original Iranian examination pages used for adaptations are available locally and visually checked separately.

The chapter independently develops definitions, proofs, numeric examples and counterexamples. It does not reproduce complete course problem sets. Course reconstructions are attributed and use changed data or explicit qualifications. The final audit identifies the finite scope and adjacent topics; no guarantee about every unseen examination is made.

## References

- [UC Berkeley CS188, Note 1, Fall 2023](https://inst.eecs.berkeley.edu/~cs188/fa23/assets/notes/cs188-fa23-note01.pdf).
- [UC Berkeley CS188 staff, Fall 2023](https://inst.eecs.berkeley.edu/~cs188/archive/fa23/staff/).
- [CMU 15-281 Introduction, Fall 2023](https://www.cs.cmu.edu/~15281-f23/lectures/15281_Fa23_Lecture_1_Introduction.pdf).
- [CMU Lecture 1 activity solutions](https://www.cs.cmu.edu/~15281-f23/activities/15281_F23_Lecture_1_Activity_Solutions.pdf).
- [Edinburgh INF2D Lecture 1, Intelligent Agents](https://opencourse.inf.ed.ac.uk/sites/default/files/https/opencourse.inf.ed.ac.uk/inf2d/2025/inf2dlectureslides-01intelligentagents_0.pdf).
- [Edinburgh INF2D Lecture 2, Problem Solving](https://opencourse.inf.ed.ac.uk/sites/default/files/https/opencourse.inf.ed.ac.uk/inf2d/2025/inf2dlectureslides-02search_0.pdf).
- [Edinburgh INF2D course team](https://opencourse.inf.ed.ac.uk/inf2d).
- [Stanford CS221, Chris Piech, Markov Decisions](https://stanford.edu/~cpiech/cs221/handouts/markovDecisions.html).
- [Stanford CS221 course and term](https://stanford.edu/~cpiech/cs221/index.html).
- [MIT 6.034 Introduction transcript](https://ocw.mit.edu/courses/6-034-artificial-intelligence-spring-2005/7bb598caab8f1df57f35ddc4016afbb0_ch1_intro.pdf).
- [Oxford AI course catalogue](https://www.cs.ox.ac.uk/teaching/courses/2025-2026/ai/).
- [Michael Wooldridge, Intelligent Agents, second-edition Lecture 2](https://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/imas/distrib/pdf-slides/lect02.pdf).

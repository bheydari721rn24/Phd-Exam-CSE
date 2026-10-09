# Simulation behavior corrections

{
  "status": "verified_locally",
  "baseline": "28fa8a031c78dc1895eb232f5f656d166854b7be",
  "chapters": 47,
  "models": 1040,
  "checkpoints": 7124,
  "liveButtonChapters": 9,
  "movingRecordTransitions": 294,
  "sampledProgress": [
    0,
    0.125,
    0.25,
    0.375,
    0.5,
    0.625,
    0.75,
    0.875,
    1
  ],
  "limitations": "Finite checks of saved and default-computed traces. Moving-body checks cover sorting and selection models. Other chapters have exact-state/layout checks and representative live button checks. This is not a proof for every possible custom input."
}

The earlier static/control-endpoint review missed actual Pause behavior, Before readout mismatch, reverse replay origin, record transit collisions, changing-camera clipping and boundary/cell spacing mismatch. The new audit checks these failures explicitly. Scientific JSON and written bodies are unchanged. Publication is recorded separately.


## Publication transport blocker (2026-10-09)

The verified source was pushed; the GitHub content commit is `e2dc17d` on `study-planner-1406`. The native archive upload repeatedly failed at the OpenAI file service before saving a version. Reconciliation confirms that online version 85 still contains the previous content. The exact 410-file archive is retained unchanged for a later supported retry. A local preview is available at http://127.0.0.1:8766/reviews/simulation-behavior-corrections.html while its process is running. See `research/player-behavior-repair/publication-pending.json`. No new chapter was started.

const byId = id => document.getElementById(id);
const escapeHtml = value => String(value ?? "").replace(/[&<>"']/g, c => ({
  "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
}[c]));
const progressKey = "phd-1406-progress-v2";
let plan, daily, courses, lessons = [], completed = {}, weekNumber = 1, dayNumber = 0;

function weekNow() {
  const tehran = Date.now() + 3.5 * 3600000;
  const days = Math.floor((tehran - Date.UTC(2026, 9, 3)) / 86400000);
  return Math.max(1, Math.min(11, Math.floor(days / 7) + 1));
}
function weekIds(week) { return [...new Set(week.units.flatMap(unit => unit.topicIds))]; }
function completion(ids) {
  const count = ids.filter(id => completed[id]).length;
  return { count, total: ids.length, percent: ids.length ? Math.round(100 * count / ids.length) : 0 };
}
function lessonFor(id) {
  return lessons.flatMap(week => week.chapters || []).find(chapter => chapter.topicId === id);
}
function firstWeek(id) {
  return plan.weeks.find(week => weekIds(week).includes(id))?.number ?? 0;
}
function saveProgress() { localStorage.setItem(progressKey, JSON.stringify(completed)); }
function showView(view, changeHash = true) {
  const valid = ["today", "weeks", "lessons", "resources", "progress"];
  const chosen = valid.includes(view) ? view : "today";
  document.querySelectorAll(".view").forEach(node => { node.hidden = node.id !== "view-" + chosen; });
  document.querySelectorAll(".tabs button").forEach(node => {
    const active = node.dataset.view === chosen;
    node.classList.toggle("active", active);
    node.setAttribute("aria-current", active ? "page" : "false");
  });
  if (changeHash) location.hash = chosen === "weeks" ? "week-" + weekNumber : chosen;
  window.scrollTo({top: 0, behavior: "smooth"});
}
function renderStart() {
  const current = plan.weeks[weekNow() - 1];
  const ready = (lessons.find(item => item.week === current.number)?.chapters || [])
    .find(chapter => chapter.status === "ready" && chapter.url);
  byId("start").innerHTML = `
    <section class="card">
      <p class="eyebrow">Begin with the reading plan</p>
      <h2>Week ${current.number}: ${escapeHtml(current.shortLabel)}</h2>
      <p class="lead">${escapeHtml(current.focus)}</p>
      <div class="notice">Start the first reading on Saturday, October 3, 2026 (1405/07/11). Read each chapter and its worked examples before independent practice. We will use past entrance-exam booklets together in the final month.</div>
      <div class="actions">
        ${ready ? `<a class="primary" href="${escapeHtml(ready.url)}">Open the completed chapter: ${escapeHtml(ready.title)}</a>` : ""}
        <button type="button" id="open-week">See this week's topics</button>
        <button type="button" id="open-library">Check chapter status</button>
      </div>
    </section>
    <div class="quick-grid">
      <section class="card"><strong>${current.totalHours} hours</strong><span>net study time this week</span></section>
      <section class="card"><strong>${weekIds(current).length} chapters</strong><span>topic boundaries in this week</span></section>
      <section class="card"><strong>4 hours</strong><span>technical English reading each week</span></section>
    </div>`;
  byId("open-week").onclick = () => { renderWeek(current.number); showView("weeks"); };
  byId("open-library").onclick = () => showView("lessons");
}
function renderDaily() {
  if (!daily) { byId("daily").hidden = true; return; }
  const item = daily.days[dayNumber] || daily.days[0];
  const total = item.blocks.reduce((sum, block) => sum + block.hours, 0);
  byId("daily").innerHTML = `
    <p class="eyebrow">Week 1 · October 3–9, 2026</p>
    <h2>Day-by-day reading</h2>
    <p>${escapeHtml(daily.guidance)}</p>
    <div class="day-buttons" aria-label="Choose a study day">
      ${daily.days.map((day, index) => `<button type="button" data-day="${index}" class="${index === dayNumber ? "active" : ""}" aria-pressed="${index === dayNumber}">${escapeHtml(day.name)}<small>${escapeHtml(day.date)}</small></button>`).join("")}
    </div>
    <h3>${escapeHtml(item.name)}, ${escapeHtml(item.date)} · ${total} net hours</h3>
    <ol class="blocks">${item.blocks.map(block => {
      const topic = block.topicId ? plan.topics[block.topicId] : null;
      const subject = topic ? plan.subjects[topic.subject]?.title : "Technical English";
      const chapter = block.topicId ? lessonFor(block.topicId) : null;
      return `<li><div class="block-meta"><span>${escapeHtml(subject)}</span><span>${block.hours} h</span></div>
        <b>${escapeHtml(topic?.title || "Technical reading")}</b><p>${escapeHtml(block.task)}</p>
        ${chapter?.status === "ready" && chapter.url ? `<a href="${escapeHtml(chapter.url)}">Open the chapter →</a>` : ""}</li>`;
    }).join("")}</ol>`;
  byId("daily").querySelectorAll("[data-day]").forEach(button => button.onclick = () => {
    dayNumber = Number(button.dataset.day); renderDaily();
  });
}
function renderWeek(number) {
  const week = plan.weeks.find(item => item.number === number);
  if (!week) return;
  weekNumber = number;
  const status = completion(weekIds(week));
  byId("week-detail").innerHTML = `
    <div class="week-head"><div><p class="eyebrow">First pass · ${escapeHtml(week.shortLabel)}</p>
      <h2>Week ${number} · ${escapeHtml(week.dateLabel)}</h2></div><span class="hours-pill">${week.totalHours} hours</span></div>
    <p class="lead">${escapeHtml(week.focus)}</p>
    <p class="muted">${status.count} of ${status.total} chapters marked read. A checkmark records reading; it does not claim mastery.</p>
    <div class="unit-grid">${week.units.map(unit => {
      const subject = plan.subjects[unit.subject]?.title || "Technical English";
      return `<article class="unit"><div class="unit-top"><h3>${escapeHtml(subject)}</h3><b>${unit.hours} h</b></div>
        ${unit.topicIds.length ? `<ul class="topic-list">${unit.topicIds.map(id => {
          const chapter = lessonFor(id);
          return `<li><input type="checkbox" id="read-${id}" data-topic="${id}" ${completed[id] ? "checked" : ""}><label for="read-${id}">${escapeHtml(plan.topics[id].title)}</label>${chapter?.status === "ready" && chapter.url ? `<a href="${escapeHtml(chapter.url)}">Read →</a>` : ""}</li>`;
        }).join("")}</ul>` : "<p>Read a technical passage closely, noting definitions, assumptions, and new vocabulary in context.</p>"}</article>`;
    }).join("")}</div>`;
  byId("week-detail").querySelectorAll("[data-topic]").forEach(box => box.onchange = () => {
    completed[box.dataset.topic] = box.checked;
    saveProgress(); renderWeek(weekNumber); renderWeekNav(); renderMetrics(); renderRoadmap();
  });
  renderWeekNav();
}
function renderWeekNav() {
  byId("week-nav").innerHTML = plan.weeks.map(week => {
    const done = completion(weekIds(week));
    return `<button type="button" data-week="${week.number}" class="${week.number === weekNumber ? "active" : ""}"><span>Week ${week.number}<small>${escapeHtml(week.shortLabel)}</small></span><b>${done.percent}%</b></button>`;
  }).join("");
  byId("week-nav").querySelectorAll("[data-week]").forEach(button => button.onclick = () => {
    renderWeek(Number(button.dataset.week)); location.hash = "week-" + weekNumber;
  });
}
function renderRoadmap() {
  byId("roadmap").innerHTML = `<p>Each entry gives the first week in which its topic appears. The map covers ${Object.keys(plan.topics).length} named chapters across seven priority subjects.</p>
    <div class="roadmap-grid">${Object.entries(plan.subjects).map(([subjectId, subject]) => {
      const topics = Object.entries(plan.topics).filter(([, data]) => data.subject === subjectId);
      return `<details><summary>${escapeHtml(subject.title)} · ${topics.length} chapters</summary>
        <ol>${topics.map(([id, topic]) => `<li>${escapeHtml(topic.title)} <button type="button" data-jump="${firstWeek(id)}">Week ${firstWeek(id)}</button></li>`).join("")}</ol></details>`;
    }).join("")}</div>`;
  byId("roadmap").querySelectorAll("[data-jump]").forEach(button => button.onclick = () => {
    renderWeek(Number(button.dataset.jump)); showView("weeks");
  });
}
function renderLibrary() {
  const ready = lessons.flatMap(item => item.chapters || []).filter(chapter => chapter.status === "ready" && chapter.url);
  const drafted = lessons.flatMap(item => item.chapters || []).filter(chapter => chapter.status === "draft" && chapter.url);
  byId("library").innerHTML = `<section class="card">
    <p class="eyebrow">Chapter library</p><h2>Read a complete chapter</h2>
    <p>A chapter is labelled complete only after its source comparison, definitions, proofs, edge cases, worked problems, concise review sheet, and presentation checks pass review. At least four genuinely reviewed courses from four universities must be synthesized. More sources are used when they resolve a real gap. Past entrance-exam booklets are reserved for the final month. <a href="sprint.html">Read the full completion standard →</a></p>
    <div class="library-grid">
      ${ready.map(chapter => `<article class="library-card"><span class="status">Ready to study</span><h3>${escapeHtml(chapter.title)}</h3><a class="chapter-link primary" href="${escapeHtml(chapter.url)}">Open chapter →</a></article>`).join("")}
      ${drafted.map(chapter => `<article class="library-card"><span class="status draft">Revision in progress</span><h3>${escapeHtml(chapter.title)}</h3><a class="chapter-link" href="${escapeHtml(chapter.url)}">View draft →</a></article>`).join("")}
      ${!ready.length && !drafted.length ? '<p>The first chapter is undergoing its English quality review. Its link will appear here when the review is complete.</p>' : ""}
    </div>
  </section>
  <section class="card"><h2>What the status means</h2><p>The short weekly overview is an orientation aid, not a substitute for a chapter. An unfinished chapter remains a draft. Chapter production has no fixed hour or recurring deadline; only completed, reviewed chapters receive a ready label.</p></section>`;
}
function renderResources() {
  const list = courses?.courses || [];
  const universities = new Set(list.map(item => item.university)).size;
  byId("resources").innerHTML = `<section class="card"><p class="eyebrow">Source evaluation</p>
    <h2>${list.length} candidate courses · ${universities} universities</h2>
    <p>A candidate appears here after its course page and topic match have been checked. A catalogue match is not evidence that its full lecture text was read. For each chapter, the source audit distinguishes candidates from the four or more course texts actually synthesized.</p>
    <div class="actions"><a href="courses-week1.html">Open the detailed course register →</a></div>
    <div class="source-grid">${Object.entries(plan.subjects).map(([id, subject]) => {
      const matching = list.filter(course => course.subject === id);
      return `<section class="source-card"><h3>${escapeHtml(subject.title)}</h3><p>${matching.length} candidate courses</p>
        ${matching.map(course => `<p><a href="${escapeHtml(course.evidence)}" target="_blank" rel="noopener noreferrer">${escapeHtml(course.university)} · ${escapeHtml(course.course)} ↗</a></p>`).join("")}</section>`;
    }).join("")}</div></section>
    <section class="card"><h2>How sources are selected</h2><p>We compare the accessible lecture text, topic coverage, mathematical precision, proof quality, and explanatory strengths for the exact chapter. The result is a documented selection, not a claim that every course in the world has been exhaustively inspected.</p></section>`;
}
function renderMetrics() {
  const total = completion(Object.keys(plan.topics));
  const current = completion(weekIds(plan.weeks[weekNumber - 1]));
  byId("metrics").innerHTML = `<div><strong>7</strong><span>priority subjects</span></div><div><strong>11</strong><span>first-pass weeks</span></div><div><strong>${total.count}/${total.total}</strong><span>chapters marked read</span></div><div><strong>${current.percent}%</strong><span>week ${weekNumber} marked read</span></div>`;
}
function renderStrategy() {
  const s = plan.strategy;
  byId("strategy").innerHTML = `<p class="eyebrow">Study priorities</p><h2>Why the plan has this shape</h2>
    <p><b>First priority.</b> ${escapeHtml(s.core)}</p>
    <p><b>Programming and digital logic.</b> ${escapeHtml(s.support)}</p>
    <p><b>Second priority.</b> ${escapeHtml(s.deferred)}</p>
    <p><b>Excluded.</b> ${escapeHtml(s.excluded)}</p>
    <p><b>English reading.</b> ${escapeHtml(s.english)}</p>
    <p><b>Review rule.</b> ${escapeHtml(s.reviewGate)}</p>`;
}
function exportProgress() {
  const payload = {schema: 2, savedAt: new Date().toISOString(), planUpdated: plan.updatedLabel,
    completedTopicIds: Object.keys(completed).filter(id => completed[id])};
  const url = URL.createObjectURL(new Blob([JSON.stringify(payload, null, 2)], {type: "application/json"}));
  const anchor = document.createElement("a"); anchor.href = url; anchor.download = "phd-1406-progress.json";
  anchor.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
}
async function importProgress(file) {
  try {
    const data = JSON.parse(await file.text());
    if (data.schema !== 2 || !Array.isArray(data.completedTopicIds) ||
        data.completedTopicIds.some(id => !plan.topics[id])) throw Error("invalid");
    completed = Object.fromEntries(data.completedTopicIds.map(id => [id, true]));
    saveProgress(); renderWeek(weekNumber); renderRoadmap(); renderMetrics();
    byId("import-status").textContent = `Restored ${data.completedTopicIds.length} chapter checkmarks.`;
  } catch {
    byId("import-status").textContent = "The selected file is not a valid progress export.";
  }
}
async function loadJson(path) {
  const response = await fetch(path);
  if (!response.ok) throw Error(path);
  return response.json();
}
async function start() {
  try {
    [plan, daily, courses, lessons] = await Promise.all([
      loadJson("schedule.en.json"), loadJson("week1-daily.en.json"),
      loadJson("course-audit-week1.en.json"), loadJson("lessons.json")
    ]);
    const saved = JSON.parse(localStorage.getItem(progressKey) || "{}");
    completed = Object.fromEntries(Object.entries(saved).filter(([id, value]) => value && plan.topics[id]));
    const requested = Number((location.hash.match(/^#week-(\d+)$/) || [])[1]);
    weekNumber = plan.weeks.some(item => item.number === requested) ? requested : weekNow();
    renderStart(); renderDaily(); renderWeek(weekNumber); renderRoadmap(); renderLibrary();
    renderResources(); renderMetrics(); renderStrategy();
    document.querySelectorAll(".tabs button").forEach(button => button.onclick = () => showView(button.dataset.view));
    byId("export").onclick = exportProgress;
    byId("import").onchange = event => { if (event.target.files?.[0]) importProgress(event.target.files[0]); };
    const initial = location.hash === "#library" ? "lessons" : requested ? "weeks" : location.hash.slice(1);
    showView(initial || "today", false);
    window.addEventListener("hashchange", () => {
      const number = Number((location.hash.match(/^#week-(\d+)$/) || [])[1]);
      if (number && plan.weeks.some(week => week.number === number)) {
        renderWeek(number); renderMetrics(); showView("weeks", false);
      } else showView(location.hash.slice(1), false);
    });
  } catch (error) {
    byId("start").innerHTML = '<section class="card"><h2>Unable to load the plan</h2><p>Refresh this page to retry. If the problem persists, report it in the project conversation.</p></section>';
    console.error(error);
  }
}
start();

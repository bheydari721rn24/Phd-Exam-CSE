const $ = id => document.getElementById(id);
const esc = value => String(value ?? '').replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
const key = 'phd-1406-progress-v2';
let plan, selected = 1, done = {};

function currentWeek() {
  const days = Math.floor((Date.now() - new Date(2026, 8, 24).getTime()) / 86400000);
  return Math.max(1, Math.min(11, Math.floor(days / 7) + 1));
}
function idsForWeek(w) { return [...new Set(w.units.flatMap(u => u.topicIds))]; }
function firstWeek(topicId) { return plan.weeks.find(w => w.units.some(u => u.topicIds.includes(topicId)))?.number || 0; }
function save() { localStorage.setItem(key, JSON.stringify(done)); }
function progress(ids) { const n = ids.filter(id => !!done[id]).length; return {n, total: ids.length, percent: ids.length ? Math.round(100*n/ids.length) : 0}; }
function renderMetrics() {
  const all = Object.keys(plan.topics), p = progress(all), w = plan.weeks[selected-1], wp = progress(idsForWeek(w));
  $('metrics').innerHTML = `
    <div><b>۵</b><span>درس اصلی</span></div>
    <div><b>۱۱</b><span>هفتهٔ دور نخست</span></div>
    <div><b>${p.n} از ${p.total}</b><span>فصل خوانده‌شده</span></div>
    <div><b>${wp.percent}٪</b><span>پیشرفت هفتهٔ انتخابی</span></div>`;
  $('week-progress').textContent = `${wp.n} از ${wp.total} فصل این هفته خوانده شده`;
  $('week-progress-fill').style.width = `${wp.percent}%`;
}
function renderWeek(number) {
  const w = plan.weeks.find(item => item.number === number);
  if (!w) return;
  selected = number;
  location.hash = `week-${number}`;
  $('phase').textContent = w.phase;
  $('week-title').textContent = `هفتهٔ ${number} · ${w.dateLabel}`;
  $('week-focus').textContent = w.focus;
  $('hours').textContent = `${w.totalHours} ساعت`;
  $('notice').textContent = w.notice;
  $('lesson-link').hidden = number !== 1;
  $('unit-list').innerHTML = w.units.map(u => `
    <article class="unit">
      <div class="unit-top"><h3>${esc(plan.subjects[u.subject]?.title || 'انگلیسی موازی')}</h3><b>${u.hours} ساعت</b></div>
      <p>${esc(u.title)}</p>
      ${u.topicIds.length ? `<div class="topic-list">${u.topicIds.map(id => `
        <label class="topic"><input type="checkbox" data-topic="${esc(id)}" ${done[id] ? 'checked' : ''}><span>${esc(plan.topics[id].title)}</span>${number === 1 ? `<a class="topic-read" href="week1.html#${esc(id)}" aria-label="خواندن جزوهٔ ${esc(plan.topics[id].title)}">جزوه ←</a>` : ''}</label>`).join('')}</div>` : '<div class="english-note">تمرین پیوستهٔ خواندن، بدون آزمون تا پایان دور نخست</div>'}
      <small>${esc(u.outcome)}</small>
    </article>`).join('');
  $('unit-list').querySelectorAll('[data-topic]').forEach(box => box.addEventListener('change', () => {
    done[box.dataset.topic] = box.checked;
    save(); renderMetrics(); renderNav(); renderRoadmap();
  }));
  renderNav(); renderMetrics(); renderCourses();
}
function renderNav() {
  $('week-nav').innerHTML = plan.weeks.map(w => {
    const p = progress(idsForWeek(w));
    return `<button class="week-btn ${w.number === selected ? 'active' : ''}" data-week="${w.number}" type="button"><span>هفتهٔ ${w.number}<small>${esc(w.shortLabel)}</small></span><b>${p.percent}٪</b></button>`;
  }).join('');
  $('week-nav').querySelectorAll('button').forEach(button => button.addEventListener('click', () => renderWeek(Number(button.dataset.week))));
}
function renderRoadmap() {
  $('roadmap').innerHTML = `<div class="section-heading"><div><div class="eyebrow">نقشهٔ درس‌ها</div><h2>مرزبندی و ترتیب فصل‌ها</h2></div><span>نخستین هفتهٔ هر فصل نمایش داده شده است.</span></div>
    <div class="subject-grid">${Object.entries(plan.subjects).map(([id, subject]) => {
      const entries = Object.entries(plan.topics).filter(([,t]) => t.subject === id);
      const p = progress(entries.map(([tid]) => tid));
      return `<details><summary><strong>${esc(subject.title)}</strong><span>${p.n} / ${p.total} فصل</span></summary><ol>${entries.map(([tid,t]) => `<li><span>${esc(t.title)}</span><button type="button" data-jump="${firstWeek(tid)}">هفتهٔ ${firstWeek(tid)}</button></li>`).join('')}</ol></details>`;
    }).join('')}</div>`;
  $('roadmap').querySelectorAll('[data-jump]').forEach(b => b.addEventListener('click', () => {renderWeek(Number(b.dataset.jump)); window.scrollTo({top:0,behavior:'smooth'});}));
}
function renderCourses() {
  const subjects = [...new Set(plan.weeks[selected-1].units.map(u => u.subject))].filter(id => id !== 'english');
  $('course-panel').innerHTML = `<div class="eyebrow">فهرست منابع مرتبط با هفتهٔ ${selected}</div><h2>گزینه‌های دانشگاهی برای مقایسه</h2>
  <p>این‌ها نقطهٔ شروع بررسی‌اند. «بهترین دوره» یا بررسی کامل ده دانشگاه برای فصل‌های این هفته هنوز ادعا نمی‌شود؛ انتخاب نهایی در یادداشت همان هفته با تطبیق سرفصل و پرسش‌های واقعی ثبت خواهد شد.</p>
  ${selected === 1 ? '<p><a class="audit-link" href="courses-week1.html">ممیزی منابع هفتهٔ اول: ۱۶ دوره از ۶ دانشگاه ←</a></p>' : ''}
  <div class="course-grid">${subjects.map(id => `<div><h3>${esc(plan.subjects[id].title)}</h3>${(plan.courseOptions[id]||[]).map(course => `<a href="${esc(course.url)}" target="_blank" rel="noopener noreferrer" dir="ltr">${esc(course.name)}</a><small>${esc(course.fit)}</small>`).join('')}</div>`).join('')}</div>`;
}
function renderStatic() {
  $('updated').textContent = plan.updatedLabel;
  const s = plan.strategy;
  $('strategy').innerHTML = `<div><div class="eyebrow">تصمیم مطالعه</div><h2>تمرکز بر پنج درس</h2><p>${esc(s.core)}</p></div><div class="strategy-details"><p><b>پیش‌نیاز هدفمند:</b> ${esc(s.support)}</p><p><b>اولویت دوم:</b> ${esc(s.deferred)}</p><p><b>حذف‌شده:</b> ${esc(s.excluded)}</p><p><b>موازی:</b> ${esc(s.english)}</p><p class="decision-gate"><b>نقطهٔ بازبینی:</b> ${esc(s.reviewGate)}</p></div>`;
  renderRoadmap();
  const mapped = new Set(plan.weeks.flatMap(w => w.units.flatMap(u => u.topicIds)));
  const missing = Object.keys(plan.topics).filter(id => !mapped.has(id));
  $('audit').innerHTML = `<div class="eyebrow">ممیزی برنامه</div><h2>پوشش تعریف‌شده: ${mapped.size} از ${Object.keys(plan.topics).length} فصل</h2><p>${missing.length ? `فصل‌های بدون هفته: ${missing.map(id => esc(plan.topics[id].title)).join('، ')}` : 'همهٔ فصل‌های تعریف‌شده در یک یا چند هفته قرار دارند.'} این نسبت پوشش برنامهٔ خودمان است، نه تضمین پوشش ۱۰۰٪ سؤال‌های آزمون آینده. سازمان سنجش مرزبندی ریزفصل‌ها و تعداد سؤال هر درس را اعلام نکرده است.</p><p>روز آزمون: ۱۶ بهمن ۱۴۰۵. پس از این ۱۱ هفته، زمان باقی‌مانده به تصمیم‌گیری برای سیستم‌عامل و معماری و مرور اختصاص می‌یابد.</p>`;
  $('sources').innerHTML = `<div class="eyebrow">مبنای تصمیم</div><h2>اسناد و دفترچه‌ها</h2><p>${esc(plan.method)}</p><div class="source-links">${plan.sources.map(source => `<a href="${esc(source.url)}" target="_blank" rel="noopener noreferrer">${esc(source.label)} ↗</a>`).join('')}</div>`;
}
function exportProgress() {
  const payload = {schema:2, savedAt:new Date().toISOString(), planUpdated:plan.updatedLabel, completedTopicIds:Object.keys(done).filter(id => done[id])};
  const blob = new Blob([JSON.stringify(payload,null,2)],{type:'application/json'});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a'); a.href=url; a.download='phd-1406-progress.json'; a.click();
  setTimeout(() => URL.revokeObjectURL(url),1000);
}
async function importProgress(file) {
  try {
    const payload = JSON.parse(await file.text());
    if (payload.schema !== 2 || !Array.isArray(payload.completedTopicIds)) throw Error('format');
    const allowed = new Set(Object.keys(plan.topics));
    if (payload.completedTopicIds.some(id => !allowed.has(id))) throw Error('unknown-topic');
    done = Object.fromEntries(payload.completedTopicIds.map(id => [id,true]));
    save(); renderRoadmap(); renderWeek(selected);
    $('import-status').textContent = `${payload.completedTopicIds.length} فصل از پرونده بازیابی شد.`;
  } catch { $('import-status').textContent = 'پروندهٔ پیشرفت معتبر نیست.'; }
}
async function start() {
  try {
    const response = await fetch('schedule.json');
    if (!response.ok) throw Error('network');
    plan = await response.json();
    const saved = JSON.parse(localStorage.getItem(key)||'{}');
    done = Object.fromEntries(Object.entries(saved).filter(([id,value]) => value && plan.topics[id]));
    renderStatic();
    const requested = Number((location.hash.match(/week-(\d+)/)||[])[1]);
    renderWeek(plan.weeks.some(w => w.number === requested) ? requested : currentWeek());
    $('go-today').addEventListener('click', () => renderWeek(currentWeek()));
    $('export').addEventListener('click', exportProgress);
    $('import').addEventListener('change', e => {if(e.target.files[0]) importProgress(e.target.files[0]);});
  } catch {
    $('strategy').textContent = 'برنامه بارگذاری نشد. لطفاً صفحه را دوباره باز کنید.';
  }
}
start();

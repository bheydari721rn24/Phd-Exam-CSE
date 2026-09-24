const $ = id => document.getElementById(id);
const esc = value => String(value ?? '').replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
const key = 'phd-1406-progress-v2';
let plan, courseAudit, lessons = [], selected = 1, done = {};

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
    <div><b>${Object.keys(plan.subjects).length}</b><span>درس اولویت اول</span></div>
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
  const lesson = lessons.find(item => item.week === number);
  $('lesson-link').hidden = !lesson;
  if (lesson) { $('lesson-link').href = lesson.url; $('lesson-link').textContent = `باز کردن جزوهٔ هفتهٔ ${number} ←`; }
  $('library-status').textContent = lesson
    ? `جزوهٔ هفتهٔ ${number} منتشر شده؛ از هر فصل برنامه نیز می‌توانید مستقیم به همان بخش بروید.`
    : `جزوهٔ هفتهٔ ${number} هنوز منتشر نشده است. پس از آماده‌سازی، پیوند آن همین‌جا و در بخش «جزوه‌ها» فعال می‌شود.`;
  $('unit-list').innerHTML = w.units.map(u => `
    <article class="unit">
      <div class="unit-top"><h3>${esc(plan.subjects[u.subject]?.title || 'انگلیسی موازی')}</h3><b>${u.hours} ساعت</b></div>
      <p>${esc(u.title)}</p>
      ${u.topicIds.length ? `<div class="topic-list">${u.topicIds.map(id => `
        <label class="topic"><input type="checkbox" data-topic="${esc(id)}" ${done[id] ? 'checked' : ''}><span>${esc(plan.topics[id].title)}</span>${lesson ? `<a class="topic-read" href="${esc(lesson.url)}#${esc(id)}" aria-label="خواندن جزوهٔ ${esc(plan.topics[id].title)}">جزوه ←</a>` : ''}</label>`).join('')}</div>` : '<div class="english-note">تمرین پیوستهٔ خواندن، بدون آزمون تا پایان دور نخست</div>'}
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
  if (selected !== 1 || !courseAudit) {
    $('course-panel').innerHTML = `<div class="eyebrow">ممیزی منابع · هفتهٔ ${selected}</div><h2>فهرست این هفته در دست تهیه است</h2><p>دوره‌های قدیمی یا نامربوط به‌صورت خودکار اینجا تکرار نمی‌شوند. پس از بررسی فصل‌های همین هفته، فهرست مستند آن منتشر می‌شود.</p>`;
    return;
  }
  const courses = courseAudit.courses;
  const universities = new Set(courses.map(c => c.university)).size;
  $('course-panel').innerHTML = `<div class="eyebrow">ممیزی واقعی منابع · هفتهٔ ۱</div><h2>${courses.length} دوره از ${universities} دانشگاه</h2>
  <p>هر پیوند از دفتر ممیزی مشترک خوانده می‌شود. سطح بررسی، محدودیت و پیوند شاهد در صفحهٔ جزئیات مشخص است؛ حضور در این فهرست به معنی خواندن کامل دوره نیست.</p>
  <p><a class="audit-link" href="courses-week1.html">باز کردن دفتر ممیزی منابع ←</a></p>
  <div class="course-grid">${subjects.map(id => {const list=courses.filter(c=>c.subject===id);return `<div><h3>${esc(plan.subjects[id].title)} <small>${list.length} دوره</small></h3>${list.map(c => `<a href="${esc(c.evidence)}" target="_blank" rel="noopener noreferrer" dir="ltr">${esc(c.university)} · ${esc(c.course)}</a>`).join('')}</div>`}).join('')}</div>`;
}
function renderLibrary() {
  $('library').innerHTML = `<div class="section-heading"><div><div class="eyebrow">کتابخانهٔ شما</div><h2>جزوه‌ها در همین اپ</h2></div><span>پیوند هر هفته پس از انتشار فعال می‌شود.</span></div>
  <p>«تهیه و انتشار جزوهٔ هفتگی» نام کارِ زمان‌بندی‌شدهٔ من است؛ خودِ جزوه نیست. متن آموزشیِ قابل خواندن و شکل‌ها در صفحه‌های زیر قرار می‌گیرند.</p>
  <div class="library-grid">${lessons.map(l => `<article class="library-card"><div class="eyebrow">هفتهٔ ${l.week} · آمادهٔ مطالعه</div><h3>${esc(l.title)}</h3><p>${esc(l.description)}</p><a class="primary-link" href="${esc(l.url)}">خواندن جزوه ←</a>${l.auditUrl ? `<a class="secondary-link" href="${esc(l.auditUrl)}">دیدن منابع و میزان بررسی ←</a>` : ''}</article>`).join('')}
  <article class="library-card pending"><div class="eyebrow">هفته‌های بعد · در صف تهیه</div><h3>جزوهٔ هر هفته، کنار برنامهٔ همان هفته</h3><p>پس از انتشار، این فهرست و پیوندِ کنار فصل‌ها به‌روز می‌شود. ساعت ۹ پنجشنبه زمان آغاز کار خودکار است؛ پایان تهیه به حجم بررسی منابع وابسته است.</p></article></div>`;
}
function renderStart() {
  const number = currentWeek(), current = plan.weeks[number-1];
  const lesson = lessons.find(item => item.week === number);
  $('start-panel').innerHTML = `<div class="start-copy"><div class="eyebrow">مسیر شروع · همین هفته</div><h2>اول جزوه را بخوانید</h2><p>فصل‌های هفتهٔ ${number} را در برنامه ببینید، بخش متناظر جزوه را با نمونه‌های حل‌شده بخوانید و پس از خواندن، فصل را علامت بزنید. در دور نخست هیچ تستی برای پاسخ‌دادن از شما خواسته نمی‌شود.</p><div class="start-actions">${lesson ? `<a class="primary-link" href="${esc(lesson.url)}${number===1?'#p_types':''}">شروع با جزوهٔ هفتهٔ ${number} ←</a>` : `<button class="primary-link" type="button" id="show-current-week">دیدن فصل‌های این هفته ←</button>`}<a class="secondary-link" href="#library">محل همهٔ جزوه‌ها ←</a></div></div><div class="start-card"><span>هفتهٔ ${number}</span><strong>${esc(current.dateLabel)}</strong><p>${current.totalHours} ساعت در برنامه</p><small>${lesson ? 'جزوهٔ این هفته آماده است.' : 'جزوهٔ این هفته هنوز منتشر نشده است.'}</small></div>`;
  $('show-current-week')?.addEventListener('click',()=>{renderWeek(number);document.querySelector('.week-panel').scrollIntoView({behavior:'smooth'});});
}
function renderStatic() {
  $('updated').textContent = plan.updatedLabel;
  const s = plan.strategy;
  $('strategy').innerHTML = `<div><div class="eyebrow">تصمیم مطالعه</div><h2>هفت درس در اولویت اول</h2><p>${esc(s.core)}</p></div><div class="strategy-details"><p><b>برنامه‌سازی و مدار منطقی:</b> ${esc(s.support)}</p><p><b>اولویت دوم:</b> ${esc(s.deferred)}</p><p><b>حذف‌شده:</b> ${esc(s.excluded)}</p><p><b>موازی:</b> ${esc(s.english)}</p><p class="decision-gate"><b>نقطهٔ بازبینی:</b> ${esc(s.reviewGate)}</p></div>`;
  renderRoadmap();
  renderLibrary();
  renderStart();
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
    try { const auditResponse = await fetch('course-audit-week1.json'); if (auditResponse.ok) courseAudit = await auditResponse.json(); } catch {}
    try { const lessonResponse = await fetch('lessons.json'); if (lessonResponse.ok) lessons = await lessonResponse.json(); } catch {}
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

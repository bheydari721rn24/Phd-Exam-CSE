const $ = id => document.getElementById(id);
const esc = value => String(value ?? '').replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
const fa = value => String(value).replace(/[0-9]/g, digit => '۰۱۲۳۴۵۶۷۸۹'[digit]);
const key = 'phd-1406-progress-v2';
let plan, courseAudit, dailyPlan, lessons = [], selected = 1, done = {};

function currentWeek() {
  const tehranNow = Date.now() + 3.5 * 3600000;
  const days = Math.floor((tehranNow - Date.UTC(2026, 9, 3)) / 86400000);
  return Math.max(1, Math.min(11, Math.floor(days / 7) + 1));
}
function idsForWeek(w) { return [...new Set(w.units.flatMap(u => u.topicIds))]; }
function readyChapters(lesson) { return (lesson?.chapters || []).filter(c => c.status === 'ready' && c.url); }
function chapterFor(lesson, id) { return readyChapters(lesson).find(c => c.topicId === id); }
function draftChapters(lesson) { return (lesson?.chapters || []).filter(c => c.status === 'draft' && c.url); }
function draftFor(lesson, id) { return draftChapters(lesson).find(c => c.topicId === id); }
function firstWeek(topicId) { return plan.weeks.find(w => w.units.some(u => u.topicIds.includes(topicId)))?.number || 0; }
function save() { localStorage.setItem(key, JSON.stringify(done)); }
function progress(ids) { const n = ids.filter(id => !!done[id]).length; return {n, total: ids.length, percent: ids.length ? Math.round(100*n/ids.length) : 0}; }
function renderMetrics() {
  const all = Object.keys(plan.topics), p = progress(all), w = plan.weeks[selected-1], wp = progress(idsForWeek(w));
  $('metrics').innerHTML = `
    <div><b>${fa(Object.keys(plan.subjects).length)}</b><span>درس اولویت اول</span></div>
    <div><b>۱۱</b><span>هفته‌ی دور نخست</span></div>
    <div><b>${fa(p.n)} از ${fa(p.total)}</b><span>فصل‌های علامت‌خورده در برنامه</span></div>
    <div><b>${fa(wp.percent)}٪</b><span>فصل‌های علامت‌خورده در این هفته</span></div>`;
  $('week-progress').textContent = `از ${fa(wp.total)} فصل این هفته، ${fa(wp.n)} فصل را پس از مطالعه علامت زده‌اید.`;
  $('week-progress-fill').style.width = `${wp.percent}%`;
}
function renderWeek(number) {
  const w = plan.weeks.find(item => item.number === number);
  if (!w) return;
  selected = number;
  location.hash = `week-${number}`;
  $('phase').textContent = w.phase;
  $('week-title').textContent = `هفته‌ی ${fa(number)} · ${fa(w.dateLabel)}`;
  $('week-focus').textContent = w.focus;
  $('hours').textContent = `${fa(w.totalHours)} ساعت`;
  $('notice').textContent = w.notice;
  const lesson = lessons.find(item => item.week === number);
  const ready = readyChapters(lesson);
  $('lesson-link').hidden = !lesson?.overviewUrl;
  if (lesson?.overviewUrl) { $('lesson-link').href = lesson.overviewUrl; $('lesson-link').textContent = `نمای کلی کوتاه هفته‌ی ${fa(number)} ←`; }
  $('library-status').textContent = lesson
    ? ready.length
      ? `برای ${fa(ready.length)} فصل از ${fa(idsForWeek(w).length)} فصل این هفته، درسنامه‌ی کامل و بازبینی‌شده منتشر شده است. پیوند هر درسنامه کنار عنوان همان فصل قرار دارد.`
      : `هنوز برای هیچ‌یک از ${fa(idsForWeek(w).length)} فصل این هفته درسنامه‌ی کامل منتشر نشده است. پیوند «نمای کلی» فقط یک متن مقدماتی است؛ وضعیت هر فصل را در کتابخانه ببینید.`
    : `هنوز درسنامه‌ی کامل فصل‌های هفته‌ی ${fa(number)} منتشر نشده است. پس از انتشار، پیوند هر درسنامه کنار عنوان فصل و در کتابخانه ظاهر می‌شود.`;
  $('unit-list').innerHTML = w.units.map(u => `
    <article class="unit">
      <div class="unit-top"><h3>${esc(plan.subjects[u.subject]?.title || 'انگلیسی موازی')}</h3><b>${fa(u.hours)} ساعت</b></div>
      <p>${esc(u.title)}</p>
      ${u.topicIds.length ? `<div class="topic-list">${u.topicIds.map(id => `
        <label class="topic"><input type="checkbox" data-topic="${esc(id)}" ${done[id] ? 'checked' : ''}><span>${esc(plan.topics[id].title)}</span>${chapterFor(lesson,id) ? `<a class="topic-read" href="${esc(chapterFor(lesson,id).url)}" aria-label="خواندن درسنامه‌ی ${esc(plan.topics[id].title)}">درسنامه ←</a>` : draftFor(lesson,id) ? `<a class="topic-read draft-link" href="${esc(draftFor(lesson,id).url)}" aria-label="خواندن پیش‌نویس ${esc(plan.topics[id].title)}">پیش‌نویس ←</a>` : '<small class="topic-pending">درسنامه هنوز منتشر نشده است</small>'}</label>`).join('')}</div>` : '<div class="english-note">این چهار ساعت برای خواندن متن علمی انگلیسی است؛ در دور نخست آزمونی ندارید.</div>'}
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
    return `<button class="week-btn ${w.number === selected ? 'active' : ''}" data-week="${w.number}" type="button"><span>هفته‌ی ${fa(w.number)}<small>${esc(fa(w.shortLabel))}</small></span><b>${fa(p.percent)}٪</b></button>`;
  }).join('');
  $('week-nav').querySelectorAll('button').forEach(button => button.addEventListener('click', () => renderWeek(Number(button.dataset.week))));
}
function renderRoadmap() {
  $('roadmap').innerHTML = `<div class="section-heading"><div><div class="eyebrow">فهرست فصل‌ها</div><h2>فصل‌های هر درس در کدام هفته قرار دارند؟</h2></div><span>نام هر درس را باز کنید؛ کنار هر فصل، نخستین هفته‌ی مطالعه‌ی آن نوشته شده است.</span></div>
    <div class="subject-grid">${Object.entries(plan.subjects).map(([id, subject]) => {
      const entries = Object.entries(plan.topics).filter(([,t]) => t.subject === id);
      const p = progress(entries.map(([tid]) => tid));
      return `<details><summary><strong>${esc(subject.title)}</strong><span>${fa(p.n)} فصل علامت‌خورده از ${fa(p.total)} فصل</span></summary><ol>${entries.map(([tid,t]) => `<li><span>${esc(t.title)}</span><button type="button" data-jump="${firstWeek(tid)}">هفته‌ی ${fa(firstWeek(tid))}</button></li>`).join('')}</ol></details>`;
    }).join('')}</div>`;
  $('roadmap').querySelectorAll('[data-jump]').forEach(b => b.addEventListener('click', () => {renderWeek(Number(b.dataset.jump)); window.scrollTo({top:0,behavior:'smooth'});}));
}
function renderCourses() {
  const subjects = [...new Set(plan.weeks[selected-1].units.map(u => u.subject))].filter(id => id !== 'english');
  if (selected !== 1 || !courseAudit) {
    const auditUrl = lessons.find(item => item.week === selected)?.auditUrl;
    $('course-panel').innerHTML = `<div class="eyebrow">منابع دانشگاهی · هفته‌ی ${fa(selected)}</div><h2>${auditUrl ? 'منابع بررسی‌شده برای فصل‌های این هفته' : 'فهرست منابع این هفته هنوز منتشر نشده است'}</h2><p>${auditUrl ? 'در دفتر منابع می‌توانید ببینید هر دوره به کدام فصل مربوط است، چه کمکی می‌کند، چه محدودیتی دارد و چه مقدار از متن آن واقعاً بررسی شده است.' : 'منابع هر هفته پس از بررسی متن درس‌ها و ارتباطشان با فصل‌های همان هفته در این بخش منتشر می‌شوند.'}</p>${auditUrl ? `<a class="audit-link" href="${esc(auditUrl)}">دیدن دفتر منابع این هفته ←</a>` : ''}`;
    return;
  }
  const courses = courseAudit.courses;
  const universities = new Set(courses.map(c => c.university)).size;
  $('course-panel').innerHTML = `<div class="eyebrow">منابع دانشگاهی · هفته‌ی ۱</div><h2>${fa(courses.length)} دوره‌ی شناسایی‌شده از ${fa(universities)} دانشگاه</h2>
  <p>این دوره‌ها برای فصل‌های هفته‌ی اول شناسایی شده‌اند. روی نام هر دوره بزنید تا به متن یا صفحه‌ی شاهد آن بروید؛ در دفتر منابع نیز میزان مطالعه‌ی واقعی، مزیت و محدودیت هر دوره ثبت شده است. قرارگرفتن در این فهرست به معنای مطالعه‌ی کامل دوره نیست.</p>
  <p><a class="audit-link" href="courses-week1.html">دیدن دفتر منابع هفته‌ی اول ←</a></p>
  <div class="course-grid">${subjects.map(id => {const list=courses.filter(c=>c.subject===id);return `<div><h3>${esc(plan.subjects[id].title)} <small>${fa(list.length)} دوره</small></h3>${list.map(c => `<a href="${esc(c.evidence)}" target="_blank" rel="noopener noreferrer" dir="ltr" lang="en">${esc(c.university)} · ${esc(c.course)}</a>`).join('')}</div>`}).join('')}</div>`;
}
function renderLibrary() {
  $('library').innerHTML = `<div class="section-heading"><div><div class="eyebrow">کتابخانه‌ی شما</div><h2>درسنامه‌ی هر فصل را از اینجا باز کنید</h2></div><span>پیوند هر درسنامه پس از تکمیل و بازبینی فعال می‌شود.</span></div>
  <p>برای هر فصل، وضعیت انتشار جداگانه نشان داده می‌شود. «نمای کلی» و «پیش‌نویس» متن آموزشی مقدماتی‌اند و هنوز معیار درسنامه‌ی کامل را ندارند.</p>
  <p class="chapter-standard"><b>معیار تهیه‌ی درسنامه:</b> متن هر فصل باید دست‌کم چهار دوره‌ی واقعاً مطالعه‌شده از چهار دانشگاه برتر را ترکیب کند و همه‌ی ریزمبحث‌های مرتبط را از پیش‌نیاز تا نکات پیشرفته، با اثبات، مثال حل‌شده و ارتباط با سؤال‌های آزمون توضیح دهد. پیش از انتشار، پوشش فصل با فهرست موضوعات و دفترچه‌های آزمون کنترل می‌شود و هر شکاف باقی‌مانده آشکار گزارش می‌شود. هدف، آمادگی برای دشوارترین سؤال‌های مرتبط است؛ برای سؤال‌های دیده‌نشده نمی‌توان تضمین قطعی داد.</p>
  <div class="library-grid">${lessons.map(l => `<article class="library-card"><div class="eyebrow">هفته‌ی ${fa(l.week)} · ${fa(readyChapters(l).length)} درسنامه‌ی کامل از ${fa(l.chapters?.length || 0)} فصل</div><h3>${esc(fa(l.title))}</h3><p>${esc(fa(l.description))}</p>${readyChapters(l).map(c => `<a class="primary-link" href="${esc(c.url)}">${esc(fa(c.title))} ←</a>`).join('')}${draftChapters(l).map(c => `<a class="secondary-link" href="${esc(c.url)}">خواندن پیش‌نویس: ${esc(fa(c.title))} ←</a>`).join('')}${l.overviewUrl ? `<a class="secondary-link" href="${esc(l.overviewUrl)}">خواندن نمای کلی هفته ←</a>` : ''}${l.auditUrl ? `<a class="secondary-link" href="${esc(l.auditUrl)}">دیدن منابع بررسی‌شده ←</a>` : ''}<p class="library-pending">برای ${fa((l.chapters || []).filter(c=>c.status!=='ready').length)} فصل، درسنامه‌ی کامل هنوز منتشر نشده است.</p></article>`).join('')}
  <article class="library-card pending"><div class="eyebrow">هفته‌های بعد · منتظر انتشار</div><h3>درسنامه‌های بعدی کجا قرار می‌گیرند؟</h3><p>پس از تکمیل و بازبینی هر فصل، پیوند آن در همین کتابخانه و کنار عنوان فصل در برنامه‌ی همان هفته ظاهر می‌شود. فرایند هفتگی پنجشنبه‌ها ساعت ۹ شب به وقت تهران برای هفته‌ی مطالعاتیِ شنبه تا جمعه‌ی پیش رو اجرا می‌شود. هر فصل پس از تکمیل و بازبینی منتشر می‌شود و پیوند آن همین‌جا قرار می‌گیرد.</p></article></div>`;
}
function renderDaily() {
  if (!dailyPlan) { $('daily-plan').hidden = true; return; }
  const lesson = lessons.find(item => item.week === dailyPlan.week);
  $('daily-plan').innerHTML = `<div class="section-heading"><div><div class="eyebrow">۱۱ تا ۱۷ مهر ۱۴۰۵</div><h2>برنامه‌ی روزبه‌روز هفته‌ی اول</h2></div><span>هر روز ${fa(dailyPlan.dailyHours)} ساعت مطالعه‌ی خالص</span></div>
  <p>${esc(dailyPlan.guidance)}</p><div class="day-grid">${dailyPlan.days.map(day => `<article class="day-card"><header><h3>${esc(day.name)} ${esc(day.date)}</h3><strong>${fa(day.blocks.reduce((sum,b)=>sum+b.hours,0))} ساعت</strong></header><ol>${day.blocks.map(block => {const chapter = block.topicId ? chapterFor(lesson,block.topicId) : null; const draft = block.topicId ? draftFor(lesson,block.topicId) : null; const title = block.topicId ? plan.topics[block.topicId]?.title : 'انگلیسی موازی'; return `<li><div class="day-block-title"><b>${esc(title)}</b><span>${fa(block.hours)} ساعت</span></div><p>${esc(block.task)}</p>${chapter ? `<a href="${esc(chapter.url)}">درسنامه‌ی بازبینی‌شده ←</a>` : draft ? `<a href="${esc(draft.url)}">خواندن پیش‌نویس ←</a>` : block.topicId ? '<small>درسنامه‌ی کامل هنوز منتشر نشده است.</small>' : ''}</li>`;}).join('')}</ol></article>`).join('')}</div>`;
}
function renderStart() {
  const number = currentWeek(), current = plan.weeks[number-1];
  const lesson = lessons.find(item => item.week === number);
  const first = readyChapters(lesson)[0], draft = draftChapters(lesson)[0];
  $('start-panel').innerHTML = `<div class="start-copy"><div class="eyebrow">از اینجا شروع کنید</div><h2>${first ? 'درسنامه‌ی کامل نخستین فصل را بخوانید' : draft ? 'با پیش‌نویس فصل نخست آشنا شوید' : 'برنامه‌ی فصل‌های این هفته را ببینید'}</h2><p>ابتدا فصل‌های هفته‌ی ${fa(number)} را در برنامه ببینید و متن آموزشی موجود برای هر فصل را بخوانید. پیوند «پیش‌نویس» یعنی متن هنوز کامل و بازبینی‌شده نیست؛ درسنامه‌ی کامل پس از تأیید در همین اپ منتشر می‌شود. پس از مطالعه‌ی هر فصل، مربع کنار عنوان آن را علامت بزنید. تا پایان دور نخست لازم نیست به تست پاسخ دهید.</p><div class="start-actions">${first ? `<a class="primary-link" href="${esc(first.url)}">خواندن درسنامه: ${esc(fa(first.title))} ←</a>` : draft ? `<a class="primary-link" href="${esc(draft.url)}">خواندن پیش‌نویس: ${esc(fa(draft.title))} ←</a>` : `<button class="primary-link" type="button" id="show-current-week">دیدن فصل‌های این هفته ←</button>`}<a class="secondary-link" href="#library">دیدن وضعیت انتشار درسنامه‌ها ←</a></div></div><div class="start-card"><span>هفته‌ی ${fa(number)}</span><strong>${esc(fa(current.dateLabel))}</strong><p>${fa(current.totalHours)} ساعت مطالعه در این هفته</p><small>${lesson ? readyChapters(lesson).length ? `درسنامه‌ی کامل ${fa(readyChapters(lesson).length)} فصل منتشر شده است؛ وضعیت فصل‌های دیگر را در کتابخانه ببینید.` : 'هنوز درسنامه‌ی کاملی برای این هفته منتشر نشده است؛ متن‌های موجود با برچسب «پیش‌نویس» مشخص شده‌اند.' : 'هنوز درسنامه‌ی کاملی برای این هفته منتشر نشده است.'}</small></div>`;
  $('show-current-week')?.addEventListener('click',()=>{renderWeek(number);document.querySelector('.week-panel').scrollIntoView({behavior:'smooth'});});
}
function renderStatic() {
  $('updated').textContent = fa(plan.updatedLabel);
  const s = plan.strategy;
  $('strategy').innerHTML = `<div><div class="eyebrow">چرا این درس‌ها در برنامه‌اند؟</div><h2>درس‌های دور نخست و ترتیب مطالعه</h2><p>${esc(s.core)}</p></div><div class="strategy-details"><p><b>سهم برنامه‌سازی و مدار منطقی:</b> ${esc(s.support)}</p><p><b>درس‌های اولویت دوم:</b> ${esc(s.deferred)}</p><p><b>درس خارج از برنامه:</b> ${esc(s.excluded)}</p><p><b>انگلیسی در کنار درس‌ها:</b> ${esc(s.english)}</p><p class="decision-gate"><b>زمان بازبینی برنامه:</b> ${esc(s.reviewGate)}</p></div>`;
  renderRoadmap();
  renderLibrary();
  renderStart();
  const mapped = new Set(plan.weeks.flatMap(w => w.units.flatMap(u => u.topicIds)));
  const missing = Object.keys(plan.topics).filter(id => !mapped.has(id));
  $('audit').innerHTML = `<div class="eyebrow">بررسی زمان‌بندی فصل‌ها</div><h2>برای ${fa(mapped.size)} فصل از ${fa(Object.keys(plan.topics).length)} فصل، هفته‌ی مطالعه مشخص شده است</h2><p>${missing.length ? `این فصل‌ها هنوز هفته‌ی مطالعه ندارند: ${missing.map(id => esc(fa(plan.topics[id].title))).join('، ')}.` : 'همه‌ی فصل‌های موجود در این برنامه در دست‌کم یک هفته قرار گرفته‌اند.'} این عدد فقط کامل‌بودن زمان‌بندی همین برنامه را نشان می‌دهد و به معنای پوشش قطعی همه‌ی سؤال‌های آزمون آینده نیست. پس از بررسی دفترچه‌ها و پیشرفت واقعی شما، در صورت نیاز فصل‌بندی را اصلاح می‌کنیم.</p><p>تاریخ درج‌شده برای آزمون، ۱۶ بهمن ۱۴۰۵ است. بعد از پایان این ۱۱ هفته، درباره‌ی مطالعه‌ی سیستم‌عامل و معماری کامپیوتر و زمان مرور درس‌ها با توجه به فرصت باقی‌مانده تصمیم می‌گیریم.</p>`;
  $('sources').innerHTML = `<div class="eyebrow">پایه‌ی اطلاعات برنامه</div><h2>این برنامه بر چه منابعی تکیه دارد؟</h2><p>${esc(fa(plan.method))}</p><div class="source-links">${plan.sources.map(source => `<a href="${esc(source.url)}" target="_blank" rel="noopener noreferrer" lang="en" dir="ltr">${esc(source.label)} ↗</a>`).join('')}</div>`;
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
    $('import-status').textContent = `${fa(payload.completedTopicIds.length)} فصل از پرونده بازیابی شد.`;
  } catch { $('import-status').textContent = 'پرونده‌ی پیشرفت معتبر نیست.'; }
}
async function start() {
  try {
    const response = await fetch('schedule.json');
    if (!response.ok) throw Error('network');
    plan = await response.json();
    try { const auditResponse = await fetch('course-audit-week1.json'); if (auditResponse.ok) courseAudit = await auditResponse.json(); } catch {}
    try { const lessonResponse = await fetch('lessons.json'); if (lessonResponse.ok) lessons = await lessonResponse.json(); } catch {}
    try { const dailyResponse = await fetch('week1-daily.json'); if (dailyResponse.ok) dailyPlan = await dailyResponse.json(); } catch {}
    const saved = JSON.parse(localStorage.getItem(key)||'{}');
    done = Object.fromEntries(Object.entries(saved).filter(([id,value]) => value && plan.topics[id]));
    renderStatic();
    renderDaily();
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

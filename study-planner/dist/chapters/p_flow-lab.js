/* A finite declared teaching model, not an interpreter for arbitrary C. */
(function () {
  'use strict';
  function traceFlow(mode, limit, start) {
    if (!['for', 'while', 'do', 'bug', 'break'].includes(mode) ||
        !Number.isInteger(limit) || !Number.isInteger(start) ||
        limit < 0 || limit > 12 || start < 0 || start > 12) {
      return {valid: false, rows: [], status: 'invalid'};
    }
    let i = start, sum = 0, tests = 0, entries = 0, updates = 0;
    let phase = mode === 'do' ? 'body' : 'guard';
    let status = 'running';
    const rows = [], seen = new Set();
    const add = (where, reason) => rows.push({phase: where, i, sum, tests, entries, updates, reason});
    add('init', `Start with index ${start}, sum 0, and limit ${limit}.`);
    while (phase !== 'exit' && rows.length < 200) {
      const key = `${phase}/${i}/${sum}`;
      if (seen.has(key)) {
        status = 'cycle';
        add('exit', 'The same complete execution state recurs: this deterministic model cycles.');
        phase = 'exit';
        break;
      }
      seen.add(key);
      if (phase === 'guard') {
        tests++;
        const admitted = i < limit;
        add('guard', `${i} < ${limit} is ${admitted ? 'true: enter the body' : 'false: leave the loop'}.`);
        phase = admitted ? 'body' : 'exit';
        if (!admitted) status = 'normal';
      } else if (phase === 'body') {
        entries++;
        if (mode === 'break' && i === 3) {
          add('body', 'Index 3 triggers break; no addition and no header update follow.');
          phase = 'exit'; status = 'break';
        } else if ((mode === 'for' || mode === 'bug') && i % 2 === 0) {
          add('body', mode === 'for' ? 'Even index triggers continue; the for-update is next.' : 'Even index triggers continue; the manual update is skipped.');
          phase = mode === 'for' ? 'update' : 'guard';
        } else {
          sum += i;
          add('body', `Add the current index ${i}; sum becomes ${sum}.`);
          phase = 'update';
        }
      } else if (phase === 'update') {
        i++; updates++;
        add('update', `Increment index to ${i}; evaluate the guard next.`);
        phase = 'guard';
      }
    }
    if (phase !== 'exit') {
      status = 'cap';
      add('exit', 'Trace limit reached; this cap alone proves nothing about termination.');
    } else if (status !== 'cycle') {
      add('exit', status === 'break' ? 'Stopped by break, with no additional guard or update.' : 'Stopped by a false guard.');
    }
    return {valid: true, rows, status, i, sum, tests, entries, updates};
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = {traceFlow};
  if (typeof document === 'undefined') return;
  const element = id => document.getElementById(id);
  if (!element('flow-case')) return;
  let current, position = 0;
  const programs = {
    for: 'int i = START, sum = 0;\nfor (; i < LIMIT; ++i) {\n    if (i % 2 == 0) continue;\n    sum += i;\n}',
    while: 'int i = START, sum = 0;\nwhile (i < LIMIT) {\n    sum += i;\n    ++i;\n}',
    do: 'int i = START, sum = 0;\ndo {\n    sum += i;\n    ++i;\n} while (i < LIMIT);',
    bug: 'int i = START, sum = 0;\nwhile (i < LIMIT) {\n    if (i % 2 == 0) continue;\n    sum += i;\n    ++i;\n}',
    break: 'int i = START, sum = 0;\nfor (; i < LIMIT; ++i) {\n    if (i == 3) break;\n    sum += i;\n}'
  };
  function show() {
    const output = element('flow-state'), table = element('flow-trace');
    table.replaceChildren();
    if (!current.valid) {
      output.textContent = 'Enter integer values between 0 and 12.';
      output.dataset.status = 'invalid';
      element('flow-explanation').textContent = 'Invalid input has no execution trace.';
      ['flow-prev','flow-next','flow-end'].forEach(id => element(id).disabled = true);
      document.querySelectorAll('.flow-track span').forEach(x => x.classList.remove('active'));
      return;
    }
    const state = current.rows[position];
    output.textContent = `After ${state.phase}: i = ${state.i}, sum = ${state.sum}`;
    Object.assign(output.dataset, {status: position === current.rows.length - 1 ? current.status : 'running',
      i: String(state.i), sum: String(state.sum), tests: String(state.tests), entries: String(state.entries), updates: String(state.updates), position: String(position), length: String(current.rows.length)});
    element('flow-explanation').textContent = `${state.reason} Guard tests: ${state.tests}; body entries: ${state.entries}; updates: ${state.updates}.`;
    current.rows.slice(0, position + 1).forEach((row, index) => {
      const tr = document.createElement('tr');
      if (index === position) tr.className = 'active';
      [index, row.phase, row.i, row.sum, row.reason].forEach(value => {
        const td = document.createElement('td'); td.textContent = String(value); tr.append(td);
      });
      table.append(tr);
    });
    document.querySelectorAll('.flow-track span').forEach(x => x.classList.toggle('active', x.dataset.phase === state.phase));
    element('flow-prev').disabled = position === 0;
    element('flow-next').disabled = position === current.rows.length - 1;
    element('flow-end').disabled = position === current.rows.length - 1;
  }
  function reset() {
    const mode = element('flow-case').value;
    const parse = id => element(id).value.trim() === '' ? NaN : Number(element(id).value);
    const limit = parse('flow-limit'), start = parse('flow-start');
    current = traceFlow(mode, limit, start); position = 0;
    element('flow-code').textContent = programs[mode].replaceAll('START', String(start)).replaceAll('LIMIT', String(limit));
    show();
  }
  ['flow-case','flow-limit','flow-start'].forEach(id => element(id).addEventListener('input', reset));
  element('flow-prev').addEventListener('click', () => {position = Math.max(0, position - 1); show();});
  element('flow-next').addEventListener('click', () => {position = Math.min(current.rows.length - 1, position + 1); show();});
  element('flow-end').addEventListener('click', () => {position = current.rows.length - 1; show();});
  reset();
}());

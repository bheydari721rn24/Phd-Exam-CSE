/* Include complete worked solutions in print, preserving the reader's open states. */
(() => {
  let states = null;
  addEventListener('beforeprint', () => {
    if (states) return;
    states = [...document.querySelectorAll('details.exam-solution')].map(node => [node, node.open]);
    states.forEach(([node]) => { node.open = true; });
  });
  addEventListener('afterprint', () => {
    if (!states) return;
    states.forEach(([node, open]) => { node.open = open; });
    states = null;
  });
})();

"use strict";
(() => {
  const subject = document.getElementById("lab-subject"), meaning = document.getElementById("lab-meaning"), form = document.getElementById("lab-form");
  if (!subject || !meaning || !form) return;
  function render() {
    const s = subject.value, c = meaning.value, mode = form.value, verb = s === "I" ? "am" : s === "Emma" ? "is" : "are";
    const tokens = mode === "question" ? [[verb[0].toUpperCase()+verb.slice(1),"verb"],[s === "I" || s === "Emma" ? s : s.toLowerCase(),"subject"],[c+"?","complement"]] : [[s,"subject"],[verb,"verb"],...(mode === "negative" ? [["not","negative"]] : []),[c+".","complement"]];
    const host = document.getElementById("lab-tokens"); host.replaceChildren();
    for (const [word, role] of tokens) {
      const box = document.createElement("div"); box.className = "sentence-token"; box.dataset.role = role; box.setAttribute("role","listitem");
      const b = document.createElement("b"); b.textContent = word; const label = document.createElement("small"); label.textContent = role === "negative" ? "Negation" : role[0].toUpperCase()+role.slice(1);
      box.append(b,label);host.append(box);
    }
    const rule = s === "You" ? "You takes are even for one listener." : s === "I" ? "I takes am." : s === "Emma" ? "Emma identifies one person and takes is." : s+" takes are.";
    const explanation = mode === "question" ? "The verb moves before the subject. The complement still describes the subject; no do or does is added." : mode === "negative" ? "Not follows the verb and denies this description. It does not identify a different condition or location." : "The subject comes first, the matching verb follows, and the complement completes this description.";
    document.getElementById("lab-explanation").textContent = rule+" "+explanation;
    host.dataset.sentence = tokens.map(t=>t[0]).join(" ");host.dataset.mode = mode;host.dataset.subject = s;
  }
  for (const control of [subject,meaning,form]) control.addEventListener("change",render);
  render();
  addEventListener("beforeprint",()=>document.querySelectorAll(".worked-answer").forEach(d=>{d.dataset.beforePrintOpen=String(d.open);d.open=true;}));
  addEventListener("afterprint",()=>document.querySelectorAll(".worked-answer").forEach(d=>{d.open=d.dataset.beforePrintOpen==="true";}));
})();

"use strict";
(() => {
  const control = document.getElementById("parity");
  if (!control) return;
  const result = document.getElementById("parity-result");
  const masses = document.getElementById("parity-masses");
  const percent = value => `${Number((value * 100).toFixed(3))}%`;
  function sentence(prefix, value, suffix = "") {
    const p = document.createElement("p");
    p.append(document.createTextNode(prefix));
    const number = document.createElement("span");
    number.className = "lab-metric";
    number.textContent = value;
    p.append(number, document.createTextNode(suffix));
    return p;
  }
  function render() {
    const theta = Number(control.value) / 100;
    document.getElementById("parity-value").value = theta.toFixed(2);
    result.replaceChildren(
      sentence("Each one-event has probability ", "50%", "."),
      sentence("Each pairwise both-one event has probability ", "25%", "."),
      sentence("All three are one with probability ", percent((1 - theta) / 8), ". The product of the three marginals is 12.5%."),
      sentence("Mutual independence: ", theta === 0 ? "yes" : "no", ". All pairs remain independent.")
    );
    result.dataset.theta = String(theta);
    result.dataset.mutual = String(theta === 0);
    masses.replaceChildren();
    for (let i = 0; i < 8; i++) {
      const bits = i.toString(2).padStart(3, "0");
      const parity = [...bits].reduce((sum, bit) => sum + Number(bit), 0) % 2;
      const mass = (1 + theta * (parity ? -1 : 1)) / 8;
      const row = document.createElement("tr");
      row.dataset.mass = String(mass);
      const outcome = document.createElement("td");
      outcome.textContent = bits;
      const value = document.createElement("td");
      value.textContent = percent(mass);
      const graphic = document.createElement("td");
      const track = document.createElement("div");
      track.className = "mass-track";
      track.setAttribute("aria-label", `${bits}: ${percent(mass)} of total probability`);
      const bar = document.createElement("span");
      bar.style.width = `${mass * 100}%`;
      track.append(bar);
      graphic.append(track);
      row.append(outcome, value, graphic);
      masses.append(row);
    }
  }
  control.addEventListener("input", render);
  render();
})();

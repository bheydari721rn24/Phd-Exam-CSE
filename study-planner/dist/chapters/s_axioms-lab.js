/* Exact four-atom probability model; no simulated observations. */
"use strict";
(() => {
  const controls = ["pa", "pb", "pq"].map(id => document.getElementById(id));
  const result = document.getElementById("lab-result");
  const regions = document.getElementById("lab-regions");
  function line(text, className) {
    const p = document.createElement("p");
    p.textContent = text;
    if (className) p.className = className;
    return p;
  }
  function render() {
    const [a, b, q] = controls.map(input => Number(input.value));
    controls.forEach(input => {
      document.getElementById(input.id + "-value").textContent = input.value + "%";
    });
    const lower = Math.max(0, a + b - 100);
    const upper = Math.min(a, b);
    const labels = ["Both events", "A only", "B only", "Neither event"];
    const masses = [q, a - q, b - q, 100 - a - b + q];
    const valid = masses.every(value => value >= 0);
    result.replaceChildren(line("Admissible overlap: " + lower + "% to " + upper + "%.", "lab-math"));
    result.dataset.valid = String(valid);
    regions.replaceChildren();
    if (!valid) {
      result.append(line("No probability law matches these values.", "lab-warning"));
      masses.forEach((mass, index) => {
        if (mass < 0) result.append(line(labels[index] + " would have a negative mass of " + mass + "%."));
      });
      return;
    }
    result.append(line("Valid model: at least one = " + (a + b - q) + "%; exactly one = " + (a + b - 2 * q) + "%; neither = " + masses[3] + "%.", "lab-math"));
    masses.forEach((mass, index) => {
      const cell = document.createElement("div");
      cell.className = "lab-region";
      cell.append(line(labels[index]), line(mass + "%", "lab-math"));
      const track = document.createElement("div");
      track.className = "lab-track";
      const fill = document.createElement("div");
      fill.style.width = mass + "%";
      track.append(fill);
      cell.append(track);
      regions.append(cell);
    });
  }
  controls.forEach(input => input.addEventListener("input", render));
  render();
})();

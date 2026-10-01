"use strict";
(() => {
  const mode = document.getElementById("type-case"), aInput = document.getElementById("type-a"), bInput = document.getElementById("type-b");
  const result = document.getElementById("type-result"), stages = document.getElementById("type-stages"), explanation = document.getElementById("type-explanation");
  const modulo = (x,m) => ((x % m) + m) % m;
  function render() {
    stages.replaceChildren();
    const rawA = aInput.value, rawB = bInput.value, a = Number(rawA), b = Number(rawB);
    const fail = message => { result.dataset.valid="false"; result.dataset.value=""; result.textContent=message; explanation.textContent="No numeric result is manufactured for a rejected model input or an undefined operation."; };
    if (rawA.trim()==="" || rawB.trim()==="" || !Number.isInteger(a) || !Number.isInteger(b) || a < -2147483648 || a > 2147483647 || b < -2147483648 || b > 2147483647) { fail("Enter two integers in the declared 32-bit signed range."); return; }
    const trace = []; let value, note;
    if(mode.value === "store") {
      if(a<0 || a>255 || b<0 || b>255) { fail("This byte-storage case requires both initial values between 0 and 255."); return; }
      const sum=a+b; value=modulo(sum,256);
      trace.push(`Both unsigned char operands promote to int without changing ${a} or ${b}.`, `The int addition computes ${sum}; its possible range here is 0 through 510.`, `Storing ${sum} into an unsigned 8-bit byte gives its residue ${value} modulo 256.`);
      note="The intermediate expression is int. The reduction belongs to the destination conversion.";
      result.textContent=`Intermediate int: ${sum} · Stored unsigned char: ${value}`;
    } else if(mode.value === "compare") {
      const unsignedB=modulo(b,4294967296), unsignedA=modulo(a,4294967296); value=Number(unsignedA<unsignedB);
      trace.push(`The second input is converted from integer ${b} to unsigned int ${unsignedB}.`, `The comparison converts signed int ${a} to unsigned int ${unsignedA}.`, `Compare ${unsignedA} with ${unsignedB}; the C comparison result has type int and value ${value}.`);
      note="Both sides of this comparison use 32-bit unsigned interpretation. The comparison result is still signed int zero or one.";
      result.textContent=`int result: ${value}`;
    } else {
      if(mode.value === "guard" && b===0) {
        value=0; trace.push("The guard b != 0 is false.", "Logical AND skips its division operand.", "The defined logical result is int zero."); note="The unevaluated division does not create a divide-by-zero execution."; result.textContent="Defined guard result: 0 · Division skipped";
      } else {
        if(b===0) { fail("Rejected: integer division by zero is undefined in C17."); return; }
        if(a===-2147483648 && b===-1) { fail("Rejected: the quotient is not representable in 32-bit signed int."); return; }
        const q=Math.trunc(a/b), r=a-b*q, floor=Math.floor(a/b), pyR=a-b*floor;
        if(mode.value === "divide") {
          value=q; result.textContent=`C: quotient ${q}, remainder ${r} · Python: quotient ${floor}, remainder ${pyR}`;
          trace.push(`C truncates the exact quotient toward zero to obtain ${q}.`, `${a} = ${b} × ${q} + ${r}.`, `Python floors the quotient to ${floor}; its remainder is ${pyR}.`);
          note="The integer models are exact for this input range. A remainder's sign depends on the quotient rule.";
        } else if(mode.value === "cast") {
          value=q; result.textContent=`Cast after: ${q} · Cast before: ${a/b}`;
          trace.push(`Integer division first yields ${q}.`, `Casting the already truncated result preserves ${q}.`, `Casting an operand first requests floating division, illustrated by ${a/b}.`);
          note="The floating display uses JavaScript binary64 formatting. It illustrates the distinction, not every C floating evaluation mode.";
        } else {
          value=Number(q>2); result.textContent=`Defined guard result: ${value} · Integer quotient: ${q}`;
          trace.push("The nonzero-divisor guard is true.", `The additional INT_MIN/-1 safety check passes; integer division yields ${q}.`, `Comparing the quotient with 2 yields int ${value}.`);
          note="The laboratory checks the representable-quotient exception as well as the nonzero divisor before executing its model.";
        }
      }
    }
    result.dataset.valid="true"; result.dataset.value=String(value);
    for(const text of trace) { const li=document.createElement("li"); li.textContent=text; stages.append(li); }
    explanation.textContent=note;
  }
  for(const input of [mode,aInput,bInput]) input.addEventListener("input",render);
  render();
})();

// =========================================================
// TERMINAL TYPING ANIMATION — the hero's signature element
// Simulates a real tutoring exchange, looping.
// =========================================================

const script = [
  { type: "prompt", text: "you: two-sum but I keep hitting O(n^2)..." },
  { type: "ai", text: "ai:  What are you doing every time you check\n     for a pair — are you scanning the array again?" },
  { type: "prompt", text: "you: yeah, nested loop" },
  { type: "ai", text: "ai:  Right. What if you remembered what you've\n     already seen instead of rescanning it?" },
  { type: "prompt", text: "you: ...a hash map of seen values" },
  { type: "ai", text: "ai:  Now you're thinking in O(n). Try it." },
];

const terminalBody = document.getElementById("terminal-body");
const TYPE_SPEED = 22;      // ms per character
const LINE_PAUSE = 500;     // pause after each line finishes
const RESTART_PAUSE = 2200; // pause before the loop restarts

async function typeLine(lineEl, text) {
  for (let i = 0; i < text.length; i++) {
    lineEl.textContent += text[i];
    await sleep(TYPE_SPEED);
  }
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function runScript() {
  terminalBody.innerHTML = "";

  for (const entry of script) {
    const line = document.createElement("span");
    line.classList.add("t-line", entry.type === "prompt" ? "t-prompt" : "t-ai");
    terminalBody.appendChild(line);

    await typeLine(line, entry.text);
    await sleep(LINE_PAUSE);
  }

  // Blinking cursor at the end of the exchange
  const cursorLine = document.createElement("span");
  cursorLine.classList.add("t-line");
  const cursor = document.createElement("span");
  cursor.classList.add("cursor");
  cursorLine.appendChild(cursor);
  terminalBody.appendChild(cursorLine);

  await sleep(RESTART_PAUSE);
  runScript(); // loop
}

// Respect users who've asked for reduced motion — show the final
// state instantly instead of animating.
const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

if (prefersReducedMotion) {
  terminalBody.innerHTML = script
    .map(e => `<span class="t-line ${e.type === "prompt" ? "t-prompt" : "t-ai"}">${e.text}</span>`)
    .join("");
} else {
  runScript();
}

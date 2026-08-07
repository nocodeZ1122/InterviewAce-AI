def build_explanation_prompt(user_message: str):

    return f"""
The user wants an explanation.

Your role is to teach, not just answer.

Follow these rules:

- Explain the intuition before the algorithm.
- Assume the user is preparing for coding interviews.
- Use the retrieved interview notes whenever they are relevant.
- If the retrieved notes are unrelated, ignore them.
- Be technically accurate.
- Never write one giant paragraph.
- Keep explanations concise but complete.

Your response MUST follow this exact Markdown structure:

## 💡 Intuition

Explain the core idea behind the solution.

---

## ⚙️ Algorithm

Give a step-by-step explanation of the approach.

Use numbered steps.

---

## ⏱ Time & Space Complexity

- **Time:** ...
- **Space:** ...

Explain *why* these complexities occur.

---

## ⚠️ Common Mistakes

Mention common interview mistakes or edge cases.

---

## 📚 Related Pattern

Mention the underlying pattern (HashMap, Sliding Window, DFS, etc.) and briefly explain why it applies.

---

## ✅ Key Takeaway

Summarize the most important idea in 2–3 sentences.

Current user request:

{user_message}

Remember:
- Return ONLY Markdown.
- Do NOT wrap your response in JSON.
- Do NOT repeat the question unless necessary.
- Keep the response interview-oriented.
"""
def build_hint_prompt(user_message: str):

    return f"""
The user is asking for a hint.

Do NOT reveal the complete algorithm immediately.

Your job is to gradually guide the user toward discovering the solution.

Follow these rules:

- Give only ONE meaningful hint.
- Never reveal the complete implementation.
- Never provide complete code.
- Encourage the user to think.
- If the user asks for another hint later, become slightly more specific.
- Keep the tone encouraging like an interviewer.

Your response MUST follow this Markdown structure:

## 💡 Hint

Provide one useful clue.

---

## 🤔 Think About

Ask 2–3 guiding questions that help the user discover the next step.

---

## 🚫 Avoid

Mention one common mistake beginners make.

---

## ▶ Next Step

Tell the user exactly what they should think about next instead of giving the answer.

Current user request:

{user_message}

Remember:
- Return ONLY Markdown.
- Do NOT wrap your response in JSON.
- Do NOT repeat the question unless necessary.
- Keep the response interview-oriented.
"""
def build_dry_run_prompt(user_message: str):

    return f"""
The user wants a dry run.

Do NOT simply explain the algorithm.

Instead, simulate it exactly like an interviewer would.

Follow these rules:

- Explain every iteration.
- Show variable updates.
- Explain WHY values change.
- Use tables whenever appropriate.
- Never skip steps.

Your response MUST follow this Markdown structure:

## ▶ Example Input

Choose a simple representative example.

---

## 🔄 Dry Run

For every iteration show:

- Current index
- Current value
- Variables
- Data structures (HashMap, Stack, Queue, etc.)
- Decision taken

---

## 🎯 Final Output

Show the final answer.

---

## 💡 Key Observation

Mention the important pattern the user should notice from the dry run.

Current user request:

{user_message}

Remember:
- Return ONLY Markdown.
- Do NOT wrap your response in JSON.
- Do NOT repeat the question unless necessary.
- Keep the response interview-oriented.
"""
def build_review_prompt(user_message: str):

    return f"""
The user wants a code review.

Act like a Senior Software Engineer conducting an interview.

Be honest, constructive and actionable.

Follow these rules:

- Evaluate correctness.
- Evaluate complexity.
- Evaluate readability.
- Suggest improvements.
- Never insult the user.
- Explain WHY something should change.

Your response MUST follow this Markdown structure:

# 📝 Overall Review

Provide a short summary.

---

## ✅ Correctness

Explain whether the solution is correct.

---

## ⚡ Complexity

- Time Complexity
- Space Complexity

Mention whether they are optimal.

---

## 📖 Readability

Comment on naming, structure and formatting.

---

## 🚀 Improvements

Give a numbered list of improvements.

---

## ⭐ Interview Verdict

Choose ONE:

- Excellent
- Good
- Acceptable
- Needs Improvement

Explain your rating.

Current user request:

{user_message}

Remember:
- Return ONLY Markdown.
- Do NOT wrap your response in JSON.
- Do NOT repeat the question unless necessary.
- Keep the response interview-oriented.
"""
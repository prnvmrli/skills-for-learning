# Lessons: additions to upstream

Upstream's rules on lessons, assets, and reference documents apply ([TEACH.md](../upstream/TEACH.md)). Add these:

## Every lesson

- **Length:** 10–15 minutes to finish. If it runs longer, split it.
- **Diagrams** for any flow, lifecycle, layering, or relationship. Use Mermaid from `https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.min.js`, or inline SVG.
- **"Where people get this wrong":** one short section per lesson covering a common confusion, a real criticism, or a production gotcha. **Take a position** and say what you'd recommend and why; "both sides have a point" doesn't help.
- **Check versions.** For version-sensitive APIs, cite the docs for the version in the learner's lockfile or manifest.
- **When no source is reachable** (offline, blocked), say so in the lesson and label the claim *unverified*. Never present an uncited claim as fact.
- **End with:**
  1. A quiz or drill.
  2. The practice hand-off ("Now do `milestones/M3-persist-habits.md`"), unless the mode is `Practice: none`.
  3. Upstream's "ask me follow-up questions" reminder.
- **Open it** for the user: `open <file>` on macOS, `xdg-open` on Linux.

## Quizzes

Upstream's rules (equal-length options, a rotating correct position, no formatting clues) apply. Also:

- Test understanding (trade-offs, predictions, failure modes), not recall of wording.
- Include at least one question that revisits an **earlier** module, for interleaving and spacing.
- Add free-recall prompts (`<details class="recall">` with a model answer) for anything the learner must be able to produce, not just recognise.

## Starter assets

New workspaces start from the templates in [../assets/](../assets/):

- `course.css`: the shared stylesheet, with light and dark themes through CSS variables.
- `quiz.js`: a markup-driven multiple-choice quiz with instant feedback. The markup is documented in the file's header comment, and each question carries one `<p class="why">` explaining the answer.

Copy both into `<workspace>/assets/` at setup. After that, the workspace copies are the ones to extend; upstream's reuse rules apply.

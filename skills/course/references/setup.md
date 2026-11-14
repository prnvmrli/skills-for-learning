# Course setup (shared by all three entry skills)

Each entry skill runs steps 0–1, then its own **derive** step, then steps 3–5 here. Until step 3 creates the files, keep everything you learn (stack choices, sources, the scope list, the sha) as notes in the conversation.

## Step 0: Workspace

- Propose `~/learning/<slug>/` and confirm it in one line.
- If that path already holds a `MISSION.md`, ask whether to continue that course (hand over to `course`) or use a different slug.
- Create the directory, run `git init`, and write a `.gitignore` containing `practice/`.

## Step 1: Mission interview

Ask one question at a time:

1. **Why** do they want this? What changes once they can do it (a job, shipping the app, an interview, contributing to this repo)?
2. **Starting point:** what do they already know, including adjacent things? "Nothing" is a valid answer; probe it once ("ever written any code? used a terminal?").
3. **Constraints:** time per week and deadline. For build courses, also ask about platform and language preferences.
4. **Done looks like:** 2–4 observable outcomes.

Once you have the answers, **write `MISSION.md`** (upstream format plus `## Starting point`), and write a prior-knowledge learning record. If the user says "just start", infer sensible defaults, write them, and say what you assumed in one line.

## Step 2: Derive (done by the entry skill)

- `project-course`: idea → MVP features → topics → dependency graph.
- `topic-course`: topic → canonical scope → project, or none → dependency graph.
- `codebase-course`: survey → concept inventory → outside-in order.

## Step 3: Write CURRICULUM.md and RESOURCES.md

Use the [CURRICULUM.md format](formats.md#curriculummd), filling in the `Practice:` line by the rules in step 4. Requirements:

- 5–12 modules. A module is 1–3 lessons plus its practice. More than 12 means the scope is too big; cut it with the user.
- Every module has a concrete [checkpoint](formats.md#checkpoint).
- Module 1 gives a visible win within 30 minutes.
- **Coverage table:** every item from the derive step maps to a module, or is marked skipped with a reason. An unmapped row is a bug.
- **Interleave:** later modules revisit earlier concepts in new contexts.

Write `RESOURCES.md` (upstream format) with the primary sources for Modules 1–2 at minimum, plus 1–2 communities.

Show the user the module list (names plus one line each), not the whole file. Adjust it if they push back.

## Step 4: Practice location

- **Build courses:** record `Practice:` as `practice/<slug>/` or the repo path the user names. **Don't create the project.** Installing the toolchain and creating the project (`flutter create`, `npm create`, `cargo new`…) are Module 1 steps the learner does, unless the user explicitly asks you to set it up.
- **Codebase courses:** leave out the `Practice:` line, because `Codebase:` covers it. Exercises run in the repo, or in a worktree for each module (see `codebase-course`).
- **Knowledge courses:** `Practice: none`.

## Step 5: Start

1. Copy [../assets/course.css](../assets/course.css) and [../assets/quiz.js](../assets/quiz.js) into `<workspace>/assets/`.
2. Commit: `chore: start course <slug>`.
3. **Hand off to the engine.** Read [../SKILL.md](../SKILL.md), [../upstream/TEACH.md](../upstream/TEACH.md), [lessons.md](lessons.md), and [coaching.md](coaching.md) now. Then run the session loop for Module 1: lesson, then milestone file, then coaching. Don't end on "the workspace is ready".

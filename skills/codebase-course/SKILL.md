---
name: codebase-course
description: Design a multi-session course that teaches an existing codebase, covering what has been built, how it's organised, and the core concepts it rests on, with exercises against the real code. Use when the user wants to learn, properly understand, or get onboarded to a repo or project ("teach me this codebase", "onboard me to this repo", "I joined this project and want to understand it", "teach me what's done in this project"). For one quick explanation use `explain`; for why a single decision was made use `walkthrough`; to learn a topic from scratch use `topic-course`.
argument-hint: "Path to the codebase (defaults to the current repo)"
---

# Codebase Course: learn an existing project

The goal is for the learner to understand what has been built and the concepts it rests on, well enough to change it with confidence. The code is the primary source for *what* the system does. Official docs are the source for the frameworks and patterns it uses.

This skill handles setup only; then the `course` skill runs the course. It uses the shared files in [../course/](../course/SKILL.md), so the whole plugin must be installed.

## Step 1: Pin the target, workspace, mission

- **Repo:** the given path, or the current git repo by default. Note the absolute path, the branch, and `git rev-parse --short HEAD`. Every code citation in a lesson is `path:line @ <sha>`, so lessons stay accurate as the repo moves on.
- **Workspace and mission:** run [setup steps 0–1](../course/references/setup.md#step-0-workspace), with the repo name as the default slug. The workspace is never inside the repo. The usual missions are "contribute to it", "maintain it", "review it", or "explain it in an interview". The mission sets the depth: a maintainer needs build and deploy; an interviewee needs the why behind the architecture.

## Step 2: Survey (read-only)

Read in this order, and keep notes in `<workspace>/SURVEY.md`. Every note cites `path:line`.

1. The README, any docs folder, and ADRs.
2. Manifests and lockfiles: the language, frameworks, key dependencies, and their **versions**.
3. Entry points: `main`, the app bootstrap, route tables, CLI commands, jobs.
4. The directory structure: how the layers and modules are cut.
5. One end-to-end path: pick the single most important user action and trace it from the entry point to storage and back.
6. Tests: what they assert shows the intended behaviour.
7. Git history: `git log --oneline -30` and the most-changed files (`git log --format= --name-only | sort | uniq -c | sort -rn | head -20`). These are where the action and the pain are.

## Step 3: Concept inventory

Sort what you found into three layers.

| Layer | Examples |
|---|---|
| **Stack concepts:** the frameworks and libraries in use | state management library, ORM, HTTP client, DI container |
| **Architecture:** how this codebase is organised | layering, module boundaries, data flow, error strategy, config/env handling |
| **Domain:** what the product actually models | the core entities, their invariants, the business rules |

Ask which stack concepts the user already knows (offer the list for them to tick). Record those as prior-knowledge learning records and skip those modules.

## Step 4: Order outside-in

1. **Run it.** Build, run, and use the main feature, then run the tests.
2. **The big picture.** The layer diagram and the one end-to-end trace from step 2.5.
3. **One module per layer**, following the trace's order (UI → state → domain → data → infrastructure, or whatever this repo uses). Teach a stack concept just before the layer that uses it.
4. **Cross-cutting concerns:** errors, logging, auth, config, concurrency.
5. **Change it.** Build, test, CI, release. The capstone is one real, small change made end to end.

Then run [setup steps 3–5](../course/references/setup.md#step-3-write-curriculummd-and-resourcesmd). Set the CURRICULUM header to `Mode: codebase` and `Codebase: <path> @ <branch> <sha>`. Coverage rows are every top-level directory plus every inventory item. `RESOURCES.md` lists the repo at the pinned sha as the primary source, plus the official docs for each stack concept at the lockfile's versions.

## Lessons in codebase mode

On top of the [lesson additions](../course/references/lessons.md):

- Quote real code, trimmed to 5–15 lines, with `path:line @ sha`. Add an editor link when `NOTES.md` sets a link style (for example `vscode://file/...`).
- Teach the general concept first, then show "in this codebase, it looks like…". This order transfers to other codebases; the reverse doesn't.
- Draw diagrams from the actual imports and calls, not from what the folder names suggest.
- Label every claim **verified** (read in code, run, or cited from docs) or **inferred** (likely, but not traced).

## Exercises

Each module's milestone file (`milestones/M{N}-*.md`, [format](../course/references/formats.md#milestone-files)) holds 2–4 exercises, ordered easy to hard. Keep the expected answers out of the file.

| Type | Example | Checked by |
|---|---|---|
| **Predict, then run** | "What does `getUser` return for a deleted user? Write it down, then run the test." | Running it |
| **Trace** | "Starting from the Login button, list every file the request passes through." | Comparing with your trace |
| **Locate** | "Where is the retry policy defined? How did you find it?" | The file path, plus their search method |
| **Explain back** | "Explain in 3 sentences why the cache sits below the repository." | Coaching feedback |
| **Modify** | "Add a field to the profile model, all the way to the UI." | Tests plus your review |

**Where exercises run:**

- **Read-only exercises** (run, predict, trace, locate, explain back) use the user's main checkout, which already has its `.env`, dependencies, and generated code. Before running anything, check that HEAD still equals the pin; if it doesn't, see the session loop's drift check.
- **Modify exercises** use a worktree for each module, never the user's working branch: `git -C <repo> worktree add ../<repo>-learn-m<N> -b learn/m<N> <pinned-sha>`. Copy in any ignored files it needs to build (ask before copying secrets such as `.env`). Write its path in the milestone file's "Work in" line. When the checkpoint passes, offer to remove it: `git -C <repo> worktree remove ../<repo>-learn-m<N>`, then `git -C <repo> branch -D learn/m<N>`.
- **The capstone** ("Change it") is a real change. It branches from the current HEAD, follows the repo's normal contribution flow, and is kept.

## Handing off to the sibling skills

- If the user asks *why* a design is the way it is (one decision, one PR), suggest the `walkthrough` skill. Its output goes into this workspace, and the lesson links to it.
- For a quick structured explanation mid-lesson, answer inline in the `explain` format.

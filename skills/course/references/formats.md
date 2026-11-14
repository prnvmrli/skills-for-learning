# Formats: extensions to upstream

The upstream formats apply unchanged: [MISSION](../upstream/MISSION-FORMAT.md), [RESOURCES](../upstream/RESOURCES-FORMAT.md), [LEARNING-RECORD](../upstream/LEARNING-RECORD-FORMAT.md), and [GLOSSARY](../upstream/GLOSSARY-FORMAT.md). This file adds what courses need on top of them.

## MISSION.md addition

Add a `## Starting point` section after `## Why`. Write down what the user already knows, in their words. "Nothing yet" is fine.

## CURRICULUM.md

```md
# Curriculum: {title}

- **Mode:** project-idea | topic | codebase
- **Practice:** practice/{slug}/ | {/abs/path/to/user/repo} | none   <!-- omitted in codebase mode -->

- **Codebase:** {/abs/path} @ {branch} {sha}   <!-- codebase mode only -->
- **Scope source:** {link to the docs TOC/spec coverage is checked against}   <!-- topic mode only -->

## Modules

- [ ] **M1: {name}**: {one-line outcome}
  - Concepts: {…}
  - Depends on: none
  - Checkpoint: {the concrete result, see "Checkpoint" below}
  - Lessons: {filled in as they're written}
  - Milestone: milestones/M1-{slug}.md   <!-- created when the module starts -->
- [ ] **M2: {name}**: …
  - Depends on: M1

## Coverage

| Feature / scope item / directory | Module(s) |
|---|---|
| {item} | M2, M5 |
| {item} | skipped: {reason} |
```

Rules:

- Every coverage row maps to a module, or is marked skipped with a reason.
- Tick a module only when its checkpoint passes.
- Add new modules (remedial or follow-up) at the end, under a heading that says why.

## Milestone files

These live in the **workspace**, at `milestones/M{N}-{slug}.md`, and are never written into the practice project. Create one when its module starts, so it can adapt to the learning records.

```md
# M{N}: {name}

> **Goal:** {one sentence}
> **Lesson:** [{NNNN-slug}](../lessons/NNNN-slug.html)
> **Work in:** {practice path, or the codebase worktree path}

- [ ] **{N}.1:** {one specific change or exercise}
  - Why: {one line}
- [ ] **{N}.2:** …
- [ ] **{N}.3: Verify:** run `{command}`; you should see `{result}`.
```

- **Build projects:** each step is a single committable change. Never include the solution.
- **Codebase mode:** each step is an exercise (predict, trace, locate, explain back, modify), with the expected answer kept out of the file.
- **`Practice: none`:** no milestone file. The lesson's quiz and drills are the practice.

## Checkpoint

There is one definition, and every other file refers to it. A module's checkpoint passes when **both** of these are true:

1. **Evidence of the skill:**
   - Build project: the milestone's verify step works on the learner's machine.
   - Codebase: the module's hardest exercise is done.
   - `Practice: none`: the module's free-recall or spoken drill is answered well, without notes.
2. **Retrieval:** the learner answers 1–2 questions on the module's concepts without the lesson open.

If retrieval fails, don't tick the module. Write an open-struggle record for the concept, re-ask the question at the next session's warm-up, and tick only once it passes.

## Learning record status

This is an optional frontmatter line added to the upstream learning-record format. Spell it exactly like this, everywhere:

```md
---
status: active | open-struggle | superseded by NNNN
---
```

- `open-struggle`: the learner needed hint rung 3 or above, failed retrieval, or showed a misconception that isn't resolved yet. Upstream says not to record coverage, but struggles *are* decision-grade evidence, so record them.
- When it's resolved, write a new record and mark the old one `superseded by NNNN`.
- A record with no frontmatter counts as `active`. Upstream's spelling `Status: superseded by LR-NNNN` is also read as superseded.
- To find the open ones: `grep -l 'status: open-struggle' learning-records/*.md`.

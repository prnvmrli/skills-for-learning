---
name: course
description: Continue and coach a multi-session course in a teaching workspace (a directory with a MISSION.md), whether it was created by `project-course`, `topic-course`, `codebase-course`, or an earlier /teach. Runs the session loop (recall warm-up, next lesson, practice hand-off, progress tracking), coaches the learner through milestones and exercises with hints and code feedback without giving away answers, and wraps up finished courses. Use when the user runs /course, or asks to "continue the course", "next lesson", or "next step", or, while working on a course's practice, says "I'm stuck", "is this right", or shares milestone code. Does not apply to ordinary code review or debugging unrelated to a course.
argument-hint: "Optional: what to work on next"
---

# Course

The engine behind every course. It is [upstream `teach`](upstream/TEACH.md) (Matt Pocock, MIT, vendored verbatim) **plus the extensions and overrides below**. Where the two conflict, this file wins.

**Read once per session** (skip it if you've already read it in this conversation): [upstream/TEACH.md](upstream/TEACH.md). Ignore its frontmatter. Its links to `./SKILL.md` mean `TEACH.md` ([why](upstream/README.md)). Then read the reference files below as each step needs them:

- [references/formats.md](references/formats.md): our file formats (curriculum, milestones, checkpoint, record status)
- [references/lessons.md](references/lessons.md): lesson additions
- [references/coaching.md](references/coaching.md): coaching during practice
- [references/setup.md](references/setup.md): only when creating a course

## 1. Find the workspace

A **workspace** is a directory with a `MISSION.md` **plus** at least one of `CURRICULUM.md`, `lessons/`, `learning-records/`, or `RESOURCES.md`. A product repo that happens to have a `MISSION.md` doesn't count.

Try these in order, and stop at the first hit:

1. The current directory, or any parent directory, is a workspace.
2. The current directory is inside a `Practice:` or `Codebase:` path listed in `~/learning/*/CURRICULUM.md`. For a git checkout, including a learning worktree, also match its main repo, `dirname "$(git rev-parse --path-format=absolute --git-common-dir)"`, against `Codebase:`.
3. The user named a course. Match it against `~/learning/*/MISSION.md` titles.
4. The user asked to continue but nothing matched: list the `~/learning/*/MISSION.md` titles and ask which one.

| Result | Do this |
|---|---|
| Found, user wants to continue | **Session loop** (section 3) |
| Found, user is mid-practice: stuck, sharing code, "is this right" | [coaching.md](references/coaching.md) |
| None found, user wants to learn something new | Hand over: a project idea goes to `project-course`, a topic to `topic-course`, an existing codebase to `codebase-course`. Can't tell project from topic? Ask: "Do you want to build something specific, or learn the topic and let me pick the project?" |
| None found, not a learning request | This skill doesn't apply. Help normally |

## 2. Overrides to upstream

| Upstream says | Here |
|---|---|
| The workspace is the current directory | The workspace is a dedicated directory, default `~/learning/<slug>/`, found as in section 1. Never inside the project being studied |
| Only the user invokes it (`disable-model-invocation`) | Claude may invoke it for course work (see the description) |
| The next lesson is picked freely from the zone of proximal development | Pick the first unticked module in `CURRICULUM.md` whose dependencies are ticked, then the zone of proximal development within that module. If the user names something specific, teach that |
| Lessons are the only practice | A module's practice is its milestone file (a build project or codebase exercises), or quizzes and drills when `Practice: none` |
| Record status is `active` or `superseded by LR-NNNN` | Lowercase frontmatter `status:` that adds `open-struggle`, written `superseded by NNNN` (no `LR-`). Read both spellings. See [formats.md](references/formats.md#learning-record-status) |
| `NOTES.md` is a scratchpad | **`NOTES.md` preferences override everything**: upstream and every default in this skill and its references, including lesson sections, diagrams, citation style, reference docs, and the expert quiz |
| `reference/*.html` | Walkthrough documents may be `.md`. A knowledge base named in `NOTES.md` (an Obsidian vault, say) replaces `reference/` |

Everything else in upstream applies unchanged: the mission first, never trusting parametric knowledge, citations, storage strength over fluency, assets reuse, the glossary, and wisdom and communities.

## 3. Session loop

1. **Re-orient.** Read `MISSION.md`, `CURRICULUM.md`, and `NOTES.md`. Read every learning record with `status: open-struggle` plus the 5 most recent records. Read `assets/`. In codebase mode, compare `git -C <repo> rev-parse --short HEAD` with the pinned sha. If it has moved, re-check the cited lines for the current module and offer to bump the pin.
2. **Retrieval warm-up.** If at least one module is ticked, ask 2–3 recall questions on earlier modules, preferring open struggles. Do this before any new material. Skip it only in the first session.
3. **Pick the next unit** (see the overrides). Say in one line what it is and why it comes next. If no unticked modules remain, go to **Course complete** in [coaching.md](references/coaching.md#course-complete).
4. **Teach, then practise.** Write the lesson (upstream plus [lessons.md](references/lessons.md)). Then hand over the module's milestone file and switch to coaching.
5. **Record as you go.** Write learning records the moment the evidence appears; the user may leave at any time. Tick a module only when its [checkpoint](references/formats.md#checkpoint) passes.
6. **Close.** One line on what the user can now do, plus the name of the next unit.

## 4. Workspace hygiene

- **Commits:** Claude commits course files only (`docs:` / `chore:` messages). The learner commits their own practice code. Skip commits if the workspace isn't a git repo, and never run `git init` on an existing workspace without asking.
- **The practice project** is its own git repo, either under `practice/` (listed in the workspace `.gitignore`) or at a path the user names. Never write course files into it.

## 5. Legacy `/teach` workspaces

You can tell one apart because it has `MISSION.md` but no `CURRICULUM.md`. Keep working in its existing style, and replace the curriculum-based steps of the session loop like this:

- **Progress** is the curriculum list in `NOTES.md` (if there is one) plus the files in `lessons/`.
- **Warm-up:** run it whenever `lessons/` isn't empty.
- **Next unit:** the next unfinished item in the `NOTES.md` list. With no list, use upstream's zone-of-proximal-development rule. Never run **Course complete** unless the user confirms the course is done.
- **Practice:** treat it as `Practice: none`. The lesson quizzes and drills are the practice.
- **Struggles:** records without frontmatter count as `active`. Read their bodies for struggles ("missed Q3", "recheck in Lesson 7") and treat those as open. A later record that says it resolves one closes it.
- **Migration:** if `NOTES.md` holds a curriculum list, offer **once** to move it into `CURRICULUM.md`. Record the answer in `NOTES.md` ("curriculum migration: declined YYYY-MM-DD") and don't ask again. When migrating, tick only items that have both a lesson and an active record showing understanding.

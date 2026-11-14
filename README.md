# skills-for-learning

Claude Code skills for learning: three ways to start a course, one engine that runs it, and two one-shot explainers.

| Skill | What it does |
| --- | --- |
| [`project-course`](./skills/project-course/SKILL.md) | **You have a project idea and know nothing.** Designs a course in which every module builds part of *your* project. |
| [`codebase-course`](./skills/codebase-course/SKILL.md) | **You have an existing codebase.** Teaches what's built, how it's organised, and the concepts underneath, with exercises on the real code. |
| [`topic-course`](./skills/topic-course/SKILL.md) | **You want to learn a topic.** Designs a project that covers it, or drills for knowledge goals such as interview prep. |
| [`course`](./skills/course/SKILL.md) | The engine. Continues any course, session after session: recall warm-up, next lesson, practice, coaching with hints instead of answers, and a wrap-up at the end. |
| [`explain`](./skills/explain/SKILL.md) | Structures a one-off explanation into **High-Level**, **Break-Down**, and **Glossary**. |
| [`walkthrough`](./skills/walkthrough/SKILL.md) | Writes a document that re-creates the experience of making one design decision, and ends in a graded verdict. |

```
project-course ─┐
topic-course ───┼─► set up a workspace ─► course (every later session)
codebase-course ┘
```

The three course skills depend on the shared files in `skills/course/`, so install the whole plugin rather than individual skills.

## Install

Inside Claude Code:

```
/plugin marketplace add iannbing/skills-for-learning
/plugin install skills-for-learning@skills-for-learning
```

The skills are then available as `/skills-for-learning:<skill>`, for example `/skills-for-learning:project-course`. Claude also invokes them on its own when a request matches.

For local development: `claude --plugin-dir ./skills-for-learning`. Before committing, run `python3 scripts/check_skills.py`. It checks frontmatter, code fences, non-breaking spaces, relative links and anchors, and the plugin JSON.

## Courses

```
/skills-for-learning:project-course a habit-tracker app, I know nothing
/skills-for-learning:topic-course Riverpod, I'm intermediate in Flutter
/skills-for-learning:topic-course TLS and certificate pinning, for interviews
/skills-for-learning:codebase-course ~/code/my-app
/skills-for-learning:course                  # every session after the first
```

Each course lives in a dedicated workspace (default `~/learning/<slug>/`), kept outside the project you're studying. `course` finds it from any subfolder, and from inside the practice project or the codebase.

| Path | Holds |
| --- | --- |
| `MISSION.md` | Why you're learning. Every lesson traces back to it |
| `CURRICULUM.md` | Every module, in dependency order, with a coverage table and progress checkboxes |
| `RESOURCES.md` | Vetted sources. Lessons cite these instead of the model's memory |
| `lessons/*.html` | Short, interactive, cited lessons with quizzes |
| `milestones/M*.md` | Each module's practice steps or code exercises, ticked as you go |
| `learning-records/*.md` | What you've shown you understand, what you struggled with, what you already knew |
| `GLOSSARY.md`, `reference/` | Canonical terms and cheat sheets |
| `practice/<project>/` | The project you build. It's its own git repo; you commit the code |

How the three course skills work:

- **`project-course`: project idea → course.** An interview pins down the mission. The idea is cut to an MVP feature list (you confirm it), turned into the concepts each feature needs, and ordered by dependency. You create the project yourself in Module 1.
- **`topic-course`: topic → project or drills.** The scope comes from the topic's official docs or spec and is cut to your mission. Skill goals get a project; knowledge goals get recall and spoken drills.
- **`codebase-course`: codebase → course.** It pins the commit, surveys the repo read-only, and sorts what it finds into stack, architecture, and domain concepts. It teaches outside-in, and exercises run in a git worktree for each module, at the pinned commit.

A module is only ticked once you pass its checkpoint: a working result, plus recall questions answered without the lesson open. When every module is ticked, you get an expert quiz and a follow-up offer that targets whatever you still struggle with.

### Relationship to `/teach`

`course` is built on Matt Pocock's [`teach`](https://github.com/mattpocock/skills) skill. That skill is copied verbatim into `skills/course/upstream/`, and our overrides and extensions are layered on top. Updating to a newer upstream is a file copy plus a diff review; see `skills/course/upstream/README.md`. A standalone `/teach` can stay installed alongside this plugin: `course` continues existing `/teach` workspaces without restructuring them.

## `explain`

```
/skills-for-learning:explain how does the OAuth 2.0 authorization code flow work
```

High-Level (3–7 bullets plus an ASCII diagram) → Break-Down (components, sequences, real code) → Glossary (domain terms only; dropped if fewer than 3).

## `walkthrough`

```
/skills-for-learning:walkthrough PR #482
/skills-for-learning:walkthrough why we moved from Redux to Zustand
```

Writes `<repo>/personal/walkthrough-<slug>.md`, kept out of git via `info/exclude`. If a `codebase-course` exists for the repo, it goes into that workspace instead. Order: Opening → Name the Problems → Consider the Alternatives → design parts → Takeaways → **Final Verdict** (A+ to F).

## License

MIT; see [LICENSE](./LICENSE). `skills/course/upstream/` is from [mattpocock/skills](https://github.com/mattpocock/skills) (MIT).

## Contributing

Issues and PRs welcome at <https://github.com/iannbing/skills-for-learning>.

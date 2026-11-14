---
name: topic-course
description: Design a multi-session course on a topic the user wants to learn (a technology, framework, language, protocol, or concept), with coverage checked against the topic's real scope. Usually it designs a hands-on project in which every in-scope part shows up. For knowledge-heavy goals, such as interview prep or understanding a protocol, it can instead use drills with no project. Use when the user names something to learn without a specific thing to build ("teach me Riverpod", "I want to learn Kubernetes", "course on event sourcing", "teach me TLS for interviews"). If they also name a specific project to build, use `project-course`; for an existing codebase, use `codebase-course`.
argument-hint: "The topic you want to learn, and your level"
---

# Topic Course: topic → project (or drills)

The topic is fixed; the practice is designed to cover it. Coverage is checked against the topic's real scope.

This skill handles setup only; then the `course` skill runs the course. It uses the shared files in [../course/](../course/SKILL.md), so the whole plugin must be installed.

## Steps

1. **Workspace and mission.** Run [setup steps 0–1](../course/references/setup.md#step-0-workspace). **Level:** if the user stated one, use it. If not, ask once. If they said "just start", assume beginner and say so.
2. **Find the canonical scope.** Use the official docs' table of contents, the spec, or a respected book's chapter list, for the version the user will use. Note it as the `Scope source`. This list is what "cover everything" means. Take the scope from a source, not from memory.
3. **Cut to the mission.** Mark each scope item as core, mission-relevant, or out of scope. Out-of-scope items go into `MISSION.md` with a one-line reason each.
4. **Choose the practice.**
   - **Skill missions** (build with it, use it at work): design a small, realistic project in which every core and mission-relevant item shows up naturally. Name it concretely ("a recipe-box CLI with search", not "a sample app"). If the topic is a framework, use that framework; if it's a concept, pick the most practical language for it. If two projects fit equally well, offer both in one line each.
   - **Knowledge missions** (interviews, explaining it, judging trade-offs): `Practice: none`. Each module's practice is free-recall and spoken drills, with small hands-on probes where they help (for example `curl -v` or `openssl s_client`).
5. **Order by dependency.** Topic X comes before Y if Y can't be understood without X. Group them into modules of 1–3 closely related scope items.
6. **Finish setup.** Run [setup steps 3–5](../course/references/setup.md#step-3-write-curriculummd-and-resourcesmd). Each coverage row is one in-scope item from step 2.

## Rules

- An in-scope item with no module is a bug. Either add a module or move the item to Out of scope with a reason.
- Never pre-build the solution.
- Every claim in every lesson is cited. The model's memory isn't a source.

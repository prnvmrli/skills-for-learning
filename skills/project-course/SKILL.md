---
name: project-course
description: Design a multi-session course around a specific project the user wants to build but doesn't yet know how to. Works backwards from the project to what must be learned, then teaches it while the user builds their own project module by module. Use when the user has a concrete thing to build ("I want to build a habit-tracker app but I know nothing", "teach me what I need to build X", "course around my idea", "learn Flutter by building a habit tracker"). When the user names both a topic and a specific project, use this skill, because the project is fixed. If they only name a topic, use `topic-course`; for an existing codebase, use `codebase-course`.
argument-hint: "The project you want to build"
---

# Project Course: idea → course

The project is fixed; the learning is worked backwards from it. Every module builds a real piece of the user's project.

This skill handles setup only; then the `course` skill runs the course. It uses the shared files in [../course/](../course/SKILL.md), so the whole plugin must be installed.

## Steps

1. **Workspace and mission.** Run [setup steps 0–1](../course/references/setup.md#step-0-workspace). Default slug: the project's name.
2. **Decompose into features.** List the features of the smallest version worth building (the MVP). Push anything else into "Later" under Out of scope in `MISSION.md`. **Confirm the MVP list with the user** before designing modules.
3. **Choose the stack.** Pick the most standard stack that fits the constraints, and justify each piece in one line. If the user has a preference, use it. Check current stable versions against official sources, and note them for `RESOURCES.md`.
4. **Derive the topics.** For each feature, list the concepts and skills it requires (for example, "save habits offline" → local persistence, data modelling, async I/O). Add the foundations the starting point lacks: the language basics, installing the toolchain, version control.
5. **Order by dependency.** Topic X comes before Y if Y can't be understood without X. Group topics into modules of 1–3 closely related topics. Where possible, order them so each module adds one visible feature to the app. Module 1 is usually "install the toolchain, create the project, run hello-world", done by the learner.
6. **Finish setup.** Run [setup steps 3–5](../course/references/setup.md#step-3-write-curriculummd-and-resourcesmd). Each coverage row is one MVP feature. `Practice:` is the user's own project, under `practice/<slug>/` or at the repo path they name.

## Rules

- Build the user's idea, not a toy version of it. If a feature is too advanced for the first version, move it to "Later". Don't substitute a different feature.
- Never pre-build the solution. The learner creates the project and writes the code.
- Every claim in every lesson is cited. The model's memory isn't a source.

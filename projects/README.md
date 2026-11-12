# projects/ — where every generated application lives

> Dinesh AI Academy · Agentic Engineering Kit

Each folder here is one application **and all of its outputs** (requirements, SPEC, ADRs, code, tests, reports),
named by you when you create it — for example `projects/acme-sop/`.

- Create one with `/create-app <project-name> <your requirement>` (or `/client-intake` then `/build`).
- Everything inside this folder is **git-ignored** and is never pushed: code, `.env`, data, reports.
  Only this README is tracked so the folder exists in a fresh clone.
- To keep a project, back it up separately or give it its own private repository.
- The project the agents are working on is the **Active project** line in the root `CLAUDE.md` (`/create-app` sets it).
- To start over, delete the project's folder — nothing else in the kit depends on it.

---
title: Development
type: index
status: active
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: Decision of Artemy 2026-11-13
parent: ../Home.md
---

# Development

Code lives in separate repositories. The vault does not copy code. Run commands are in each repository's `README.md`.

| Repository | Purpose | Status |
|---|---|---|
| [tender-firmware](https://github.com/milvalen/tender-firmware) | interface unit firmware and voice unit software | table board on `ai/table-board`, not on hardware |
| [tender-hardware](https://github.com/milvalen/tender-hardware) | parametric enclosure (build123d), wiring, BOM | enclosure rev 0.1 in `dev`, not printed |

## Branches

1. The default branch is `dev`. `main` is the release branch and is never ahead of `dev`.
2. Agents work in `ai/<area>` branches.
3. When the work is ready, the agent merges `ai/<area>` into `feature/<area>`. If `feature/<area>` does not exist, the agent makes it from `dev`. The agent pushes both branches.
4. Artemy examines the result on `feature/<area>` and accepts it.
5. After acceptance, the agent merges `feature/<area>` into `dev` when Artemy tells it to.

[Parent](../Home.md)

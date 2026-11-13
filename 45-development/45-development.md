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
| [tender-firmware](https://github.com/milvalen/tender-firmware) | interface unit firmware; the phone voice link (stage 1) | `dev` `d5a8b01` (2026-11-13): table board, simulator, quiet floor `MUTED`, board self-test, `PAY` stage, shift log, `CHECK MAINS` hint; not run on hardware |
| [tender-hardware](https://github.com/milvalen/tender-hardware) | parametric enclosure (build123d), wiring, BOM | `dev` `23b3785` (2026-11-13): enclosure rev 0.4, the print package and the tolerance coupons; not printed |

## Branches

1. The default branch is `dev`. `main` is the release branch and is never ahead of `dev`.
2. Agents work in `ai/<area>` branches.
3. When the work is ready, the agent merges `ai/<area>` into `feature/<area>`. If `feature/<area>` does not exist, the agent makes it from `dev`. The agent pushes both branches.
4. Artemy examines the result on `feature/<area>` and accepts it.
5. After acceptance, the agent merges `feature/<area>` into `dev` when Artemy tells it to.
6. The vault describes the state of `dev`. Before the merge into `dev`, work is only a Home task to review it, with the branch and commit. See the [decision log](../70-decisions/70-decisions.md#2026-11-13-the-vault-records-the-state-of-dev).
7. Nobody merges `dev` into `main` without an explicit command from Artemy after a careful review of `dev`.
8. Exception to steps 3 to 5: changes to working rules only (`CLAUDE.md`, branch and process rules) go straight into `dev`, without a `feature/<area>` review. See the [decision log](../70-decisions/70-decisions.md#2026-11-13-working-rule-changes-go-straight-into-dev).

[Parent](../Home.md)

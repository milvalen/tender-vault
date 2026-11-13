---
title: Project dashboard
type: index
status: active
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: Conversation of Artemy with Claude 2026-11-13
parent: README.md
---

# Project dashboard

**Project:** TENDER, device TND-01 `[A]`, 2026-11-13.

**Summary:** a self-contained wearable unit on the forearm or the apron belt. The device helps a server through a shift without a phone, the internet or the restaurant POS. Details: [concept](10-concept/concept.md).

## Stage 0: prototype without soldering

- [x] **Artemy:** approve the [stage 0 shopping list](40-hardware/stage-0-bom.md). Approved 2026-11-13.
- [ ] **Artemy:** buy the boards and modules from the [stage 0 shopping list](40-hardware/stage-0-bom.md).
- [x] **Claude:** make 3 enclosure [concept sketches](10-concept/concept-sketches.md) in the [design language](10-concept/design-language.md). Done 2026-11-13.
- [ ] **Artemy:** pick a sketch direction or a mix.
- [x] **Claude:** build the first parametric enclosure in `tender-hardware` (build123d). Rev 0.1 in `dev`, 2026-11-13; see [hardware](40-hardware/40-hardware.md).
- [x] **Artemy:** review enclosure rev 0.1 and accept it into `dev`. Accepted 2026-11-13.
- [x] **Claude:** table board and timers for the stage 0 board in `tender-firmware`, branch `ai/table-board`, 2026-11-13. Builds for StickS3 and passes native tests; not run on a real board. Accepted by Artemy into `dev` after the desk test, commit `df802b7`, 2026-11-13.
- [x] **Artemy:** decide on the [UX audit](10-concept/ux-principles.md) changes. All approved 2026-11-13; applied in firmware `a3548d5` on `ai/table-board`.
- [x] **Claude:** screen simulator for the desk test, `tender-firmware` `ai/table-board` `43e4681`, 2026-11-13. See the [UX audit](10-concept/ux-principles.md#desk-test-before-the-shift).
- [x] **Artemy:** desk test in 4-key mode. Passed on run 5, 2026-11-13, after 4 rounds of changes; see the [UX audit](10-concept/ux-principles.md#simulator-check-before-artemy-plays).
- [x] **Artemy:** desk test in 2-key mode. Run 6, 2026-11-13: failed only on 5 presses in the first 30 s; after that, within the pass rule. The 4-key mode (Dual Button unit) is the stage 0 setup; the 2-key mode stays as a fallback `[Claude]`.
- [x] **Artemy:** decide on the [design review of enclosure rev 0.1](10-concept/design-review-rev-0-1.md) findings R1–R9. All approved 2026-11-13; applied in enclosure rev 0.2.
- [x] **Artemy:** review enclosure [rev 0.2](40-hardware/40-hardware.md) and accept it into `dev`. Accepted 2026-11-13, commit `e8d4bf6`.
- [x] **Claude:** enclosure rev 0.3 for the real Dual Button unit, `tender-hardware` `ai/enclosure-rev-0-3` `5c0953d`, 2026-11-13.
- [x] **Artemy:** review enclosure [rev 0.3](40-hardware/40-hardware.md#enclosure-rev-03) and accept it into `dev`. Accepted 2026-11-13, commit `5c0953d`.
- [ ] **Artemy:** after 2–3 shifts, write observations in the [field notes](30-field/30-field.md).

## Open questions

- Is it allowed to wear the device on the floor? The answer sets the form: a forearm sleeve or a hidden belt module.
- Which computer runs voice: Raspberry Pi Zero 2 WH, or a cloud request through the phone? See [device](20-device/device.md).

## Navigation

- [Inbox](00-inbox/00-inbox.md)
- [Concept and design language](10-concept/10-concept.md)
- [Device and functions](20-device/20-device.md)
- [Field notes](30-field/30-field.md)
- [Hardware](40-hardware/40-hardware.md)
- [Development](45-development/45-development.md)
- [Tools](50-tools/50-tools.md)
- [Decision log](70-decisions/70-decisions.md)
- [System](90-system/90-system.md)

[Parent](README.md)

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

- [ ] **Artemy:** approve the [stage 0 shopping list](40-hardware/stage-0-bom.md) and buy the boards after the desk test.
- [x] **Claude:** make 3 enclosure [concept sketches](10-concept/concept-sketches.md) in the [design language](10-concept/design-language.md). Done 2026-11-13.
- [ ] **Artemy:** pick a sketch direction or a mix.
- [x] **Claude:** build the first parametric enclosure in `tender-hardware` (build123d). Rev 0.1 in `dev`, 2026-11-13; see [hardware](40-hardware/40-hardware.md).
- [x] **Artemy:** review enclosure rev 0.1 and accept it into `dev`. Accepted 2026-11-13.
- [x] **Claude:** table board and timers for the stage 0 board in `tender-firmware`, branch `ai/table-board`, 2026-11-13. Builds for StickS3 and passes native tests; not run on a real board.
- [x] **Artemy:** decide on the [UX audit](10-concept/ux-principles.md) changes. All approved 2026-11-13; applied in firmware `a3548d5` on `ai/table-board`.
- [x] **Claude:** screen simulator for the desk test, `tender-firmware` `ai/table-board` `43e4681`, 2026-11-13. See the [UX audit](10-concept/ux-principles.md#desk-test-before-the-shift).
- [ ] **Artemy:** play the desk test in both key modes: `make -C ui-unit sim`, then `make -C ui-unit sim ARGS=--two-keys`.
- [x] **Artemy:** decide on the [design review of enclosure rev 0.1](10-concept/design-review-rev-0-1.md) findings R1–R9. All approved 2026-11-13; applied in enclosure rev 0.2.
- [x] **Artemy:** review enclosure [rev 0.2](40-hardware/40-hardware.md) and accept it into `dev`. Accepted 2026-11-13, commit `e8d4bf6`.
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

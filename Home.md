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

**Summary:** a self-contained wearable unit on the apron belt. The device helps a server through a shift without a phone, the internet or the restaurant POS. Details: [concept](10-concept/concept.md).

## Stage 0: prototype without soldering

- [x] **Artemy:** approve the [stage 0 shopping list](40-hardware/stage-0-bom.md). Approved 2026-11-13.
- [ ] **Artemy:** buy the boards and modules from the [stage 0 shopping list](40-hardware/stage-0-bom.md).
- [ ] **Artemy:** when the boards arrive, fill in the [measurement sheet](40-hardware/measurement-sheet.md) and give it to Claude.
- [ ] **Claude:** update the enclosure and firmware constants from the measurement sheet, then run the fit checks.
- [ ] **Artemy:** order the enclosure print with the [print order](40-hardware/print-order.md) runbook, after the package has no `-DRAFT`.
- [x] **Claude:** make 3 enclosure [concept sketches](10-concept/concept-sketches.md) in the [design language](10-concept/design-language.md). Done 2026-11-13.
- [x] **Artemy:** pick a sketch direction or a mix. Direction B `[A]` 2026-11-13; the enclosure revisions already follow it.
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
- [x] **Artemy:** review enclosure [rev 0.4](40-hardware/40-hardware.md#enclosure-rev-04) (belt clip, `TALK` key) and accept it into `dev`. Accepted 2026-11-13, commit `535f230`.
- [x] **Claude:** split the desk-test simulator into readable parts, `tender-firmware` `ai/sim-refactor` `a2ce472`, 2026-11-13. No behaviour change: the autoplay logs and the drawn screen are the same as before.
- [x] **Artemy:** review the simulator code on `ai/sim-refactor` and accept it into `dev`. Accepted 2026-11-13, commit `a2ce472`.
- [ ] **Artemy:** [vibrator desk test](40-hardware/40-hardware.md#silent-alert-desk-test-first) on an open board. Buy the Grove cable with **male** 2.54 mm pins, not female. The enclosure place for the vibrator waits for the result.
- [x] **Artemy:** review the screen label `TALK` for the blue key (was `REQ`) and accept it into `dev`. Accepted 2026-11-13, `tender-firmware` `dev` commit `72ae11a`. Not run on a real board. See [controls](20-device/controls.md).
- [x] **Claude:** change `MUTED` in `tender-firmware` to the quiet floor mode (vibration only, the screen off when idle), see the [decision log](70-decisions/70-decisions.md#2026-11-13-muted-is-the-quiet-floor-mode). Done 2026-11-13: `ai/quiet-mute` `0e5d109`, in `feature/quiet-mute` `6599ba7`. Native tests and the StickS3 build pass; not run on a real board.
- [x] **Artemy:** review `MUTED` on `feature/quiet-mute` and accept it into `dev`. Accepted 2026-11-13, merge commit `52725fd`. The first press on an off screen only turns it on.
- [x] **Claude:** vibration indicator `BZZ` in the desk-test simulator, so a `MUTED` alert can be seen. Accepted by Artemy into `tender-firmware` `dev` 2026-11-13, commit `2c4d4a5`.
- [x] **Artemy:** review the release rule in `CLAUDE.md` ("`dev` goes to `main` only after a review of `dev`; the vault follows `dev`") on `feature/release-rule` and accept it into `dev`: `tender-firmware` `68b634e`, `tender-hardware` `9ae18ad`. Accepted into `dev` 2026-11-13. See the [decision log](70-decisions/70-decisions.md#2026-11-13-the-vault-records-the-state-of-dev).
- [x] **Artemy:** review the board self-test on `tender-firmware` `feature/self-test` `1274ce3` and accept it into `dev`. Type `!` in the serial console; it checks the Dual Button pins, display rotation, vibrator GPIO and PWM, battery and USB voltage, and the reset reason. Tests pass, the firmware builds; not run on a real board. Battery current still needs a multimeter. Accepted 2026-11-13, `tender-firmware` `dev` merge commit `c9eeb51`. Not run on a real board.
- [ ] **Artemy:** after 2–3 shifts, write observations in the [field notes](30-field/30-field.md).

## Open questions

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

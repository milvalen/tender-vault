---
title: Decision log
type: record
status: active
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: Conversation of Artemy with Claude 2026-11-13
parent: ../Home.md
---

# Decision log

Add a new decision at the top with the [template](../90-system/templates/decision.md).

## 2026-11-13. The vault records the state of dev

**Decision:** vault pages describe what is in the `dev` branch of `tender-firmware` and `tender-hardware`, not in `ai/<area>` or `feature/<area>` branches `[A]`. Work on `ai/<area>` or `feature/<area>` appears only as a Home task to review it, with the branch and commit. `dev` goes to `main` only after a careful review of `dev` and an explicit command from Artemy `[A]`.

**Rejected:** record the result of an agent branch before acceptance. The pages then describe code that is not accepted.

**Consequence:** the vault agent updates topic notes after the merge into `dev`. See [branches](../45-development/45-development.md#branches). Older dated entries with `ai/<area>` branches stay as history.

## 2026-11-13. MUTED is the quiet floor mode

**Decision:** `MUTED` and the "quiet floor" mode from the inbox are one mode `[A]`. In `MUTED`, alerts come by vibration only, with no screen burst, and the screen turns off when idle. `MUTED` stays on until the next hold of `ACK`. The "mute all alerts for 10 min" behaviour is removed. `ACK` stops one alert; a high alert comes back after 3 min.

**Rejected:** keep the 10 min mute as a second mode (`SNOOZE`): one more hold meaning on a key. Keep `MUTED` as it is and drop the quiet floor idea.

**Consequence:** [controls](../20-device/controls.md#open-points) change (open point 7); the firmware must change. After 2–3 shifts, write in the [field notes](../30-field/30-field.md) if a full stop of all alerts was needed.

## 2026-11-13. Vault follows dev; main after review

**Decision:** the vault records the state of the `dev` branches of the code repositories `[A]`. `dev` goes to `main` only after Artemy carefully examines `dev` `[A]`. See [branches](../45-development/45-development.md#branches).

## 2026-11-13. Feature branches for review

**Decision:** agents merge each `ai/<area>` branch into a `feature/<area>` branch. Artemy examines and accepts the work there. After acceptance, the agent merges `feature/<area>` into `dev` when Artemy tells it to `[A]`. This replaces the direct merge of `ai/<area>` into `dev`. See [branches](../45-development/45-development.md#branches).

## 2026-11-13. Vibrator: desk test before an enclosure place

**Decision:** test the Unit Vibrator on an open board before the enclosure gets a place for it `[A]`. See [silent alert: desk test first](../40-hardware/40-hardware.md#silent-alert-desk-test-first).

**Rejected for now:** a third bay below the Dual Button unit (shell about 78 × 90 × 31 mm `[?]`) and a separate belt module with a cable. The decision comes after the test.

## 2026-11-13. Belt clip and final key names

**Decision:** the enclosure hangs on the belt with a spring clip, as a hand-held radio does, and comes off at any time `[A]`. The engravings name the keys of the final version with voice: the REQUEST key becomes `TALK` (hold and speak) `[A]`. There is no separate talk button. See [enclosure rev 0.4](../40-hardware/40-hardware.md#enclosure-rev-04).

## 2026-11-13. Stage 0 shopping list

**Decision:** stage 0 uses the M5Stack StickS3 with the Dual Button unit, a short Grove cable and enclosure rev 0.3 `[A]`. The StopWatch Dev Kit is removed. The vibration module is recommended, not required. See the [shopping list](../40-hardware/stage-0-bom.md).

## 2026-11-13. Desk test run 4 changes

**Decision:** STEP closes an open guest request, and its label reads `DONE`; REQUEST only opens a request `[A]`. This replaces "a second press of REQUEST closes an open request" from the control scheme decision below. The undo hint moves to the status line. STEP keeps the snooze of an open request. Findings D14 to D17 in the [UX audit](../10-concept/ux-principles.md#simulator-check-before-artemy-plays).

## 2026-11-13. Desk test run 3 changes

**Decision:** the label of the key that ends an alert is orange; the STEP key shows `HOLD: UNDO` for 5 s after each STEP; the simulator ends an alert only with the matching action `[A]`. Findings D9, D10, D12 in the [UX audit](../10-concept/ux-principles.md#simulator-check-before-artemy-plays).

## 2026-11-13. Desk test changes: table strip, no dessert stage

**Decision:** after the first desk test runs `[A]`:

- tables are chosen on a fixed strip in number order (finding D5);
- the dessert stage is removed, and the STEP key label names the next stage (finding D6);
- ACK removes the dessert hint;
- the simulator counts extra presses apart from wrong-table actions (finding D7).

**Consequence:** the [controls](../20-device/controls.md) page and the firmware on `ai/table-board` changed. The desk test runs again.

## 2026-11-13. Design review changes

**Decision:** apply all changes R1–R9 of the [design review of enclosure rev 0.1](../10-concept/design-review-rev-0-1.md) `[A]`. One enclosure part for each firmware key, key functions engraved and shown on screen (`STEP`, `NEXT`, `ACK`, `REQ`), no visor, no fixed battery marking, no orange part on the enclosure. The screen uses black, white, the accent and grey for secondary text.

**Consequence:** enclosure rev 0.2 on `ai/enclosure-rev-0-2`, screen labels changed on `ai/table-board`, the [design language](../10-concept/design-language.md) changed.

## 2026-11-13. UX audit changes

**Decision:** apply all changes of the [UX audit](../10-concept/ux-principles.md) `[A]`. One function per key, 2 alert levels, one alert burst instead of endless flashing, action text on screen, confirmation after every press, stable list order, house seat numbering.

**Consequence:** the [controls](../20-device/controls.md) page and the firmware on `ai/table-board` changed. A desk test runs before the boards are bought.

## 2026-11-13. Orders by seat and pickup

**Decision:** the device records orders by table and seat. At the pass, the server says the menu item and the device shows the table and the seat. STEP marks the item as served `[A]`. Details: [orders by seat and pickup](../20-device/orders-and-pickup.md).

**Consequence:** the voice unit (stage 1) becomes the main input for orders. Stage 0 keeps only the table board and timers.

## 2026-11-13. Control scheme and thresholds

**Decision:** a second press of REQUEST closes an open request. The stage thresholds are approved: `SEAT` 3 min, `MAIN` 15 min, `BILL` 3 min, request 2 min `[A]`. Details: [controls](../20-device/controls.md).

**Rejected:** closing a request with ACK, because ACK only snoozes signals.

## 2026-11-13. Documentation in English

**Decision:** all documentation, including the vault, is written in English under ASD-STE100 `[A]`.

**Consequence:** the vault notes were translated from Russian. Russian stays only as product content: on-screen labels, menu items, speech phrases.

## 2026-11-13. Name TENDER

**Decision:** the project is TENDER, the device is TND-01, the subtitle is FIELD SERVICE UNIT `[A]`.

**Rejected:** names that reference other companies' games and brands.

## 2026-11-13. Own design language

**Decision:** the look follows the [Ink Industrial design language](../10-concept/design-language.md). Public files do not reference other companies' games, brands or artists `[A]`.

## 2026-11-13. Public repositories

**Decision:** `tender-vault`, `tender-firmware` and `tender-hardware` are public `[A]`.

**Consequence:** personal income, tips, the restaurant name and people's names are stored only in `_private/`.

## 2026-11-13. Stage 0 without soldering or a printer

**Decision:** stage 0 uses ready-made boards with snap-in connectors. An on-demand service prints the enclosure `[A]`.

[Parent](../Home.md)

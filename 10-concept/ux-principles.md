---
title: UX principles and audit
type: standard
status: active
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: Web research [Claude] 2026-11-13 — Apple HIG for watchOS and notifications (developer.apple.com); Dieter Rams, ten principles of good design (rams-foundation.org, ixdf.org); calm technology, Weiser, Brown and Case (calmtech.com); ICU alarm fatigue studies (JMIR 2026, MDPI MTI 3(1):15, UCI 2016, TU Delft 2025); hidden gesture discoverability (AAU thesis, uxdesign.cc); server seat numbering (realservertraining.com, NCRLA ProStart guide, restaurant-hospitality.com)
parent: 10-concept.md
---

# UX principles and audit

Request of Artemy 2026-11-13: check that the device is easy to use before more code is written. This page lists the principles from research and an audit of the current design against them.

Limit: most sources are design commentary and small studies. No test with real servers was done yet `[Claude]`.

## Principles

| # | Principle | Source | Rule for TND-01 |
|---|---|---|---|
| P1 | Glance, then act | Apple HIG, watchOS | The screen gives one fact and one action, readable in about 2 s. Interactions last seconds |
| P2 | Say what to do, not the state | Apple HIG, notifications: short titles | Show "BRING CHECK", not `BILL T+04` |
| P3 | Recognition over recall | HCI research on hidden gestures | One function per key. No double-press. Long press only for rare, reversible actions. Show key labels on screen |
| P4 | Feedback for every press | Gesture design practice | Each press gives an immediate, visible confirmation of what changed |
| P5 | Forgiving | Rams: honest, understandable | Every action can be undone in one move |
| P6 | Few, ranked, actionable alerts | ICU alarm fatigue studies | 2 alert levels. Signal only when an action is needed. One alert at a time. No endless flashing |
| P7 | Calm by default | Calm technology (Weiser, Brown, Case) | The device stays in peripheral attention. It communicates without demanding focus |
| P8 | As little design as possible | Rams: "less, but better" | Remove all screen elements that do not lead to an action |
| P9 | Stable places | Spatial memory; mode errors | Items do not jump while the server reads or acts |
| P10 | House standard for seats | Server training material | Seat 1 is the seat with its back to the house pivot point, then clockwise |

## Audit of the current design

Design state on 2026-11-13: [controls](../20-device/controls.md), firmware `ai/table-board` commit `495d6c0`.

Artemy approved all changes `[A]` 2026-11-13. Status column: where each change is now.

| # | Finding | Principle | Severity | Change | Status |
|---|---|---|---|---|---|
| A1 | Stage 0 firmware maps 6 actions to 2 buttons with single, double and long presses. The server must remember a hidden table of gestures. Single press also waits about 0.3 s for a possible double press | P3 | high | Single and long press only. Show the label of each button on screen. Buy a snap-in key unit for stage 0 if the 2-button version fails a desk test | done in firmware `a3548d5`: single and long press only, key labels on screen; Dual Button unit added to the [stage 0 list](../40-hardware/stage-0-bom.md) |
| A2 | The screen flashes for as long as any table is due. This is an endless alarm | P6, P7 | high | One alert burst, then a steady accent marker. Repeat after the snooze only | done in firmware `a3548d5` |
| A3 | All due tables alert in the same way. "Offer dessert" (low) and "guest waits for the check" (high) look the same | P6 | high | 2 levels. High: request, `SEAT` (order not taken), `BILL`. Low: `MAIN` (dessert): accent marker on the list, no flash, no vibration | done in firmware `a3548d5` and [controls](../20-device/controls.md#alerts) |
| A4 | The main line shows a stage code and minutes (`TBL-07 T+12`, `MAIN`). The server must translate the code into an action | P1, P2 | medium | Main line: table and action: `TBL-07 OFFER DESSERT`. Minutes become secondary | done in firmware `a3548d5` and [controls](../20-device/controls.md#screen) |
| A5 | When an alert starts, the selection stays on another table. STEP then acts on the wrong table | P1, P9 | high | On a high alert, select the alerting table. The key labels name it | done in firmware `a3548d5` |
| A6 | The list re-sorts every second. The selected table and the rows below it can move while the server reads | P9 | medium | Re-sort only on a key press or when the screen wakes. Selection stays on its table | done in firmware `a3548d5` |
| A7 | A press gives no confirmation. The change is visible only in the stage code | P4 | medium | Show "TBL-07 → ORDER TAKEN" for 1 s after STEP, and "UNDONE" after undo | done in firmware `a3548d5` |
| A8 | The header always shows `LOAD 3/4` and `UNIT TND-01` | P8 | low | Show the battery only below 25 %. Keep the unit marking on the enclosure only | done in firmware `a3548d5` |
| A9 | ACK, REQUEST and MUTE all exist. The server must choose between 3 "not now" style actions | P3, P8 | medium | Keep REQUEST and ACK. Move MUTE to a long press of ACK (already planned). Do not add more modes | done: MUTE is a long press of ACK |
| A10 | The seat numbering example "seat 1 at the window" is a guess | P10 | low | Use the house pivot point: seat 1 has its back to it, then clockwise. Ask the restaurant for its rule | done in [orders and pickup](../20-device/orders-and-pickup.md#seat-numbering); restaurant rule still unknown |
| A11 | Stage 0 board has no vibration motor. A screen flash is not seen when the device is on the belt | P6, P7 | high | Add a snap-in vibration module in the lower bay `[?]`, or move the screen signal to an always-visible place | open: firmware has `kVibroPin`; module not chosen |

## Desk test before the shift

Run before the boards are bought, so the controls can still change.

1. Build a screen simulator that runs the same table board core on a computer.
2. Write a 10 min shift script: 6 tables, 2 requests, 1 check, 1 undo.
3. Artemy plays the script with keyboard keys that map to the device keys, without a briefing.
4. Count: wrong-table actions, missed alerts, questions "what does this key do".
5. Pass: 0 wrong-table actions, 0 missed high alerts, no more than 1 question.

[Parent](10-concept.md)

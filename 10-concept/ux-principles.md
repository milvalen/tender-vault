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
| A11 | Stage 0 board has no vibration motor. A screen flash is not seen when the device is on the belt | P6, P7 | high | Add a snap-in vibration module in the lower bay `[?]`, or move the screen signal to an always-visible place | open: candidate module Unit Vibrator (U059) `[A]`; firmware has `kVibroPin` and a PWM limit (`dev` `29ffb53`); waits for the [vibrator desk test](../40-hardware/40-hardware.md#silent-alert-desk-test-first) |

## Desk test before the shift

Run before the boards are bought, so the controls can still change.

1. Build a screen simulator that runs the same table board core on a computer. Done `[Claude]` 2026-11-13: `tender-firmware` branch `ai/table-board`, `ui-unit/sim/`. The device and the simulator share the interface code (`app.h`), so the simulator shows the real screen. The terminal cannot vibrate: since 2026-11-13 the simulator shows `BZZ` in orange under the screen while the vibration motor runs, also in `MUTED` (firmware `dev` `2c4d4a5`) `[Claude]`.
2. Write a shift script. Done: 32 min of shift time on 8 tables, 7 parties, 3 guest requests, 3 order reminders, 1 kitchen mix-up that needs UNDO, 1 slow payment. At speed x4 it takes 8 min.
3. Artemy plays the script with keyboard keys that map to the device keys, without a briefing: `make -C ui-unit sim` (4 keys) and `make -C ui-unit sim ARGS=--two-keys` (2 keys). The `?` key records a question. Each run writes a log.
4. Count: wrong-table actions, missed alerts, questions "what does this key do".
5. Pass: 0 wrong-table actions, 0 missed high alerts, no more than 1 question.

### Simulator check before Artemy plays

A scripted good player passes in both key modes. A scripted sloppy player (acts late, on the selected table only) fails with 15 wrong-table actions and 4 missed alerts. So the score can tell a pass from a fail `[Claude]`.

Findings of the scripted run `[Claude]`:

| # | Finding | Principle | Status |
|---|---|---|---|
| D1 | 2-key mode: an overdue request turned hold B into ACK. The request could not be closed and alerted every 3 min | P3, P6 | fixed in firmware `43e4681`: hold B closes an open request first, label `HOLD B: DONE` |
| D2 | No stage for "check brought". `BILL` alerts while the guests pay | P6 | done: stage `PAY` (check brought, no timer), firmware `dev` `7d8b0bd`; one more STEP for each table |
| D3 | Skipping dessert needs 2 STEP presses | P3 | done: see D6 |
| D4 | 132 of 180 presses are NEXT to reach a table | P1 | open: measure with Artemy; a direct table choice can come with voice (stage 1) |
| D5 | Desk test, Artemy, first minute: "I do not understand how to select a table" `[A]` 2026-11-13. The big number is the selected table, but nothing shows a list or a cursor. NEXT replaces the content in place, and the order is by urgency, so the next table is not predictable | P3, P9 | done in firmware `ai/table-board`: fixed table strip in number order with a box on the selected table; NEXT moves in number order. Scripted player: 82 instead of 132 move presses in 4-key mode |
| D6 | Desk test, Artemy, full shift in 4-key mode: "I got confused that we always pass through dessert" `[A]` 2026-11-13. 98 STEP presses for about 30 needed changes. 4 of 4 check requests missed. The stage cycle has a fixed `DESSERT` step, and the STEP key does not say which stage comes next, so Artemy pressed STEP around the full cycle | P2, P3, P4 | done in firmware `ai/table-board`: no dessert stage; the STEP key label names the next stage (`ORDER`, `SERVED`, `CHECK`, `CLEAR`); ACK removes the dessert hint |
| D7 | The simulator score counted 72 extra STEP presses on the correct table as wrong-table actions. Only 1 of 73 was on a table without guests. The score must count extra presses apart from wrong-table actions | — | done: the score has a separate line for extra presses |
| D8 | Desk test run 3, Artemy, 4-key mode `[A]` 2026-11-13: 34 of 35 floor events in time, 6 of 6 high alerts handled, 0 questions, 10 extra presses (before: 72). Result FAIL: 5 wrong-table presses, a full STEP circle on a table without guests | — | record |
| D9 | On a `GUEST REQUEST` alert Artemy pressed STEP 2 times, not REQ. The table went to `FREE`, and that closed the request by accident. The screen does not show which key ends the alert | P3, P4 | done in firmware `ai/table-board`: the label of the key that ends the alert is orange |
| D10 | UNDO was used 0 times. To correct a wrong STEP, Artemy pressed STEP around the full circle (4 to 5 presses). UNDO is a hidden long press with no label | P3, P5 | done in firmware `ai/table-board`: `HOLD: UNDO` on the STEP key for 5 s after each STEP |
| D11 | 232 of 292 presses moved between tables (scripted player: 79). A thumb wheel would cut this | P1 | open: decide on the wheel and the Grove port plan |
| D12 | The simulator counted a STEP on a request alert as a correct answer to the alert | — | done: REQUEST ends a request alert, STEP a stage alert, ACK and MUTE end all. Since firmware `dev` `52725fd` (2026-11-13), MUTE (quiet floor) does not end alerts |
| D13 | Desk test run 4, Artemy, 4-key mode `[A]` 2026-11-13: 32 of 37 floor events in time, 4 of 8 high alerts missed, 6 wrong-table, 19 extra presses, 3 questions. FAIL, worse than run 3 | — | record |
| D14 | Firmware bug: STEP clears the alert snooze of the table. On an overdue request, STEP starts the same alert again at once. Each of the 2 missed request alerts was counted 2 times | P6 | done: STEP keeps the snooze of an open request |
| D15 | On both request alerts Artemy pressed STEP again, with `REQ` in orange. Artemy uses the main key as "done" | P3 | done: STEP reads `DONE` and closes an open request; REQ only opens |
| D16 | After the `HOLD: UNDO` label came, Artemy pressed STEP 5 more times on TBL-03 and asked 3 questions. The label hid what the next tap does | P3, P4 | done: the key keeps the next-stage label; the status line reads `HOLD STEP = UNDO` for 5 s |
| D17 | Script: "order dessert. You serve it." made Artemy press STEP 5 times on TBL-07 to record the dessert. There is no dessert stage | — | done in the shift script |
| D18 | Desk test run 5, Artemy, 4-key mode `[A]` 2026-11-13: **PASS**. 0 wrong-table, 3 of 3 high alerts handled, 0 questions, 3 extra presses, 32 of 37 floor events in time | — | record |
| D19 | Guest requests: Artemy opened 0 of 3 requests when the guest asked (run 4: 0 of 3). A request handled at once needs no timer, so REQ may be extra work | P8 | open: check on a real shift whether REQ is used |
| D20 | A `TAKE ORDER` alert on TBL-05 moved the selection 2 s before the kitchen called TBL-02. TBL-02 then missed `SERVED`, and its check and its departure were missed too. One missed STEP leaves a table 1 stage behind, and nothing shows it | P1, P5 | open |
| D21 | The simulator counted 486 moves; a held key repeats in the terminal. On the device a held key is 1 long press | — | open: ignore key repeat in the simulator |
| D22 | Desk test run 6, Artemy, 2-key mode `[A]` 2026-11-13: FAIL by the rule, but all 5 wrong-table presses came in the first 30 s, before the first guests. Artemy pressed STEP on TBL-01 (the start selection) and went round the full circle back to `FREE`. After that: 0 wrong-table, 6 of 6 high alerts handled, 1 question, 35 of 37 floor events in time. Requests opened at the guest's ask: 1 of 3 (see D19) | P3 | record |
| D23 | 2 of 6 runs started with STEP on the start selection `TBL-01` (run 2 and run 6). The confirmation `TBL-01 GUESTS SEATED` shows the error, but the fix was the full circle, not UNDO | P5 | open: watch on a real shift |

[Parent](10-concept.md)

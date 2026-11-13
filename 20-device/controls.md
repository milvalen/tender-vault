---
title: Controls
type: plan
status: proposed
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: Conversation of Artemy with Claude 2026-11-13; concept sketch B; UX audit 2026-11-13 (all changes approved by Artemy)
parent: 20-device.md
---

# Controls

Control scheme for the table board and timers ([function 1](functions.md#1-table-board-and-timers)). The scheme uses the controls of [concept sketch B](../10-concept/concept-sketches.md#b-belt-module): a thumb wheel and 3 keys. It follows the [UX principles](../10-concept/ux-principles.md). Not tested on a shift yet.

## Screen

1. The top line shows the selected table: `TBL-07`.
2. The second line says what to do now: `BRING CHECK`. If nothing is due, it says what happened last: `ORDER TAKEN`.
3. The third line shows the minutes since the last event and a bar toward the threshold.
4. Below is the table strip: all tables by number, always in the same place, `1 2 3 [4] 5 6 7 8`. A box marks the selected table. Orange numbers need an action; an orange box is a guest who waits.
5. The bottom line shows the current meaning of each key.
6. The status line shows only what needs attention: `MUTED`, `LOW BATTERY` (below 25 %).

After every press, the second line shows a 1 s confirmation of what changed. Example: `TBL-07 ORDER TAKEN`, `TBL-07 UNDONE`. For 5 s after a STEP the status line reads `HOLD STEP = UNDO` (desk test D10, D16).

During an alert the label of the key that ends it is orange (desk test D9). For a guest request or a stage alert it is the STEP key. For the dessert hint it is `ACK`.

## Choosing a table

NEXT moves the box one table to the right on the strip; after the last table it goes back to the first. In 4-key mode a long press of NEXT moves left. On a high alert the box moves to the alerting table by itself.

The strip is in number order and does not change, so each table has a fixed place. Changed after desk test finding D5 `[A]` 2026-11-13. In the old design NEXT went through a list sorted by urgency. Artemy could not tell how to reach a table.

When the thumb wheel comes back, it moves the box in the same way.

## Keys

One function per key. A long press is used only for rare actions that can be reversed.

| Key | Press | Long press |
|---|---|---|
| **1. STEP** | Move the table to the next stage. After a pickup, mark the menu item as served ([orders and pickup](orders-and-pickup.md)) | Undo the last step |
| **2. ACK** | Stop the current alert. A high alert comes back after 3 min if the table is not served | `MUTED` (quiet floor) on or off: alerts by vibration only, no screen burst; the screen turns off when idle. In firmware `dev` `52725fd`: see open point 7 |
| **3. REQUEST** | Open a guest request (water, cutlery, napkins) with a 2 min timer. STEP closes it: while a request is open, the STEP key reads `DONE` (desk test D15). The stage does not change | Open the table menu: table map by seat, allergens, number of guests, free the table |

Each key has its own shape, so the server can find it without a look:

- STEP: convex;
- ACK: flat;
- REQUEST: ribbed.

In the final version the REQUEST key becomes `TALK`: hold it and speak. There is no separate talk button (enclosure rev 0.4).

## Alerts

Alerts have 2 levels. Only actions that a guest waits for raise an alert.

| Level | When | What the device does |
|---|---|---|
| High | order not taken (`SEAT` 3 min), check not brought (`BILL` 3 min), guest request open 2 min | 1 burst of 2 s (vibration and screen), then a steady accent marker. The table becomes the selected table, so STEP acts on it. If the table is not served, the alert comes back after 3 min |
| Low | offer dessert (`MAIN` 15 min) | Accent marker on the strip only. No burst, no vibration. ACK on the table removes it until the next STEP |

## Table stages

STEP moves a table through these stages. The STEP key label on the screen names the next stage: `SEAT`, `ORDER`, `SERVED`, `CHECK`, `BROUGHT`, `CLEAR`. There is no dessert stage: changed after desk test finding D6 `[A]` 2026-11-13. The `PAY` stage (check brought, the guests pay) has no threshold: changed after desk test finding D2 `[A]` 2026-11-13, firmware `dev` `7d8b0bd`. Thresholds are configurable. Artemy approved the values below `[A]` 2026-11-13; they are not tested on a shift yet.

| Stage | After STEP the screen says | Threshold | Action when due | Level |
|---|---|---|---|---|
| `SEAT` | GUESTS SEATED | 3 min | TAKE ORDER | high |
| `ORD` | ORDER TAKEN | not set | — | — |
| `MAIN` | MAINS SERVED | 15 min | OFFER DESSERT | low |
| `BILL` | CHECK REQUESTED | 3 min | BRING CHECK | high |
| `PAY` | CHECK BROUGHT | not set | — | — |
| `FREE` | TABLE FREE | — | — | — |

## Stage 0 key mapping

The stage 0 board (M5Stack StickS3) has 2 keys and no wheel. Firmware: `tender-firmware`, branch `dev`. The screen and the enclosure (rev 0.2 and later) name keys by function, not by colour.

The enclosure engraves the key names of the final version: the blue key is `TALK` (rev 0.4, `[A]` 2026-11-13). With voice (stage 1, through the phone), hold `TALK` and speak a request: a guest request, an order, a menu question. In stage 0 a press opens a guest request. The bottom line of the screen reads `TALK`: firmware `dev` commit `72ae11a`, accepted by Artemy 2026-11-13.

| Mode | `STEP`: key A (front) | `NEXT`: key B (top) | `ACK`: red key | `TALK`: blue key |
|---|---|---|---|---|
| 4 keys: Dual Button unit on Grove | STEP (`DONE` closes an open request), hold UNDO | NEXT table, hold previous | ACK, hold MUTE | open a REQUEST (engraved `TALK`) |
| 2 keys: StickS3 alone | STEP (`DONE` closes an open request), hold UNDO | NEXT table; hold: ACK when an alert is shown, else open a request | — | — |

The 2-key mode gives one key 3 meanings on hold. The bottom line of the screen shows the current meaning: `HOLD NEXT: DONE`, `HOLD NEXT: ACK` or `HOLD NEXT: REQ`. An open request comes first, so an overdue request can always be closed. Use the 4-key mode if the desk test shows confusion.

## Example

1. Guests sit at table 7. Select `TBL-07` with the wheel and press STEP. The screen confirms `TBL-07 GUESTS SEATED`.
2. After 3 min, the device gives one burst and selects `TBL-07`. The screen says `TAKE ORDER`. Take the order and press STEP: `TBL-07 ORDER TAKEN`.
3. A guest asks for water. Press REQUEST: `REQUEST OPEN`. If it is still open after 2 min, a high alert starts. Bring the water and press STEP, which now reads `DONE`: `REQUEST DONE`.
4. Serve the mains and press STEP. After 15 min, the list marks `OFFER DESSERT` without a burst.
5. Offer dessert and press ACK: `DESSERT OFFERED`. The marker goes. Dessert needs no STEP: the table stays in `MAIN`.
6. The guests ask for the check. Press STEP: `CHECK REQUESTED`. After 3 min without the check, a high alert starts: `BRING CHECK`.
7. Bring the check and press STEP (the key reads `BROUGHT`): `CHECK BROUGHT`. There is no alert while the guests pay.
8. After payment, press STEP (the key reads `CLEAR`): `TABLE FREE`.
## Open points

1. Check the thresholds on a real shift and record the results in the [field notes](../30-field/30-field.md).
2. Desk test: done. Artemy passed it in 4-key mode on run 5, 2026-11-13; see the [UX audit](../10-concept/ux-principles.md#simulator-check-before-artemy-plays). Open findings from the desk test stay in the audit.
3. Vibration module: the M5Stack Unit Vibrator (U059) is the candidate `[A]` 2026-11-13, see the [shopping list](../40-hardware/stage-0-bom.md#recommended-silent-alert). The firmware drives it (`kVibroPin`, PWM limit, firmware `dev` `29ffb53`). The [vibrator desk test](../40-hardware/40-hardware.md#silent-alert-desk-test-first) decides if it stays.
4. Skipping dessert: done. The dessert stage is removed and STEP goes from `MAIN` to `BILL` in 1 press (desk test D6).
5. No stage for "check brought": done. The `PAY` stage has no timer; STEP in `BILL` reads `BROUGHT` (desk test D2, firmware `dev` `7d8b0bd`, 2026-11-13). Cost: one more STEP for each table. Scripted good player on the simulator shift: 4 high alerts, 0 false (before: 5, 1 false); 136 key presses (before: 121) `[Claude]`.
6. Moving between tables costs presses. The table strip in number order cut the presses of a scripted player from 132 to 79 in 4-key mode `[Claude]`. Check again in the desk test.
7. `MUTED` is the "quiet floor" mode. Decided `[A]` 2026-11-13, see the [decision log](../70-decisions/70-decisions.md#2026-11-13-muted-is-the-quiet-floor-mode):
   - alerts come by vibration only, with no screen burst;
   - the screen turns off after 20 s without a press, the same time as the dim; the first key press only turns it on and does no action, because the server cannot see the selection; an alert vibrates but does not turn the screen on;
   - there is no "mute all alerts for 10 min"; to stop one alert, use `ACK`.

   - `MUTED` stays on until the next hold of `ACK`; it does not end after a time `[A]` 2026-11-13.

   Without a vibrator, `MUTED` hides high alerts, so the stage 0 board needs the [vibrator desk test](../40-hardware/40-hardware.md#silent-alert-desk-test-first) first. Firmware: `tender-firmware` `ai/quiet-mute` `0e5d109`, merged into `feature/quiet-mute` `6599ba7`. Accepted by Artemy into `dev`, merge commit `52725fd`, 2026-11-13. Native tests and the StickS3 build pass; not run on a real board.

[Parent](20-device.md)

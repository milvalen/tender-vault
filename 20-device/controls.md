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
4. Below are the next 2 tables in the list, each with its action or minutes.
5. The bottom line shows the current meaning of each key.
6. The status line shows only what needs attention: `MUTED`, `LOW BATTERY` (below 25 %).

After every press, the second line shows a 1 s confirmation of what changed. Example: `TBL-07 ORDER TAKEN`, `TBL-07 UNDONE`.

## Wheel and list

The wheel scrolls through the tables. The list is sorted by urgency: high alerts first, then low alerts, then tables by time left, then free tables.

The list keeps its order while the server reads it. It re-sorts only after an action, after an alert, or while the screen is dimmed.

## Keys

One function per key. A long press is used only for rare actions that can be reversed.

| Key | Press | Long press |
|---|---|---|
| **1. STEP** | Move the table to the next stage. After a pickup, mark the menu item as served ([orders and pickup](orders-and-pickup.md)) | Undo the last step |
| **2. ACK** | Stop the current alert. A high alert comes back after 3 min if the table is not served | Mute all alerts for 10 min |
| **3. REQUEST** | Open a guest request (water, cutlery, napkins) with a 2 min timer. A second press closes it. The stage does not change | Open the table menu: table map by seat, allergens, number of guests, free the table |

Each key has its own shape, so the server can find it without a look:

- STEP: convex;
- ACK: flat;
- REQUEST: ribbed.

The talk button from [concept sketch A](../10-concept/concept-sketches.md#a-forearm-bracer) sits separately on the side, under the thumb.

## Alerts

Alerts have 2 levels. Only actions that a guest waits for raise an alert.

| Level | When | What the device does |
|---|---|---|
| High | order not taken (`SEAT` 3 min), check not brought (`BILL` 3 min), guest request open 2 min | 1 burst of 2 s (vibration and screen), then a steady accent marker. The table becomes the selected table, so STEP acts on it. If the table is not served, the alert comes back after 3 min |
| Low | offer dessert (`MAIN` 15 min) | Accent marker on the list only. No burst, no vibration |

## Table stages

STEP moves a table through these stages. Thresholds are configurable. Artemy approved the values below `[A]` 2026-11-13; they are not tested on a shift yet.

| Stage | After STEP the screen says | Threshold | Action when due | Level |
|---|---|---|---|---|
| `SEAT` | GUESTS SEATED | 3 min | TAKE ORDER | high |
| `ORD` | ORDER TAKEN | not set | — | — |
| `MAIN` | MAINS SERVED | 15 min | OFFER DESSERT | low |
| `DSRT` | DESSERT SERVED | not set | — | — |
| `BILL` | CHECK REQUESTED | 3 min | BRING CHECK | high |
| `FREE` | TABLE FREE | — | — | — |

## Stage 0 key mapping

The stage 0 board (M5Stack StickS3) has 2 keys and no wheel. Firmware: `tender-firmware`, branch `ai/table-board`.

| Mode | Key A (front) | Key B (side) | Red key | Blue key |
|---|---|---|---|---|
| 4 keys: Dual Button unit on Grove | STEP, hold UNDO | NEXT table, hold previous | ACK, hold MUTE | REQUEST |
| 2 keys: StickS3 alone | STEP, hold UNDO | NEXT table; hold: close the open request, else ACK when an alert is shown, else open a request | — | — |

The 2-key mode gives one key 3 meanings on hold. The bottom line of the screen shows the current meaning: `HOLD B: DONE`, `HOLD B: ACK` or `HOLD B: REQ`. An open request comes first, so an overdue request can always be closed. Use the 4-key mode if the desk test shows confusion.

## Example

1. Guests sit at table 7. Select `TBL-07` with the wheel and press STEP. The screen confirms `TBL-07 GUESTS SEATED`.
2. After 3 min, the device gives one burst and selects `TBL-07`. The screen says `TAKE ORDER`. Take the order and press STEP: `TBL-07 ORDER TAKEN`.
3. A guest asks for water. Press REQUEST: `REQUEST OPEN`. If it is still open after 2 min, a high alert starts. Bring the water and press REQUEST again: `REQUEST DONE`.
4. Serve the mains and press STEP. After 15 min, the list marks `OFFER DESSERT` without a burst.
5. Serve the dessert and press STEP: `DESSERT SERVED`. If the guests take no dessert, skip this step.
6. The guests ask for the check. Press STEP: `CHECK REQUESTED`. After 3 min without the check, a high alert starts: `BRING CHECK`.
7. After payment, press STEP: `TABLE FREE`.
## Open points

1. Check the thresholds on a real shift and record the results in the [field notes](../30-field/30-field.md).
2. Artemy runs the desk test from the [UX audit](../10-concept/ux-principles.md#desk-test-before-the-shift). The simulator is ready.
3. Choose a vibration module for the stage 0 board `[?]`.
4. Skipping dessert: step 5 is skipped in words, but the firmware still passes through `DESSERT SERVED`. The server presses STEP twice. The simulator shows this on 5 of 7 tables `[Claude]`. Check in the desk test whether this confuses.
5. No stage for "check brought". `CHECK REQUESTED` alerts after 3 min even when the check is on the table and the guests are paying. The simulator gives this false alert on the slow-payment table `[Claude]`. Possible fix: a STEP after the check is brought, or a longer threshold.
6. Moving between tables costs presses. In the simulated shift a scripted player used 132 of 180 presses on NEXT to reach the table `[Claude]`. The order by urgency helps for alerts, but not for floor events at any table. Check in the desk test.

[Parent](20-device.md)

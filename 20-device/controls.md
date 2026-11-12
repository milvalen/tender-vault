---
title: Controls
type: plan
status: proposed
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: Conversation of Artemy with Claude 2026-11-13; based on concept sketch B
parent: 20-device.md
---

# Controls

Control scheme for the table board and timers ([function 1](functions.md#1-table-board-and-timers)). The scheme uses the controls of [concept sketch B](../10-concept/concept-sketches.md#b-belt-module): a thumb wheel and 3 keys. Not tested on a shift yet.

## Screen

The main line shows the selected table and the time since its last event. Example: `TBL-07  T+12` means table 7, 12 min since the last event.

A bar under the line fills up toward the threshold of the current stage. When the bar is full, the device vibrates and shows the table in the accent color.

## Wheel

The wheel scrolls through the tables. The list is sorted by urgency: tables with an expired or nearly expired threshold are at the top.

## Keys

| Key | Short press | Long press |
|---|---|---|
| **1. STEP** | Move the table to the next stage. The timer resets to `T+0`. After a pickup, mark the menu item as served ([orders and pickup](orders-and-pickup.md)) | Undo the last step |
| **2. ACK** | Stop the vibration and snooze the signal for 3 min | Mute all signals for 10 min |
| **3. REQUEST** | Mark a small guest request (water, cutlery, napkins) with a 2 min timer. The table stage does not change. A second press closes the open request `[A]` 2026-11-13 | Open the table menu: table map by seat, allergens, number of guests, free the table |

Each key has its own shape, so the server can find it without a look:

- STEP: convex;
- ACK: flat;
- REQUEST: ribbed.

The talk button from [concept sketch A](../10-concept/concept-sketches.md#a-forearm-bracer) sits separately on the side, under the thumb.

## Table stages

STEP moves a table through these stages. Thresholds are configurable. Artemy approved the values below `[A]` 2026-11-13; they are not tested on a shift yet.

| Stage | Meaning | Threshold | Signal |
|---|---|---|---|
| `SEAT` | guests are seated | 3 min | take the order |
| `ORD` | order taken | not set | — |
| `MAIN` | mains served | 15 min | offer dessert |
| `DSRT` | dessert served | not set | — |
| `BILL` | check requested | 3 min | bring the check |
| `FREE` | table is free | — | — |

## Example

1. Guests sit at table 7. Select `TBL-07` with the wheel and press STEP. The screen shows `SEAT T+0`.
2. After 3 min, the device vibrates. Take the order and press STEP. The stage is `ORD`.
3. A guest asks for water. Press REQUEST. If the request is not closed in 2 min, the device vibrates. Bring the water and press REQUEST again to close it.
4. Serve the mains and press STEP. The stage is `MAIN`. After 15 min, the device signals to offer dessert.
5. The guests ask for the check. Press STEP. The stage is `BILL`.
6. After payment, press STEP. The table is `FREE`.

## Open points

1. Check the thresholds on a real shift and record the results in the [field notes](../30-field/30-field.md).

[Parent](20-device.md)

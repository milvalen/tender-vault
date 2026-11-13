---
title: Orders by seat and pickup
type: plan
status: proposed
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: Request of Artemy 2026-11-13; conversation with Claude 2026-11-13
parent: 20-device.md
---

# Orders by seat and pickup

The device records who ordered what at which table. When the kitchen puts a dish on the pass, the device shows where to carry it. Requested by Artemy `[A]` 2026-11-13.

## Problem

A server writes each order by seat. When a dish appears on the pass, the server must carry it to the correct guest without asking "who has the carbonara?". The server must also know which dishes of a table are still in the kitchen.

## Seat numbering

The device follows the common house standard from server training material `[Claude]` 2026-11-13:

1. The restaurant fixes one pivot point per room, usually the kitchen door or the pass.
2. Seat 1 is the seat with its back to the pivot point.
3. The other seats follow clockwise.

House rules can differ: some restaurants count counter-clockwise or use a separate rule for booths. Ask the restaurant for its rule `[?]`. Seat numbers appear as `ST-N`.

## Flow

### 1. Take the order

1. Hold the talk button.
2. Say the table, the seat, the menu item and the modifiers. Example: "table seven, seat two, carbonara no bacon".
3. Release the button. The device records the menu item under `TBL-07 ST-2` with the status "in kitchen".

### 2. Pick up at the pass

1. At the pass, hold the talk button and say the menu item. Example: "carbonara".
2. The device shows the table and the seat: `TBL-07 ST-2`, with the modifiers.
3. If more than one open order has the same menu item, the oldest order is first. Turn the wheel to select another one.

### 3. Mark as served

1. Put the dish in front of the guest.
2. Press STEP. The device marks the menu item as served.
3. When all mains of a table are served, the table moves to stage `MAIN` and the dessert timer starts.

### 4. Table map

1. Select the table with the wheel.
2. Long-press REQUEST. The device shows the seats and their menu items: served items are struck through, items in the kitchen are highlighted.

## Limits

1. The device is not connected to the kitchen or the restaurant POS. It does not know when a dish is ready. It knows only the orders that the server dictated.
2. Comfortable order entry needs voice (stage 1, cloud recognition through the phone). In stage 0, order entry with the wheel through the menu is slow; stage 0 shows only the table board and timers.

## Related

- [Controls](controls.md): keys and table stages.
- [Functions](functions.md): function 2, voice order notebook.

[Parent](20-device.md)

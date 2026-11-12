---
title: Functions
type: plan
status: proposed
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: Conversation of Artemy with Claude 2026-11-13
parent: 20-device.md
---

# Functions

## 1. Table board and timers

Stage 0. The device shows the list of tables and the time since the last event at each table.

1. The server marks an event: "order taken", "mains served", "check requested".
2. The device starts the event timer.
3. When the timer expires, the device vibrates and highlights the table with the accent color.

Example thresholds: ask about dessert 15 min after mains; bring the check 3 min after the request. Thresholds are configurable `[?]`. Keys and stages: [controls](controls.md).

## 2. Voice order notebook

Stage 1. The server holds the button and says: "table seven, seat two, carbonara without bacon".

1. The voice unit recognizes the speech offline.
2. The parser extracts the table, the seat, the menu item and the modifiers.
3. The parser matches the item against the menu. If the item contains a guest's allergen, the device warns the server.
4. The server copies the order into the restaurant POS from the list on the screen.

## 3. Menu trainer

Stage 0 or 1. Cards: ingredients, portion weight, allergens, what to offer with the dish. A quiz mode for free minutes. The menu loads from a computer.

## 4. Shift and tip log

Stage 1. Shift start and end, number of tables, tips. Data exports to a computer. Personal figures are stored only in `_private/` and never reach public repositories.

## 5. Allergens and upsells

Stage 2. The query "gluten free" shows the matching menu items. A query for a dish shows what to offer with it.

[Parent](20-device.md)

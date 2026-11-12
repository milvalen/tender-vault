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

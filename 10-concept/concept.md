---
title: TENDER concept
type: plan
status: proposed
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: Conversation of Artemy with Claude 2026-11-13; market review of server apps [Claude] 2026-11-13
parent: 10-concept.md
---

# TENDER concept

## Name

**TENDER** `[A]`, 2026-11-13. The word has 3 meanings:

1. *to tend tables* — to serve tables.
2. *tender* — a supply vessel that supports a fleet.
3. *tender* — gentle, careful.

Device designation: **TND-01**. Subtitle: **FIELD SERVICE UNIT**.

## Problem

A server keeps tables, orders, times, guest allergies and the menu in memory. A mistake costs money and tips. The device takes over memory and time, so the server stays with the guest.

## Principles

1. **Self-contained.** The device works without a phone, the internet or the restaurant POS. It syncs with a computer only for the menu and statistics.
2. **One hand, no long look.** Input: a talk button, a rotary encoder, 3–4 keys. Output: vibration and a short look at the screen.
3. **A full shift.** The battery lasts 10–12 h.
4. **A quiet floor.** The device makes no sound. Signals are vibration only.
5. **Its own form.** The look follows the [design language](design-language.md).

## Why not an existing product

Market review `[Claude]` 2026-11-13. Limit: the review uses open sources only; server reviews in Telegram and VK were not checked.

| Product class | Examples | Why it does not fit |
|---|---|---|
| Mobile POS for servers | r_keeper Waiter, Saby Presto, iiko | The restaurant chooses it; personal functions cannot be added |
| Tip services | CloudTips, one2tips | Only take payments; no tracking or analytics |
| Tip trackers | ServerLife, Server44 | US market, no Russian language |
| Voice AI for orders | Loman and similar | Work over the phone and through the restaurant POS |

## Functions in order

Details: [functions](../20-device/functions.md).

1. Table board and timers with vibration.
2. Voice order notebook.
3. Menu trainer.
4. Shift and tip log.
5. Allergen and upsell lookup.

[Parent](10-concept.md)

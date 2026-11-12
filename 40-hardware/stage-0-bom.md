---
title: Stage 0 shopping list
type: plan
status: proposed
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: hackster.io (M5Stack StopWatch, May 2026), cnx-software.com (M5Stack StickS3, 2026-01-23), learn.pimoroni.com (Qw/ST) [Claude] 2026-11-13
parent: 40-hardware.md
---

# Stage 0 shopping list

Status `proposed`: Artemy has not approved the list yet. Prices are in US dollars from the maker's store `[Claude]` 2026-11-13. Prices in Russia with delivery were not checked.

## Required

| Item | Purpose | Price |
|---|---|---|
| M5Stack StopWatch Dev Kit | interface unit: ESP32-S3, round AMOLED, microphone, speaker, battery | about $45 |
| USB-C data cable | flashing and charging | probably at home `[?]` |

## Recommended for stage 0

| Item | Purpose | Price |
|---|---|---|
| M5Stack StickS3 | interface unit used by the firmware and enclosure rev 0.1: 2 keys, 1.14-inch screen, no vibration motor | not checked |
| M5Stack Dual Button unit | 2 more keys on the Grove port: ACK and REQUEST, one function per key ([UX audit](../10-concept/ux-principles.md)) | not checked |
| Vibration module with a Grove or Hat connector | silent alert on the belt | not chosen `[?]` |

The firmware and enclosure rev 0.1 target the StickS3, not the StopWatch kit above. Decision of 2026-11-13 by Claude when the enclosure was built `[Claude]`; confirm before the purchase.

## For voice (stage 1)

| Item | Purpose | Price |
|---|---|---|
| Raspberry Pi Zero 2 WH | voice unit; the header is already soldered | not checked |
| 2-microphone board for Raspberry Pi | speech input; plugs into the header | not checked |
| microSD card, 32 GB | system and speech model | not checked |
| Battery pack with USB output | power for the voice unit | not checked |

## Fallback

M5Stack StickS3: ESP32-S3, 1.14-inch screen, microphone, speaker, Grove connector. Use it if the StopWatch is not available.

## No soldering

Modules connect with snap-in Qwiic, STEMMA QT or Grove connectors. Stage 0 needs no soldering iron.

[Parent](40-hardware.md)

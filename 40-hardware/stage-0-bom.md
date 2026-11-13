---
title: Stage 0 shopping list
type: plan
status: active
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: docs.m5stack.com (StickS3, Unit Dual Button, Unit Vibrator), cnx-software.com (StickS3 launch price, 2026-01-23), thepihut.com, robotshop.com [Claude] 2026-11-13
parent: 40-hardware.md
---

# Stage 0 shopping list

Approved by Artemy 2026-11-13 `[A]`. The list follows the desk test: the 4-key mode (StickS3 with the Dual Button unit) passed, the 2-key mode is the fallback. See the [UX audit](../10-concept/ux-principles.md#simulator-check-before-artemy-plays).

Prices are in US dollars or pounds from shops outside Russia `[Claude]` 2026-11-13. Prices in Russia with delivery were not checked.

## Required

| Item | Purpose | Price |
|---|---|---|
| M5Stack StickS3 | interface unit: ESP32-S3, 1.14-inch screen, 2 keys, microphone, speaker, battery, 1 Grove port, Hat2 header. Firmware and enclosure rev 0.2 are made for it | about $21.50 (M5Stack store, launch price) |
| M5Stack Unit Dual Button (U025) | keys `ACK` and `REQ` on the Grove port | about £2.90 or €3.50 |
| Grove cable HY2.0-4P, 5 to 10 cm | connects the Dual Button unit inside the enclosure; the 20 cm cable in the box does not fit in the cable bay | not checked `[?]` |
| USB-C data cable | flashing and charging | probably at home `[?]` |

## Enclosure rev 0.3

| Item | Purpose | Price |
|---|---|---|
| Print by an on-demand service, SLA resin | front shell, back cover, 4 key parts | not checked |
| 4 × M2 × 16 self-tapping screws | back cover | not checked |
| 25 mm webbing belt | belt loop on the back cover | not checked |
| White paint marker | fill the engraved markings | not checked |

Do not order the print before these checks:

1. Measure the real StickS3 and Dual Button unit against the values from the maker drawings in `enclosure/params.py`.
2. Plug the USB-C cable and the Grove cable into the StickS3 at the same time: the plugs must not touch. See the [rev 0.3 open points](40-hardware.md#enclosure-rev-03).

## Recommended: silent alert

The StickS3 has no vibration motor ([UX audit](../10-concept/ux-principles.md) A11).

| Item | Purpose | Price |
|---|---|---|
| M5Stack Unit Vibrator (U059) | vibration on a high alert. N20 motor, 5 V, GPIO or PWM | about $3 |
| Cable HY2.0-4P to female 2.54 mm pins | connects the vibrator to the Hat2 header: the Grove port is taken by the Dual Button unit | not checked `[?]` |

Open points `[?]`:

- The vibrator connects to a free GPIO, 5 V and GND on the Hat2 header (G1 to G8 are on the header). Confirm the pins and the 5 V output on the real board, then set `kVibroPin` in the firmware.
- The enclosure has no place for the vibrator yet.

## For voice (stage 1)

| Item | Purpose | Price |
|---|---|---|
| Raspberry Pi Zero 2 WH | voice unit; the header is already soldered | not checked |
| 2-microphone board for Raspberry Pi | speech input; plugs into the header | not checked |
| microSD card, 32 GB | system and speech model | not checked |
| Battery pack with USB output | power for the voice unit | not checked |

## Fallback

Without the Dual Button unit, the StickS3 works in the 2-key mode. In the desk test the 2-key mode failed only on 5 presses in the first 30 s.

## Removed

M5Stack StopWatch Dev Kit: it was the first choice before the firmware and the enclosure were made for the StickS3 `[Claude]` 2026-11-13.

## No soldering

Modules connect with snap-in Grove cables and 2.54 mm pin sockets. Stage 0 needs no soldering iron.

[Parent](40-hardware.md)

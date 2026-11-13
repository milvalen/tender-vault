---
title: Stage 0 shopping list
type: plan
status: active
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: docs.m5stack.com (StickS3, Unit Dual Button, Unit Vibrator), cnx-software.com (StickS3 launch price, 2026-01-23), thepihut.com, robotshop.com, market.yandex.ru, eicom.ru, siusystem.ru, future-perfect.design, 3dzipper.ru [Claude] 2026-11-13
parent: 40-hardware.md
---

# Stage 0 shopping list

Approved by Artemy 2026-11-13 `[A]`. The list follows the desk test: the 4-key mode (StickS3 with the Dual Button unit) passed, the 2-key mode is the fallback. See the [UX audit](../10-concept/ux-principles.md#simulator-check-before-artemy-plays).

Prices in the tables are in US dollars or pounds from shops outside Russia `[Claude]` 2026-11-13. For shops in Russia, see [Where to buy in Russia](#where-to-buy-in-russia).

## Required

| Item | Purpose | Price |
|---|---|---|
| M5Stack StickS3 | interface unit: ESP32-S3, 1.14-inch screen, 2 keys, microphone, speaker, battery, 1 Grove port, Hat2 header. Firmware and enclosure rev 0.2 are made for it | about $21.50 (M5Stack store, launch price) |
| M5Stack Unit Dual Button (U025) | keys `ACK` and `REQ` on the Grove port | about £2.90 or €3.50 |
| Grove cable HY2.0-4P, 5 to 10 cm | connects the Dual Button unit inside the enclosure; the 20 cm cable in the box does not fit in the cable bay | not checked `[?]` |
| USB-C data cable | flashing and charging | probably at home `[?]` |

## Where to buy in Russia

Checked 2026-11-13 `[Claude]`. Prices include the delivery to a pickup point. Delivery times depend on the address and the seller; prices change daily.

| Item | Shop | Price | Delivery |
|---|---|---|---|
| StickS3 | Yandex Market, seller with 43 sales and rating 5.0, ships from Russia | 4,090 RUB | about 2 days |
| Dual Button unit (U025) | Yandex Market, ships from abroad | 506 RUB | about 2 weeks |
| Dual Button unit (U025) | eicom.ru, 168 in stock | 539 RUB | 3 to 6 weeks |
| Grove cable HY2.0-4P 10 cm, 5 pieces | Yandex Market, several sellers | 532 to 822 RUB | 3 to 4 weeks |
| Unit Vibrator (N20, U059) | Yandex Market, ships from abroad | 508 RUB | about 2 weeks |
| Unit Vibrator (N20, U059) | eicom.ru, 114 in stock | 539 RUB | 3 to 6 weeks |
| Grove2Dupont cable 20 cm, 5 pairs (vibrator to Hat2 header) | Yandex Market, ships from abroad | 660 RUB | about 2 weeks |

Total for the required items with the 4-key mode: about 5,130 RUB. With the silent alert: about 6,300 RUB.

Notes:

- Ozon also lists the StickS3 (about 3,230 RUB on sale, seen in search results). The product page was not checked: it showed an anti-bot check.
- eicom.ru has only 20 cm and longer M5Stack Grove cables (A034-B: 20 cm). The 10 cm cables are from marketplace sellers; check the HY2.0-4P plug in the photos.
- Order all at the same time: the StickS3 arrives first, the modules from abroad in about 2 weeks.

## Enclosure rev 0.4

| Item | Purpose | Price |
|---|---|---|
| Print by an on-demand service, SLA resin | front shell, 4 key parts, 2 of each (1 spare). See the [print order](print-order.md) | not checked |
| Print by an on-demand service, PA12 nylon (MJF or SLS) | back cover with the spring belt clip; resin breaks in the clip | not checked |
| 4 × M2 × 16 self-tapping screws | back cover | not checked |
| White paint marker | fill the engraved markings | not checked |

Do not order the print before these checks:

1. Measure the real StickS3 and Dual Button unit with the [measurement sheet](measurement-sheet.md).
2. Plug the USB-C cable and the Grove cable into the StickS3 at the same time: the plugs must not touch. A USB-C plug body of 5.3 mm or less is needed `[?]`. See the [plug check](40-hardware.md#plug-check).

### Where to print in Russia

Checked 2026-11-13 `[Claude]`. Prices are from the service pages, before the upload of the model. Part volumes from `build.py` (rev 0.4): front shell 29.4 cm³, back cover 16.4 cm³, 4 key parts 1.3 cm³ together. The STL files are in `out/` after `build.py`.

| Service | What | Price | Time | Notes |
|---|---|---|---|---|
| SIU System, Moscow | back cover, SLS PA12, black | 90 RUB/cm³: about 1,500 RUB | 3 to 5 working days | STL calculator on the site; ships across Russia. The general print page gives a minimum order of 10,000 RUB: ask if it applies to SLS |
| Future Perfect, Moscow | back cover, SLS polyamide (partner) | from 3,000 RUB per part | 3 to 5 days | Also prints SLA in-house in 1 to 2 days: both parts in 1 order. STL and STEP calculator |
| 3D ZIPPER, Pushkino | front shell and keys, SLA | standard resin 22 RUB/g: about 800 RUB; Tough resin 32 RUB/g | from 1 day | Minimum 1 part; ships by courier services. Their PA12 is not SLS: do not order the back cover there |

Estimate for 1 set: about 2,300 to 4,000 RUB without delivery. Before the order:

1. Ask for SLS or MJF PA12, not FDM nylon: the clip must be one solid part.
2. Ask for black or dyed black PA12: no bare white parts on the unit.
3. The engraving on the front shell is 0.4 mm deep: SLA keeps it; SLS can blur it.

## Recommended: silent alert

The StickS3 has no vibration motor ([UX audit](../10-concept/ux-principles.md) A11).

| Item | Purpose | Price |
|---|---|---|
| M5Stack Unit Vibrator (U059) | vibration on a high alert. N20 motor, 5 V, GPIO or PWM. 32 × 24 × 8 mm, 10.6 g | about $3 |
| Cable HY2.0-4P to **male** 2.54 mm pins | connects the vibrator to the Hat2 header: the Grove port is taken by the Dual Button unit. The Hat2 header has sockets, so the cable needs pins | not checked `[?]` |

Correction 2026-11-13 `[Claude]`: an earlier version of this list gave a cable with female pins. Female pins do not fit the Hat2 sockets. The "Grove2Dupont" cable in [Where to buy in Russia](#where-to-buy-in-russia) is correct only if its ends are male; check the photos before the order.

Open points `[?]`:

- The vibrator connects to a free GPIO, 5 V and GND on the Hat2 header (G1 to G8 are on the header). Confirm the pins and the 5 V output on battery on the real board, then set `kVibroPin` in the firmware.
- The maker gives 5 V at 424 mA for the motor at 10 kHz PWM, 50 % duty (docs.m5stack.com, U059) `[Claude]`. The StickS3 page gives a limit of 0.38 A for 5 V on the Grove port. The firmware drives the motor with PWM at about 35 % duty (`kVibroDuty`, firmware `dev` `29ffb53`); increase it only after a current measurement on battery.
- The enclosure has no place for the vibrator. Do the [vibrator desk test](40-hardware.md#silent-alert-desk-test-first) first.

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

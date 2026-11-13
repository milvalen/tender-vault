---
title: TND-01 device
type: plan
status: proposed
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: Conversation of Artemy with Claude 2026-11-13; board specifications [Claude] from cnx-software.com and hackster.io, 2026-11-13
parent: 20-device.md
---

# TND-01 device

## Stage 0 limits

- Artemy has no 3D printer and no soldering iron `[A]`, 2026-11-13.
- The budget is limited but reasonable `[A]`, 2026-11-13.

Therefore stage 0 uses ready-made boards and modules with snap-in connectors. An on-demand service prints the enclosure.

## Architecture

The device has 2 units. In stage 0, only the interface unit works.

| Unit | Task | Candidate |
|---|---|---|
| Interface unit | screen, keys, vibration, timers, table board | M5Stack StopWatch Dev Kit: ESP32-S3, round AMOLED, microphone, battery |
| Voice unit | offline Russian speech recognition, order parsing | Raspberry Pi Zero 2 WH with a microphone board |

The units connect over UART or BLE `[?]`. The decision is made after stage 0.

### Why voice runs on a separate unit

ESP32-S3 cannot run offline recognition of free Russian speech `[Claude]`. Raspberry Pi Zero 2 W can run Vosk or whisper.cpp with a small model `[?]`. Measure the speed on Russian speech.

### Screen

The final version considers a Sharp Memory LCD. The screen is 1-bit, readable in bright light and uses almost no power. It matches the [design language](../10-concept/design-language.md). Stage 0 uses the board's AMOLED with 1-bit graphics.

## Input and output

| Element | Purpose |
|---|---|
| Talk button | hold it and say the order |
| Rotary encoder | scroll tables and menu items |
| 3–4 keys | select, back, mark as done |
| Vibration motor | silent timer signal |
| Microphone | voice notebook |

## Power

Target: 10–12 h of a shift on one charge. Charging through USB-C. Measure the real run time in stage 0.

## Mounting

The device is allowed on the floor, on the belt `[A]` 2026-11-13. It hangs on the apron belt with a spring clip, screen up. See the [decision log](../70-decisions/70-decisions.md#2026-11-13-the-device-is-worn-on-the-belt).

Rejected: a forearm sleeve with the screen toward the face (sketch A).

[Parent](20-device.md)

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

The device is 1 unit and the server's phone. In stage 0, only the interface unit works.

| Part | Task | Candidate |
|---|---|---|
| Interface unit | screen, keys, vibration, timers, table board; records the speech while `TALK` is held | M5Stack StickS3 (stage 0) |
| Phone | sends the speech to a cloud recognition service, returns the text | the server's own phone |

Voice runs in the cloud through the phone `[A]` 2026-11-13, see the [decision log](../70-decisions/70-decisions.md#2026-11-13-voice-runs-in-the-cloud-through-the-phone).

Open points:

1. The link between the unit and the phone: BLE `[?]`.
2. Which cloud service recognizes Russian speech, and where does the order parsing run: on the phone or in the cloud `[?]`? See the [comparison of services](voice-recognition.md).
3. Without the mobile internet there is no voice. The table board and timers still work.
4. Does the StickS3 microphone give speech good enough for recognition on the floor `[?]`?

Rejected: a separate voice unit, Raspberry Pi Zero 2 WH with offline Vosk or whisper.cpp. ESP32-S3 cannot run offline recognition of free Russian speech `[Claude]`.

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

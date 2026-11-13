---
title: Hardware
type: index
status: active
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: Conversation of Artemy with Claude 2026-11-13
parent: ../Home.md
---

# Hardware

- [Stage 0 shopping list](stage-0-bom.md): boards and modules without soldering.
- [Measurement sheet](measurement-sheet.md): values to measure on the real boards before the enclosure print.
- [Print order](print-order.md): how to make the print package and order the enclosure print.

The enclosure model, the wiring and the full BOM are in the [tender-hardware](https://github.com/milvalen/tender-hardware) repository.

## Silent alert: desk test first

Status: planned. Decided by Artemy `[A]` 2026-11-13: test the vibrator on an open board before the enclosure gets a place for it.

Why the enclosure does not change now `[Claude]` 2026-11-13:

- The Unit Vibrator (U059) is 32 × 24 × 8 mm. It does not fit in rev 0.4 in any orientation. Behind the boards there is no depth. On edge it needs 24 mm of depth; the inside is 15.4 mm. The cable bay is 9.4 mm wide. Below the lower bay there is about 7.8 mm.
- The Hat2 header is on the screen end of the StickS3 (maker drawing K150), at the left wall. The left wall is 7.6 mm and holds the screws. A 2.54 mm pin plug with the cable bend needs about 15 to 18 mm `[?]`.
- A third bay below the Dual Button unit makes the shell about 78 × 90 × 31 mm `[?]`, from 68 × 62 × 31 mm. The desk test shows if the silent alert is worth this size.

Test steps:

1. Connect the vibrator to the Hat2 header with the Grove cable to male pins: signal to a free GPIO (G1 to G8), 5 V, GND. Write down the pins.
2. Set `kVibroPin` in `ui-unit/src/main.cpp` of `tender-firmware` to the GPIO number. The firmware drives the motor with PWM: 10 kHz, duty 90 of 255 (about 35 %), `kVibroDuty`. Accepted by Artemy into `dev`, merge commit `29ffb53`, 2026-11-13: builds for the StickS3 and passes the native tests; not run on a real board. Measure the current on battery before you increase the duty (see the [shopping list](stage-0-bom.md#recommended-silent-alert)).
   With the board self-test (firmware `dev` `c9eeb51`, type `!` in the serial console): type `vibro <GPIO>`. Allowed pins: Hat2 G1 to G3 and G5 to G8, Grove G9 and G10. Do not use G4 (Boot) or G43 and G44 (UART0). Type `pulse` for one alert pattern, or `on` and `off`. `duty <n>` sets the PWM duty, 0 to 128 of 255 (default 90, about 35 %). Write the pin and the duty into `kVibroPin` and `kVibroDuty`.
3. Run on battery, USB not connected. Check that the 5 V output works and the board does not restart when the motor starts. On battery the screen shows `USB OFF`. If the board restarts when the motor starts, the self-test and the boot line show the reset reason `BROWNOUT`.
4. Put the board and the vibrator in a pocket or tape them to the belt. Walk and bend. Is a high alert felt through the clothes? Is it heard by a guest at the table?
5. Measure the battery time with the alerts on. Type `log`: the self-test writes a battery line every 10 s (level, voltage). The StickS3 power chip does not report the battery current (`I N/A`). Measure the current with a multimeter.

Write the result here. Then decide: a third bay in the enclosure, a separate belt module with a cable, or no vibrator.

## Enclosure rev 0.4

Status: built and checked in code, not printed. Accepted by Artemy into `dev` of `tender-hardware`, commit `535f230`, 2026-11-13.

- **Belt clip.** A spring clip on the back cover replaces the webbing loop, as on a hand-held radio. The unit comes off the belt at any time: pull the flared tip out with a finger and lift. The belt goes in from below between the tongue and the cover. A ridge near the tip holds the bottom edge of the belt.
- Clip: 30 mm wide, 46 mm long, tongue 2.6 mm, gap 2 mm. A 4 mm belt preloads the tongue. At full opening for a 4.5 mm belt, the strain at the root is 1.1 % (check in `build.py`).
- **Print the back cover in nylon (PA12, MJF or SLS).** Standard SLA resin breaks at about 2 % strain. The front shell and the key caps can stay SLA.
- **Key names for the final version.** The ribbed key is `TALK`: hold it and speak a request; the phone sends it to cloud recognition. In stage 0, without voice, a press opens a guest request; the screen shows this meaning. Approved by Artemy `[A]` 2026-11-13. The separate talk button on the top face is no longer planned.
- Depth with the clip: 31.3 mm, 1.7 mm more than with the loop.

Open points `[?]`: the clip force on a real belt, and whether the catch ridge holds when the server bends down.

### Plug check

Accepted by Artemy into `dev` of `tender-hardware`, commit `b970452`, 2026-11-13. Not checked with real plugs.

- `build.py` models the USB-C plug body and the Grove plug with its cable bend at the right end of the StickS3. It checks that the plugs do not touch each other or the shell. The sizes are in `Plugs` in `enclosure/params.py`.
- The plug sizes are guesses. USB-C plug body: 12.35 × 6.5 mm, the largest size in the USB Type-C specification `[Claude]`. Grove plug: 9.9 × 4.5 mm, 4 mm out of the port, from the 4-way JST PH housing `[?]`. While `Plugs.measured` is false, a plug problem is a warning.
- The cable bay top moved up 0.6 mm. At the old height the widest USB-C plug body touched it.
- Result with the guessed sizes: the USB-C plug body and the Grove plug overlap by 0.6 mm in height. The port centres are 4.9 mm apart. A USB-C plug body of 5.3 mm or less clears the Grove plug `[?]`.
- The USB-C cable is needed only to charge and flash. If the plugs touch, use a thin or right-angle USB-C plug. The enclosure cannot move the ports.
- The Grove plug with the cable bend needs 7.0 mm. The cable bay gives 9.7 mm.

## Enclosure rev 0.3

Accepted by Artemy into `dev` of `tender-hardware`, commit `5c0953d`, 2026-11-13. Rev 0.4 adds the belt clip and the `TALK` key name.

Fits the real Dual Button unit. Sizes come from the maker drawings of the StickS3 (K150) and the Dual Button unit (U025):

- The Dual Button unit is 48 × 24 × 15 mm with its keys, not 48 × 24 × 8 mm. The keys are on the centre line, 14 mm apart. The lower bay is now 48.6 × 24.6 mm. The `ACK` and `REQ` caps are over the keys with a 0.2 mm gap.
- The StickS3 Grove port is on the USB-C end, behind the USB-C port. A cable bay at the right end holds both Grove plugs and the short cable.
- The pocket and the bay move left. The shell is 68 × 62 × 20.6 mm, 6 mm wider than rev 0.2: the top-left screw needs wall around it.
- The back cover screws move 1 mm in. In rev 0.2 the screw heads cut through the corner chamfers.
- The USB-C opening is sized for the plug body, at the port height.
- The fit check in `build.py` now also checks the Dual Button unit, the wall around each screw and the cable bay width.

Open points `[?]`:

1. In the cable bay, the USB-C plug body and the Grove plug can touch: the ports are about 5 mm apart in height. Check with the real plugs before the print. See the [plug check](#plug-check).
2. The cable bay is 9.4 mm wide. A Grove cable of 20 cm does not fit in it; use a cable of 5 to 10 cm.
3. Key B height on the StickS3 side and the cap retention are not measured.
4. The vibration module has no place yet.

## Enclosure rev 0.2

Accepted by Artemy into `dev` of `tender-hardware`, commit `e8d4bf6`, 2026-11-13. Replaced by rev 0.3: its lower bay was too small for the Dual Button unit.

Applies the [design review of rev 0.1](../10-concept/design-review-rev-0-1.md):

- One part for each firmware key. The `STEP` cap is over StickS3 key A. The `NEXT` pusher on the top face is over key B. The `ACK` and `REQ` caps are over the Dual Button unit in the lower bay.
- Each function is engraved next to its key.
- No visor, no `LOAD 3/4` marking, no orange part. The thumb wheel and the talk button are off until electronics stand behind them.
- Shell 62 × 62 × 20.6 mm.
- Limit: screen window, key and USB-C positions are guesses `[?]`. Measure the real boards before printing. Key B of the StickS3 must face up.

## Enclosure rev 0.1

Accepted by Artemy into `dev` of `tender-hardware`, commit `d632dfb`, 2026-11-13. Concept B with the talk button of sketch A, a visor, 3 placeholder key caps and a thumb wheel. Replaced by rev 0.2.

[Parent](../Home.md)

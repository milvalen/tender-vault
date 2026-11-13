---
title: Measurement sheet for the stage 0 boards
type: runbook
status: active
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: tender-hardware enclosure/params.py and tender-firmware ui-unit/src/main.cpp at dev 2026-11-13; maker drawings K150 (StickS3) and U025 (Dual Button unit) [Claude]
parent: 40-hardware.md
---

# Measurement sheet for the stage 0 boards

Use this sheet on the day the boards arrive. It lists each value that the enclosure and the firmware take from a maker drawing or from a guess. Enclosure rev 0.4 is printed only after this sheet is complete.

Write each result in the column "Measured". Then give the sheet to Claude. Claude updates `enclosure/params.py` in `tender-hardware` and the constants in `tender-firmware`, then runs the fit checks again.

## Tools

- Digital calipers, 0.01 mm display.
- The USB-C cable that you will use on the floor.
- A Grove cable of 5 to 10 cm.
- A multimeter, for part E only.

## Rules

1. Measure each value 2 times. Write the mean to 0.1 mm.
2. Close the calipers gently. Do not press the plastic.
3. If a result differs from the model value by more than 0.2 mm, mark it with `!`.
4. If you cannot measure a value, write `—` and the reason.

## Board position

Put the StickS3 on the table, screen up. Turn it so that the Hat2 header end is on the left and the USB-C end is on the right. This is its position in the enclosure. "Left end" in this sheet is the Hat2 header end. "Back face" is the face opposite the screen.

## S. StickS3

| No. | Value | How to measure | Model | Source | Measured |
|---|---|---|---|---|---|
| S1 | Length | Left end to right end, at the widest point | 48.0 | maker spec | |
| S2 | Width | Long side to long side, without key B | 24.0 | maker spec | |
| S3 | Depth | Back face to screen face, at the deepest point | 15.0 | maker spec | |
| S4 | Screen window start | Left end to the left edge of the dark glass area | 3.8 | drawing | |
| S5 | Screen window length | Left edge to right edge of the dark glass area | 26.3 | drawing | |
| S6 | Screen window height | Top edge to bottom edge of the dark glass area | 16.4 | drawing | |
| S7 | Key A position | Left end to the centre of key A on the screen face | 37.5 | drawing | |
| S8 | Key B side | Which long side has key B: top (away from you) or bottom? | top | needed | |
| S9 | Key B position | Left end to the centre of key B | 24.0 | drawing | |
| S10 | Key B height | Back face to the centre of key B | 7.5 | `[?]` | |
| S11 | USB-C port height | Back face to the centre of the USB-C port | 10.2 | drawing | |
| S12 | Grove port height | Back face to the centre of the Grove port | 5.3 | drawing | |
| S13 | Ports along the width | Top long side to the centre of each port. Both ports are on the centre line if the result is 12.0 | 12.0 | drawing | |

## P. Plugs

Plug both cables into the StickS3 at the same time. The cable bay holds both plugs side by side.

| No. | Value | How to measure | Model | Source | Measured |
|---|---|---|---|---|---|
| P1 | USB-C plug body width | Across the plastic body, the long direction of the port | 12.35 | USB Type-C largest `[Claude]` | |
| P2 | USB-C plug body thickness | Across the plastic body, the short direction of the port. 5.3 or less clears the Grove plug | 6.5 | USB Type-C largest `[Claude]` | |
| P3 | Grove plug reach | Right end of the board to the farthest point of the Grove plug and the cable bend, with the cable bent down along the board | 8.0 or less | `[?]` | |
| P4 | Gap between the plugs | Smallest gap between the USB-C plug body and the Grove plug or cable. Write 0 if they touch | more than 0 | open point 1 of rev 0.3 | |
| P5 | Plugs pushed apart | Do the plugs push each other out of the ports? Yes or no | no | needed | |
| P6 | Grove plug width | Across the part of the plug outside the port, the long direction | 9.9 | `[?]` | |
| P7 | Grove plug thickness | Across the part of the plug outside the port, the short direction, with the latch | 4.5 | `[?]` | |
| P8 | Grove plug out of the port | Right end of the board to the back of the Grove plug, without the cable | 4.0 | `[?]` | |

If S8 is "bottom", tell Claude: the `NEXT` pusher on the top face does not reach key B.

If P4 is 0 or P5 is "yes", stop here and tell Claude. Try a USB-C cable with a thinner or right-angle plug first: the ports on the board cannot move.

Claude writes P1 to P8 into `Plugs` in `enclosure/params.py` and sets `Plugs.measured` to true. Then `build.py` fails on a plug problem.

## D. Dual Button unit

Put the unit keys up, with the keys on the left and the Grove port on the right.

| No. | Value | How to measure | Model | Source | Measured |
|---|---|---|---|---|---|
| D1 | Length | Left end to right end | 48.0 | drawing U025 | |
| D2 | Width | Side to side | 24.0 | drawing U025 | |
| D3 | Height to the key tops | Back face to the top of the key caps, keys not pressed | 15.0 | drawing U025 | |
| D4 | Key 1 position | Left end to the centre of the first key | 11.0 | drawing U025 | |
| D5 | Key 2 position | Left end to the centre of the second key | 25.0 | drawing U025 | |
| D6 | Key cap diameter | Across a key cap | 11.5 | drawing U025 | |
| D7 | Key travel | Key top height not pressed minus key top height fully pressed | not modelled | needed | |
| D8 | Keys on the centre line | Top side to the centre of each key. On the centre line if 12.0 | 12.0 | drawing U025 | |

D3 is the most important value in this part. The `ACK` and `TALK` caps have a gap of only 0.2 mm above the keys.

## B. Belt

Measure the belt or the apron band that will hold the unit on the floor.

| No. | Value | How to measure | Model | Source | Measured |
|---|---|---|---|---|---|
| B1 | Belt thickness | At the thickest point where the clip will sit | 4.0 to 4.5 | `[?]` | |
| B2 | Belt width | Top edge to bottom edge | 30 or more | `[?]` | |

The clip takes a belt of up to 4.5 mm. A belt thinner than 2 mm does not preload the clip.

## E. Firmware checks on the board

Do these steps after the measurements. Each result changes one constant in `ui-unit/src/main.cpp`.

1. Set `kHasDualButton` to `true` and upload the firmware.
2. Press the red key. Then press the blue key.
3. Write the result in E1. If the keys work only when released, or the screen reacts all the time, set `kDualActiveHigh` to `false`.
4. Put the board in the enclosure position from [Board position](#board-position). Look at the screen.
5. Write the result in E2. If the text is upside down, set the display rotation to 3.

| No. | Check | Expected | Constant | Result |
|---|---|---|---|---|
| E1 | Red key gives `ACK`, blue key gives `TALK` on a press | yes | `kDualActiveHigh`, `kRedPin`, `kBluePin` | |
| E2 | Text reads correctly with the Hat2 end on the left | yes | display rotation 1 | |
| E3 | Vibrator pins and current | see the [vibrator desk test](40-hardware.md#silent-alert-desk-test-first) | `kVibroPin`, `kVibroDuty` | |

[Parent](40-hardware.md)

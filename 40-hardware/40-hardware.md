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

The enclosure model, the wiring and the full BOM are in the [tender-hardware](https://github.com/milvalen/tender-hardware) repository.

## Enclosure rev 0.3

Status: built and checked in code, not printed. Accepted by Artemy into `dev` of `tender-hardware`, commit `5c0953d`, 2026-11-13.

Fits the real Dual Button unit. Sizes come from the maker drawings of the StickS3 (K150) and the Dual Button unit (U025):

- The Dual Button unit is 48 × 24 × 15 mm with its keys, not 48 × 24 × 8 mm. The keys are on the centre line, 14 mm apart. The lower bay is now 48.6 × 24.6 mm. The `ACK` and `REQ` caps are over the keys with a 0.2 mm gap.
- The StickS3 Grove port is on the USB-C end, behind the USB-C port. A cable bay at the right end holds both Grove plugs and the short cable.
- The pocket and the bay move left. The shell is 68 × 62 × 20.6 mm, 6 mm wider than rev 0.2: the top-left screw needs wall around it.
- The back cover screws move 1 mm in. In rev 0.2 the screw heads cut through the corner chamfers.
- The USB-C opening is sized for the plug body, at the port height.
- The fit check in `build.py` now also checks the Dual Button unit, the wall around each screw and the cable bay width.

Open points `[?]`:

1. In the cable bay, the USB-C plug body and the Grove plug can touch: the ports are about 5 mm apart in height. Check with the real plugs before the print.
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

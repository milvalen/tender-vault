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

## Enclosure rev 0.2

Status: built and checked in code, not printed. Accepted by Artemy into `dev` of `tender-hardware`, commit `e8d4bf6`, 2026-11-13.

Applies the [design review of rev 0.1](../10-concept/design-review-rev-0-1.md):

- One part for each firmware key. The `STEP` cap is over StickS3 key A. The `NEXT` pusher on the top face is over key B. The `ACK` and `REQ` caps are over the Dual Button unit in the lower bay.
- Each function is engraved next to its key.
- No visor, no `LOAD 3/4` marking, no orange part. The thumb wheel and the talk button are off until electronics stand behind them.
- Shell 62 × 62 × 20.6 mm.
- Limit: screen window, key and USB-C positions are guesses `[?]`. Measure the real boards before printing. Key B of the StickS3 must face up.

## Enclosure rev 0.1

Accepted by Artemy into `dev` of `tender-hardware`, commit `d632dfb`, 2026-11-13. Concept B with the talk button of sketch A, a visor, 3 placeholder key caps and a thumb wheel. Replaced by rev 0.2.

[Parent](../Home.md)

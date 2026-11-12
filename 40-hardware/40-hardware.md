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

## Enclosure rev 0.1

Status: built and checked in code, not printed. Branch `ai/enclosure` of `tender-hardware`, commit `d632dfb`, 2026-11-13.

- Form: [concept sketch B](../10-concept/concept-sketches.md#b-belt-module) with the talk button of sketch A.
- Payload: M5Stack StickS3, landscape. Shell 62 × 62 × 20.6 mm.
- Parts: front shell, back cover with a loop for 25 mm webbing, 3 key caps, thumb wheel, talk button.
- The build script checks that the solids are valid and that parts do not collide.
- Limit: screen window and USB-C positions are guesses `[?]`. Measure the real board before printing.

[Parent](../Home.md)

---
title: Ink Industrial design language
type: standard
status: proposed
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: Conversation of Artemy with Claude 2026-11-13
parent: 10-concept.md
---

# Ink Industrial design language

Ink Industrial is the design language of TENDER. It joins field equipment with ink graphics. The rules below apply to the enclosure, the screen, the icons and the posters.

## Form

1. The enclosure is made of angular, asymmetric plates. The plates overlap.
2. Fasteners are exposed. Seams and joints are visible.
3. Every part has a job: it protects the screen, gives a finger rest or holds the strap. There are no decorative parts.
4. Edges are straight. Fillets are small, radius up to 1 mm `[?]`; confirm after the first print.
5. Every key has its function engraved next to it. Keys differ in shape, so the hand can find them without a look. Colour does not name a key.

## Graphics

1. The screen uses black, white and the accent. Grey is only for secondary text. Changed after the [design review](design-review-rev-0-1.md) (R6) `[A]` 2026-11-13.
2. Icons and posters are drawn with a brush stroke that has a rough edge.
3. Empty space is part of the composition. Dense blocks stand next to empty fields.

## Markings

Capitals only. Stencil typeface on the enclosure and on posters. The screen uses a plain bold font: stencil gaps make small screen text hard to read. The project's own designation system:

| Designation | Meaning |
|---|---|
| `UNIT TND-01` | the device, on the enclosure only |
| `TBL-07` | table 7 |
| `ST-2` | seat 2 at the table |
| `STEP`, `NEXT`, `ACK`, `TALK` | key functions, on the enclosure and on the screen |
| `12 MIN` | 12 min since the last stage change |
| `LOW BATTERY` | shown only below 25 % charge |

A fixed battery value on the enclosure is false; the battery shows only on the screen.

## Palette

| Role | Color |
|---|---|
| Base | matte black |
| Second base | dark olive or graphite |
| Accent | one signal color: red or orange |
| Markings | white or light grey; fill engraved markings with white paint after the print |

The accent marks only what needs action. Example: a table whose timer has expired. No part of the enclosure is in the accent colour: a permanent orange part teaches the eye to ignore orange.

[Parent](10-concept.md)

---
title: Design review of enclosure rev 0.1
type: record
status: active
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: Review by Claude 2026-11-13 of tender-hardware dev d632dfb (renders front, back, exploded), concept sketch B, firmware ai/table-board 43e4681
parent: 10-concept.md
---

# Design review of enclosure rev 0.1

Request of Artemy 2026-11-13: check the device against the [design language](design-language.md) and the [UX principles](ux-principles.md). Inputs: enclosure rev 0.1 renders in `tender-hardware/renders/`, [concept sketch B](concept-sketches.md#b-belt-module), firmware on `ai/table-board`.

Limit: the review uses renders only. No printed part and no paper mockup was checked `[Claude]`.

## What conforms

| Rule | Where |
|---|---|
| Form 1: angular, asymmetric plates that overlap | large top-left corner cut; lower plate overlaps the key row |
| Form 2: exposed fasteners, visible seams | screw heads on the plates; back cover seam |
| Palette: black base, olive second base, one accent | front shell black, back cover olive, one orange part |
| P3: keys can be told apart without a look | 3 key caps with different tops: rounded, flat, ribbed |

## Findings

Artemy approved all changes `[A]` 2026-11-13. Status column: where each change is now.

| # | Finding | Rule | Severity | Change | Status |
|---|---|---|---|---|---|
| R1 | The controls lead nowhere in stage 0. The 3 key caps, the wheel and the talk button are form placeholders. The front wall covers key A of the StickS3, and key B on the side has no pusher. So the 2-key firmware mode cannot be used in the enclosure, and the 2 keys of the Dual Button unit are not under the caps | Form 3; P3 | high | Rev 0.2: one cap for each firmware key. Cap A over StickS3 key A, a side pusher on key B, 2 caps over the Dual Button keys in the lower bay. Measure the key positions on the real board `[?]` | done in `tender-hardware` `dev` `e8d4bf6`; key positions still `[?]` |
| R2 | The screen labels name colours that the device does not have: `RED ACK`, `BLUE REQ`. The caps are grey. Red and blue caps would break the one-accent rule | P3; Palette | high | Name keys by function: screen labels `ACK` and `REQ` above their caps, the same words engraved next to the caps | done: enclosure `e8d4bf6`, firmware `74093a6` |
| R3 | The visor sits over the top edge of the screen. On the belt the server looks down from above, so the visor is between the eye and the top line. The top line is the table number, the most important fact | P1; Form 3 | high | Remove the visor, or move the guard to the sides of the screen. Check the view angle with a paper mockup on the belt | done: no visor in `e8d4bf6`; paper mockup not done |
| R4 | `LOAD 3/4` is engraved on the shell. A fixed battery value is false after the first minute. The UX audit (A8) removed it from the screen | Rams: honest; P8 | medium | Engrave `UNIT TND-01` only | done in `e8d4bf6` |
| R5 | The talk button is the only orange part, but it has no function in stage 0. Orange on the screen means "act now". A permanent orange part teaches the eye to ignore orange | Palette: accent only for action; P6, P7 | medium | Graphite talk button. Remove it until the voice unit (stage 1) | done: wheel and talk button off in `e8d4bf6`, no orange part |
| R6 | The design language says the screen is 1-bit, no grey, stencil type. The firmware uses grey for secondary text, an orange accent and a plain bitmap font. Stencil gaps make small screen text hard to read | Graphics 1; Markings | medium | Change the design language: screen in black, white and the accent; grey only for secondary text; stencil only on the enclosure, a plain bold font on the screen | done in the [design language](design-language.md) |
| R7 | The designation table in the design language still lists `LOAD 3/4` and `T+12`. The screen now shows `LOW BATTERY` only below 25 % and `12 MIN` | Markings | low | Update the table to the current screen text | done in the [design language](design-language.md) |
| R8 | Engraved markings are black on black. The design language asks for white or light grey markings | Palette: markings | low | Fill the engraving with white paint after the print | done in the design language and the `tender-hardware` README; paint after the print |
| R9 | Concept sketch B shows old content: `TBL-07 T+12`, 3 keys `START / STOP`, `LAP`, `ACK`, the text "compact timer". It is 58 × 38 mm; rev 0.1 is 62 × 62 × 21 mm | P2; P7 | low | Mark the sketch text as replaced by the UX audit. Check the size on the belt with a paper mockup before rev 0.2 | done in [concept sketches](concept-sketches.md); paper mockup not done |

## Note on the wheel

The simulator shows that 132 of 180 presses move between tables (finding D4 in the [UX audit](ux-principles.md#simulator-check-before-artemy-plays)). A real thumb wheel would cut this. The M5Stack encoder unit uses I2C on the Grove port; the Dual Button unit uses 2 GPIO pins on the same port. Both together need a different port plan `[?]`. Decide after the desk test.

[Parent](10-concept.md)

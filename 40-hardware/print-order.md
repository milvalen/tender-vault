---
title: Enclosure print order
type: runbook
status: active
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: tender-hardware enclosure/package.py at dev 5fba3b9, 2026-11-13 [Claude]
parent: 40-hardware.md
---

# Enclosure print order

This runbook tells how to order the print of the enclosure from an on-demand print service. Artemy approves each order `[A]`.

## Before the order

Do not order until all of these conditions are true:

1. The [measurement sheet](measurement-sheet.md) is complete.
2. Claude wrote the results into `enclosure/params.py` and set `Tnd01Params.measured` and `Plugs.measured` to true.
3. The change is accepted into `dev` of `tender-hardware`.
4. The package name has no `-DRAFT` and `ORDER.txt` does not start with "DO NOT ORDER".

## Make the package

1. Open the `tender-hardware` repository on the `dev` branch.
2. Run `.venv/bin/python enclosure/package.py`.
3. Find the zip file in `out/print-package/`. Its name has the revision and the commit, for example `tnd01-rev0.4-5fba3b9.zip`.

The script stops with status 1 if a fit check fails. Then it writes no package.

## Package contents

| Folder or file | Contents |
|---|---|
| `sla/` | front shell and 4 key caps, for SLA resin |
| `pa12/` | back cover with the belt clip, for PA12 nylon |
| `step/` | 1 STEP file for each part, for services that take STEP |
| `parts.csv` | part, material, quantity, volume, size and print notes |
| `ORDER.txt` | the request to the service, the volumes and the commit |

Quantities at `dev` 5fba3b9: 1 front shell, 1 back cover, 2 of each key cap. The second key cap is a spare. Each key cap is 0.2 to 0.4 cm³.

Volumes with the spares: SLA 31.9 cm³, PA12 16.4 cm³.

## Place the order

1. Pick a service from [Where to print in Russia](stage-0-bom.md#where-to-print-in-russia).
2. Upload `sla/` to a service that prints SLA resin.
3. Upload `pa12/` to a service that prints PA12 by MJF or SLS. One service can do both orders.
4. Copy the requests from `ORDER.txt` into the order form or the message.
5. Ask the service these questions before you pay:
   - Which hole and gap tolerance does each process give?
   - Is the PA12 part dyed black?
   - Does a minimum order price apply?
6. Write the service, the price and the date in the [shopping list](stage-0-bom.md) with the mark `[A]`.

## Requests to the service

- SLA, black or dark grey resin. No supports on the front face of the front shell: the 0.4 mm engraving must stay sharp. No supports on the top faces of the key caps.
- PA12 nylon, MJF or SLS, dyed black. Not FDM nylon: the belt clip must be 1 solid part. The clip tongue bends 1.1 % in use.

## When the parts arrive

1. Look at the engraving on the front shell. Each letter must be clear.
2. Pull the clip tip out by hand by 3 to 4 mm. A 4.5 mm belt opens it by 3.5 mm. Release it. The tongue must return with no white marks.
3. Put the boards in the front shell. Write each tight or loose fit in the [measurement sheet](measurement-sheet.md).
4. Fill the engraving with the white paint marker.

[Parent](40-hardware.md)

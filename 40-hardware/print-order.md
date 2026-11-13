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
| `sla/` | front shell, 4 key caps and the SLA tolerance coupon, for SLA resin |
| `pa12/` | back cover with the belt clip and the PA12 tolerance coupon, for PA12 nylon |
| `step/` | 1 STEP file for each part, for services that take STEP |
| `parts.csv` | part, material, quantity, volume, size and print notes |
| `ORDER.txt` | the request to the service, the volumes and the commit |

Quantities at `dev` 23b3785: 1 front shell, 1 back cover, 2 of each key cap, 1 SLA coupon, 1 PA12 coupon. The second key cap is a spare. Each key cap is 0.2 to 0.4 cm³.

Volumes with the spares and the coupons: SLA 37.5 cm³, PA12 21.3 cm³. The PA12 coupon is 4.9 cm³; leave it out to save cost if needed.

## Tolerance coupons

Two small test parts go in the same order. They show the gaps that the service really gives. The next enclosure revision uses these results instead of guesses. Labels: key gaps are in hundredths of a millimetre per side, holes in tenths of a millimetre (`17` = 1.7 mm). Source: `tender-hardware` `enclosure/coupon.py` at `dev` `23b3785` `[Claude]` 2026-11-13.

| Coupon | Material | Feature | Range | Model value |
|---|---|---|---|---|
| `coupon_sla` | SLA | window at the payload pocket size, label `POCKET 30` | 0.30 mm gap per side | 0.30 |
| `coupon_sla` | SLA | square key holes | 0.10 to 0.30 mm gap per side | 0.20 |
| `coupon_sla` | SLA | screw pilot bosses, 8 mm deep | 1.5 to 1.9 mm | 1.7 |
| `coupon_sla` | SLA | engraving depth, each label cut to its own depth | 0.3 to 0.5 mm | 0.4 |
| `coupon_pa12` | PA12 | 10 mm strip of the real belt clip profile | — | — |
| `coupon_pa12` | PA12 | screw clearance holes with head recess | 2.2 to 2.6 mm | 2.4 |

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
2. Put the StickS3 and the Dual Button unit in the window of `coupon_sla`. Write "tight", "good" or "loose".
3. Put a spare key cap in each key hole of `coupon_sla`. Write the smallest gap where the cap moves freely.
4. Turn an M2 self-tapping screw into each pilot boss of `coupon_sla`. Write the smallest hole where the boss does not crack and the screw holds.
5. Look at the 3 engraving depths. Write the smallest depth that stays clear after the paint marker.
6. Bend the clip strip of `coupon_pa12` 100 times by 3 to 4 mm. Then bend it until it breaks. Write the bend at the break.
7. Push an M2 screw through each clearance hole of `coupon_pa12`. Write the smallest hole where the screw goes in freely.
8. Pull the clip tip out by hand by 3 to 4 mm. A 4.5 mm belt opens it by 3.5 mm. Release it. The tongue must return with no white marks.
9. Put the boards in the front shell. Write each tight or loose fit in the [measurement sheet](measurement-sheet.md).
10. Fill the engraving with the white paint marker.
11. Give the coupon results to Claude for the next enclosure revision.

[Parent](40-hardware.md)

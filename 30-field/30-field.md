---
title: Field notes
type: index
status: active
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: Documentation standard
parent: ../Home.md
---

# Field notes

This section keeps observations from shifts: what gets in the way, what is forgotten, where time is lost. The observations test the device [functions](../20-device/functions.md).

## Rules

1. One note covers one shift or one problem. The filename names the problem, for example `forgotten-dessert-check.md`.
2. Write in general terms: "the restaurant", "a colleague", "a guest". No names.
3. Record income and tips only in `_private/`.

There are no notes yet. The first one comes after a shift.

## Read the shift log

The device keeps a shift log (firmware `dev` `939676f`, 2026-11-13):

- every key action, with the table and its stage after the action;
- every high alert;
- each boot, with the reset reason;
- the battery level every 10 min.

The log holds table numbers, stages and actions only. Only the last boot gets wall-clock time, because the board has no clock.

1. After a shift, connect the device to USB.
2. In `tender-firmware`, run `python3 tools/shift_log.py --port <port> --out ../tender-vault/_private/shift-<date>.csv`. It needs `pip install pyserial`.
3. Read the summary: presses, alerts, the time of tables in each stage against the thresholds (median, max, over), restarts and the battery drain per hour.
4. Keep the CSV in `_private/`. Write the summary numbers in the field note of the shift.
5. To delete the log, type `clearlog` in the board self-test.

[Parent](../Home.md)

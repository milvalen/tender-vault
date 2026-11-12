# tender vault — instructions for agents

Read [Home](Home.md), the [documentation standard](90-system/documentation-standard.md) and the [glossary](90-system/glossary.md). Write in English under ASD-STE100. Use the terms from the glossary. File and folder names contain only Latin letters, digits and hyphens.

Scope: the TENDER device (TND-01) for restaurant floor work. Concept, design language, functions, shift field notes, hardware, enclosure, tools. Code is kept in the separate repositories `tender-firmware` and `tender-hardware`, not here.

## Public repository

This repository is public. Do not put into it:

- the owner's income, tips, pay rates and shift schedules;
- the restaurant name and address, the names of colleagues and guests;
- passwords, tokens, keys;
- external style references: names of artists, games, brands and other companies' devices.

Such data goes to `_private/`. Git ignores that folder. In a public note, write in general terms: "the restaurant", "a colleague", "a guest".

## Git

Work only on the `main` branch. Do not create branches, forks or pull requests. Do not use `git push --force`.

1. Before you write, run `git status -sb`. The clone must be clean and up to date.
2. Run `git pull --rebase`.
3. Before you commit, run `python3 -I 90-system/tools/check-vault.py` and `git diff --check`.
4. Make short commits, one topic each, and push only to `main`.

The owner approves purchases, social media posts and print service orders separately.

## Content

Do not invent facts. Mark prices and specifications with a source: `[A]` Artemy, `[Claude]` web research, `[?]` guess. A new fact does not erase an old one: write the date.

Pages with status `verified` describe only what was checked: what, when, on which hardware and commit. Plans have status `proposed` or `planned`.

## Updates

Update the minimum set: Home (actions), the topic note, the decision log for significant decisions. Add raw notes to the [inbox](00-inbox/00-inbox.md).

---
title: Documentation standard
type: standard
status: active
owner: Artemy
created: '2026-11-13'
updated: '2026-11-13'
observed: '2026-11-13'
sensitivity: public
source: miniatures vault standard (2026-11-11), adapted for TENDER 2026-11-13; ASD-STE100 Issue 9
parent: 90-system.md
---

# Documentation standard

## Scope

The standard applies to all vault notes except raw entries in the [inbox](../00-inbox/00-inbox.md).

## Language

We write in English under ASD-STE100 Issue 9 (Simplified Technical English). We follow its writing rules; we do not claim full compliance with its dictionary. The project vocabulary is in the [glossary](glossary.md).

### Writing rules

1. Write one idea in one sentence. Use up to 25 words in a description sentence and up to 20 in an instruction.
2. Name the actor, the condition, the action and the result.
3. Use the active voice and simple verbs. Avoid noun clusters of more than 3 words.
4. Write instructions as a numbered list. One step is one action. Start each step with an imperative verb.
5. One term means one concept. Add a new term to the glossary.
6. Write numbers as digits. Give units: ₽, mm, mAh, h. Write dates in ISO format: `2026-11-13`.
7. Do not write praise or advertising. Write a fact that can be checked.
8. Do not use `etc.`, `soon` or `recently`. Do not write "about" without a range.
9. Keep fact and guess apart. Add a source mark.

### Code and README

1. Write code, identifiers, comments, commit messages, developer-facing program output and `README.md` in English.
2. Russian text is allowed in code only as product content: on-screen labels, menu item names, speech phrases.
3. A code repository's `README.md` links to the vault and does not copy it.
4. The default branch of a code repository is `dev`. `main` is the release branch and is never ahead of `dev`.

## Structure

| Folder | Contents |
|---|---|
| `00-inbox` | raw ideas |
| `10-concept` | concept and design language |
| `20-device` | device and functions |
| `30-field` | shift observations |
| `40-hardware` | boards, modules, purchases |
| `45-development` | code repositories and their components |
| `50-tools` | design and development tools |
| `70-decisions` | decision log |
| `90-system` | standard, glossary, templates, check |

Each folder has an overview named after the folder. Do not use `index.md`. File and folder names contain only Latin letters, digits and hyphens. Links are relative Markdown links. Do not create empty pages or folders.

## Metadata

Each note starts with flat YAML: `title`, `type`, `status`, `owner`, `created`, `updated`, `observed`, `sensitivity`, `source`, `parent`. `README.md` has no `parent`. `AGENTS.md` and `CLAUDE.md` have no metadata.

| Field | Value |
|---|---|
| `type` | `index`, `reference`, `plan`, `record`, `runbook`, `standard`, `template` |
| `status` | `draft`, `proposed`, `active`, `verified`, `historical`, `deprecated`, `planned`, `template` |
| `created`, `updated` | ISO dates |
| `observed` | the date of the event or source; `unknown` if the date is not known |
| `sensitivity` | `public`: the vault is public |
| `source` | a specific source |
| `parent` | relative path to the parent; the note ends with the link `[Parent](...)` |

Status `verified` requires what was checked, when, and on which hardware and commit.

## Sources

Marks: `[A]` Artemy, `[Claude]` web research or a conclusion of Claude, `[?]` guess. A new fact does not erase an old one: write the date next to both.

## Public vault and personal data

The vault is public. Do not put passwords, tokens, keys, income, tips, shift schedules, the restaurant name or the names of colleagues and guests into it. Such data goes to `_private/`; Git ignores that folder.

Public notes do not use other companies' games, brands or artists as a model. External references are stored in `_private/`.

## Git

1. Work only on the `main` branch. Do not create branches, forks or pull requests.
2. Before an edit, run `git pull --rebase`.
3. Make short commits, one topic each.
4. Do not use `git push --force`.

## Check

Before a commit, run:

```bash
python3 -I 90-system/tools/check-vault.py
git diff --check
```

[Parent](90-system.md)

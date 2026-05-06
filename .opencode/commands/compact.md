---
description: Rewrite one file with compact style (formatting + docstrings only)
---

Rewrite `$ARGUMENTS` in the project's compact style. Do not change logic,
public API, behavior, imports, or file structure. Do not run or modify tests.

## Step 1 — Read instructions

Read `style.md` and `docstrings.md` before doing anything else.

## Step 2 — Audit the target file

Scan every function call, definition, collection, docstring, and helper
function in the file and produce a violation list.

**Formatting — check every function call and definition explicitly:**

- Any call or definition with one argument per line → violation, always,
  regardless of length. The fix is grouping, not leaving it.
- Any call, return, or assignment split across lines that fits in 100
  characters → collapse to one line.
- Any collection with one item per line → group by logical chunks.
- Any missed tuple unpacking opportunity.

For each violation write:
- the line number
- the type (one-arg-per-line / can-collapse / one-item-per-line)
- the fix (collapse / group as: ...)

**Helper functions — audit every existing private helper:**

A helper should be inlined when any of the following is true:
- it is only called once and is short enough to fit as a titled inline block
- it splits closely related logic that belongs together
- inlining it makes the algorithm more visible, not less

For each helper to inline, write:
- the function name and line number
- the reason (called once / splits related logic / obscures algorithm)

**Logic blocks:**
- Any meaningful block of logic missing a `# Title` comment.

**Docstrings:**
- Any public object with a vague Notes section (describes what, not how).
- Any public object with placeholder or non-runnable Examples.

This list is your work order. Only touch what is on it, plus any helpers
you decide to extract or inline (see below).

## Step 3 — Rewrite

Work through the violation list in this priority order:

1. **Formatting** — fix every violation on the list:
   - One-arg-per-line calls → group related args onto shared lines
   - One-arg-per-line definitions → group parameters by role
   - Collapsible lines → collapse
   - One-item-per-line collections → group by chunks
2. **Helpers** — reconcile helper functions:
   - Inline any helper that does not meet the extraction criteria; replace
     its call site with a `# Title` comment block
   - Extract a new private helper only when all three conditions are met:
     the same logic appears 3+ times, or the block is complex enough that
     naming it genuinely improves readability of the caller; the helper
     follows all style and docstring rules (one-line docstring if private);
     extraction does not split closely related logic or obscure the algorithm
   - When unsure, keep it inline under a title comment
3. **Logic blocks** — add missing title comments
4. **Docstrings** — rewrite vague Notes, fix placeholder Examples
5. **Comments** — remove obvious ones, add non-obvious ones

Do not rename public objects. Do not edit any other file.

## Step 4 — Self-check

After rewriting, scan the file again:

- Any remaining one-arg-per-line calls or definitions? Fix them.
- Any lines under 100 characters that are still split? Collapse them.
- Any helper that should be inlined but wasn't? Inline it.
- Do new or remaining helpers follow style and docstring rules?

Do not skip this step.

## Step 5 — Report

Summarize:
- The full violation list with line numbers
- Any helpers inlined and why
- Any helpers extracted and why
- What was changed
- Confirmation that logic and public API are preserved
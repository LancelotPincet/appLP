---
description: Rewrite one file with same logic but compact project style
---

Rewrite `$ARGUMENTS` in the project's compact style. Do not change logic,
public API, behavior, imports, errors, tests, or file structure.

## Step 1 — Read instructions

Read all files in `.opencode/instructions/*.md` before doing anything else.

## Step 2 — Find the test file

- If the target is `<name>_LP/<name>.py` → test file is `<name>_LP/test_<name>.py`
- If the target is inside `<name>_LP/_functions/` → test file is still `<name>_LP/test_<name>.py`

If either file cannot be found, stop and explain what is missing.

## Step 3 — Run tests before editing

Run the test file:

```
pytest <name>_LP/test_<name>.py -v
```

If any test fails, stop immediately. Do not edit anything. Report the
failing command and the failure message.

## Step 4 — Audit the target file

Before rewriting, scan every function call, definition, and collection in
the file and produce a violation list.

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

**Logic blocks:**
- Any meaningful block of logic missing a `# Title` comment.

**Docstrings:**
- Any public object with a vague Notes section (describes what, not how).
- Any public object with placeholder or non-runnable Examples.

This list is your work order. Only touch what is on it.

## Step 5 — Rewrite

Work through the violation list in this priority order:

1. **Formatting** — fix every violation on the list:
   - One-arg-per-line calls → group related args onto shared lines
   - One-arg-per-line definitions → group parameters by role
   - Collapsible lines → collapse
   - One-item-per-line collections → group by chunks
2. **Logic blocks** — add missing title comments
3. **Docstrings** — rewrite vague Notes, fix placeholder Examples
4. **Comments** — remove obvious ones, add non-obvious ones

Do not extract new helpers. Do not rename public objects. Do not edit
any other file.

## Step 6 — Self-check before running tests

After rewriting, scan the file again:

- Are there any remaining one-arg-per-line calls or definitions? If yes, fix them.
- Are there any lines under 100 characters that are still split? If yes, collapse them.

Do not skip this step.

## Step 7 — Run tests after editing

Run the same pytest command again.

If tests fail:
- If the cause is obvious, make one targeted fix and run again.
- If still failing, stop and report clearly what broke and why.

## Step 8 — Report

If tests pass, summarize:
- The exact pytest command used
- The full violation list with line numbers
- What was changed
- Confirmation that logic and public API are preserved
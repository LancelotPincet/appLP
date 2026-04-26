## Docstring Rules

- All functions and classes must have a docstring.
- Private or simple helper functions may use a short one-line docstring.
- Public objects must have comprehensive docstrings.

## Public vs Private

- Public objects:
  - main `{myname}` objects,
  - objects exposed through `__init__.py`,
  - children in `parent` and `collab` doctypes.
- Private helpers:
  - functions in `_functions/` not meant for direct use,
  - files starting with `_`.

## General Style

- Use clear, concise language.
- Avoid unnecessary verbosity.
- Keep docstrings structured and readable.
- Do not include decorative formatting.

## One-Line Docstrings

- For simple helpers:
  - describe what the function does in one sentence.
  - no sections required.

Example:

    """Normalize input array shape."""

## Comprehensive Docstrings

Public objects must include:

- Summary
- Parameters
- Returns
- Raises (if relevant)
- Notes
- Examples

## Structure (NumPy-style)

Use a NumPy-style structure:

Summary line.

Parameters
----------
param1 : type
    Description.

param2 : type
    Description.

Returns
-------
type
    Description.

Raises
------
ErrorType
    Description.

Notes
-----
Detailed explanation of the logic.

Examples
--------
Example usage.

## Summary

- First line should be a short, clear description.
- Should describe the purpose of the object.

## Parameters

- Document all parameters.
- Include:
  - type
  - meaning
  - expected formats
- If multiple input modes exist, describe each clearly.

## Returns

- Describe all outputs.
- If multiple outputs, explain each one clearly.

## Raises

- Include when relevant.
- Document expected errors and when they occur.

## Notes

- This is a critical section for public objects.
- Must explain:
  - the algorithm or logic,
  - important transformations,
  - equations or models used,
  - assumptions made,
  - conventions and edge-case handling.
- The reader should understand the main algorithmic steps from this section.

## Examples

- Must include multiple examples when relevant.
- Cover:
  - standard usage,
  - edge cases,
  - different input formats,
  - different usage scenarios.
- If a parameter supports multiple modes, include one example per mode.
- Examples should be realistic and directly usable.

## Expectations

- After reading the docstring, the user should:
  - understand how the function works,
  - know how to use it,
  - understand its assumptions,
  - see how to apply it in different scenarios.

## Consistency

- Keep a consistent format across the entire library.
- Rewrite inconsistent docstrings when modifying code.
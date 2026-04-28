## Style

The goal is **compact readability**: the algorithm must be visible at a glance.
Sparse code that spreads simple things across many lines is a violation, not a
safe default.

When in doubt, make it shorter.

---

## Formatting rules

### One-argument-per-line is never acceptable

This is the most violated rule. It applies to calls, definitions, and
collections of any length. One item per line is always wrong.

```python
# WRONG — call
result = some_function(
    first_arg,
    second_arg,
    third_arg,
    fourth_arg,
)

# WRONG — definition
def some_function(
    first_arg,
    second_arg,
    third_arg,
    fourth_arg,
):

# WRONG — collection
KEYS = [
    "alpha",
    "beta",
    "gamma",
]
```

### If it fits on one line, keep it on one line

Collapse anything under 100 characters onto a single line.

```python
# WRONG
result = some_function(
    first_arg,
    second_arg,
)

# RIGHT
result = some_function(first_arg, second_arg)
```

```python
# WRONG
return (
    x[mask],
    y[mask],
)

# RIGHT
return x[mask], y[mask]
```

```python
# WRONG
KEYS = [
    "alpha",
    "beta",
    "gamma",
]

# RIGHT
KEYS = ["alpha", "beta", "gamma"]
```

### If it does not fit on one line, group by logical chunks

When a call, definition, or collection is too long for one line, group
related arguments together — never one per line.

```python
# WRONG — one arg per line
def integrate(crops, ch, x_fit, y_fit,
              channels_gains, channels_QE,
              channels_psf_sigmas_nm,
              channels_psf_xsigmas_nm,
              channels_psf_ysigmas_nm,
              cuda=False, parallel=True):

# RIGHT — grouped by role
def integrate(crops, ch, x_fit, y_fit,
              channels_gains, channels_QE,
              channels_psf_sigmas_nm, channels_psf_xsigmas_nm, channels_psf_ysigmas_nm,
              cuda=False, parallel=True):
```

```python
# WRONG — one arg per line
result = _normalize_channels_parameter(
    channels_psf_sigmas_nm,
    n_channels,
    "channels_psf_sigmas_nm",
)

# RIGHT — all on one line if it fits
result = _normalize_channels_parameter(channels_psf_sigmas_nm, n_channels, "channels_psf_sigmas_nm")

# RIGHT — grouped if too long
result = _normalize_channels_parameter(
    channels_psf_sigmas_nm, n_channels, "channels_psf_sigmas_nm",
    required=needs_spline,
)
```

```python
# WRONG — one item per line
PARAMS = [
    "alpha",
    "beta",
    "gamma",
    "delta",
    "epsilon",
    "zeta",
]

# RIGHT — grouped by chunks
PARAMS = [
    "alpha", "beta", "gamma",
    "delta", "epsilon", "zeta",
]
```

### Other formatting rules

**Keep comprehensions on one line when under 100 characters.**

```python
# RIGHT
pairs = [(x, y) for x in xs for y in ys if x != y]
```

**Use tuple unpacking when more compact.**

```python
# WRONG
a = result[0]
b = result[1]

# RIGHT
a, b = result
```

---

## Logic blocks

Write function bodies as sequential titled blocks. Do not extract a helper
just to name a block.

- Every meaningful block starts with a `# Title` comment
- Keep related operations together under one title
- No blank lines within a block; one blank line between blocks

```python
# Initialize containers
a, b, c = [], [], []

# Normalize inputs
x = np.asarray(x, dtype=np.float32)
y = np.asarray(y, dtype=np.float32)

# Build valid mask
mask = np.isfinite(x) & np.isfinite(y)
mask &= ids != 0  # zero means missing id

# Return filtered results
return x[mask], y[mask]
```

---

## Control flow

Inline short guards. Expand only when the condition or body is complex.

```python
# RIGHT
if value is None: return None

# RIGHT — complex enough to expand
if value is None:
    logger.warning("missing value")
    return None
```

Use early exits to keep the main logic flat.

---

## Comments

- Comment non-obvious lines, conventions, and key assumptions
- Do not comment obvious code
- No decorative banners or separators

---

## Helper functions

Extract a helper when:
- the same logic appears 3+ times
- the block is long or complex enough that naming it improves readability of the caller

Do not extract when:
- a titled inline block is already clear
- extraction would split closely related logic
- the helper would only be called once and is short

When unsure: keep it inline under a title comment.

---

## File structure

- Preserve top-of-file headers and module docstrings
- Use `# %% Section name` for major file regions
- Follow existing project patterns over external conventions
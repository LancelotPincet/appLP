## Docstrings

Every function and class must have a docstring. No exceptions.

---

## Public vs private

**Public** — full NumPy-style docstring required:
- the main object of a file (same name as the file)
- objects exposed in `applp/__init__.py`
- children in `parent` and `collab` doctypes

**Private** — one-line docstring only:
- files or objects starting with `_`
- objects not exposed at the package root

---

## Private docstrings

One sentence. Describes what it does, not how.

```python
def _normalize(x):
    """Normalize input array to float32 with shape (n,)."""
```

---

## Public docstrings

Use NumPy style. The section order is fixed:

```
Summary line.

Parameters
----------
name : type
    Description.

Returns
-------
name : type
    Description.

Raises
------
ErrorType
    When it is raised.

Notes
-----
...

Examples
--------
...
```

**Notes and Examples are mandatory** for every public object, even if Parameters or Returns are absent.

---

## Notes — mandatory

Notes must explain the algorithm internally, step by step.

**WRONG — too vague:**
```
Notes
-----
Fits a model to the input data and returns predictions.
```

**RIGHT — explains what happens internally:**
```
Notes
-----
1. Inputs are cast to float32 and checked for NaN/Inf.
2. A boolean mask selects valid rows; invalid rows are silently dropped.
3. The model is fit on the valid subset using least squares.
4. Predictions are returned in the original row order, with NaN
   for any row that was dropped.

Assumes x and y have the same length. Raises ValueError otherwise.
```

The reader must understand how the algorithm works, not just what it returns.

---

## Examples — mandatory

Examples must be explicit and runnable. Do not write placeholder examples.

**WRONG — trivial and useless:**
```
Examples
--------
>>> obj = MyClass(x, y)
>>> obj.fit()
```

**RIGHT — shows realistic inputs, multiple modes, edge cases:**
```
Examples
--------
Standard usage:

>>> import numpy as np
>>> x = np.array([1.0, 2.0, 3.0, 4.0])
>>> y = np.array([2.1, 3.9, 6.2, 7.8])
>>> model = MyClass(x, y)
>>> model.fit()
>>> model.predict(np.array([5.0]))
array([9.85])

With missing values (NaN rows are dropped silently):

>>> x = np.array([1.0, np.nan, 3.0])
>>> y = np.array([2.1, 3.9, 6.2])
>>> MyClass(x, y).fit().predict(np.array([2.0]))
array([4.05])

Empty input returns empty array:

>>> MyClass(np.array([]), np.array([])).fit().predict(np.array([1.0]))
array([])
```

If multiple modes exist, include at least one example per mode.
Prefer several simple examples over one complex one.

---

## Parameters and Returns

- Document every parameter: type, meaning, shape/format if relevant
- For multiple return values, describe each one separately
- Do not write "see above" or leave any field empty

---

## Consistency

- Same structure in every file
- Update docstrings whenever the code changes
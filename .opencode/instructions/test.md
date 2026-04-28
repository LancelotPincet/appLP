## Tests

Use pytest. Every `<name>_LP/` folder must contain `test_<name>.py`.

Tests define expected public behavior. A reader must understand how each
public object works just from reading the tests.

---

## What to test

Test every public object: the main object `<name>`, and all public children,
collaborators, and instances declared in `_doctype.txt`.

Each object must be covered for:
- normal behavior
- edge cases
- expected errors
- each mode or input format, if multiple exist

Use docstring examples as test cases when relevant.

---

## Imports

Always import from the package root:

```python
# RIGHT
from smlmlp import MyObject

# WRONG
from smlmlp.modules.myobject_LP.myobject import MyObject
```

Only import from internal paths when explicitly testing private behavior.

---

## Organization

Group tests by object using `# %%` sections. One test, one behavior.

```python
# %% MyObject

def test_myobject_standard():
    ...

def test_myobject_empty_input():
    ...

def test_myobject_raises_on_mismatched_lengths():
    ...


# %% MyChild

def test_mychild_basic():
    ...
```

---

## Style

- Small, explicit, readable test data
- No randomness, or use a fixed seed
- No external dependencies unless required
- Prefer explicit tests over parametrized templates when clearer

**WRONG — over-abstracted:**
```python
@pytest.mark.parametrize("inp,expected", CASES)
def test_all(inp, expected):
    assert MyObject(inp).run() == expected
```

**RIGHT — explicit and readable:**
```python
def test_returns_sorted_output():
    result = MyObject([3, 1, 2]).run()
    assert result == [1, 2, 3]

def test_empty_input_returns_empty():
    assert MyObject([]).run() == []
```

---

## Pytest tools

Use when they genuinely simplify:
- `pytest.raises` for expected errors
- `pytest.mark.parametrize` for tightly related cases with no logic difference
- fixtures for setup reused across 3+ tests

Do not use fixtures or parametrize to avoid writing explicit tests.

---

## Footer

End every test file and its associated main file with:

```python
if __name__ == "__main__":
    from corelp import test
    test(__file__)
```
## Testing Rules

- Tests use `pytest`.
- Each `{myname}_LP/` folder should contain a `test_myname.py` file.
- `test_myname.py` should test the behavior of all public objects in the module.
- Public objects include:
  - the main `{myname}` object,
  - public children in `parent` doctypes,
  - public collaborating objects in `collab` doctypes,
  - public instances in `instance` doctypes.

## Test Organization

- Organize tests by tested object.
- Use `# %%` sections to separate test groups.

Example:
```python
# %% test myname

def test_myname_normal_case():
    ...

def test_myname_edge_case():
    ...


# %% test child_object

def test_child_object_normal_case():
    ...
```

## Test Coverage

- Test normal behavior.
- Test edge cases.
- Test expected errors.
- Test important public behavior.
- Test different usage scenarios.
- If inputs support multiple modes, test each mode separately.
- Use docstring examples as starting points for tests when relevant.

## Test Style

- Keep tests deterministic, readable, and focused.
- Prefer simple tests over large, overly abstract test templates.
- Avoid fragile tests that depend on implementation details unless the behavior requires it.
- Use clear test names describing the behavior being tested.
- Keep each test focused on one behavior when practical.

## Pytest Usage

- Use `pytest` helpers when relevant:
  - `pytest.raises` for expected errors,
  - `pytest.mark.parametrize` for related input/output cases,
  - fixtures when setup is reused across multiple tests.
- Do not overuse fixtures or parametrization when simple explicit tests are clearer.

## Test Data

- Use small, readable test data.
- Avoid randomness unless explicitly controlled with a fixed seed.
- Avoid external dependencies, network calls, or environment-specific assumptions unless required.

## Footer

- Test files and the associated main files should all finish by :
```python

if __name__ == "__main__" :
    from corelp import test
    test(__file__)
```

## Goal

- Tests should verify public behavior, not private implementation.
- A reader should understand what the public objects are expected to do by reading the tests.
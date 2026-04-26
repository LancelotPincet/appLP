## Library Structure

- The library is organized under `src/applp` into two main parts:
  - `modules/`: reusable building blocks (functions, classes).
  - `routines/`: higher-level pipelines combining multiple modules into ready-to-use workflows.

## Module & Routine Layout

- Each module or routine follows this structure:

    {myname}_LP/
        myname.py
        test_myname.py
        _functions/
        _doctype.txt

- `{myname}` is the main public object name.
- The main object is defined in:
  - `myname.py`
  - and imported as: `from applp import myname`

## Design Philosophy

- Each `{myname}` represents a relatively independent building block.
- The main object defines the core logic.
- Additional behaviors and helpers are organized around it.

## `_functions/` Folder

- Contains additional functions related to `{myname}`.
- Structure depends on `_doctype.txt`.

### General rules

- Files in `_functions/`:
  - should be focused and small,
  - typically contain one main function per file.
- Files starting with `_` are private helpers and should be imported relatively.

## `_doctype.txt`

Defines how the module is structured and documented.

### `default`

- `myname.py` defines the main public object.
- `_functions/` contains helper functions.
- Only `myname` is considered public.

---

### `parent`

- `myname` is a parent object (e.g., class, decorator).
- `_functions/` contains subfolders grouping child objects.
- Each child is defined in its own file.
- Childs are public and usable independently.
- Documentation includes:
  - the parent object,
  - all children grouped by folder.

---

### `collab`

- `myname` and functions in `_functions/` are all public.
- They are designed to work together in a shared logic.
- Each object is independently usable.

---

### `instance`

- `myname` defines an instance from a private class.
- The class is not intended for direct use.
- Documentation focuses on the instance usage.
- `_functions/` contains helper functions.

## Imports & Exposure

- A script automatically:
  - scans `.py` files not starting with `_` or `test`,
  - adds lazy imports to the main `__init__.py`.
- Each file defines one main object named after the file.
- All such objects become importable from the package root directly with ```from applp import myname```.
- File names must therefore be unique across the package.

## Testing

- Each `{myname}_LP` folder contains:
  - `test_myname.py`
- Testing rules and coverage requirements are defined in `test.md`.

## Documentation

- All documentation rules are defined in `docstrings.md`.

## Design Principles

- Favor modular, independent building blocks.
- Keep logic grouped around a central object (`myname`).
- Avoid tightly coupled cross-module dependencies.
- Keep helper functions local to their module when possible.
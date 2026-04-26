## Code Style

- Prefer compact code that preserves a clear overview of the logic.
- Avoid overly sparse code; do not split simple logic unnecessarily.
- Favor chronological, readable blocks of logic inside functions.

### File Structure

- Preserve top-of-file header comments such as date, author, license, and metadata.
- Preserve top-level module docstrings unless explicitly asked to change them.
- Use `# %% Section name` sections to separate major file regions when helpful, such as imports, constants, functions, and tests.

### Line Length & Formatting

- Keep lines under ~100 characters when possible.
- Break lines when they become too long, dense, or harder to read.
- Keep simple expressions on one line when they remain clear:
  - simple list comprehensions,
  - simple double-loop comprehensions,
  - function calls with few arguments,
  - small lists, tuples, sets, and dictionaries.
- Avoid over-fragmenting short or simple code across many lines.
- Keep short related assignments grouped together.

### Control Flow

- Allow short inline control flow when clear:
  - `if condition: continue`
  - `if condition: break`
  - `if condition: simple_function()`
- Expand control flow to multiple lines when the condition or action is non-trivial.
- Prefer readable early exits when they simplify the logic.

### Logical Blocks

- Organize code into compact, coherent logical blocks.
- Precede meaningful blocks with short title comments, such as:
  - `# Normalize inputs`
  - `# Get doc type`
  - `# Write output`
- Comments may describe the next compact block even when the code is fairly readable.
- Keep related steps close together when that improves the overview.

### Functions & Abstraction

- Use helper functions when:
  - they represent a meaningful algorithmic step,
  - they are reused multiple times,
  - or they clearly improve the overview of a long function.
- Avoid creating helper functions used only once if they only replace a short titled block.
- Inline short, single-use logic blocks and document them with a short comment instead.
- Consider extracting a helper function when a block exceeds ~15 lines, forms a clear reusable or algorithmic unit, and extraction improves clarity.

### Comments

- Use comments frequently to explain intent, steps, and structure.
- Prefer short comments above logical blocks.
- Add short inline comments for non-obvious operations or important details.
- Comments should explain what the block is doing or why it exists.
- Avoid comments that only restate the exact code mechanically.
- Avoid decorative or noisy comment styles: no boxes, banners, or repeated symbol separators.

### General Principle

- Prefer existing project patterns over introducing new ones.
- Favor compact readability: dense enough to keep the algorithm visible, but not so dense that a line carries too much information.
- These rules can be relaxed when another structure clearly improves understanding.
# Markdown Validation Rules

This document explains the validation rules applied by the markdown validator.

## Standard Markdown Syntax

### Headings

**ATX-style headings (preferred)**
- Must have space after `#` characters
- Example: `# Heading 1`, `## Heading 2`
- Invalid: `#Heading` (missing space)

**Heading hierarchy**
- Should not skip levels (e.g., `#` to `###`)
- This is a warning, not an error

**Setext-style headings**
- Underlined with `=` or `-`
- Less common; validator flags for potential conversion to ATX style
- These are logged as uncertain changes

### Lists

**Unordered lists**
- Must have single space after marker (`*`, `-`, or `+`)
- Example: `* Item one`
- Invalid: `*Item` or `*  Item` (no space or multiple spaces)

**Ordered lists**
- Must have single space after number and period
- Example: `1. First item`
- Invalid: `1.Item` or `1.  Item`

**List marker consistency**
- While mixed markers are valid markdown, consistency is preferred
- The validator does not enforce marker type but notes inconsistencies

### Links and Images

**Inline links**
- Format: `[text](url)`
- Must have both text and URL
- Bare URLs should be wrapped in `< >` or proper link syntax

**Reference links**
- Format: `[text][ref]` with `[ref]: url` elsewhere
- Validator checks that references exist

**Broken links**
- Flags `[text]` without URL or reference

### Code Blocks

**Fenced code blocks (preferred)**
- Enclosed by ` ``` ` or `~~~` (minimum 3 characters)
- Opening and closing fences must match
- Example:
  ````markdown
  ```python
  def hello():
      print("world")
  ```
  ````

**Indented code blocks**
- 4 spaces or 1 tab
- Less explicit; validator suggests conversion to fenced blocks

### Emphasis

**Italic**
- Single `*` or `_`: `*italic*` or `_italic_`

**Bold**
- Double `**` or `__`: `**bold**` or `__bold__`

**Mismatched markers**
- `*text_` or `_text*` are errors
- Opening and closing markers must match

### Horizontal Rules

- Require at least 3 characters: `---`, `***`, or `___`
- Can have spaces between characters: `- - -`
- Invalid: `--` (only 2 characters)

### Whitespace

**Trailing whitespace**
- Two spaces at line end create a line break (intentional)
- Other trailing whitespace is flagged as uncertain
- Leading/trailing whitespace in the file is preserved

**Line endings**
- Validator prefers Unix-style (LF) but doesn't enforce
- Formatter normalizes to LF

## Markdown-it Extensions

These extensions are checked by the extension checker script.

### Containers

**Syntax:** `:::name` ... `:::`

- Opening and closing markers must match
- Must have equal number of colons (minimum 3)
- Container type is optional but recommended

**Example:**
```markdown
:::warning
This is a warning message.
:::
```

### Admonitions

Special container types for callouts:
- `:::note` - Informational note
- `:::tip` - Helpful tip
- `:::warning` - Warning message
- `:::danger` - Danger/error message
- `:::info` - General information
- `:::caution` - Caution message

### Definition Lists

**Syntax:**
```markdown
Term
: Definition

Another term
: Another definition
```

- Term line followed by `: definition` line
- Validator checks that definitions have terms

### Footnotes

**Reference:** `[^1]`, `[^note]`, etc.

**Definition:** `[^1]: Footnote text`

- Validator checks that:
  - All references have definitions
  - No duplicate definitions
  - Unused definitions are flagged as uncertain

### Task Lists

**Syntax:**
```markdown
- [ ] Unchecked task
- [x] Checked task
```

- Must have space after checkbox
- Prefer lowercase `x` for checked items
- Must be part of a list (start with `*`, `-`, or `+`)

### Custom Attributes

**Syntax:** `{.class #id key=value}`

- Classes start with `.`
- IDs start with `#`
- Attributes are `key=value` pairs
- Can be applied to various elements depending on plugin

**Example:**
```markdown
# Heading {#custom-id .important}

Paragraph with custom class.
{.highlight}
```

## Validation Philosophy

### Text Content Preservation

**CRITICAL:** The validator and formatter NEVER modify text content.

This means:
- No rewording, rephrasing, or content changes
- No fixing of spelling or grammar
- No restructuring of sentences or paragraphs
- Only markdown syntax and formatting are modified

### Certain vs. Uncertain Changes

**Certain changes** (applied automatically by formatter):
- Adding missing space after `#` in headings
- Fixing list marker spacing
- Normalizing code fence markers
- Fixing clearly mismatched emphasis markers
- Ensuring final newline

**Uncertain changes** (logged for manual review):
- Converting setext to ATX headings
- Converting indented code blocks to fenced
- Changing bare URLs to links
- Removing trailing whitespace (might be intentional line break)
- Removing unused footnotes
- Unknown admonition types

### Severity Levels

**Error:** Clear syntax violation
- Mismatched markers
- Unclosed code fences
- Broken link syntax

**Warning:** Potential issue or style concern
- Heading hierarchy skipped
- Missing footnote definitions
- Inconsistent style

**Uncertain:** Change depends on context
- Setext vs. ATX heading preference
- Bare URLs
- Trailing whitespace

## Working with Specifications

When a specification file is provided:

1. The checker extracts extension definitions
2. Validates content matches spec syntax
3. Cross-references with example files
4. Reports deviations from spec

The specification should document:
- Extension names
- Syntax patterns
- Required and optional elements
- Valid values/types
- Examples of correct usage

## Working with Examples

Example files help the validator:
1. Learn valid patterns from real usage
2. Identify common extension use cases
3. Provide context for validation decisions
4. Serve as reference for uncertain cases

The validator uses examples to:
- Confirm extension syntax
- Validate custom patterns
- Check consistency with existing content

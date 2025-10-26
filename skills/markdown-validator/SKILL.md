---
name: markdown-validator
description: Validate and format markdown files using linters and formatters, checking custom markdown-it extensions against specifications and example documents. CRITICAL - preserves all text content while fixing only markdown syntax and formatting. Use when validating .md files, checking markdown syntax, formatting markdown documents, or verifying custom markdown extensions are used correctly.
---

# Markdown Validator

Validate and format markdown files with focus on syntax correctness and custom extension compliance, while ensuring zero changes to text content.

## Critical Principle: Text Content Preservation

**NEVER modify text content during validation or formatting.** This skill only corrects markdown syntax and formatting. Any change that affects the actual text, wording, or meaning must be logged for manual review, never applied automatically.

## Workflow Overview

When validating markdown files, follow this process:

1. **Understand the requirements** - Determine if spec/examples are provided
2. **Validate syntax** - Check standard markdown correctness
3. **Check extensions** - Verify custom markdown-it extension usage
4. **Format safely** - Apply only certain corrections
5. **Log uncertainties** - Document all questionable changes for review

## Step 1: Understanding Requirements

Before validating, determine what materials are available:

**Ask these questions:**
- Is there a markdown specification document?
- Are there example markdown files showing correct usage?
- What custom markdown-it extensions should be validated?
- Should validation be strict (errors only) or include warnings?

**Locate resources:**
- Specification file: Describes syntax rules and extensions
- Examples directory: Contains reference markdown files
- Both are optional but improve validation accuracy

## Step 2: Standard Markdown Validation

Use `scripts/validate_markdown.py` to check standard markdown syntax.

**Basic usage:**
```bash
python scripts/validate_markdown.py <file.md>
python scripts/validate_markdown.py <directory/>
```

**With specification and examples:**
```bash
python scripts/validate_markdown.py <file.md> --spec spec.md --examples examples/
```

**What it checks:**
- Heading structure and hierarchy
- List formatting and spacing
- Link and image syntax
- Code block delimiters
- Emphasis marker matching
- Horizontal rule syntax
- Trailing whitespace patterns

**Output:**
- Console report of issues found
- `markdown_validation_report.json` with detailed results
- Exit code 0 if valid, 1 if issues found

**Key validation rules:**
- Headings must have space after `#`
- Lists must have single space after marker
- Code fences must match (opening and closing)
- Emphasis markers must be paired correctly

See `references/validation_rules.md` for complete rule documentation.

## Step 3: Custom Extension Checking

Use `scripts/check_extensions.py` to validate markdown-it extension usage.

**Basic usage:**
```bash
python scripts/check_extensions.py <file.md>
python scripts/check_extensions.py <directory/>
```

**With specification and examples:**
```bash
python scripts/check_extensions.py <file.md> --spec spec.md --examples examples/
```

**Extensions checked:**
- **Containers** - `:::name` ... `:::` blocks
- **Admonitions** - Special container types (note, warning, tip, etc.)
- **Definition lists** - Term/definition pairs
- **Footnotes** - `[^1]` references and definitions
- **Task lists** - `- [ ]` and `- [x]` checkboxes
- **Custom attributes** - `{.class #id key=value}` syntax

**Output:**
- Console report of extension issues
- `extension_check_report.json` with detailed results
- Exit code 0 if valid, 1 if issues found

**When to use:**
- Working with markdown-it plugins
- Validating custom syntax against spec
- Checking extension consistency across files

## Step 4: Safe Formatting

Use `scripts/format_markdown.py` to fix certain syntax issues.

**Basic usage:**
```bash
python scripts/format_markdown.py <file.md>
```

**Format in place:**
```bash
python scripts/format_markdown.py <file.md> --in-place
```

**Custom review file:**
```bash
python scripts/format_markdown.py <file.md> --review my_review.md
```

**What it fixes automatically:**
- Missing space after `#` in headings
- Incorrect list marker spacing
- Code fence marker inconsistency (normalizes to ```)
- Clearly mismatched emphasis markers
- Line ending normalization (to LF)
- Missing final newline

**What it logs for review:**
- Setext heading conversion suggestions
- Indented code block conversion
- Bare URL link suggestions
- Trailing whitespace removal
- Unused footnote definitions
- Unknown admonition types

**Output:**
- Formatted file (`.formatted.md` or in-place)
- `formatting_review.md` with uncertain changes
- `formatting_report.json` with all changes
- Exit code 0 if successful, 1 if errors

**CRITICAL:** Formatter never modifies text content, only markdown syntax.

## Step 5: Manual Review Process

After formatting, always review uncertain changes:

1. **Read the review file** (`formatting_review.md` or custom path)
2. **For each logged change:**
   - Understand the context and reason
   - Verify the suggested change preserves meaning
   - Manually apply if appropriate
   - Skip if change would alter text content or meaning
3. **Revalidate** after manual changes

**Review file format:**
```markdown
## Line 42

**Type:** trailing_whitespace

**Reason:** Trailing whitespace (may be intentional for line break)

**Current content:**
...content...
```

## Working with Specifications

When a specification document is provided:

**Spec should include:**
- Extension names and descriptions
- Syntax patterns with examples
- Required vs. optional elements
- Valid values and types
- Usage guidelines

**How the validator uses specs:**
- Extracts extension definitions
- Validates syntax matches spec
- Cross-references with examples
- Reports deviations

**Spec format example:**
```markdown
## Container Extension

**Extension:** container
**Syntax:** `:::type` content `:::`

### Valid Types
- note
- warning
- tip
- danger

### Example
:::warning
This is a warning message.
:::
```

## Working with Examples

Example files provide real-world validation patterns:

**Example directory structure:**
```
examples/
├── basic.md          # Basic markdown features
├── extensions.md     # Custom extensions
├── complex.md        # Advanced usage
└── spec-example.md   # Spec-compliant example
```

**How the validator uses examples:**
- Learns valid usage patterns
- Identifies common conventions
- Provides context for validation
- Serves as reference for edge cases

**Best practices:**
- Include diverse examples
- Show correct extension usage
- Cover edge cases
- Document any intentional style choices

## Common Validation Scenarios

### Scenario 1: Quick syntax check
```bash
python scripts/validate_markdown.py document.md
```
Review console output for issues.

### Scenario 2: Fix formatting automatically
```bash
python scripts/format_markdown.py document.md --in-place
cat formatting_review.md  # Review uncertain changes
```
Manually apply changes from review file if appropriate.

### Scenario 3: Validate with specification
```bash
python scripts/check_extensions.py document.md --spec markdown-spec.md
```
Ensure custom extensions match spec.

### Scenario 4: Batch validation
```bash
python scripts/validate_markdown.py docs/ > validation_summary.txt
python scripts/check_extensions.py docs/ > extension_summary.txt
```
Review JSON reports for detailed analysis.

### Scenario 5: Complete workflow
```bash
# 1. Validate
python scripts/validate_markdown.py doc.md --spec spec.md --examples examples/

# 2. Check extensions
python scripts/check_extensions.py doc.md --spec spec.md --examples examples/

# 3. Format safely
python scripts/format_markdown.py doc.md --review review.md

# 4. Review and manually apply changes from review.md

# 5. Revalidate
python scripts/validate_markdown.py doc.md
```

## Output Files Reference

**Validation outputs:**
- `markdown_validation_report.json` - Detailed validation results
- Console output - Human-readable summary

**Extension check outputs:**
- `extension_check_report.json` - Extension validation details
- Console output - Issue summary

**Formatting outputs:**
- `<filename>.formatted.md` - Formatted file (if not in-place)
- `formatting_review.md` - Uncertain changes for review
- `formatting_report.json` - All changes applied and logged
- Console output - Change summary

## Integration with External Tools

While this skill provides comprehensive validation, you may also use:

**markdownlint** (if available):
```bash
markdownlint document.md
```

**remark** (if available):
```bash
remark document.md --use remark-lint
```

**prettier** (if available):
```bash
prettier --check document.md
```

These tools complement the skill's scripts but may not handle custom extensions.

## Troubleshooting

**Script not executable:**
```bash
chmod +x scripts/*.py
```

**Python dependencies missing:**
The scripts use only Python standard library, no installation needed.

**Encoding errors:**
All scripts use UTF-8 encoding. Ensure files are UTF-8 encoded.

**Empty validation reports:**
Check that files have `.md` extension and contain markdown content.

**Custom extension not recognized:**
Provide specification file with `--spec` flag or add extension rules to `check_extensions.py`.

## References

For detailed information on validation rules, see:
- `references/validation_rules.md` - Complete rule documentation

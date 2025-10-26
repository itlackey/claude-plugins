# Markdown Validator Skill

A comprehensive skill for validating and formatting markdown files with support for custom markdown-it extensions.

## Overview

This skill provides three main capabilities:
1. **Standard Markdown Validation** - Check syntax correctness of standard markdown
2. **Custom Extension Checking** - Validate markdown-it plugin usage against specifications
3. **Safe Formatting** - Automatically fix certain issues while logging uncertain changes

## Critical Feature: Text Content Preservation

**The skill NEVER modifies text content.** It only corrects markdown syntax and formatting. Any changes that might affect the actual text are logged for manual review.

## What's Included

### Scripts
- `validate_markdown.py` - Validates standard markdown syntax
- `check_extensions.py` - Checks custom markdown-it extension usage
- `format_markdown.py` - Safely formats markdown files

### References
- `validation_rules.md` - Complete documentation of validation rules

## Installation

1. Download the `markdown-validator.skill` file
2. Import it into Claude (via the skills interface)
3. The skill will be available for use

## Quick Start

### Validate a Markdown File
```bash
python scripts/validate_markdown.py document.md
```

### Check Custom Extensions
```bash
python scripts/check_extensions.py document.md
```

### Format a File (with manual review)
```bash
python scripts/format_markdown.py document.md
# Review uncertain changes in formatting_review.md
# Apply manual changes as needed
```

## What Gets Validated

### Standard Markdown
- **Headings**: Proper spacing, hierarchy
- **Lists**: Consistent spacing, proper nesting
- **Links**: Complete syntax, valid references
- **Code blocks**: Matching fences, proper delimiters
- **Emphasis**: Matched markers
- **Horizontal rules**: Minimum characters
- **Whitespace**: Trailing spaces, line endings

### Custom Extensions (markdown-it)
- **Containers**: `:::type` ... `:::` blocks
- **Admonitions**: Note, tip, warning, danger, etc.
- **Definition lists**: Term/definition pairs
- **Footnotes**: `[^1]` references and definitions
- **Task lists**: `- [ ]` checkboxes
- **Custom attributes**: `{.class #id key=value}`

## What Gets Fixed Automatically

The formatter applies these changes with 100% confidence:
- Missing space after `#` in headings
- Incorrect list marker spacing
- Code fence inconsistency (normalizes to ```)
- Clearly mismatched emphasis markers
- Line ending normalization (to LF)
- Missing final newline

## What Gets Logged for Review

These changes are uncertain and require manual verification:
- Setext heading conversion to ATX style
- Indented code block conversion to fenced
- Bare URL wrapping suggestions
- Trailing whitespace removal
- Unused footnote definitions
- Unknown admonition types

## Usage Examples

### Example 1: Basic Validation
```bash
# Validate a single file
python scripts/validate_markdown.py README.md

# Validate all markdown files in a directory
python scripts/validate_markdown.py docs/
```

### Example 2: With Specification
```bash
# Validate against a spec document
python scripts/validate_markdown.py doc.md --spec markdown-spec.md

# Also use example files as reference
python scripts/validate_markdown.py doc.md --spec spec.md --examples examples/
```

### Example 3: Format and Review
```bash
# Format file (creates .formatted.md)
python scripts/format_markdown.py document.md

# Format in place
python scripts/format_markdown.py document.md --in-place

# Custom review file location
python scripts/format_markdown.py document.md --review my-review.md
```

### Example 4: Complete Workflow
```bash
# 1. Validate syntax
python scripts/validate_markdown.py doc.md

# 2. Check extensions
python scripts/check_extensions.py doc.md --spec spec.md

# 3. Format safely
python scripts/format_markdown.py doc.md --review changes.md

# 4. Review changes.md and apply manually

# 5. Revalidate
python scripts/validate_markdown.py doc.md
```

## Output Files

### Validation
- `markdown_validation_report.json` - Detailed validation results
- Console output with human-readable summary

### Extension Checking
- `extension_check_report.json` - Extension validation details
- Console output with issue summary

### Formatting
- `<filename>.formatted.md` - Formatted version (if not in-place)
- `formatting_review.md` - Changes needing manual review
- `formatting_report.json` - All changes (applied and logged)

## Working with Specifications

If you have a markdown specification document, provide it with `--spec`:

```bash
python scripts/check_extensions.py doc.md --spec your-spec.md
```

Your spec should document:
- Extension names and descriptions
- Syntax patterns with examples
- Valid values and types
- Usage guidelines

Example spec format:
```markdown
## Container Extension

**Extension:** container
**Syntax:** `:::type` content `:::`

### Valid Types
- note
- warning
- tip

### Example
:::warning
Warning message
:::
```

## Working with Examples

Example files help the validator learn valid patterns:

```bash
python scripts/validate_markdown.py doc.md --examples examples/
```

Example directory structure:
```
examples/
├── basic.md          # Basic markdown
├── extensions.md     # Custom extensions
├── advanced.md       # Advanced usage
```

## Troubleshooting

**Scripts not executable?**
```bash
chmod +x scripts/*.py
```

**Python not found?**
- Scripts require Python 3.6+
- Use only standard library (no pip install needed)

**Encoding errors?**
- Ensure files are UTF-8 encoded

**Empty reports?**
- Check files have `.md` extension
- Verify files contain markdown content

## Testing

The skill includes test files demonstrating functionality:
- `test_document.md` - Sample file with various issues
- Can be used to verify scripts work correctly

## Features

✅ **Text content preservation** - Never modifies actual text  
✅ **Zero dependencies** - Uses only Python standard library  
✅ **Comprehensive validation** - Checks standard and custom markdown  
✅ **Safe formatting** - Only applies certain changes  
✅ **Manual review** - Logs uncertain changes for review  
✅ **Spec support** - Validates against custom specifications  
✅ **Example learning** - Uses example files as reference  
✅ **Batch processing** - Handles directories of files  
✅ **Detailed reports** - JSON and human-readable output  

## Best Practices

1. **Always review** the formatting_review.md file after formatting
2. **Provide specifications** when working with custom extensions
3. **Include examples** to improve validation accuracy
4. **Run validation** after making manual changes
5. **Commit frequently** when making bulk changes
6. **Test first** on a single file before batch processing

## License

This skill is provided as-is for markdown validation and formatting tasks.

## Support

For issues or questions about this skill:
- Review the SKILL.md file for detailed usage
- Check references/validation_rules.md for rule documentation
- Test with test_document.md to verify functionality

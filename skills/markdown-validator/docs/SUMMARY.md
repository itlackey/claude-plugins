# Markdown Validator Skill - Summary

## What You're Getting

A complete skill for validating and formatting markdown files with these three Python scripts:

1. **validate_markdown.py** - Validates standard markdown syntax
2. **check_extensions.py** - Checks custom markdown-it extensions 
3. **format_markdown.py** - Safely formats files

## Key Features

### Text Content is NEVER Modified
The most important feature: All scripts only modify markdown syntax and formatting. Text content is completely preserved. Any uncertain changes are logged for manual review rather than applied automatically.

### What Gets Fixed Automatically
- Missing space after `#` in headings (e.g., `##Heading` → `## Heading`)
- List marker spacing issues (e.g., `*Item` → `* Item`)
- Code fence consistency (normalizes `~~~` to ` ``` `)
- Clearly mismatched emphasis markers (e.g., `*text_` → `*text*`)
- Line endings (normalizes to LF)
- Missing final newline

### What Gets Logged for Review
- Setext heading conversions (underlined headings)
- Indented code block conversions
- Bare URL wrapping suggestions
- Trailing whitespace (might be intentional line breaks)
- Unknown admonition/extension types
- Unused footnote definitions

## Quick Start Commands

```bash
# Validate a file
python scripts/validate_markdown.py document.md

# Check extensions with spec
python scripts/check_extensions.py document.md --spec spec.md --examples examples/

# Format safely and review
python scripts/format_markdown.py document.md
# Then check formatting_review.md for manual changes
```

## Output Files

Each script creates:
- **JSON report** - Machine-readable detailed results
- **Console output** - Human-readable summary
- **Review file** (formatter only) - Changes needing manual verification

## Validated Extensions

The skill checks these markdown-it extensions:
- Containers (`:::type` ... `:::`)
- Admonitions (note, tip, warning, danger, info, caution)
- Definition lists
- Footnotes (`[^1]`)
- Task lists (`- [ ]` and `- [x]`)
- Custom attributes (`{.class #id key=value}`)

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)
- Works on any platform (Windows, Mac, Linux)

## File Structure

```
markdown-validator/
├── SKILL.md                        # Main skill documentation
├── scripts/
│   ├── validate_markdown.py        # Syntax validator
│   ├── check_extensions.py         # Extension checker
│   └── format_markdown.py          # Safe formatter
└── references/
    └── validation_rules.md         # Complete rule documentation
```

## Workflow Recommendation

1. **Validate** first to see all issues: `validate_markdown.py`
2. **Check extensions** if using custom syntax: `check_extensions.py`
3. **Format** to auto-fix certain issues: `format_markdown.py`
4. **Review** the `formatting_review.md` file
5. **Apply** manual changes from review
6. **Revalidate** to confirm everything is correct

## Why Use This Skill?

- **Safe**: Never modifies text content
- **Comprehensive**: Checks both standard and custom markdown
- **Intelligent**: Distinguishes certain from uncertain changes
- **Transparent**: Logs all changes with clear reasoning
- **Flexible**: Works with specifications and examples
- **Portable**: No dependencies beyond Python standard library

## Common Use Cases

1. **Documentation maintenance** - Ensure docs follow consistent style
2. **Content validation** - Check markdown files before publishing
3. **CI/CD integration** - Validate markdown in automated pipelines
4. **Migration** - Convert between markdown dialects
5. **Quality assurance** - Enforce markdown standards across team
6. **Extension verification** - Ensure custom syntax is used correctly

## Next Steps

1. Download `markdown-validator.skill`
2. Install in Claude skills
3. Read the full `README.md` for detailed usage
4. Check `SKILL.md` for workflow guidance
5. Review `validation_rules.md` for all rules

The skill is ready to use immediately with zero configuration!

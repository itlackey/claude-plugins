# Markdown Validator - Usage Examples

This document provides real-world examples of using the markdown validator skill.

## Example 1: Basic Validation

**Scenario**: You have a README.md file and want to check for syntax issues.

```bash
# Run validation
python scripts/validate_markdown.py README.md
```

**Sample Output**:
```
============================================================
File: README.md
Valid: False

Issues found: 3
  Line 5 [ERROR] heading_format: Heading must have space after #
  Line 23 [ERROR] list_spacing: List item should have single space after marker
  Line 45 [WARNING] heading_hierarchy: Heading level skipped from 2 to 4
```

**Next Steps**: Review the issues and decide whether to fix them manually or use the formatter.

---

## Example 2: Format and Review

**Scenario**: You want to automatically fix simple issues but review uncertain changes.

```bash
# Format the file
python scripts/format_markdown.py README.md --in-place

# Review uncertain changes
cat formatting_review.md
```

**Sample Review File**:
```markdown
# Markdown Formatting Review

## Line 34

**Type:** trailing_whitespace
**Reason:** Trailing whitespace (may be intentional for line break)

**Current content:**
This line has trailing spaces.  

---

## Line 56

**Type:** bare_url
**Reason:** Bare URL - consider wrapping in < > or proper link syntax

**Current content:**
Check out https://example.com for more info.
```

**Next Steps**: 
- Line 34: Keep the trailing spaces (intentional line break)
- Line 56: Manually change to `Check out [https://example.com](https://example.com) for more info.`

---

## Example 3: Custom Extensions with Spec

**Scenario**: Your team uses custom markdown-it extensions and you have a specification document.

**Your spec file (markdown-spec.md)**:
```markdown
# Custom Markdown Extensions

## Admonitions

**Extension:** admonition
**Syntax:** `:::type` content `:::`

### Valid Types
- note
- warning
- tip
- danger
- info

### Example
:::warning
This is important!
:::
```

**Check your document**:
```bash
python scripts/check_extensions.py docs/guide.md --spec markdown-spec.md
```

**Sample Output**:
```
============================================================
File: docs/guide.md
Valid: False

Extension issues found: 2
  Line 12 [ERROR] container: Unclosed container of type "note"
  Line 34 [WARNING] admonition: Unknown admonition type "alert"

Uncertain changes: 1
  Line 45 [admonition]: Unknown admonition type "alert" - verify this is correct
```

**Next Steps**:
- Line 12: Add closing `:::` 
- Line 34: Change `:::alert` to `:::warning` (per spec)

---

## Example 4: Batch Processing

**Scenario**: You have a docs/ directory with many markdown files to validate.

```bash
# Validate all files
python scripts/validate_markdown.py docs/ > validation_summary.txt

# Check for files with issues
grep "Valid: False" validation_summary.txt

# Review detailed JSON report
cat markdown_validation_report.json | python -m json.tool
```

**Automated filtering**:
```bash
# Find all files with errors (not warnings)
python3 << 'EOF'
import json
with open('markdown_validation_report.json') as f:
    data = json.load(f)
    
for result in data:
    errors = [i for i in result.get('issues', []) if i['severity'] == 'error']
    if errors:
        print(f"{result['filepath']}: {len(errors)} errors")
EOF
```

---

## Example 5: CI/CD Integration

**Scenario**: Add markdown validation to your CI pipeline.

**GitHub Actions Example** (.github/workflows/markdown-lint.yml):
```yaml
name: Markdown Validation

on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      
      - name: Validate Markdown
        run: |
          python scripts/validate_markdown.py docs/
          
      - name: Check Extensions
        run: |
          python scripts/check_extensions.py docs/ --spec docs/markdown-spec.md
      
      - name: Upload Reports
        if: failure()
        uses: actions/upload-artifact@v2
        with:
          name: validation-reports
          path: '*.json'
```

---

## Example 6: Pre-commit Hook

**Scenario**: Validate markdown files before every commit.

**Create .git/hooks/pre-commit**:
```bash
#!/bin/bash

# Get staged markdown files
STAGED_MD=$(git diff --cached --name-only --diff-filter=ACM | grep '\.md$')

if [ -n "$STAGED_MD" ]; then
    echo "Validating markdown files..."
    
    for file in $STAGED_MD; do
        python scripts/validate_markdown.py "$file"
        if [ $? -ne 0 ]; then
            echo "❌ Validation failed for $file"
            echo "Please fix the issues or use --no-verify to skip"
            exit 1
        fi
    done
    
    echo "✅ All markdown files validated successfully"
fi

exit 0
```

Make it executable:
```bash
chmod +x .git/hooks/pre-commit
```

---

## Example 7: Migration from Different Markdown Dialect

**Scenario**: Converting setext-style headings to ATX style.

**Input file**:
```markdown
Main Title
==========

This is a section.

Subsection
----------

More content here.
```

**Steps**:
1. Run validator to identify setext headings:
```bash
python scripts/validate_markdown.py document.md
```

2. Check the uncertain changes:
```bash
python scripts/format_markdown.py document.md
cat formatting_review.md
```

3. Review suggests conversion:
```
Line 1: setext_heading
Current: Main Title
         ==========
Suggested: # Main Title
Reason: Setext-style heading - ATX style is more common
```

4. Apply manually or accept the suggestion.

---

## Example 8: Footnote Validation

**Scenario**: Ensuring all footnotes are properly defined.

**Input file**:
```markdown
This has a footnote[^1] and another[^2] and one more[^3].

[^1]: First footnote
[^2]: Second footnote
```

**Run extension checker**:
```bash
python scripts/check_extensions.py document.md
```

**Output**:
```
Extension issues found: 1
  Line 0 [WARNING] footnote: Footnote reference [^3] without definition
```

**Next Steps**: Add the missing footnote definition:
```markdown
[^3]: Third footnote
```

---

## Example 9: Working with Examples

**Scenario**: You have example markdown files showing correct usage.

**Directory structure**:
```
examples/
├── basic.md          # Basic syntax examples
├── extensions.md     # Custom extensions
└── style-guide.md    # Team style preferences
```

**Run with examples**:
```bash
python scripts/check_extensions.py document.md \
  --spec spec.md \
  --examples examples/
```

The validator will:
1. Load specification rules
2. Learn patterns from example files
3. Cross-reference your document against both
4. Report deviations

---

## Example 10: Custom Review File Location

**Scenario**: You want to organize review files in a specific directory.

```bash
# Create reviews directory
mkdir -p reviews

# Format with custom review location
python scripts/format_markdown.py document.md \
  --review reviews/document-review-$(date +%Y%m%d).md

# Later, review all pending changes
ls reviews/
cat reviews/document-review-20250126.md
```

---

## Best Practices Summary

1. **Validate First**: Always run validation before formatting
   ```bash
   python scripts/validate_markdown.py file.md
   ```

2. **Review Changes**: Always check `formatting_review.md` after formatting
   ```bash
   python scripts/format_markdown.py file.md
   cat formatting_review.md
   ```

3. **Use Specs**: Provide specification files when working with custom extensions
   ```bash
   python scripts/check_extensions.py file.md --spec spec.md
   ```

4. **Batch Wisely**: Test on one file before batch processing
   ```bash
   # Test first
   python scripts/validate_markdown.py sample.md
   
   # Then batch
   python scripts/validate_markdown.py docs/
   ```

5. **Keep Specs Updated**: Update your specification as extensions evolve

6. **Version Control**: Commit the skill files and specs to your repository

7. **Document Decisions**: Add comments in review files about why changes were skipped

8. **Automate**: Integrate validation into your CI/CD pipeline

9. **Train Team**: Share examples of correct usage

10. **Iterate**: Refine validation rules based on your team's needs

---

## Troubleshooting Common Issues

### Issue: Too Many Warnings

**Solution**: Focus on errors first, treat warnings as suggestions
```bash
# Filter for errors only
python scripts/validate_markdown.py doc.md | grep ERROR
```

### Issue: False Positives

**Solution**: Review uncertain changes carefully - they're flagged for a reason
```markdown
# In formatting_review.md
## Line 42
Reason: Trailing whitespace (may be intentional for line break)

# Decision: Keep it, it's intentional
```

### Issue: Custom Extension Not Recognized

**Solution**: Add it to your specification file
```markdown
# In spec.md
## Custom Extension

**Extension:** my-custom-extension
**Syntax:** `[[custom]]` ... `[[/custom]]`
```

### Issue: Batch Processing Too Slow

**Solution**: Process files in parallel
```bash
find docs -name '*.md' | parallel python scripts/validate_markdown.py
```

---

## Advanced Usage

### Integrate with VS Code

Create `.vscode/tasks.json`:
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Validate Markdown",
      "type": "shell",
      "command": "python",
      "args": [
        "scripts/validate_markdown.py",
        "${file}"
      ],
      "group": "test"
    }
  ]
}
```

### Create Wrapper Script

Make validation easier with a wrapper:
```bash
#!/bin/bash
# validate.sh

FILE="$1"

echo "📝 Validating $FILE..."
python scripts/validate_markdown.py "$FILE"

echo "🔍 Checking extensions..."
python scripts/check_extensions.py "$FILE"

echo "✨ Formatting (creating review)..."
python scripts/format_markdown.py "$FILE" --review "review-$FILE"

echo "✅ Done! Check review-$FILE for manual changes."
```

Usage:
```bash
chmod +x validate.sh
./validate.sh README.md
```

---

These examples should cover most common use cases. Adapt them to your specific needs!

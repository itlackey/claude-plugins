# Markdown Validator Skill - Quick Start Checklist

## Installation ✓

- [ ] Download `markdown-validator.skill`
- [ ] Import skill into Claude
- [ ] Verify Python 3.6+ is installed: `python3 --version`

## First Use

- [ ] Extract or access the skill files
- [ ] Make scripts executable: `chmod +x scripts/*.py`
- [ ] Test with a sample file: `python scripts/validate_markdown.py test.md`

## Understanding the Skill

- [ ] Read `README.md` for overview
- [ ] Read `SUMMARY.md` for key features
- [ ] Browse `EXAMPLES.md` for usage patterns
- [ ] Check `references/validation_rules.md` for all rules

## Basic Workflow

### For Single Files

- [ ] **Step 1**: Validate syntax
  ```bash
  python scripts/validate_markdown.py document.md
  ```

- [ ] **Step 2**: Check extensions (if using custom markdown)
  ```bash
  python scripts/check_extensions.py document.md
  ```

- [ ] **Step 3**: Format safely
  ```bash
  python scripts/format_markdown.py document.md
  ```

- [ ] **Step 4**: Review uncertain changes
  ```bash
  cat formatting_review.md
  ```

- [ ] **Step 5**: Apply manual changes from review

- [ ] **Step 6**: Revalidate
  ```bash
  python scripts/validate_markdown.py document.md
  ```

### For Multiple Files

- [ ] Validate directory: `python scripts/validate_markdown.py docs/`
- [ ] Check results in `markdown_validation_report.json`
- [ ] Format files one by one or in batch
- [ ] Review all changes before committing

## With Specifications

If you have a markdown specification document:

- [ ] Create or locate your spec file (e.g., `markdown-spec.md`)
- [ ] Document your custom extensions in the spec
- [ ] Include syntax examples in the spec
- [ ] Run with spec: `--spec markdown-spec.md`

## With Examples

If you have example markdown files:

- [ ] Create an `examples/` directory
- [ ] Add example files showing correct usage
- [ ] Include diverse examples (basic, advanced, edge cases)
- [ ] Run with examples: `--examples examples/`

## Key Reminders

- [ ] ✅ **Text content is NEVER modified** - only markdown syntax
- [ ] ✅ **Review uncertain changes** - in `formatting_review.md`
- [ ] ✅ **Validate after manual changes** - ensure correctness
- [ ] ✅ **Use specifications** - for custom extensions
- [ ] ✅ **Keep examples updated** - as patterns evolve

## Common Tasks Checklist

### Validating a New Document
- [ ] Run validator
- [ ] Review all errors and warnings
- [ ] Run extension checker (if applicable)
- [ ] Fix errors manually or use formatter
- [ ] Revalidate to confirm fixes

### Batch Processing Documentation
- [ ] Test on one file first
- [ ] Run validation on directory
- [ ] Review JSON reports
- [ ] Identify files with most issues
- [ ] Process systematically
- [ ] Verify all changes

### Setting Up for a Team
- [ ] Create specification document
- [ ] Add example files
- [ ] Document team style preferences
- [ ] Add to version control
- [ ] Set up CI/CD integration (optional)
- [ ] Train team on usage

### Integrating with CI/CD
- [ ] Add validation to pipeline
- [ ] Configure to fail on errors
- [ ] Upload reports as artifacts
- [ ] Document process for team
- [ ] Test pipeline thoroughly

## Output Files Reference

After running the scripts, you'll see these files:

- [ ] `markdown_validation_report.json` - Detailed validation results
- [ ] `extension_check_report.json` - Extension validation
- [ ] `formatting_report.json` - All formatting changes
- [ ] `formatting_review.md` - Manual review needed
- [ ] `*.formatted.md` - Formatted versions (if not in-place)

## Troubleshooting Checklist

If something isn't working:

- [ ] Check Python version: `python3 --version` (need 3.6+)
- [ ] Verify scripts are executable: `ls -l scripts/`
- [ ] Check file encoding: should be UTF-8
- [ ] Verify file extension: must be `.md`
- [ ] Review error messages in console output
- [ ] Check JSON reports for detailed info
- [ ] Ensure no syntax errors in spec file
- [ ] Verify examples directory exists (if using)

## Best Practices Checklist

- [ ] Always validate before formatting
- [ ] Always review `formatting_review.md`
- [ ] Keep specification up to date
- [ ] Add new examples as you find edge cases
- [ ] Document why you skipped certain review items
- [ ] Version control your specs and examples
- [ ] Test changes on one file before batch processing
- [ ] Revalidate after manual changes
- [ ] Use meaningful commit messages
- [ ] Share knowledge with team

## Advanced Features Checklist

- [ ] Set up pre-commit hooks
- [ ] Integrate with CI/CD
- [ ] Create custom wrapper scripts
- [ ] Configure VS Code tasks
- [ ] Automate batch processing
- [ ] Filter reports programmatically
- [ ] Parallel process large directories
- [ ] Archive review files for audit trail

## Documentation Checklist

For your team:

- [ ] Document your markdown style guide
- [ ] Create specification for custom extensions
- [ ] Provide usage examples
- [ ] Document common edge cases
- [ ] Share troubleshooting tips
- [ ] Keep examples directory updated
- [ ] Document CI/CD integration
- [ ] Create quick reference guide

## Ready to Use!

Once you've completed the installation section, you're ready to start validating markdown files. Remember:

✅ Text content preservation is guaranteed  
✅ Uncertain changes are always logged  
✅ You have full control over what gets changed  
✅ Comprehensive validation for standard and custom markdown  
✅ No external dependencies required  

## Quick Commands Reference

```bash
# Validate
python scripts/validate_markdown.py file.md

# Check extensions
python scripts/check_extensions.py file.md --spec spec.md

# Format
python scripts/format_markdown.py file.md

# Review
cat formatting_review.md

# Batch validate
python scripts/validate_markdown.py docs/

# With spec and examples
python scripts/check_extensions.py file.md --spec spec.md --examples examples/
```

## Next Steps

- [ ] Read through `EXAMPLES.md` for real-world scenarios
- [ ] Try the validator on your own markdown files
- [ ] Create a specification if you use custom extensions
- [ ] Set up examples directory with your team's style
- [ ] Consider CI/CD integration for automated validation
- [ ] Share the skill with your team

---

**You're all set! Start validating markdown files with confidence.**

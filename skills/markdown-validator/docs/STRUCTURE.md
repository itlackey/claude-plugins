# Markdown Validator Skill - Structure Reference

## Skill Package Contents

```
markdown-validator.skill (packaged zip file)
│
└── markdown-validator/
    ├── SKILL.md                          # Main skill documentation (8KB)
    │   ├── Overview and workflow
    │   ├── Step-by-step usage instructions
    │   ├── Common scenarios
    │   ├── Integration guidance
    │   └── Troubleshooting
    │
    ├── scripts/                          # Executable Python scripts
    │   ├── validate_markdown.py          # Standard markdown validator (12KB)
    │   │   ├── Validates heading structure
    │   │   ├── Checks list formatting
    │   │   ├── Verifies link syntax
    │   │   ├── Validates code blocks
    │   │   └── Checks emphasis markers
    │   │
    │   ├── check_extensions.py           # Custom extension checker (11KB)
    │   │   ├── Validates containers
    │   │   ├── Checks admonitions
    │   │   ├── Verifies definition lists
    │   │   ├── Validates footnotes
    │   │   └── Checks task lists
    │   │
    │   └── format_markdown.py            # Safe formatter (9KB)
    │       ├── Fixes heading spacing
    │       ├── Corrects list spacing
    │       ├── Normalizes code fences
    │       ├── Fixes emphasis markers
    │       └── Logs uncertain changes
    │
    └── references/                       # Documentation
        └── validation_rules.md           # Complete rule reference (8KB)
            ├── Standard markdown rules
            ├── Extension syntax
            ├── Validation philosophy
            └── Spec/example guidelines
```

## File Descriptions

### SKILL.md
The main documentation file that Claude reads when using the skill.

**Contains:**
- Critical principle: text content preservation
- Five-step workflow overview
- Detailed usage for each script
- Specification and example guidance
- Common validation scenarios
- Output file reference
- Troubleshooting guide

**When Claude reads this:**
- At the start of any markdown validation task
- When user asks about markdown linting/formatting
- When working with .md files and validation is needed

### validate_markdown.py
Primary script for checking standard markdown syntax.

**Validates:**
- Heading format (ATX and Setext styles)
- Heading hierarchy (no level skipping)
- List spacing (after markers)
- Link completeness (text + URL)
- Code fence matching (opening/closing)
- Emphasis marker pairing (*/_ matching)
- Horizontal rule syntax (3+ characters)
- Trailing whitespace patterns

**Accepts:**
- Single file path
- Directory path (recursive .md search)
- Optional: `--spec spec.md` flag
- Optional: `--examples examples/` flag

**Outputs:**
- Console report (human-readable)
- `markdown_validation_report.json` (machine-readable)
- Exit code 0 (valid) or 1 (issues found)

**Usage patterns:**
```bash
# Single file
python scripts/validate_markdown.py file.md

# Directory
python scripts/validate_markdown.py docs/

# With spec
python scripts/validate_markdown.py file.md --spec spec.md
```

### check_extensions.py
Specialized script for validating markdown-it plugin usage.

**Checks:**
- Container syntax (`:::type` ... `:::`)
- Admonition types (note, warning, tip, danger, etc.)
- Definition list structure
- Footnote references and definitions
- Task list syntax (`- [ ]` and `- [x]`)
- Custom attribute syntax (`{.class #id}`)

**Accepts:**
- Single file path
- Directory path (recursive .md search)
- Optional: `--spec spec.md` flag
- Optional: `--examples examples/` flag

**Outputs:**
- Console report (human-readable)
- `extension_check_report.json` (machine-readable)
- Exit code 0 (valid) or 1 (issues found)

**Usage patterns:**
```bash
# Basic check
python scripts/check_extensions.py file.md

# With specification
python scripts/check_extensions.py file.md --spec spec.md

# With examples
python scripts/check_extensions.py file.md --examples examples/
```

### format_markdown.py
Safe formatter that fixes certain issues and logs uncertain ones.

**Fixes automatically:**
- Missing space after `#` in headings
- Incorrect list marker spacing
- Code fence inconsistency (→ ```)
- Clearly mismatched emphasis
- Line endings (→ LF)
- Missing final newline

**Logs for review:**
- Setext heading conversion
- Indented code block conversion
- Bare URL suggestions
- Trailing whitespace
- Unknown admonition types
- Unused footnotes

**Accepts:**
- Single file path
- Directory path (recursive .md search)
- Optional: `--in-place` flag
- Optional: `--review filename.md` flag

**Outputs:**
- Formatted file (`.formatted.md` or in-place)
- `formatting_review.md` (uncertain changes)
- `formatting_report.json` (all changes)
- Console summary
- Exit code 0 (success) or 1 (error)

**Usage patterns:**
```bash
# Create .formatted.md
python scripts/format_markdown.py file.md

# Modify in place
python scripts/format_markdown.py file.md --in-place

# Custom review file
python scripts/format_markdown.py file.md --review my-review.md
```

### validation_rules.md
Comprehensive reference documentation for all validation rules.

**Sections:**
- Standard Markdown Syntax
  - Headings (ATX and Setext)
  - Lists (ordered and unordered)
  - Links and images
  - Code blocks (fenced and indented)
  - Emphasis (italic and bold)
  - Horizontal rules
  - Whitespace handling

- Markdown-it Extensions
  - Containers
  - Admonitions
  - Definition lists
  - Footnotes
  - Task lists
  - Custom attributes

- Validation Philosophy
  - Text content preservation
  - Certain vs uncertain changes
  - Severity levels

- Working with Specs and Examples

**When to reference:**
- Understanding specific validation rules
- Clarifying why something was flagged
- Learning about extension syntax
- Understanding uncertain changes

## Dependencies

**Python Standard Library Only:**
- `sys` - Command line arguments
- `json` - Report generation
- `re` - Pattern matching
- `pathlib` - File operations
- `typing` - Type hints

**No pip install required!**

## File Sizes

Total skill size: ~40KB uncompressed

- SKILL.md: ~8KB
- validate_markdown.py: ~12KB
- check_extensions.py: ~11KB
- format_markdown.py: ~9KB
- validation_rules.md: ~8KB

## Output Files Generated

When you use the skill, these files are created:

### Validation Outputs
- `markdown_validation_report.json` - Detailed results
  - File path
  - Valid status
  - List of issues (line, type, description, severity)
  - Uncertain changes

### Extension Check Outputs
- `extension_check_report.json` - Extension results
  - File path
  - Valid status
  - Extension issues
  - Uncertain changes

### Formatting Outputs
- `<filename>.formatted.md` - Formatted version (unless --in-place)
- `formatting_review.md` - Manual review needed
  - Line number
  - Change type
  - Current content
  - Reason for uncertainty
- `formatting_report.json` - All changes
  - Changes applied automatically
  - Changes logged for review

## Integration Points

The skill integrates with:

1. **Claude's file system**
   - Reads .md files from uploads
   - Writes outputs to outputs directory
   - Works with any accessible file path

2. **Command line**
   - All scripts are executable
   - Accept standard CLI arguments
   - Return standard exit codes

3. **CI/CD pipelines**
   - GitHub Actions
   - GitLab CI
   - Jenkins
   - Any system with Python

4. **Git hooks**
   - Pre-commit validation
   - Pre-push checks
   - Post-checkout formatting

5. **IDEs**
   - VS Code tasks
   - PyCharm run configurations
   - Vim/Emacs integration

## Customization Points

The skill can be customized:

1. **Validation rules** (edit scripts)
   - Add new checks
   - Modify severity levels
   - Custom pattern matching

2. **Extension support** (edit check_extensions.py)
   - Add new extension types
   - Custom syntax patterns
   - Spec format parsing

3. **Formatting behavior** (edit format_markdown.py)
   - Change what gets auto-fixed
   - Modify uncertain change logging
   - Custom review file format

4. **Specifications** (user-provided)
   - Define custom extensions
   - Document syntax rules
   - Provide examples

5. **Examples** (user-provided)
   - Show valid patterns
   - Document style preferences
   - Reference implementations

## Version Control

Recommended to track in git:

```
your-repo/
├── .markdown-validator/        # Skill configuration
│   ├── spec.md                 # Your specification
│   └── examples/               # Your examples
├── docs/                       # Your markdown files
└── scripts/                    # Validator scripts
    ├── validate_markdown.py
    ├── check_extensions.py
    └── format_markdown.py
```

## Security Considerations

✅ **Safe:**
- Uses only Python standard library
- No network access
- No system modifications
- Read-only operations (except output files)
- Text content never modified

⚠️ **Be aware:**
- Scripts execute Python code
- Review scripts before first use
- Limit file system access as needed
- Use in trusted environments

## Performance

**Typical performance:**
- Single file: <1 second
- 100 files: ~5 seconds
- 1000 files: ~30 seconds

**Factors:**
- File size
- Complexity of markdown
- Number of extensions
- Disk I/O speed

**Optimization tips:**
- Process files in parallel for large batches
- Use specification to limit extension checks
- Filter by file patterns before processing

## Maintenance

**Regular maintenance tasks:**
1. Update validation rules as standards evolve
2. Add new extension types as needed
3. Refine uncertain change detection
4. Update specifications
5. Add new example files
6. Review and improve performance

**Skill updates:**
- Download new version when available
- Review changelog for breaking changes
- Test on sample files before deployment
- Update team documentation

---

This skill is designed to be:
- **Simple** - Easy to understand and use
- **Safe** - Never modifies text content
- **Extensible** - Customizable for your needs
- **Maintainable** - Clear code structure
- **Portable** - Works anywhere Python runs

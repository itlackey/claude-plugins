---
name: pdf-review
description: Visual quality assurance review for print-ready PDF documents, especially TTRPG books. Use for page-by-page layout review, margin and safe zone verification, typography and spacing checks, image quality assessment, print standards compliance, and identifying layout issues before printing. Provides systematic review methodology and detailed checklists.
---

# PDF Review & Quality Assurance Skill

This skill provides comprehensive visual review methodology for print-ready PDFs, with specialized focus on TTRPG book layouts, print quality standards, and systematic page-by-page quality assurance.

## When to Use This Skill

Use this skill when you need to:

- **Review print-ready PDFs** - Full quality assurance before sending to printer
- **Check page layouts** - Verify margins, spacing, alignment across all pages
- **Assess print quality** - Resolution, color mode, bleed, technical requirements
- **Find layout issues** - Widows, orphans, awkward breaks, inconsistencies
- **Verify typography** - Font sizes, hierarchy, readability, consistency
- **Check TTRPG elements** - Stat blocks, tables, sidebars, maps, character sheets
- **Document problems** - Systematic issue tracking and severity classification
- **Prepare for printing** - Final checklist before production

## Review Methodology

### Three-Pass Review System

**Pass 1: Structural Review (Fast - 5-10 minutes for 100 pages)**
- Flip through entire PDF quickly
- Check page numbering sequence
- Verify chapter/section breaks
- Identify obvious layout problems
- Note missing or blank pages

**Pass 2: Detailed Review (Thorough - 1-2 hours for 100 pages)**
- Page-by-page examination
- Margins and safe zones
- Typography and spacing
- Images and graphics quality
- Headers, footers, page numbers
- Consistency checks

**Pass 3: Edge Cases (Critical - 30-60 minutes)**
- First/last pages of sections
- Pages with complex layouts
- Tables, sidebars, stat blocks
- Special pages (TOC, index, character sheets)
- Cross-references and page numbers
- Print-specific technical requirements

## Reference Documents

### references/print-quality-checklist.md

Comprehensive print quality standards and review checklist.

**Contains:**
- Visual review methodology
- Margins and safe zones specifications
- Typography and text standards
- Page numbering rules
- Headers and footers requirements
- Image and graphics quality criteria
- Tables and data formatting
- Page break best practices
- Color and printing technical specs
- Final review checklist
- Common red flags

**When to read:**
- First time reviewing a PDF
- Need margin specifications
- Checking typography standards
- Verifying print technical requirements
- Looking for specific issue types
- Creating review documentation

### references/ttrpg-standards.md

TTRPG-specific layout standards and best practices.

**Contains:**
- Page layout standards (columns, spacing)
- Stat blocks and game mechanics formatting
- Tables and charts for gameplay
- Sidebars and call-out boxes
- Art and illustration placement
- Maps and diagrams requirements
- Character sheets and forms
- Typography for game text
- Color usage and B&W considerations
- Usability at the table
- TTRPG-specific red flags

**When to read:**
- Reviewing TTRPG books
- Checking stat block consistency
- Verifying game mechanics formatting
- Assessing table layouts
- Reviewing maps and character sheets
- Ensuring playability

## Quick Start Guide

### For First-Time PDF Review

1. **Upload PDF to Claude**
2. **Ask for review:** "Review this PDF page-by-page for print quality"
3. **Specify focus areas** (if any): "Pay special attention to stat blocks and tables"
4. **Review findings** - Claude will provide systematic page-by-page feedback
5. **Get recommendations** - Prioritized list of issues to fix

### For Targeted Reviews

**Check specific issue:**
> "Check margins on pages 20-50 of this PDF"

**Verify specific element:**
> "Review all stat blocks for consistency in this PDF"

**Technical verification:**
> "Verify this PDF meets print requirements (CMYK, 300 DPI, bleeds)"

**Compare to spec:**
> "Check if this layout matches these specifications: [your specs]"

## Common Review Tasks

### Task 1: Full Pre-Print Review

**What:** Complete quality assurance before sending to printer

**Process:**
1. **Structural pass** - Verify completeness
2. **Detailed pass** - Check every page systematically
3. **Edge cases pass** - Focus on complex elements
4. **Document issues** - Categorize by severity
5. **Provide fix list** - Prioritized action items

**Claude will check:**
- Page numbering and sequencing
- Margins and safe zones
- Typography consistency
- Image quality and placement
- Headers and footers
- Print technical requirements
- TTRPG-specific elements (if applicable)

**Output:**
- Issues by severity (CRITICAL/MAJOR/MINOR)
- Page-specific problems
- Pattern issues across document
- Recommended fixes
- Technical compliance status

### Task 2: Margin and Layout Verification

**What:** Verify margins, safe zones, and layout consistency

**Check for:**
- Content too close to edges (will be cut)
- Text in gutter (unreadable when bound)
- Inconsistent margins across pages
- Content in bleed area
- Safe zone violations

**Specifications:**
- **Inner margin (gutter):** 0.75" - 1" minimum
- **Outer margin:** 0.5" - 0.75" minimum
- **Top/bottom:** 0.5" - 0.75" minimum
- **Safe zone:** 0.25" inside trim
- **Bleed:** 0.125" beyond trim (if applicable)

**Claude will:**
- Measure margins visually
- Identify violations
- Note inconsistencies
- Flag critical issues

### Task 3: Typography and Consistency Check

**What:** Verify fonts, sizes, spacing, and hierarchy

**Check for:**
- Font sizes appropriate (body 9-11pt minimum)
- Heading hierarchy clear and consistent
- Line spacing adequate (1.2-1.5x font size)
- Widows and orphans (single lines isolated)
- Inconsistent styling

**Claude will:**
- Verify font size minimums
- Check heading hierarchy
- Identify spacing issues
- Find widows/orphans
- Note inconsistencies

### Task 4: TTRPG-Specific Element Review

**What:** Check game-specific layouts and formatting

**Elements reviewed:**
- **Stat blocks** - Formatting, consistency, placement
- **Tables** - Readability, headers, page breaks
- **Sidebars** - Visual distinction, page breaks
- **Maps** - Size, quality, placement
- **Dice notation** - Consistent formatting
- **Character sheets** - Usability, field sizes

**Claude will:**
- Check consistency across all instances
- Verify readability and usability
- Flag formatting issues
- Note page break problems
- Assess functional design

### Task 5: Image Quality Assessment

**What:** Verify all images meet print standards

**Check for:**
- Resolution adequate (300 DPI minimum)
- No pixelation or blurriness
- Proper cropping and framing
- Appropriate placement
- Caption presence and positioning
- Color mode correct (CMYK)

**Claude will:**
- Identify low-resolution images
- Note placement issues
- Check caption consistency
- Flag quality concerns
- Verify technical specs

### Task 6: Page Break Review

**What:** Ensure content breaks naturally across pages

**Check for:**
- Headings isolated at bottom (orphans)
- Single lines at top/bottom (widows/orphans)
- Images split across pages
- Tables breaking awkwardly
- Context lost across page turns

**Claude will:**
- Identify problematic breaks
- Flag orphaned headings
- Note split elements
- Assess reading flow
- Recommend adjustments

## Issue Severity Classification

### CRITICAL - Must Fix Before Printing

Issues that will cause problems in final printed product:
- Content in margins (will be cut off)
- Text in gutter (unreadable when bound)
- Unreadable text (too small, low contrast)
- Missing pages or content
- Wrong information
- Technical spec violations (wrong color mode, insufficient resolution)

**Example:**
```
Page 47: CRITICAL
- Body text extends 0.1" into bottom margin
- Will be cut off during trimming
- Fix: Reduce text size or adjust layout
```

### MAJOR - Should Fix Before Printing

Issues affecting professionalism and usability:
- Poor aesthetics
- Inconsistent formatting
- Confusing layouts
- Awkward page breaks
- Quality concerns

**Example:**
```
Pages 23-45: MAJOR
- Left page headers show wrong chapter title
- Shows "Chapter 2" on Chapter 3 pages
- Fix: Update header template
```

### MINOR - Nice to Fix If Time

Polish and perfectionist details:
- Small inconsistencies
- Minor aesthetic issues
- Non-critical spacing
- Optional improvements

**Example:**
```
Page 52: MINOR
- Paragraph spacing varies (0.5em vs 0.75em)
- Not noticeable unless looking closely
- Fix: Standardize to 0.75em if time permits
```

## Review Documentation Format

### Page-Specific Issues

```
Page [#]: [SEVERITY]
- [Description of issue]
- [Impact/why it matters]
- [Suggested fix]
```

### Pattern Issues

```
Pattern across pp. [range]:
- [SEVERITY]: [Description]
- [How many instances]
- [Systematic fix needed]
```

### Summary Report

```
SUMMARY:
- Total pages: [#]
- CRITICAL issues: [#]
- MAJOR issues: [#]
- MINOR issues: [#]

TOP PRIORITIES:
1. [Most important fix]
2. [Second priority]
3. [Third priority]
```

## Working with User Specifications

### If User Provides Specs

When user says "check against these specs":
1. **Capture their requirements** - Margins, fonts, colors, etc.
2. **Compare PDF against specs** - Systematic verification
3. **Note deviations** - Where PDF doesn't match
4. **Assess severity** - How critical is each deviation
5. **Recommend fixes** - Specific actions to match specs

### Common Spec Categories

**Layout Specs:**
- Page size (6x9, 8.5x11, A4, etc.)
- Margins (inner, outer, top, bottom)
- Columns (number, width, gutter)
- Bleed area

**Typography Specs:**
- Body font and size
- Heading fonts and hierarchy
- Line spacing
- Paragraph spacing

**Color Specs:**
- Color mode (CMYK, B&W, spot colors)
- Brand colors (if applicable)
- Image treatment

**Element Specs:**
- Stat block formatting
- Table styles
- Sidebar design
- Header/footer content

## Print Technical Requirements

### Essential Checks

**Color Mode:**
- ✓ CMYK (not RGB) for color printing
- ✓ Grayscale or B&W for black & white
- ✓ Black text as 100% K (not 4-color black)

**Resolution:**
- ✓ Images at 300 DPI minimum
- ✓ No pixelation visible
- ✓ Vector graphics for logos/icons

**Bleed:**
- ✓ Full-bleed elements extend 0.125" past trim
- ✓ No important content in bleed area
- ✓ Background colors/images reach bleed

**Fonts:**
- ✓ All fonts embedded in PDF
- ✓ No font substitutions
- ✓ Text remains selectable (not flattened)

**Page Size:**
- ✓ Matches intended trim size
- ✓ Consistent throughout document
- ✓ Meets printer specifications

## Best Practices

### For Efficient Review

1. **Start with quick pass** - Get overall sense
2. **Focus on CRITICAL first** - Fix show-stoppers
3. **Document as you go** - Don't rely on memory
4. **Use page numbers** - Specific references
5. **Screenshot issues** - Visual evidence helps
6. **Prioritize fixes** - Not everything needs fixing
7. **Check patterns** - One issue may repeat
8. **Verify after fixes** - Re-review changed sections

### For Working with Claude

**Be specific about concerns:**
✓ "Check margins on all pages"
✓ "Verify stat blocks are consistent"
✓ "Focus on image quality"
✓ "Check if this meets printer specs"

**Provide context:**
✓ "This is a 250-page TTRPG rulebook"
✓ "Using print-on-demand (6x9)"
✓ "Interior will be B&W"
✓ "Need to stay under budget"

**Ask for priorities:**
✓ "What are the critical issues?"
✓ "What MUST be fixed before printing?"
✓ "What's optional polish?"

## PDF Limitations

### What Claude Can See

When reviewing PDFs, Claude can:
- ✓ See page layouts visually
- ✓ Identify obvious margin issues
- ✓ Spot typography problems
- ✓ Find consistency issues
- ✓ Assess image quality visually
- ✓ Check page breaks and flow
- ✓ Verify element placement

### What Claude Cannot Measure Precisely

- ✗ Exact measurements in inches/mm (estimates visually)
- ✗ Precise DPI of embedded images (assesses quality)
- ✗ Exact color values (can see color mode issues)
- ✗ Font embedding status (assumes from appearance)

**Claude provides:** Visual assessment and professional judgment based on print standards and best practices.

## Quick Reference

### "Is this ready to print?"
→ Full three-pass review with technical verification

### "Check page 47 for margin issues"
→ Focused review of specific pages

### "Are all my stat blocks formatted consistently?"
→ TTRPG-specific element check

### "Does this meet standard print requirements?"
→ Technical compliance verification

### "What are the critical issues I must fix?"
→ Prioritized issue list

### "Review against these specs: [specs]"
→ Specification compliance check

## Final Checklist

Before declaring PDF print-ready:

**Technical:**
- [ ] Correct color mode (CMYK/B&W)
- [ ] Resolution adequate (300 DPI)
- [ ] Fonts embedded
- [ ] Bleed correct (if applicable)
- [ ] Page size matches spec

**Layout:**
- [ ] Margins adequate and consistent
- [ ] No content in unsafe zones
- [ ] Headers/footers correct
- [ ] Page numbers sequential
- [ ] Page breaks logical

**Content:**
- [ ] All pages present
- [ ] No placeholder text
- [ ] Images high quality
- [ ] Tables formatted well
- [ ] Typography consistent

**TTRPG-Specific (if applicable):**
- [ ] Stat blocks consistent
- [ ] Tables readable and complete
- [ ] Maps appropriately sized
- [ ] Sidebars don't break badly
- [ ] Dice notation consistent

**Professional:**
- [ ] Consistent styling throughout
- [ ] No obvious errors
- [ ] Meets design standards
- [ ] Ready for production

## Tips for Best Results

1. **Upload the actual PDF** - Claude can see the rendered pages
2. **Be specific about concerns** - Focus the review
3. **Provide specifications** - What are your requirements?
4. **Ask about patterns** - "Check all stat blocks" not just one
5. **Request priority list** - What's most important to fix?
6. **Use for final check** - After you've done your own review
7. **Get a second opinion** - Fresh eyes catch issues

## Working with Other Skills

**Combines with:**
- **Paged.js skill** - Create layouts, then review them
- **PDF skill** - Extract, manipulate, then review quality
- **DOCX skill** - Export to PDF, then review before print

**Workflow:**
1. Design layout (Paged.js or DOCX skill)
2. Generate PDF
3. Review with PDF Review skill
4. Fix issues
5. Generate final PDF
6. Final review pass
7. Send to printer

You now have comprehensive PDF review capabilities to ensure your print-ready documents meet professional standards! 📄✓

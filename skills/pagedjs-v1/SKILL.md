---
name: pagedjs
description: HTML/CSS print layout design and debugging using Paged.js polyfill library. Use for creating, editing, and troubleshooting paginated documents (books, reports, manuals) with CSS Paged Media features like page breaks, running headers/footers, page counters, and print-specific layouts. Includes browser preview, PDF rendering workflows, and layout debugging.
---

# Paged.js Print Layout Skill

This skill provides comprehensive support for designing and debugging HTML/CSS layouts using the Paged.js polyfill library for print media. It covers the complete workflow from editing content to reviewing final PDFs.

## Workflow Overview

The typical workflow for working with Paged.js documents:

1. **Edit content** - Modify HTML/Markdown source files
2. **Preview in browser** - View with Paged.js polyfill applied
3. **Debug layouts** - Fix page breaks, adjust spacing, refine CSS
4. **Render to PDF** - Generate final output using CLI tools
5. **Review PDF** - Check final output and iterate as needed

## When to Use This Skill

Use this skill when working on:

- Multi-page print documents (books, reports, manuals)
- Page layout issues (breaks, spacing, overflow)
- Running headers and footers with dynamic content
- Page numbering and counters
- CSS Paged Media features (@page rules, margin boxes, break properties)
- Converting HTML to print-quality PDFs
- Debugging layout and rendering issues

## Core CSS Patterns

### Quick Reference

For detailed CSS patterns and examples, see `references/css-patterns.md`. Key areas covered:

- **@page rules** - Page size, margins, named pages
- **Page breaks** - Control where content breaks across pages
- **Headers/footers** - Running content in margin boxes
- **Counters** - Page numbers, chapter numbers, figure numbers
- **Cross-references** - Dynamic page number references
- **Layout patterns** - Multi-column, bleeds, running elements

**When to read css-patterns.md:**
- Setting up page structure for first time
- Implementing headers/footers or page numbers
- Need examples of specific CSS features
- Creating complex layouts

### Common Patterns Quick Guide

```css
/* Basic page setup */
@page {
  size: A4;
  margin: 2cm;
}

/* Page breaks */
.chapter {
  break-before: page;  /* Start new page */
}

h1, h2, h3 {
  break-after: avoid;   /* Keep with next */
  break-inside: avoid;  /* Don't split */
}

/* Running headers */
h1 {
  string-set: chapter-title content();
}

@page {
  @top-center {
    content: string(chapter-title);
  }
}

/* Page numbers */
@page {
  @bottom-center {
    content: counter(page);
  }
}
```

## Debugging and Troubleshooting

For comprehensive troubleshooting guidance, see `references/troubleshooting.md`. It covers:

- Page break issues (unwanted, missing, blank pages)
- Header/footer problems (not showing, wrong content)
- Counter issues (not incrementing, wrong values)
- Layout and overflow problems
- Performance issues
- Browser-specific issues
- Diagnostic techniques

**When to read troubleshooting.md:**
- Encountering specific layout issues
- Headers/footers not behaving as expected
- Page breaks in wrong places
- Content overflowing or positioned incorrectly
- Need systematic debugging approach

### Quick Debugging

```css
/* Visual debugging - add temporarily */
* {
  outline: 1px solid rgba(255, 0, 0, 0.1);
}

@page {
  border: 2px solid red;
}

h1, h2, h3 {
  background: rgba(0, 255, 0, 0.1);
}
```

## Scripts

### validate_pagedjs.py

Validates HTML and CSS for common Paged.js issues.

**Usage:**
```bash
python scripts/validate_pagedjs.py document.html
python scripts/validate_pagedjs.py document.html --css styles.css
```

**What it checks:**
- Paged.js script inclusion
- @page rules and page configuration
- string-set/string() cross-references
- counter-reset/counter-increment usage
- Named pages
- Common CSS issues (absolute positioning, missing break properties)
- Orphans and widows configuration

**When to use:**
- Before rendering to PDF
- After making significant CSS changes
- Debugging mysterious layout issues
- Checking for missing dependencies

### preview_template.py

Generates a minimal HTML preview template for quick CSS testing.

**Usage:**
```bash
python scripts/preview_template.py --output preview.html
python scripts/preview_template.py --css custom.css --output preview.html
```

**When to use:**
- Testing new CSS rules quickly
- Isolating CSS issues from complex content
- Creating minimal reproducible examples
- Learning Paged.js features

## Working with Page Layouts

### Starting a New Document

1. **Set up basic @page rules**
   ```css
   @page {
     size: A4 portrait;  /* or Letter, B5, etc. */
     margin: 2.5cm 2cm 2.5cm 2cm;
   }
   ```

2. **Define page break behavior**
   ```css
   /* Chapters start on new page */
   .chapter {
     break-before: page;
   }
   
   /* Keep headings with content */
   h1, h2, h3 {
     break-after: avoid;
     break-inside: avoid;
   }
   ```

3. **Add basic headers/footers**
   ```css
   @page {
     @top-center {
       content: string(chapter-title);
     }
     @bottom-center {
       content: counter(page);
     }
   }
   
   h1 {
     string-set: chapter-title content();
   }
   ```

### Refining Layouts

**For page break issues:**
1. Use browser DevTools to inspect where breaks occur
2. Add `break-inside: avoid` to elements that split awkwardly
3. Use `break-after: avoid` to keep related content together
4. Consider `orphans` and `widows` properties for paragraphs

**For header/footer issues:**
1. Verify `string-set` elements exist on each page
2. Check that string names match between set and use
3. Use `:first` pseudo-class to hide headers on chapter starts
4. Use `:left` and `:right` for different recto/verso headers

**For spacing issues:**
1. Reset margins on all elements, then add back systematically
2. Use consistent vertical rhythm (e.g., 1em = 1 line)
3. Be careful with margin collapse
4. Test with actual content length, not just samples

### Reviewing PDF Output

After rendering to PDF, check for:

- **Page breaks** - Verify chapters start correctly, no awkward splits
- **Headers/footers** - Confirm content updates properly across pages
- **Page numbers** - Check sequence, formatting, special sections
- **Margins** - Ensure consistent spacing, no content in bleed areas
- **Fonts** - Verify all fonts render correctly and are embedded
- **Images** - Check quality, positioning, and page boundary behavior
- **Overall flow** - Read through to catch visual rhythm issues

## Common Workflow Patterns

### Pattern 1: Fixing Page Break Issues

1. Identify the problem area (element breaking across pages)
2. Add visual debugging CSS to see page boundaries
3. Apply `break-inside: avoid` to the element
4. If still breaking, check parent containers
5. Consider reducing font size or padding if content is too large
6. Validate with `validate_pagedjs.py`
7. Re-render PDF and review

### Pattern 2: Setting Up Running Headers

1. Identify what content should appear in headers (chapter titles, section names)
2. Add `string-set` to the element that holds this content
3. Define `@page` margin box with `content: string(...)`
4. Test that content updates across pages
5. Add `:first` rules to remove header on chapter starts if desired
6. Configure different left/right pages if needed

### Pattern 3: Debugging Layout Issues

1. Run `validate_pagedjs.py` to catch obvious issues
2. Add visual debugging CSS (outlines, backgrounds)
3. Use browser DevTools to inspect computed styles
4. Test with simplified content to isolate the issue
5. Check `references/troubleshooting.md` for specific issue patterns
6. Make incremental changes and test after each one

### Pattern 4: Perfecting Final Layout

1. Generate full PDF and review page by page
2. Note all issues (breaks, spacing, alignment)
3. Prioritize issues (critical vs. nice-to-have)
4. Fix critical issues first (content loss, illegibility)
5. Iterate on refinements (spacing, widows/orphans)
6. Do final read-through checking for:
   - Consistent vertical rhythm
   - Proper heading hierarchy
   - Clean page breaks
   - Correct headers/footers
   - Accurate page numbers

## Tips for Large Documents (200+ pages)

- **Use named pages** for different sections (frontmatter, chapters, appendices)
- **Test in sections** rather than always rendering entire document
- **Optimize images** before including (compress, resize)
- **Simplify CSS selectors** for better performance
- **Use browser preview** for quick iteration, PDF for final review
- **Keep reference documents open** (css-patterns.md, troubleshooting.md)
- **Validate frequently** with `validate_pagedjs.py` to catch issues early
- **Use version control** to track CSS changes and revert if needed

## Best Practices

1. **Start simple** - Basic @page rules first, then add complexity
2. **Test incrementally** - Add one feature at a time
3. **Use semantic HTML** - Makes CSS targeting easier
4. **Keep CSS organized** - Group by feature (page setup, breaks, headers, etc.)
5. **Document custom rules** - Add comments for complex CSS
6. **Preview frequently** - Catch issues early before they compound
7. **Validate before final render** - Save time by catching errors early
8. **Keep backups** - CSS changes can have cascading effects

## Additional Resources

The skill includes these reference documents:

- **css-patterns.md** - Comprehensive CSS examples for all Paged.js features
- **troubleshooting.md** - Systematic debugging guide for common issues

Read these references when you need detailed examples or are troubleshooting specific issues. The patterns and solutions in these documents are proven to work and cover edge cases.

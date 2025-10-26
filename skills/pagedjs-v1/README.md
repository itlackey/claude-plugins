# Paged.js Skill - Installation and Usage Guide

## What This Skill Provides

This skill gives Claude comprehensive knowledge and tools for working with Paged.js print layouts, including:

- **CSS Paged Media patterns** - Complete reference for @page rules, page breaks, headers/footers, counters
- **Troubleshooting guide** - Systematic debugging for common layout issues
- **Validation script** - Checks HTML/CSS for common Paged.js issues
- **Preview template generator** - Creates test HTML files for quick CSS testing
- **Workflow patterns** - Step-by-step guides for common tasks

## Installation

1. **Upload the skill to Claude**
   - Click the settings icon (⚙️) in Claude
   - Navigate to "Skills" section
   - Click "Upload skill"
   - Select the `pagedjs.skill` file

2. **Enable the skill**
   - Toggle the skill on in your skills list
   - The skill will now be available in all your conversations

## What the Skill Contains

```
pagedjs/
├── SKILL.md                           # Main skill documentation
├── scripts/
│   ├── validate_pagedjs.py           # Validates HTML/CSS for issues
│   └── preview_template.py           # Generates test HTML templates
└── references/
    ├── css-patterns.md               # Comprehensive CSS examples
    └── troubleshooting.md            # Debugging guide
```

## How to Use the Skill

Once installed, Claude will automatically use this skill when you:

- Ask about Paged.js layouts
- Request help with page breaks, headers, or footers
- Need to debug print layout issues
- Want to create or edit HTML/CSS for print media
- Ask for help reviewing or improving paginated documents

### Example Queries

**Setting up a new document:**
> "I'm starting a new book with Paged.js. Help me set up the basic page structure with headers, footers, and page numbers."

**Fixing layout issues:**
> "My chapter headings are breaking across pages. How do I keep them together with the following content?"

**Reviewing CSS:**
> "Can you review this CSS and check for common Paged.js issues?"
> [Upload your CSS file]

**Debugging problems:**
> "The headers aren't showing up on my pages. Can you help me debug this?"
> [Upload your HTML file]

**Using the scripts:**
> "Can you validate this Paged.js document for me?"
> [Upload HTML file, Claude will run validate_pagedjs.py]

## Sample Document

I've included a sample HTML document (`sample-pagedjs-document.html`) that demonstrates:

- Basic page setup with @page rules
- Running headers with chapter titles
- Page numbering in footer
- Page break control
- Proper heading hierarchy
- Typography best practices

**To preview the sample:**
1. Open `sample-pagedjs-document.html` in a modern web browser (Chrome recommended)
2. The Paged.js polyfill will automatically paginate the content
3. You'll see the document broken into pages with headers and page numbers

**To test the validation script:**
```bash
python validate_pagedjs.py sample-pagedjs-document.html
```

## Your Workflow with the Skill

### Typical Workflow

1. **Edit your content** (Markdown/HTML)
2. **Ask Claude to help** with CSS or layout issues
3. **Preview in browser** with Paged.js applied
4. **Validate** using the validation script
5. **Render to PDF** using your CLI tool
6. **Review and iterate** with Claude's help

### When to Use the Skill

The skill is most valuable for:

- **Initial setup** - Getting page structure, headers, and basic CSS right
- **Debugging** - When things aren't working as expected
- **Optimization** - Perfecting page breaks and spacing
- **Learning** - Understanding Paged.js features and best practices
- **Review** - Having Claude check your CSS for issues

## Tips for Best Results

1. **Be specific** - The more details you provide about your issue, the better Claude can help
2. **Share files** - Upload your HTML/CSS so Claude can analyze actual code
3. **Describe the problem** - Explain what's happening vs. what you expect
4. **Iterate** - Make small changes and test frequently
5. **Use the scripts** - The validation script catches many common issues

## Common Use Cases

### Case 1: Starting a New Book

**You:** "I'm creating a 250-page book with Paged.js. I need chapters to start on new pages, running headers with chapter titles, and page numbers. Can you help me set this up?"

**Claude will:**
- Provide starter CSS with @page rules
- Set up proper page breaks
- Configure running headers with string-set
- Add page number counters
- Explain the code

### Case 2: Fixing Page Breaks

**You:** "Images in my document are splitting across pages. How do I keep them on one page?"

**Claude will:**
- Explain the break-inside property
- Show you the exact CSS to add
- Suggest best practices for figures
- Offer additional tips for similar elements

### Case 3: Debugging Headers

**You:** "My chapter titles aren't showing up in the header on some pages."

**Claude will:**
- Ask to see your HTML/CSS
- Check for common issues (string-set placement, selector problems)
- Run validation if needed
- Provide a fix with explanation

### Case 4: Perfecting Layout

**You:** "Can you review my CSS and suggest improvements for better page layout?"

**Claude will:**
- Analyze your CSS structure
- Run validation script
- Identify issues or anti-patterns
- Suggest optimizations
- Explain best practices

## Troubleshooting the Skill

If the skill doesn't seem to be working:

1. **Check skill is enabled** in your settings
2. **Use specific keywords** like "Paged.js", "page breaks", "print layout"
3. **Be explicit** - Say "use the Paged.js skill" if needed
4. **Upload files** - Claude works better with actual code to analyze

## Additional Resources

Inside the skill, Claude has access to:

- **css-patterns.md** - 200+ lines of CSS examples for every Paged.js feature
- **troubleshooting.md** - Comprehensive debugging guide with solutions
- **validate_pagedjs.py** - Python script to check for common issues
- **preview_template.py** - Generates quick test HTML files

Claude will reference these automatically when needed, but you can also ask Claude to look at specific references:

> "Can you show me the CSS patterns for left and right page headers?"
> "What does the troubleshooting guide say about missing page breaks?"

## Getting Help

If you encounter issues with the skill or need additional features:

1. Ask Claude to help you extend the skill
2. The skill can be updated with new patterns and scripts
3. Share your specific use cases to improve the skill

Enjoy creating beautiful print layouts with Paged.js! 📚✨

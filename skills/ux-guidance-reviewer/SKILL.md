---
name: ux-guidance-reviewer
description: Review web applications for UX writing quality, user guidance clarity, accessibility, and visual layout. Analyzes contextual help, labels, error messages, button text, tooltips with both content and visual analysis using screenshots. Supports JWT authentication, can reference existing help documentation for context improvement, and generates comprehensive reports with layout and placement recommendations.
---

# UX Guidance Reviewer

## Overview

This skill enables systematic review of web application user interfaces to evaluate and improve user guidance, including labels, help text, error messages, button text, tooltips, and overall UX writing quality. It combines Chrome MCP tools for web crawling, visual screenshot analysis for layout review, automated content analysis, and optional context from existing help documentation to identify accessibility issues, clarity problems, inconsistencies, and placement issues.

## Review Process

The UX guidance review follows these steps:

1. **Plan the crawl** - Identify scope, authentication needs, documentation context, and key pages to review
2. **Navigate and extract** - Use Chrome MCP tools to systematically visit pages, capture HTML and screenshots
3. **Analyze content** - Run analysis scripts to identify UX elements and issues
4. **Visual review** - Evaluate screenshots for guidance placement, visual hierarchy, and layout
5. **Context enhancement** - Cross-reference with existing help documentation if provided
6. **Compile findings** - Aggregate results and categorize by priority
7. **Generate report** - Create comprehensive report with content and visual recommendations

## Step 1: Planning the Review

Before starting, establish the review scope and approach:

### Determine Scope
Ask the user to clarify:
- Application URL and main entry points
- Authentication requirements (credentials, JWT token file path, or form-based login)
- Path to existing help/documentation folder (optional, for context enhancement)
- Specific sections to focus on or exclude
- Expected number of pages (for time estimation)
- Any known problem areas to prioritize

### Gather Authentication Details

**JWT Authentication:**
If the application uses JWT tokens:
1. Ask user for the path to a file containing JWT credentials (e.g., `/path/to/jwt_token.json`)
2. Read the JWT token from the file
3. Use Chrome MCP's evaluate tool to set the Authorization header in browser context
4. Verify authentication before proceeding with crawl

**Form-Based Authentication:**
If using traditional login forms:
1. Navigate to login page using Chrome MCP
2. Fill credentials using `fill` tool
3. Submit and verify successful authentication
4. Proceed with authenticated session

### Load Documentation Context (Optional)

If the user provides a path to existing help documentation:
1. Ask for the documentation folder path (e.g., `/path/to/docs` or `/mnt/user-data/uploads/docs`)
2. Scan the documentation folder for relevant content
3. Read key documentation files (README, help pages, user guides)
4. Use this context to:
   - Identify gaps between documentation and in-app guidance
   - Suggest content that could be integrated into the UI
   - Check consistency between docs and interface language
   - Recommend cross-references or help links

### Choose Crawl Strategy

**Breadth-first approach** (recommended for most reviews):
- Visit all main sections before drilling down
- Better for overall coverage
- Easier to organize findings by section

**Flow-based approach** (for specific user journeys):
- Follow complete user flows (signup, checkout, etc.)
- Captures validation and error states
- Best for testing specific experiences

**Targeted approach** (for quick audits):
- Review specific pages or components
- Useful for focused improvements
- Faster turnaround

## Step 2: Navigate and Extract Content

Use Chrome MCP tools systematically to capture both content and visual state.

### Navigation Pattern with Visual Capture
```
For each page to review:
1. Navigate to page URL using chrome_navigate
2. Wait for page load using chrome_wait_for_navigation
3. Wait for key elements to render (chrome_wait_for_selector)
4. Capture screenshot using chrome_screenshot for visual analysis
5. Capture full HTML using chrome_get_html
6. Save HTML to file with descriptive name (e.g., page_name.html)
7. Save screenshot with matching name (e.g., page_name.png)
8. Note the page URL and navigation path in your tracking
```

### Screenshot Strategy

**When to capture screenshots:**
- Every main page reviewed (for comprehensive visual analysis)
- Before and after interactions (to show state changes)
- Error states and validation messages (to assess visibility)
- Modal dialogs and tooltips (to check placement)
- Forms with help text (to evaluate layout and proximity)

**What to look for in screenshots:**
- **Visual hierarchy**: Is guidance prominent enough?
- **Proximity**: Are labels close to their inputs?
- **Help text placement**: Is it near the relevant field?
- **Error message visibility**: Are errors easy to spot?
- **Tooltip accessibility**: Can users easily trigger them?
- **White space**: Is there enough breathing room?
- **Color and contrast**: Is text readable?
- **Responsive layout**: Does guidance fit well on the page?

### Handling Dynamic Content
- Use `chrome_wait_for_selector` for lazy-loaded content
- Execute JavaScript if needed with `chrome_evaluate`
- Allow time for single-page app frameworks to render
- Check for modals, dropdowns, or hidden content
- Capture screenshots of different states (collapsed/expanded, empty/filled)

### Capturing Interactive States
For forms and interactive elements:
- Trigger validation by attempting submission with empty fields
- Interact with dropdowns and radio buttons
- Hover over elements to reveal tooltips (capture screenshots)
- Test error states intentionally (capture before/after)
- Fill forms partially to see inline validation

### JWT Authentication Setup

If using JWT authentication:

```javascript
// Read JWT token from provided file
const tokenPath = '/path/to/jwt_token.json';  // From user input
const tokenData = JSON.parse(fs.readFileSync(tokenPath, 'utf8'));

// Inject authorization header using chrome_evaluate
await chrome_evaluate(`
  // Store token for use in fetch requests
  window.AUTH_TOKEN = '${tokenData.token}';
  
  // Override fetch to include Authorization header
  const originalFetch = window.fetch;
  window.fetch = function(...args) {
    if (args[1] === undefined) {
      args[1] = {};
    }
    if (args[1].headers === undefined) {
      args[1].headers = {};
    }
    args[1].headers['Authorization'] = 'Bearer ' + window.AUTH_TOKEN;
    return originalFetch.apply(this, args);
  };
  
  // Also set for XMLHttpRequest
  const originalOpen = XMLHttpRequest.prototype.open;
  XMLHttpRequest.prototype.open = function(...args) {
    const result = originalOpen.apply(this, args);
    this.setRequestHeader('Authorization', 'Bearer ' + window.AUTH_TOKEN);
    return result;
  };
`);

// Verify authentication by navigating to a protected page
chrome_navigate to protected_page_url
// Check if redirected to login or if page loads successfully
```

**JWT Token File Format:**
The JWT token file should be JSON with at minimum:
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

Optional fields that may be useful:
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "refresh_token_here",
  "expires_at": "2025-10-26T00:00:00Z",
  "user_id": "user123"
}
```

### Example Navigation Sequence with Visual Analysis

```
# Set up JWT authentication (if needed)
Read JWT token from /mnt/user-data/uploads/auth.json
Inject auth headers using chrome_evaluate

# Review dashboard
chrome_navigate to https://app.example.com/dashboard
chrome_wait_for_navigation
chrome_wait_for_selector selector=".main-content"
chrome_screenshot -> save to dashboard.png
chrome_get_html -> save to dashboard.html

# Review form with help text
chrome_navigate to https://app.example.com/settings
chrome_wait_for_selector selector="form"
chrome_screenshot -> save to settings_empty.png
chrome_get_html -> save to settings.html

# Trigger error states
chrome_click selector="button[type='submit']"
chrome_wait_for_selector selector=".error"
chrome_screenshot -> save to settings_errors.png
chrome_get_html -> save to settings_errors.html

# Continue for other key pages...
```

## Step 3: Analyze Content

Run the analysis script on each captured HTML file to extract UX elements and identify issues.

### Run Analysis Script
```bash
python3 scripts/analyze_ux_elements.py page_name.html > page_name_analysis.json
```

The script outputs JSON with:
- **elements**: All extracted labels, buttons, inputs, help text, tooltips, etc.
- **issues**: Identified problems with severity levels
- **summary**: Counts and statistics

### Manual Review Complement
While the script catches common issues, also manually review for:
- **Tone and voice**: Is it consistent and appropriate?
- **Reading level**: Too technical or complex?
- **Cultural sensitivity**: Any potentially problematic language?
- **Context appropriateness**: Does help text match user needs?
- **Visual hierarchy**: Is important guidance prominent?

### Consult Best Practices
Review `references/ux_writing_best_practices.md` when evaluating:
- Ambiguous cases
- Writing style decisions
- Accessibility standards
- Component-specific guidelines

## Step 4: Visual Analysis of Screenshots

Review captured screenshots to evaluate guidance placement, visual hierarchy, and layout effectiveness.

### Visual Review Checklist

For each screenshot, assess:

**1. Visual Hierarchy**
- Is help text visually distinguished from primary content?
- Are labels appropriately sized and weighted?
- Do error messages stand out enough to catch attention?
- Are tooltips/info icons visible but not distracting?

**2. Proximity and Association**
- Are labels immediately adjacent to their inputs?
- Is help text close enough to the relevant field?
- Can users easily connect error messages to fields?
- Are related elements grouped visually?

**3. Layout and Spacing**
- Is there adequate white space around guidance text?
- Do help sections feel cramped or buried?
- Are error messages pushed below the fold?
- Is the layout responsive and guidance still visible on smaller viewports?

**4. Visual Affordances**
- Are interactive help elements (tooltips, info icons) discoverable?
- Do help icons follow consistent visual patterns?
- Are required fields clearly marked?
- Is there visual feedback for interactive states?

**5. Color and Contrast**
- Is help text readable (sufficient contrast)?
- Are error messages visually distinct from normal text?
- Does color-coding enhance or confuse?
- Will guidance work for colorblind users?

**6. Information Density**
- Is guidance text appropriately concise for the space?
- Are users overwhelmed with too much help text?
- Is critical guidance buried in walls of text?
- Could progressive disclosure improve the layout?

### Document Visual Issues

For each visual problem identified, note:
- **Screenshot reference**: Which image shows the issue
- **Element location**: Where on the page it appears
- **Visual problem**: What's wrong with the placement/appearance
- **User impact**: How it affects usability
- **Recommendation**: Specific layout or styling improvement

### Examples of Visual Issues

**Poor Proximity:**
```
Issue: Label "Email address" appears 20px above input, with unrelated 
       text in between, breaking visual association
Screenshot: signup.png
Recommendation: Place label directly above input with minimal spacing
```

**Hidden Help Text:**
```
Issue: Important password requirements appear in tiny gray text below 
       the submit button, easily missed
Screenshot: signup.png  
Recommendation: Move requirements next to password field, increase 
       font size, use darker color
```

**Buried Error Messages:**
```
Issue: Validation errors appear at top of long form, requiring scroll 
       to see which fields failed
Screenshot: settings_errors.png
Recommendation: Show errors inline next to each problem field
```

## Step 5: Context Enhancement with Documentation

If user provided a documentation folder path, cross-reference the in-app guidance with existing help documentation.

### Load and Index Documentation

1. **Scan documentation folder** for relevant files:
   ```bash
   find /path/to/docs -type f \( -name "*.md" -o -name "*.html" -o -name "*.txt" \)
   ```

2. **Read key documentation files**:
   - User guides and tutorials
   - FAQ documents  
   - Feature documentation
   - API or technical reference (if relevant)

3. **Index documentation content** by topic/feature:
   - Extract headings and sections
   - Note which features are documented
   - Identify documented workflows
   - Map documentation to UI pages

### Cross-Reference Analysis

Compare in-app guidance against documentation:

**1. Consistency Check**
- Does UI use same terminology as docs?
- Are steps/instructions aligned?
- Do examples match between docs and UI?
- Are there conflicting explanations?

**2. Gap Analysis**
- Are documented features missing in-app help?
- Are UI elements unexplained in docs?
- Could complex doc sections be summarized in UI?
- Should UI link to relevant doc sections?

**3. Content Opportunity Identification**
- Can lengthy doc explanations be condensed for in-app tooltips?
- Should certain UI help text link to fuller doc coverage?
- Are there doc diagrams/examples that could inform better UI copy?
- Could FAQ answers improve in-app error messages?

**4. Integration Recommendations**
- Suggest specific doc links to add to UI
- Identify doc content that should be surfaced in-app
- Recommend help text that references doc sections
- Propose inline examples from documentation

### Document Documentation-Related Findings

For each documentation-related issue:
```
Issue: Password complexity requirements differ between signup 
       form and documentation
In-app: "8 characters minimum"
Docs: "8-32 characters, must include number and special character"
Recommendation: Update UI help text to match documented requirements
```

```
Opportunity: Documentation has excellent examples of valid date 
            formats, but date input has no guidance
Docs: Section "Date Format Guide" with 5 clear examples
Recommendation: Add example placeholder or help text: "MM/DD/YYYY 
                (e.g., 12/25/2025)"
```

## Step 6: Compile Findings

Aggregate analysis results across all reviewed pages, including both content and visual findings.

### Categorize Issues by Priority

**High Priority** (address first):
- Missing labels or ARIA labels
- Inaccessible interactive elements  
- Unclear or missing error messages
- Broken functionality due to poor guidance
- Critical visual hierarchy problems (errors not visible, help text hidden)
- Documentation contradicting UI guidance

**Medium Priority** (address soon):
- Vague button or link text
- Inconsistent terminology
- Missing help text on complex forms
- Technical jargon without explanation
- Poor proximity between labels and inputs
- Help text with insufficient contrast
- Minor documentation inconsistencies

**Low Priority** (polish):
- Inconsistent capitalization
- Overly formal tone
- Minor wording improvements
- Unnecessary punctuation
- Spacing and layout refinements
- Opportunities to integrate documentation links

### Identify Patterns
Look for recurring issues across pages:
- Same problem appearing multiple times
- Inconsistent approaches to similar components
- Missing patterns (no help text anywhere)
- Good patterns to standardize
- Visual layout issues that repeat
- Documentation gaps affecting multiple pages
- Good patterns to standardize

### Group by Location
Organize findings by:
- Page/section (for targeted fixes)
- Component type (for systematic improvements)
- User flow (for journey optimization)
- Visual layout issues (for design team)
- Documentation integration opportunities (for content team)

## Step 7: Generate Report

Create a comprehensive report using the template in `assets/report_template.md`.

### Report Structure
1. **Executive Summary**: High-level overview and key metrics
2. **Findings by Priority**: Detailed content and visual issues with recommendations
3. **Visual Analysis**: Screenshot-based layout and placement findings
4. **Documentation Integration**: Opportunities to leverage existing help content
5. **Page-by-Page Analysis**: Specific findings for each page
6. **Patterns and Consistency**: Cross-cutting observations
7. **Accessibility Considerations**: WCAG compliance issues
8. **Recommendations Summary**: Actionable next steps

### Writing the Report

**Be specific**: Include actual examples of current text, screenshots references, and suggested improvements

**Be actionable**: Provide clear recommendations, not just problems

**Be constructive**: Highlight positive findings alongside issues

**Be organized**: Use consistent formatting and clear hierarchy

**Provide context**: Explain why each issue matters to users

**Include visual evidence**: Reference screenshots that show the issues

**Link to documentation**: When relevant, reference existing help docs that could be integrated

### Populate Template
Copy `assets/report_template.md` and fill in:
- Application details and review metadata
- All findings organized by priority (content + visual)
- Screenshot references for visual issues
- Documentation cross-reference findings
- Specific examples from analysis results
- Page-by-page breakdowns with screenshots
- Summary recommendations

### Output Format
Save the completed report as a Markdown file and provide to user:
- Create file in `/mnt/user-data/outputs/ux_review_report.md`
- Include embedded screenshot references (using relative paths or base64)
- Offer to convert to other formats if requested (DOCX, PDF)
- Provide summary of key findings in response with screenshot highlights

## Tips for Effective Reviews

### Thoroughness
- Don't rush through pages - take time to interact
- Check responsive behavior if possible
- Test error states intentionally
- Review both happy path and edge cases

### Objectivity
- Apply guidelines consistently
- Don't impose personal preferences
- Ground feedback in UX best practices
- Consider the target audience

### Practicality
- Prioritize realistically - not everything is urgent
- Consider implementation effort
- Suggest quick wins separately
- Acknowledge good work

### Clarity
- Use examples liberally in findings
- Show before/after comparisons
- Explain the "why" behind recommendations
- Keep recommendations specific and testable

## Reference Documentation

### UX Writing Best Practices
See `references/ux_writing_best_practices.md` for comprehensive guidelines on:
- Component-specific best practices
- Accessibility considerations  
- Common issues to flag
- Review checklist

Load this reference when:
- Evaluating ambiguous cases
- Making style recommendations
- Explaining accessibility requirements
- Providing examples of good practices

### Visual Analysis Guide
See `references/visual_analysis_guide.md` for comprehensive guidelines on:
- Visual hierarchy principles
- Proximity and spacing standards
- Component-specific visual patterns
- Color and contrast requirements
- Layout evaluation criteria

Load this reference when:
- Reviewing screenshots for visual issues
- Evaluating guidance placement
- Assessing visual hierarchy
- Checking WCAG contrast compliance
- Making layout recommendations

### Chrome MCP Guide
See `references/chrome_mcp_guide.md` for details on:
- Available Chrome MCP tools
- Crawling strategies
- Extraction patterns
- Troubleshooting common issues

Load this reference when:
- Setting up complex crawls
- Handling authentication
- Dealing with dynamic content
- Optimizing performance

## Common Scenarios

### "Review our signup flow with visual analysis"
1. Navigate to signup page
2. Capture initial state screenshot
3. Intentionally trigger validation errors
4. Capture error state screenshot
5. Fill form with various inputs
6. Capture each step's HTML and screenshots
7. Analyze form labels, error messages, help text
8. Review screenshots for placement and visibility issues
9. Test completion and confirmation messages
10. Report on clarity, accessibility, visual hierarchy, and user guidance

### "Audit our entire application with our help docs"
1. Load documentation from provided folder path
2. Index help documentation by topic/feature
3. Get sitemap or main navigation structure
4. Systematically visit each major section
5. Capture screenshots and HTML for representative pages
6. Run content analysis on all HTML files
7. Cross-reference UI guidance with documentation
8. Review screenshots for layout and visual issues
9. Identify documentation integration opportunities
10. Generate comprehensive report with visual and content findings
11. Prioritize findings by impact and frequency

### "Check accessibility and visual layout of our forms"
1. Identify all form pages
2. Navigate and capture screenshots of each form
3. Extract form elements and labels from HTML
4. Check for ARIA attributes and label associations
5. Review screenshots for proximity and visual hierarchy
6. Verify error message visibility in screenshots
7. Test keyboard navigation patterns
8. Assess color contrast and readability
9. Report WCAG compliance issues with visual evidence

### "Review with JWT authentication and existing docs"
1. Load JWT token from provided file path
2. Inject authorization headers using chrome_evaluate
3. Verify authentication by accessing protected page
4. Load and index help documentation from provided folder
5. Navigate through authenticated pages
6. Capture screenshots and HTML content
7. Analyze guidance content against best practices
8. Cross-reference with existing documentation
9. Review visual layout and guidance placement
10. Identify inconsistencies between docs and UI
11. Generate report with authentication context preserved

### "Improve our button text and visual prominence"
1. Extract all button elements across pages
2. Capture screenshots showing button context
3. Categorize by type (primary, secondary, etc.)
4. Flag vague text ("Submit", "OK", "Click here")
5. Review screenshots for visual hierarchy of CTAs
6. Check for consistency across similar actions
7. Assess button placement and surrounding guidance
8. Suggest specific, action-oriented alternatives
9. Provide before/after examples with visual recommendations

## Bundled Resources

### scripts/analyze_ux_elements.py
Python script that analyzes HTML files to extract and evaluate UX elements.

**Usage:**
```bash
python3 scripts/analyze_ux_elements.py <html_file>
echo '<html>...</html>' | python3 scripts/analyze_ux_elements.py -
```

**Extracts:**
- Labels and their associations
- Button text and types
- Form inputs and placeholders
- Help text and tooltips
- Error messages
- Links and navigation
- Headings and structure
- ARIA attributes

**Identifies:**
- Missing labels
- Vague button/link text
- Inputs without guidance
- Accessibility issues
- Missing help text

### references/ux_writing_best_practices.md
Comprehensive guide to UX writing standards covering:
- Core principles (clarity, conciseness, consistency)
- Component-specific guidelines
- Accessibility considerations
- Common issues with priority levels
- Review checklist

### references/visual_analysis_guide.md
Comprehensive guide to visual UX analysis covering:
- Core visual principles (hierarchy, proximity, white space)
- Component-specific visual guidelines (labels, help text, errors, buttons)
- Layout patterns and spacing standards
- Color and contrast requirements
- Common visual issues by priority level
- Visual review checklist

### references/chrome_mcp_guide.md
Guide to using Chrome MCP tools effectively:
- Available tools and their usage
- Crawling strategies
- Extraction patterns
- JWT authentication setup
- Screenshot capture strategies
- Best practices
- Troubleshooting

### assets/report_template.md
Structured template for creating comprehensive UX review reports with sections for content findings, visual analysis, documentation integration, and recommendations with screenshot references.

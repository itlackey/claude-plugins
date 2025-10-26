# Chrome MCP Tools Reference

This reference explains how to use Chrome Model Context Protocol (MCP) tools for web application crawling and analysis, including JWT authentication setup.

## Available Chrome MCP Tools

The Chrome MCP server provides tools for controlling a Chrome browser instance. Common tools include:

### Navigation Tools
- **navigate**: Navigate to a URL
- **go_back**: Go back in browser history
- **go_forward**: Go forward in browser history
- **reload**: Reload current page

### Interaction Tools
- **click**: Click an element by selector
- **fill**: Fill a form field
- **select**: Select from a dropdown
- **press_key**: Press keyboard keys
- **hover**: Hover over an element

### Content Extraction Tools
- **screenshot**: Capture a screenshot
- **get_html**: Get the full HTML of the page
- **get_element**: Get specific element content
- **evaluate**: Execute JavaScript in the page context

### Page State Tools
- **wait_for_selector**: Wait for an element to appear
- **wait_for_navigation**: Wait for page navigation to complete

## Authentication Methods

### JWT (JSON Web Token) Authentication

Many modern web applications use JWT tokens for authentication. Here's how to set up JWT auth with Chrome MCP:

#### Reading the JWT Token File

The JWT token should be stored in `.claude/jwt.json` in the following format:

**Token file format:**
```json
{
  "value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
  "expires": null
}
```

Where:
- `value`: The JWT token string
- `expires`: Token expiration timestamp (ISO 8601 format) or `null` if no expiration

#### Injecting JWT into Browser Context

Use the `evaluate` tool to inject authentication headers:

```javascript
// Step 1: Read token file
const fs = require('fs');
const tokenPath = '.claude/jwt.json';
const authData = JSON.parse(fs.readFileSync(tokenPath, 'utf8'));
const token = authData.value;

// Step 2: Inject using chrome_evaluate
await chrome_evaluate(`
  // Store token globally
  window.AUTH_TOKEN = '${token}';
  
  // Override fetch API to include Authorization header
  const originalFetch = window.fetch;
  window.fetch = function(...args) {
    // Ensure headers object exists
    if (!args[1]) args[1] = {};
    if (!args[1].headers) args[1].headers = {};
    
    // Add Authorization header
    if (typeof args[1].headers === 'object' && !Array.isArray(args[1].headers)) {
      args[1].headers['Authorization'] = 'Bearer ' + window.AUTH_TOKEN;
    }
    
    return originalFetch.apply(this, args);
  };
  
  // Override XMLHttpRequest for older AJAX calls
  const XHR_OPEN = XMLHttpRequest.prototype.open;
  XMLHttpRequest.prototype.open = function(method, url, async, user, pass) {
    this._url = url;
    return XHR_OPEN.apply(this, arguments);
  };
  
  const XHR_SEND = XMLHttpRequest.prototype.send;
  XMLHttpRequest.prototype.send = function(data) {
    this.setRequestHeader('Authorization', 'Bearer ' + window.AUTH_TOKEN);
    return XHR_SEND.apply(this, arguments);
  };
  
  // Also set as cookie if application expects it there
  document.cookie = 'auth_token=' + window.AUTH_TOKEN + '; path=/; SameSite=Strict';
  
  // Log success
  console.log('JWT authentication headers injected successfully');
`);
```

#### Verifying Authentication

After injecting the token, verify it works:

```javascript
// Navigate to a protected page
await chrome_navigate('https://app.example.com/dashboard');
await chrome_wait_for_navigation();

// Check if we're still authenticated (not redirected to login)
const currentUrl = await chrome_evaluate('window.location.href');

if (currentUrl.includes('/login') || currentUrl.includes('/signin')) {
  // Authentication failed
  console.error('JWT authentication failed - redirected to login');
} else {
  // Success
  console.log('JWT authentication successful');
}
```

#### Alternative: Direct Header Injection

Some Chrome MCP implementations support direct header manipulation:

```javascript
// Set extra HTTP headers for all requests
await chrome_evaluate(`
  // Using Chrome DevTools Protocol (if available)
  chrome.webRequest.onBeforeSendHeaders.addListener(
    function(details) {
      details.requestHeaders.push({
        name: 'Authorization',
        value: 'Bearer ${token}'
      });
      return {requestHeaders: details.requestHeaders};
    },
    {urls: ["<all_urls>"]},
    ["blocking", "requestHeaders"]
  );
`);
```

#### Troubleshooting JWT Auth

**Token not working:**
- Verify token format (should be three base64 segments separated by dots)
- Check token expiration (decode JWT to see `exp` claim)
- Ensure token has proper permissions for the routes you're accessing
- Check if application expects token in header vs cookie vs localStorage

**Headers not being sent:**
- Verify the fetch/XHR override code executed successfully
- Check browser console for errors (use chrome_evaluate to read console)
- Some apps may use different header names (e.g., 'X-Auth-Token' instead of 'Authorization')

**Still redirected to login:**
- Application may check additional cookies or session data
- Token may need to be refreshed
- Application may require additional authentication steps (2FA, etc.)

### Form-Based Authentication

For traditional username/password login:

```javascript
// Navigate to login page
await chrome_navigate('https://app.example.com/login');
await chrome_wait_for_selector('input[type="email"]');

// Fill credentials
await chrome_fill('input[type="email"]', 'user@example.com');
await chrome_fill('input[type="password"]', 'password123');

// Submit form
await chrome_click('button[type="submit"]');
await chrome_wait_for_navigation();

// Verify login success
const url = await chrome_evaluate('window.location.href');
if (!url.includes('/login')) {
  console.log('Login successful');
}
```

### Session Persistence

Once authenticated (via JWT or form), the session persists for the browser instance:
- Cookies are maintained across navigations
- JWT tokens in localStorage/sessionStorage persist
- No need to re-authenticate for each page
- Session ends when browser instance closes

## Crawling Strategy

### Systematic Exploration

**Start with main entry points:**
1. Home page / landing page
2. Main navigation menu
3. Common user flows (signup, login, checkout)
4. Settings/configuration pages

**Navigate systematically:**
- Use navigation links rather than direct URL access when possible
- Respect application state (login when needed)
- Follow breadcrumb trails
- Track visited pages to avoid duplication

### Depth-First vs Breadth-First

**Breadth-first (recommended for UX review):**
- Capture all pages at one level before going deeper
- Better for getting overall coverage
- Easier to organize findings by section

**Depth-first:**
- Follow one path to completion before backtracking
- Better for understanding user flows
- Useful for multi-step processes

## Extraction Patterns

### Pattern 1: Page-by-Page Analysis with Screenshots
```
For each page in application:
  1. Navigate to page
  2. Wait for page load
  3. Wait for key elements to render
  4. Capture screenshot for visual analysis
  5. Extract HTML content
  6. Run analyze_ux_elements.py
  7. Store results with page context
  8. Link screenshot to HTML analysis
  9. Move to next page
```

### Pattern 2: Interactive Flow Analysis with State Capture
```
For each user flow:
  1. Start at entry point
  2. Capture initial state screenshot
  3. Interact with elements (fill forms, click buttons)
  4. Capture screenshots after each interaction
  5. Note error messages and validation
  6. Capture error state screenshots
  7. Extract guidance at each step
  8. Complete or abandon flow
  9. Capture completion screenshot
```

### Pattern 3: Component Inventory with Visual Documentation
```
For application:
  1. Visit representative pages
  2. Capture screenshots of each page
  3. Extract all unique components
  4. Screenshot individual components (if needed)
  5. Categorize by type (forms, buttons, modals)
  6. Analyze patterns and inconsistencies
  7. Document visual patterns with screenshot evidence
```

## Screenshot Capture Best Practices

### When to Capture Screenshots

**Essential Screenshots:**
- Every main page reviewed (for comprehensive analysis)
- Forms in empty state (baseline)
- Forms with validation errors (error visibility)
- Modal dialogs and overlays (placement check)
- Tooltips triggered (visibility and positioning)
- Success/confirmation states (feedback visibility)

**Optional Screenshots:**
- Hover states for interactive elements
- Expanded/collapsed sections
- Different viewport sizes (if testing responsive)
- Before/after user interactions

### Screenshot Timing

Wait for content to fully load before capturing:

```javascript
// Navigate to page
await chrome_navigate(url);
await chrome_wait_for_navigation();

// Wait for specific content
await chrome_wait_for_selector('.main-content');

// Additional wait for animations/transitions (if needed)
await chrome_evaluate('new Promise(resolve => setTimeout(resolve, 500))');

// Now capture
await chrome_screenshot();
```

### Screenshot Naming Convention

Use descriptive, consistent naming:

```
Good names:
- signup_form_empty.png
- signup_form_errors.png
- dashboard_main.png
- settings_account_section.png
- modal_delete_confirmation.png

Poor names:
- screenshot1.png
- image.png
- temp.png
```

### Full Page vs Viewport Screenshots

**Viewport screenshots** (default):
- Captures visible area only
- Faster to capture
- Good for above-the-fold analysis
- May miss content requiring scroll

**Full page screenshots** (if supported):
- Captures entire page including below-fold content
- Slower to capture
- Shows complete layout
- Useful for long forms or pages

```javascript
// Viewport screenshot (default)
await chrome_screenshot();

// Full page screenshot (if your MCP server supports it)
await chrome_screenshot({ fullPage: true });
```

### Organizing Screenshots

Keep screenshots organized for easy reference:

```
/home/claude/
  ├── html/
  │   ├── dashboard.html
  │   ├── signup.html
  │   └── settings.html
  └── screenshots/
      ├── dashboard_main.png
      ├── signup_empty.png
      ├── signup_errors.png
      ├── settings_account.png
      └── settings_security.png
```

### Screenshot Analysis Workflow

1. Capture screenshot and HTML simultaneously
2. Run content analysis on HTML
3. Manually review screenshot for visual issues
4. Cross-reference content issues with visual placement
5. Document findings with screenshot references
6. Include screenshot filenames in report

## Best Practices

### Page Load Handling
- Always wait for navigation to complete
- Use wait_for_selector for dynamic content
- Allow time for JavaScript frameworks to render
- Check for lazy-loaded content

### Error Handling
- Handle authentication requirements
- Gracefully handle 404s and errors
- Retry failed navigations (with limit)
- Skip problematic pages and continue

### Performance
- Screenshots are expensive operations - capture strategically
- Take screenshots of key pages/states, not every single navigation
- For large sites (50+ pages), prioritize representative pages
- Cache HTML content when revisiting pages
- Set reasonable timeouts (30-60s for page loads)
- Don't crawl too aggressively (rate limiting, 1-2s between pages)
- Consider batching: navigate → HTML → screenshot for multiple pages before analysis

### Scope Management
- Define clear boundaries (which domains/paths to crawl)
- Set maximum page limits for large sites
- Exclude admin/irrelevant sections
- Focus on user-facing interfaces

## Common Selectors for UX Elements

### Forms and Inputs
```css
/* All form elements */
form, input, textarea, select, button[type="submit"]

/* Specific input types */
input[type="text"], input[type="email"], input[type="password"]

/* Labels and help text */
label, .help-text, .hint, [role="tooltip"], .error-message
```

### Navigation
```css
/* Navigation elements */
nav, [role="navigation"], .navbar, .menu, .breadcrumb

/* Links */
a, [role="link"], button[role="link"]
```

### Interactive Elements
```css
/* Buttons */
button, [role="button"], input[type="button"], input[type="submit"]

/* Clickable regions */
[onclick], [role="button"], .clickable, .btn
```

### Content Regions
```css
/* Main content */
main, [role="main"], .content, article

/* Headings */
h1, h2, h3, h4, h5, h6

/* Alerts and messages */
[role="alert"], .alert, .notification, .message, .toast
```

## Example Workflow

### Complete Application Review
```
1. Setup Phase:
   - Identify application entry point
   - Determine authentication needs
   - List main sections to review
   - Define exclusions

2. Authentication (if needed):
   - Navigate to login page
   - Fill credentials
   - Submit and verify login
   - Capture any auth-related UX issues

3. Systematic Crawl:
   - Extract navigation menu structure
   - Visit each main section
   - For each section:
     * Get HTML content
     * Run UX analysis
     * Capture screenshots (selectively)
     * Note navigation context
     * Extract forms and interactions
   
4. Flow Testing:
   - Identify key user flows
   - Execute each flow step-by-step
   - Capture validation messages
   - Note error states
   - Test edge cases

5. Compilation:
   - Aggregate all findings
   - Group by page/section
   - Prioritize by severity
   - Create structured report
```

## Troubleshooting

### Page Not Loading
- Check URL validity
- Verify network connectivity
- Increase timeout duration
- Check for JavaScript errors

### Element Not Found
- Wait longer for dynamic content
- Check selector specificity
- Verify element exists in page
- Use more robust selectors (data attributes)

### Authentication Issues
- Clear cookies and retry
- Verify credentials
- Check for CAPTCHA or 2FA
- Use session persistence

### Content Not Captured
- Ensure JavaScript execution complete
- Check for iframes (separate context)
- Look for shadow DOM elements
- Verify page fully rendered

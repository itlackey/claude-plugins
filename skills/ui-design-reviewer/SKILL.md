---
name: ui-design-reviewer
description: Comprehensive UI/UX design review using specialized design agent personas. Evaluates visual design, interaction design, information architecture, responsive behavior, accessibility, and brand consistency. Uses screenshots and HTML analysis with expert-level critique from multiple design perspectives. Supports JWT authentication for protected applications.
---

# UI/UX Design Reviewer

## Overview

This skill enables comprehensive design review of web applications using specialized design agent personas. Each agent brings expert-level evaluation from their specific design discipline, providing actionable feedback on visual design, interaction patterns, information architecture, accessibility, and brand consistency. The skill combines screenshot analysis, HTML inspection, and design principles to deliver professional design critique.

## Design Agent Personas

When conducting reviews, Claude adopts specialized design agent personas, each evaluating the interface through their expert lens:

### 🎨 Visual Design Agent
**Focus:** Aesthetics, visual hierarchy, color theory, typography, spacing

**Evaluates:**
- Visual hierarchy and focal points
- Color palette effectiveness and harmony
- Typography choices and readability
- White space and layout balance
- Consistency of visual style
- Shadow, depth, and dimension usage
- Icon and imagery quality
- Overall aesthetic appeal

**Output Style:** Detailed visual critique with specific design recommendations

### 🖱️ Interaction Design Agent
**Focus:** User flows, micro-interactions, feedback, state management

**Evaluates:**
- Button states (hover, active, disabled, focus)
- Form interaction patterns
- Loading and transition states
- Error and success feedback
- Navigation patterns
- Click targets and touch areas
- Micro-interactions and animations
- Drag and drop interactions
- Modal and overlay behavior

**Output Style:** User flow analysis with interaction improvements

### 📐 Information Architecture Agent
**Focus:** Content structure, navigation, mental models, findability

**Evaluates:**
- Navigation structure and hierarchy
- Content organization and grouping
- Labels and categorization
- Search and filtering capabilities
- Information scent and wayfinding
- Progressive disclosure
- Mental model alignment
- Task completion paths

**Output Style:** Structural recommendations for improved organization

### ♿ Accessibility Agent
**Focus:** WCAG compliance, inclusive design, assistive technology support

**Evaluates:**
- Keyboard navigation and focus management
- Screen reader compatibility
- Color contrast ratios (WCAG AA/AAA)
- Text scaling and zoom behavior
- Alternative text for images
- ARIA attributes and semantic HTML
- Focus indicators visibility
- Touch target sizes (mobile)
- Motion and animation considerations

**Output Style:** Compliance-focused with remediation steps

### 📱 Responsive Design Agent
**Focus:** Cross-device experience, breakpoints, mobile optimization

**Evaluates:**
- Mobile, tablet, desktop layouts
- Breakpoint effectiveness
- Touch-friendly interactions
- Content prioritization across sizes
- Performance on mobile devices
- Orientation handling (portrait/landscape)
- Responsive typography
- Image and media responsiveness

**Output Style:** Device-specific recommendations

### 🎯 Brand Consistency Agent
**Focus:** Brand alignment, voice, personality, consistency

**Evaluates:**
- Brand color usage
- Typography alignment with brand
- Tone of voice in UI copy
- Imagery style consistency
- Component consistency across pages
- Overall brand expression
- Competitive differentiation
- Emotional impact

**Output Style:** Brand-focused recommendations

## Review Process

The design review follows these steps:

1. **Plan the review** - Define scope, authentication, agents to deploy, and pages to review
2. **Capture visual state** - Screenshot all pages and key interaction states
3. **Extract structural data** - Get HTML for technical analysis
4. **Deploy design agents** - Each agent reviews from their perspective
5. **Synthesize findings** - Combine insights across agents
6. **Generate report** - Create comprehensive design review with prioritized recommendations

## Step 1: Planning the Design Review

### Determine Scope

Ask the user to clarify:
- Application URL and key pages to review
- Authentication requirements (JWT token file or credentials)
- Which design agents to deploy (all six or subset)
- Specific design concerns or focus areas
- Target devices/viewports to evaluate
- Brand guidelines or design system (if available)

### Select Design Agents

**Full Review** (deploy all agents):
- Comprehensive evaluation from all perspectives
- Best for initial audits or major redesigns
- Expect 60-90 minutes for thorough review

**Targeted Review** (select specific agents):
- Visual + Interaction for visual design polish
- Accessibility + Responsive for compliance
- IA + Interaction for UX flow improvements
- Choose based on known concerns

### Authentication Setup

**JWT Authentication:**
1. Get path to JWT token JSON file from user
2. Read token file (format: `{"token": "jwt-string"}`)
3. Inject authorization headers using chrome_evaluate (see chrome_mcp_guide.md)
4. Verify authentication with test navigation

**Form-Based Authentication:**
1. Navigate to login page
2. Fill credentials
3. Submit and verify
4. Proceed with authenticated session

### Load Design Context (Optional)

If user provides design system or brand guidelines:
1. Ask for file paths or URLs
2. Review design tokens, color palettes, typography scales
3. Use as reference during agent evaluations
4. Check for consistency with established patterns

## Step 2: Capture Visual State

Screenshots are critical for design review - capture comprehensively.

### Screenshot Strategy

**Essential Captures:**
- Homepage / landing page (above fold and full page)
- Main navigation (expanded states)
- All key user flows (signup, dashboard, settings, etc.)
- Forms (empty, filled, error, success states)
- Modals and overlays (all variations)
- Data tables and lists (empty, populated, loading states)
- Interactive components (buttons, dropdowns, tooltips in various states)
- Mobile viewport (if responsive review requested)

**State Variations:**
- Default/rest state
- Hover state (when possible)
- Active/pressed state
- Disabled state
- Focus state (for keyboard navigation)
- Error state
- Success/confirmation state
- Loading state

### Capture Pattern

```
For each page/component:
1. Navigate and wait for full render
2. Capture default state screenshot
3. Trigger hover states (use chrome_hover)
4. Capture hover screenshot
5. Trigger interactions (clicks, fills)
6. Capture interactive state screenshots
7. Extract HTML for technical analysis
8. Name screenshots descriptively (e.g., homepage_hero.png, signup_errors.png)
```

### Viewport Variations

If responsive review requested:

```javascript
// Desktop (1920x1080)
await chrome_evaluate('window.resizeTo(1920, 1080)');
await chrome_screenshot(); // desktop_page.png

// Tablet (768x1024)
await chrome_evaluate('window.resizeTo(768, 1024)');
await chrome_screenshot(); // tablet_page.png

// Mobile (375x667)
await chrome_evaluate('window.resizeTo(375, 667)');
await chrome_screenshot(); // mobile_page.png
```

## Step 3: Extract Structural Data

Get HTML for technical analysis alongside visual review.

### HTML Extraction Pattern

```
For each page:
1. After screenshot capture, get HTML using chrome_get_html
2. Save with matching name (page_name.html)
3. Extract computed styles for key elements (if needed)
4. Note any JavaScript-driven behavior
```

### Computed Styles Extraction

For key elements, capture computed styles:

```javascript
const styles = await chrome_evaluate(`
  const el = document.querySelector('.primary-button');
  const computed = window.getComputedStyle(el);
  ({
    color: computed.color,
    backgroundColor: computed.backgroundColor,
    fontSize: computed.fontSize,
    fontFamily: computed.fontFamily,
    padding: computed.padding,
    borderRadius: computed.borderRadius,
    boxShadow: computed.boxShadow
  });
`);
```

## Step 4: Deploy Design Agents

Each agent conducts their specialized review.

### Agent Review Process

For each selected agent:

1. **Load relevant reference** - Agent reads their design guidelines
2. **Review screenshots** - Systematic visual analysis
3. **Analyze HTML** - Technical inspection where relevant
4. **Document findings** - Record issues and recommendations
5. **Prioritize issues** - Severity levels based on impact

### Visual Design Agent Review

**Process:**
1. Load `references/visual_design_principles.md`
2. Review all screenshots for visual quality
3. Evaluate color usage and contrast
4. Assess typography hierarchy
5. Check spacing and alignment
6. Analyze visual consistency

**Questions Asked:**
- Does the visual hierarchy guide the eye effectively?
- Is the color palette harmonious and purposeful?
- Are typography choices appropriate for the content?
- Is white space used to create breathing room?
- Do shadows and depth enhance or distract?
- Is the overall aesthetic professional and polished?

**Output:**
- Color palette analysis
- Typography assessment
- Layout and spacing critique
- Visual hierarchy recommendations
- Specific design improvements

### Interaction Design Agent Review

**Process:**
1. Load `references/interaction_design_patterns.md`
2. Review state variation screenshots
3. Analyze user flow between pages
4. Evaluate feedback mechanisms
5. Check interaction affordances
6. Assess micro-interactions

**Questions Asked:**
- Do interactive elements communicate their affordance?
- Is feedback immediate and clear?
- Are loading states handled gracefully?
- Do transitions enhance or confuse?
- Are error states helpful and recoverable?
- Can users complete tasks efficiently?

**Output:**
- State management analysis
- User flow improvements
- Feedback mechanism recommendations
- Micro-interaction suggestions
- Interaction pattern proposals

### Information Architecture Agent Review

**Process:**
1. Load `references/information_architecture_principles.md`
2. Analyze navigation structure
3. Review content organization
4. Evaluate labeling and categorization
5. Assess findability
6. Check mental model alignment

**Questions Asked:**
- Can users find what they need quickly?
- Is the navigation structure logical?
- Are labels clear and meaningful?
- Is content grouped appropriately?
- Does the structure match user mental models?
- Is progressive disclosure used effectively?

**Output:**
- Navigation restructuring suggestions
- Content organization improvements
- Labeling recommendations
- Search and filter enhancements
- Wayfinding improvements

### Accessibility Agent Review

**Process:**
1. Load `references/accessibility_standards.md`
2. Review HTML for semantic structure and ARIA
3. Check color contrast ratios in screenshots
4. Evaluate keyboard navigation capability
5. Assess focus indicator visibility
6. Check touch target sizes

**Questions Asked:**
- Can the interface be used with keyboard only?
- Are color contrast ratios WCAG compliant?
- Are all interactive elements accessible to screen readers?
- Are focus indicators clearly visible?
- Can content be zoomed to 200% without breaking?
- Are touch targets large enough on mobile?

**Output:**
- WCAG compliance scorecard
- Specific violations with severity
- Remediation steps for each issue
- Code examples for fixes
- Priority accessibility improvements

### Responsive Design Agent Review

**Process:**
1. Load `references/responsive_design_guidelines.md`
2. Compare screenshots across viewports
3. Evaluate breakpoint effectiveness
4. Check content prioritization
5. Assess touch optimization
6. Review performance implications

**Questions Asked:**
- Does the layout adapt gracefully to all sizes?
- Are breakpoints at logical points?
- Is content appropriately prioritized on mobile?
- Are touch targets large enough (44x44px minimum)?
- Do images and media scale appropriately?
- Does navigation work well on mobile?

**Output:**
- Breakpoint recommendations
- Mobile-specific improvements
- Content prioritization suggestions
- Touch optimization proposals
- Performance considerations

### Brand Consistency Agent Review

**Process:**
1. Load brand guidelines if provided (or `references/brand_consistency_guide.md`)
2. Review visual consistency across pages
3. Evaluate brand expression
4. Check component consistency
5. Assess tone and personality
6. Compare with competitor benchmarks (if applicable)

**Questions Asked:**
- Does the interface express the brand personality?
- Are brand colors used consistently and purposefully?
- Does typography align with brand guidelines?
- Is the tone of voice consistent?
- Are components used consistently?
- Does the design differentiate from competitors?

**Output:**
- Brand alignment assessment
- Consistency violations
- Brand expression recommendations
- Component standardization needs
- Competitive positioning insights

## Step 5: Synthesize Findings

Combine insights from all agents into coherent recommendations.

### Cross-Agent Patterns

Identify issues mentioned by multiple agents:
- Visual + Accessibility agent both flag contrast → High priority
- IA + Interaction agent both note confusing flow → Critical UX issue
- Visual + Brand agent both see inconsistency → Style guide needed
- Accessibility + Responsive agent both flag touch targets → Fix immediately

### Prioritization Framework

**Critical (Fix Immediately):**
- Accessibility violations (WCAG A failures)
- Broken user flows that prevent task completion
- Brand misalignment that damages trust
- Major visual hierarchy problems causing confusion
- Navigation that blocks critical features

**High Priority (Address Soon):**
- Accessibility issues (WCAG AA failures)
- Interaction pattern inconsistencies
- Visual design polish needs affecting credibility
- IA improvements for findability
- Responsive issues on key devices

**Medium Priority (Plan for Next Iteration):**
- Accessibility enhancements (WCAG AAA)
- Micro-interaction refinements
- Visual design optimization
- IA enhancements for efficiency
- Brand expression improvements

**Low Priority (Future Consideration):**
- Visual polish and delight details
- Advanced interaction patterns
- Experimental features
- Minor consistency improvements

### Consolidation Strategy

Group related findings:
- All button-related issues together
- All navigation issues together
- All color/contrast issues together
- All responsive issues by breakpoint
- All component consistency issues together

## Step 6: Generate Comprehensive Report

Create detailed design review report using `assets/design_review_template.md`.

### Report Structure

1. **Executive Summary**
   - Overall design maturity assessment (1-5 scale)
   - Key findings by agent
   - Critical recommendations
   - Design system needs

2. **Agent-by-Agent Findings**
   - Visual Design Agent findings
   - Interaction Design Agent findings
   - Information Architecture Agent findings
   - Accessibility Agent findings
   - Responsive Design Agent findings
   - Brand Consistency Agent findings

3. **Cross-Cutting Themes**
   - Patterns seen by multiple agents
   - System-wide improvements needed
   - Component library needs
   - Design system recommendations

4. **Page-by-Page Review**
   - Screenshots with annotations
   - Specific issues per page
   - Priority improvements

5. **Prioritized Roadmap**
   - Critical fixes (0-2 weeks)
   - High priority (2-6 weeks)
   - Medium priority (6-12 weeks)
   - Long-term vision

6. **Design System Recommendations**
   - Color palette refinements
   - Typography system
   - Spacing scale
   - Component patterns
   - Interaction patterns

### Report Quality Standards

**Be Specific:**
```
Bad: "Button spacing needs improvement"
Good: "Primary buttons have 8px padding but should have 12px vertical and 24px horizontal padding for optimal touch targets (44x44px minimum)"
```

**Provide Examples:**
```
Bad: "Colors clash"
Good: "The red CTA button (#FF0000) clashes with the purple header (#7B2CBF). Recommend using brand teal (#00B4D8) for CTAs to maintain harmony"
```

**Reference Screenshots:**
```
Issue: Visual hierarchy unclear in hero section
Screenshot: homepage_hero.png
Problem: Headline (32px) and CTA text (30px) are too similar in size
Recommendation: Increase headline to 48px, reduce CTA to 16px
```

## Common Scenarios

### "Full design audit of our application"
1. Authenticate to application (JWT or form-based)
2. Capture all key pages and states (desktop + mobile)
3. Deploy all six design agents
4. Each agent conducts thorough review
5. Synthesize findings across agents with cross-agent pattern analysis
6. Generate comprehensive report with prioritized roadmap
7. Provide design system recommendations

### "Accessibility-focused review"
1. Deploy Accessibility Agent (primary)
2. Deploy Visual Design Agent (for contrast analysis)
3. Capture screenshots and HTML
4. Conduct WCAG compliance evaluation (A, AA, AAA)
5. Test keyboard navigation patterns
6. Generate remediation report with code examples
7. Provide priority ranking for fixes

### "Evaluate our new signup flow"
1. Deploy Interaction Design Agent (primary)
2. Deploy Visual Design Agent (secondary)
3. Capture each step of flow with all states
4. Capture empty, filled, error, and success states
5. Analyze user flow efficiency and friction points
6. Evaluate interaction patterns and feedback
7. Provide flow optimization recommendations with mockups

### "Review with our design system"
1. Load design system documentation from provided path
2. Deploy Visual + Brand agents primarily
3. Capture all components across pages
4. Check consistency with design system tokens
5. Identify deviations and violations
6. Provide alignment recommendations
7. Suggest design system additions for new patterns

### "Mobile app design review"
1. Deploy Responsive Agent (primary)
2. Deploy Interaction Agent (secondary for touch)
3. Capture mobile viewport screenshots (375x667, 414x896)
4. Test touch interactions and target sizes
5. Evaluate mobile-specific patterns
6. Check performance on mobile (if possible)
7. Provide mobile optimization recommendations

### "Competitive design analysis"
1. Review target application with all agents
2. Review 2-3 competitor applications similarly
3. Deploy all agents for each application
4. Compare findings across applications
5. Identify industry best practices and gaps
6. Provide differentiation recommendations
7. Create competitive positioning matrix

## Tips for Effective Design Reviews

### Agent Selection Strategy

**Choose agents based on goals:**
- New design → All agents for comprehensive audit
- Accessibility compliance → Accessibility + Visual agents
- User flow issues → IA + Interaction agents
- Brand refresh → Brand + Visual agents
- Mobile optimization → Responsive + Interaction agents
- Design system consistency → Visual + Brand agents

### Screenshot Best Practices

- Capture at actual size (no scaling artifacts)
- Ensure full render (wait for all assets)
- Get clean screenshots (hide browser UI if possible)
- Capture multiple states exhaustively
- Organize systematically by page/component
- Name descriptively (page_state_viewport.png)

### Agent Perspective Maintenance

Each agent should:
- Maintain their specific lens/expertise
- Provide actionable, specific recommendations
- Cite exact examples from screenshots
- Prioritize issues appropriately
- Suggest concrete improvements with details
- Use their domain's terminology correctly

### Synthesis Quality

- Find patterns across agents (indicates system issues)
- Avoid redundancy in recommendations
- Group related issues logically
- Prioritize based on user and business impact
- Create clear, actionable items
- Provide estimated effort for fixes

## Reference Documentation

### Visual Design Principles
See `references/visual_design_principles.md` for comprehensive guide on color theory, typography, layout, spacing, and visual hierarchy evaluation.

Load when: Visual Design Agent is deployed

### Interaction Design Patterns
See `references/interaction_design_patterns.md` for common patterns, state management, micro-interactions, and user flow best practices.

Load when: Interaction Design Agent is deployed

### Information Architecture Principles
See `references/information_architecture_principles.md` for navigation structures, content organization, labeling, and findability strategies.

Load when: Information Architecture Agent is deployed

### Accessibility Standards
See `references/accessibility_standards.md` for complete WCAG 2.1 compliance guide with remediation steps and code examples.

Load when: Accessibility Agent is deployed

### Responsive Design Guidelines
See `references/responsive_design_guidelines.md` for breakpoint strategies, mobile optimization, and cross-device best practices.

Load when: Responsive Design Agent is deployed

### Brand Consistency Guide
See `references/brand_consistency_guide.md` for brand evaluation framework, consistency checking, and competitive analysis.

Load when: Brand Consistency Agent is deployed

## Bundled Resources

### scripts/analyze_design_elements.py
Python script that analyzes HTML and screenshots for design metrics including color extraction, typography detection, spacing patterns, and contrast calculation.

### references/visual_design_principles.md
Comprehensive visual design evaluation guide covering color theory, typography, layout, spacing, and visual hierarchy.

### references/interaction_design_patterns.md
Common interaction patterns, state management standards, micro-interactions, feedback mechanisms, and animation principles.

### references/information_architecture_principles.md
Navigation structures, content organization strategies, labeling guidelines, search patterns, and mental model alignment.

### references/accessibility_standards.md
WCAG 2.1 Level A, AA, AAA criteria, keyboard navigation, screen reader best practices, color contrast, and focus management.

### references/responsive_design_guidelines.md
Breakpoint strategies, mobile-first approaches, touch optimization, content prioritization, and performance considerations.

### references/brand_consistency_guide.md
Brand evaluation framework, component consistency checking, tone assessment, and competitive benchmarking methodology.

### assets/design_review_template.md
Structured template for comprehensive design review reports with agent-specific sections, screenshot annotations, and prioritized recommendations.
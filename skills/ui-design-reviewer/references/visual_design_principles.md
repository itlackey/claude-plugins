# Visual Design Principles

This reference provides the Visual Design Agent with comprehensive guidelines for evaluating visual aesthetics, hierarchy, color usage, typography, and layout.

## Core Visual Design Principles

### 1. Visual Hierarchy

The arrangement of elements to show their order of importance.

**Evaluation Criteria:**
- **Primary focus point**: Is there a clear entry point for the eye?
- **Reading order**: Does the eye flow logically through content?
- **Relative importance**: Do sizing/weight/color reflect content priority?
- **Grouping**: Are related elements visually similar?

**Common Issues:**
- Everything is the same size (no hierarchy)
- Too many competing focal points
- Important elements buried or too small
- Illogical visual flow

**Best Practices:**
- Use scale to show importance (larger = more important)
- Limit to 3-4 levels of hierarchy
- Use one dominant focal point per screen
- Create clear visual paths

### 2. Color Theory

Strategic use of color for communication, emotion, and usability.

**Color Palette Structure:**
- **Primary color**: Main brand color, used sparingly for key actions
- **Secondary colors**: Supporting colors (2-3 colors)
- **Neutral colors**: Grays, blacks, whites for UI (3-5 shades)
- **Semantic colors**: Success (green), error (red), warning (yellow), info (blue)
- **Accent color**: Optional highlight color

**Evaluation Criteria:**
- **Harmony**: Do colors work well together?
- **Purpose**: Is each color used intentionally?
- **Consistency**: Are colors used consistently across pages?
- **Contrast**: Is there sufficient contrast for readability?
- **Balance**: Is color distribution balanced (not overwhelming)?

**Color Harmony Models:**
- Monochromatic: Variations of one hue
- Analogous: Adjacent colors on color wheel
- Complementary: Opposite colors on wheel
- Triadic: Three evenly spaced colors
- Split-complementary: One color + two adjacent to complement

**Common Issues:**
- Too many colors (chaotic, unprofessional)
- Insufficient contrast (hard to read)
- Inconsistent semantic colors (red sometimes error, sometimes brand)
- Clashing colors (uncomfortable to view)
- Using color alone to convey meaning (accessibility issue)

**Best Practices:**
- Stick to 5-7 core colors total
- Use 60-30-10 rule (60% dominant, 30% secondary, 10% accent)
- Ensure 4.5:1 contrast minimum for text
- Use color purposefully, not decoratively
- Test in grayscale to check hierarchy works without color

### 3. Typography

The art and technique of arranging type for readability and visual appeal.

**Type Scale:**
- H1: 32-48px (hero headings)
- H2: 24-32px (section headings)
- H3: 20-24px (subsection headings)
- H4: 18-20px (component headings)
- Body: 16px (default reading size)
- Small: 14px (secondary info)
- Tiny: 12px (captions, legal text - use sparingly)

**Evaluation Criteria:**
- **Hierarchy**: Do heading levels clearly differ?
- **Readability**: Is body text comfortable to read?
- **Line length**: 45-75 characters per line (ideal: 66)
- **Line height**: 1.4-1.6 for body text
- **Font pairing**: Do fonts complement each other?
- **Consistency**: Are fonts used consistently?

**Font Selection:**
- **Serif**: Traditional, formal, print-like (Georgia, Merriweather)
- **Sans-serif**: Modern, clean, digital (Inter, Roboto, Helvetica)
- **Display**: Unique, attention-grabbing, use sparingly
- **Monospace**: Code, technical content (Fira Code, Monaco)

**Common Issues:**
- Too many font families (unprofessional, distracting)
- Insufficient size differences between levels
- Body text too small (<14px)
- Line length too long (>100 characters - tiring to read)
- Poor line height (cramped or too loose)
- All caps overuse (harder to read)

**Best Practices:**
- Use 2-3 font families maximum
- Establish clear type scale with consistent ratios
- Body text 16px minimum
- Line height 1.5x font size for body text
- Limit line length to 70 characters
- Use font weight for hierarchy (not just size)
- Left-align body text (easier to read)

### 4. Spacing and Layout

The use of white space to create breathing room and organization.

**Spacing Scale:**
Use consistent spacing based on a scale (e.g., 4px base):
- 4px: Tight spacing within components
- 8px: Between related elements
- 16px: Between components
- 24px: Between sections
- 32px: Between major sections
- 48px: Between page sections
- 64px+: Large visual breaks

**Layout Systems:**
- **Grid**: Column-based structure (8-12 columns typical)
- **Flexbox**: Flexible row/column layouts
- **Baseline grid**: Vertical rhythm based on line height

**Evaluation Criteria:**
- **Breathing room**: Is there adequate white space?
- **Consistency**: Is spacing consistent across pages?
- **Grouping**: Does spacing show relationships?
- **Alignment**: Are elements properly aligned?
- **Balance**: Is visual weight distributed well?

**Common Issues:**
- Elements too cramped (claustrophobic)
- Inconsistent spacing (unprofessional)
- Poor alignment (sloppy appearance)
- Excessive white space (disconnected elements)
- Unbalanced layouts (heavy on one side)

**Best Practices:**
- Use consistent spacing scale throughout
- More space = less related
- Align elements to grid
- Balance visual weight on page
- Use white space as design element
- Maintain consistent margins and padding

### 5. Visual Consistency

Using the same design patterns and styles throughout.

**Consistency Areas:**
- Button styles (primary, secondary, tertiary)
- Input field appearance
- Card/panel styles
- Icon style and size
- Shadow patterns
- Border radius values
- Hover/focus states

**Evaluation Criteria:**
- **Component consistency**: Same components look the same
- **Pattern consistency**: Similar elements use similar patterns
- **Style consistency**: Visual style is cohesive
- **Behavior consistency**: Interactions work predictably

**Common Issues:**
- Multiple button styles for same action
- Inconsistent card shadows
- Mixed border radius values
- Inconsistent icon styles
- Different hover effects on similar elements

**Best Practices:**
- Create component library
- Document design system
- Reuse patterns consistently
- Establish and maintain design tokens

### 6. Depth and Dimension

Using shadows, layers, and visual cues to create spatial relationships.

**Elevation Levels:**
- Level 0: Base surface (no shadow)
- Level 1: Cards, slight elevation (subtle shadow)
- Level 2: Raised buttons, hover states (medium shadow)
- Level 3: Modals, dropdowns (strong shadow)
- Level 4: Tooltips, top-level overlays (strongest shadow)

**Shadow Guidelines:**
```css
/* Level 1 - Subtle */
box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);

/* Level 2 - Medium */
box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);

/* Level 3 - Strong */
box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);

/* Level 4 - Very Strong */
box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22);
```

**Common Issues:**
- Inconsistent shadow usage
- Too many elevation levels (confusing)
- Shadows too strong (distracting)
- Flat design without any depth cues
- Shadows point in different directions

**Best Practices:**
- Use 3-4 elevation levels maximum
- Shadows should always point down (consistent light source)
- Use subtle shadows for most elements
- Reserve strong shadows for modals and key overlays
- Consider flat design if brand-appropriate

### 7. Visual Balance

Distribution of visual weight to create stable, pleasing compositions.

**Types of Balance:**
- **Symmetrical**: Mirror image (formal, stable)
- **Asymmetrical**: Different elements balanced by weight (dynamic, interesting)
- **Radial**: Elements arranged around center point

**Visual Weight Factors:**
- Size (larger = heavier)
- Color (bright/dark = heavier)
- Density (more elements = heavier)
- Texture (complex = heavier)
- Position (isolated = heavier)

**Common Issues:**
- Too heavy on one side (feels unstable)
- Perfectly symmetrical everything (boring)
- No focal point (everything competes)

**Best Practices:**
- Balance visual weight across page
- Use asymmetry for interest
- Create intentional imbalance for movement
- Consider the whole page, not just sections

## Design Evaluation Framework

### Visual Quality Scorecard

Rate each aspect on scale of 1-5:

**Visual Hierarchy**: 
- 1: No clear hierarchy, everything same importance
- 3: Some hierarchy but inconsistent
- 5: Clear, consistent, effective hierarchy throughout

**Color Usage**:
- 1: Clashing, too many colors, no consistency
- 3: Adequate colors but some inconsistency or harmony issues
- 5: Beautiful, harmonious palette used consistently

**Typography**:
- 1: Poor readability, inconsistent, too many fonts
- 3: Adequate but lacks polish or has minor issues
- 5: Excellent type system, perfect readability

**Spacing & Layout**:
- 1: Cramped, inconsistent, poor alignment
- 3: Functional but lacks consistency or refinement
- 5: Perfect spacing, great white space, consistent

**Visual Consistency**:
- 1: Different patterns everywhere, no system
- 3: Mostly consistent with some variations
- 5: Perfect consistency, clear design system

**Overall Polish**:
- 1: Looks unfinished or amateur
- 3: Functional and adequate but not refined
- 5: Highly polished, professional, beautiful

### Common Design Smells

**Red Flags:**
- More than 3-4 font families
- More than 7-8 colors in regular use
- Inconsistent button styles
- No clear visual hierarchy
- Poor contrast (hard to read)
- Cramped spacing
- Misaligned elements
- Multiple shadow patterns
- Clashing colors

**Design Debt Indicators:**
- Inconsistent patterns across pages
- Multiple versions of same component
- One-off designs that don't fit system
- No design system or tokens
- Hard-coded values instead of variables

## Specific Component Guidelines

### Buttons

**Visual Treatment:**
- Primary: Filled with brand color, high contrast
- Secondary: Outline or low contrast fill
- Tertiary: Text only, no background

**Sizing:**
- Small: 32px height, 12px 16px padding
- Medium: 40px height, 12px 24px padding  
- Large: 48px height, 16px 32px padding

**States:**
- Default: Base colors
- Hover: Slightly darker/lighter (5-10% change)
- Active: Darker still
- Disabled: 40% opacity or gray
- Focus: Clear focus ring (3px, brand color)

**Common Issues:**
- All buttons look the same (no hierarchy)
- Hover state too subtle or missing
- Disabled state unclear
- Focus state invisible
- Inconsistent sizing across pages

### Cards

**Visual Treatment:**
- Subtle shadow for elevation (1-2 level)
- 8-16px border radius for rounded corners
- Consistent padding (16-24px)
- White or light background

**Common Issues:**
- No elevation (flat, hard to distinguish)
- Inconsistent shadows
- Mixed border radius values
- Cramped content (insufficient padding)

### Forms

**Visual Treatment:**
- Clear field boundaries
- Adequate spacing between fields (16px minimum)
- Labels above or left of inputs
- Visual feedback on focus (border color change)
- Error states clearly visible (red border + text)

**Common Issues:**
- Fields blend into background
- No focus indicator
- Error state not obvious
- Labels disconnected from fields
- Insufficient spacing between fields

### Navigation

**Visual Treatment:**
- Clear active state (different from inactive)
- Hover state for feedback
- Consistent styling
- Appropriate size for importance

**Common Issues:**
- Active state same as inactive
- No hover feedback
- Inconsistent patterns (top nav vs side nav)
- Too many nav levels visible at once

## Reporting Visual Issues

### Issue Documentation Format

**Problem Statement:**
Clear, specific description of what's wrong

**Screenshot Reference:**
Which screenshot(s) show the issue

**Visual Analysis:**
What design principles are violated

**User Impact:**
How this affects user experience

**Recommendation:**
Specific design changes with values

**Example:**

```
Issue: Insufficient visual hierarchy on homepage hero

Screenshot: homepage_hero.png

Analysis:
- Headline (32px) and CTA text (28px) are too similar in size
- Both use the same font weight (600)
- Color contrast doesn't differentiate importance
- Eye doesn't know where to focus first

Impact:
Users don't immediately understand the value proposition
or see the call-to-action, reducing conversion

Recommendation:
- Increase headline to 48px, weight 700
- Reduce CTA text to 16px, weight 600
- Use brand color (#0066CC) for CTA, keep headline black
- Add more spacing (32px) between headline and CTA

Expected Result:
Clear visual path from headline to CTA, improved conversion
```

## Design Maturity Levels

**Level 1 - Functional**
- Works but not polished
- Inconsistent patterns
- No design system
- Visual issues prevalent

**Level 2 - Adequate**
- Generally works well
- Some consistency
- Basic patterns established
- Minor visual issues

**Level 3 - Good**
- Polished appearance
- Mostly consistent
- Emerging design system
- Few visual issues

**Level 4 - Excellent**
- Highly polished
- Consistent throughout
- Clear design system
- Minimal visual issues

**Level 5 - Outstanding**
- Beautiful, refined
- Perfect consistency
- Mature design system
- Industry-leading visuals

# Visual UX Analysis Guidelines

This reference provides guidelines for evaluating user interface guidance through visual analysis of screenshots.

## Core Visual Principles

### Visual Hierarchy
The relative importance and order in which users process visual information.

**Key Questions:**
- Does the visual weight match information priority?
- Are the most important elements most prominent?
- Is there a clear visual path through the content?
- Do less important elements recede appropriately?

### Proximity
Elements that are close together are perceived as related.

**Key Questions:**
- Are labels adjacent to their inputs?
- Is help text near the relevant field?
- Can users easily connect error messages to problem fields?
- Are related form fields visually grouped?

### White Space
Empty space that gives content room to breathe.

**Key Questions:**
- Is guidance text cramped or comfortable?
- Does spacing help distinguish different sections?
- Is there enough padding around help text?
- Does the layout feel cluttered or spacious?

## Component-Specific Visual Guidelines

### Form Labels

**Optimal Placement:**
- **Above input**: Most accessible, works well for all screen sizes
- **Left-aligned**: Good for compact forms, requires more horizontal space
- **Avoid right-aligned**: Creates ragged edge, harder to scan

**Spacing:**
- 4-8px between label and input (above placement)
- 8-12px between label and input (left placement)
- Labels should be closer to their input than to previous input

**Visual Weight:**
- Medium weight (500-600) for labels
- Sufficient contrast (minimum 4.5:1 for normal text)
- Slightly smaller than body text is acceptable

**Example Issues:**
```
❌ Label 30px above input with other content in between
✅ Label 6px directly above input

❌ Label same distance from input above and below
✅ Label closer to its own input than neighboring elements

❌ Gray label on white background (2:1 contrast)
✅ Dark gray label on white background (7:1 contrast)
```

### Help Text

**Placement Options:**
1. **Below the input**: Most common, works for short hints
2. **Tooltip/info icon**: Good for optional detailed information
3. **Above the input, below label**: For critical pre-fill guidance
4. **Expandable section**: For lengthy explanations

**Visual Styling:**
- Smaller font size than label (85-90% of body text)
- Reduced visual weight (lighter color, thinner font)
- Clearly associated with relevant field
- Icon indicators should be 16-24px and clearly clickable

**Spacing:**
- 4-6px from input when below
- 2-4px from label when between label and input
- Adequate padding around help sections

**Example Issues:**
```
❌ Help text in tiny 10px font, unreadable
✅ Help text in 14px font (90% of 16px body)

❌ Help text 40px below input, near next field
✅ Help text 6px below input, clearly associated

❌ Info icon 12px, looks like a bullet point
✅ Info icon 20px with hover state, clearly interactive
```

### Error Messages

**Placement Requirements:**
- **Inline**: Next to or below the problem field (essential)
- **Summary**: Optional list at top for multiple errors
- **Both**: Ideal for complex forms

**Visual Prominence:**
- High contrast with background
- Color coding (typically red, but not only indicator)
- Icon to enhance scannability
- Larger or bolder than help text

**Timing:**
- Should appear near the field that failed
- Should persist until corrected
- Should not obscure the input

**Example Issues:**
```
❌ All errors at top of form, user must scroll to find problems
✅ Inline errors below each problem field + summary at top

❌ Error text in standard gray (3:1 contrast)
✅ Error text in dark red (5:1 contrast) with red icon

❌ Red text only (fails for colorblind users)
✅ Red text + error icon + "Error:" prefix
```

### Buttons and CTAs

**Visual Hierarchy:**
- Primary action most prominent (filled, high contrast)
- Secondary actions less prominent (outline, lower contrast)
- Tertiary actions minimal (text only, lowest contrast)
- Spacing between buttons indicates grouping

**Placement:**
- Consistent position across similar pages
- Appropriate for screen size (bottom on mobile)
- Associated with relevant form section
- Not too far from last input

**Size and Spacing:**
- Large enough for easy targeting (minimum 44x44px touch target)
- Adequate spacing between adjacent buttons (8-12px minimum)
- Text has internal padding for easy readability

**Example Issues:**
```
❌ "Cancel" button more prominent than "Submit"
✅ "Submit" in high-contrast blue, "Cancel" in gray outline

❌ Buttons crammed together with no spacing
✅ Buttons with 12px gap, clearly separate targets

❌ Tiny 28px button on mobile interface
✅ Full-width 48px button on mobile
```

### Tooltips and Popovers

**Trigger Design:**
- Info icons should be 16-24px
- Position near the content they explain
- Clear hover/focus states
- Color contrast for icon (not just outline)

**Popover Design:**
- Appears near trigger element
- Arrow/pointer to show connection
- Readable width (200-400px)
- High contrast background
- Easy to dismiss

**Example Issues:**
```
❌ Gray circle with "i" that's barely visible
✅ Blue info icon with clear contrast

❌ Tooltip appears far from trigger point
✅ Tooltip directly above/below with connecting arrow

❌ Tooltip with white text on light gray (1.5:1 contrast)
✅ Tooltip with white text on dark gray (10:1 contrast)
```

## Layout Patterns

### Form Layout Best Practices

**Single Column Forms:**
- Easier to scan and complete
- Better for mobile responsiveness
- Clearer visual path
- Use for most forms

**Multi-Column Forms:**
- Only for short, related fields (first name / last name)
- Can confuse scanning order
- May break on mobile
- Use sparingly

**Progressive Disclosure:**
- Show only relevant fields based on previous answers
- Reduces overwhelming appearance
- Keeps focus on current step
- Must be clearly indicated

### Spacing and Density

**Comfortable Spacing:**
- 16-24px between form fields
- 8-12px between label and input
- 4-8px between input and help text
- 32-48px between form sections

**Too Dense:**
- Fields touching or too close
- Labels and help text cramped
- No visual breathing room
- Overwhelming appearance

**Too Sparse:**
- Excessive white space disconnects related items
- Difficult to scan as a group
- Wastes screen real estate
- Makes short forms seem long

## Common Visual Issues

### High Priority Visual Issues

**1. Hidden or Buried Help Text**
- Critical guidance in tiny text below the fold
- Help text same color as placeholder (disappears when typing)
- Important information in low-contrast text
- Required field indicators missing or unclear

**2. Poor Error Visibility**
- Errors only at top of long form (must scroll to see)
- Error text too small or low contrast
- No visual indicator which field has error
- Error appears then disappears too quickly

**3. Disconnected Labels**
- Label far from input with other content in between
- Inconsistent label placement across forms
- Labels aligned wrong direction
- No visual connection between label and input

**4. Inaccessible Interactive Elements**
- Tooltips that can't be triggered on mobile
- Clickable areas too small
- No visual feedback on interaction
- Help icons that look decorative not interactive

### Medium Priority Visual Issues

**1. Weak Visual Hierarchy**
- All text same size and weight
- No distinction between primary and secondary actions
- Help text as prominent as labels
- No clear visual path through form

**2. Inconsistent Styling**
- Different help text styles across pages
- Inconsistent error message appearance
- Mixed button styles for similar actions
- No pattern to interactive elements

**3. Poor Use of Space**
- Cramped forms with no breathing room
- Excessive space disconnecting related items
- Help text pushed off screen
- Buttons in awkward positions

### Low Priority Visual Issues

**1. Minor Spacing Issues**
- Slightly inconsistent padding
- Minor alignment problems
- Uneven gaps between elements

**2. Polish Opportunities**
- Could use icons to enhance scannability
- Opportunity for progressive disclosure
- Could group related fields better
- Minor contrast improvements possible

## Visual Review Checklist

When analyzing screenshots, evaluate:

- [ ] Can users easily identify form fields and their labels?
- [ ] Is help text visible without scrolling?
- [ ] Are error messages immediately apparent?
- [ ] Do interactive elements look clickable?
- [ ] Is there sufficient contrast for readability?
- [ ] Are related elements visually grouped?
- [ ] Is there adequate white space?
- [ ] Does visual hierarchy match information priority?
- [ ] Are buttons appropriately sized and spaced?
- [ ] Do tooltips/info icons stand out enough?
- [ ] Is the layout consistent across similar pages?
- [ ] Would this work on smaller screens?

## Documenting Visual Issues

For each visual issue, capture:

**Screenshot Reference:**
```
File: signup_form.png
Region: Password field area (center-left)
```

**Visual Problem Description:**
```
Password requirements text appears in 10px gray text 
at the bottom of the form, 300px below the password 
field. Easy to miss when filling form.
```

**User Impact:**
```
Users don't see requirements until after submission 
fails, leading to frustration and repeated attempts.
```

**Recommendation:**
```
Move requirements directly below password input with:
- 14px font size (up from 10px)
- Medium gray color (#666 instead of #ccc)
- 8px spacing from input
- Consider icon for visual emphasis
```

**Mock-up or Example (optional):**
```
[ Password input field ]
  Requirements: 8+ characters, 1 number, 1 special character
```

## Color and Contrast

### WCAG Standards

**Normal Text (< 18pt):**
- Level AA: Minimum 4.5:1 contrast ratio
- Level AAA: Minimum 7:1 contrast ratio

**Large Text (≥ 18pt or 14pt bold):**
- Level AA: Minimum 3:1 contrast ratio
- Level AAA: Minimum 4.5:1 contrast ratio

**Interactive Elements:**
- Minimum 3:1 contrast for UI components and states

### Common Contrast Issues

```
❌ Light gray text on white (#ccc on #fff = 1.6:1)
✅ Medium gray text on white (#666 on #fff = 5.7:1)

❌ Pale yellow help text on white
✅ Dark blue help text on white

❌ Color as only error indicator
✅ Color + icon + text prefix for errors
```

## Responsive Considerations

When evaluating layouts, consider:

**Mobile Adaptations:**
- Labels should stack above inputs (not left-aligned)
- Buttons should be full-width or large enough
- Help text must remain visible
- Touch targets minimum 44x44px
- Adequate spacing for fat finger syndrome

**Tablet Considerations:**
- Balanced between desktop and mobile
- May use multi-column for wide forms
- Maintain comfortable touch targets

**Desktop Advantages:**
- Can use tooltips effectively (hover states)
- More room for inline help text
- Multi-column layouts possible for short fields
- Larger screens allow more context visible

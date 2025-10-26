# Responsive Design Guidelines

Guide for evaluating cross-device experiences.

## Breakpoint Strategy

**Common Breakpoints:**
- Mobile: 320-767px
- Tablet: 768-1023px
- Desktop: 1024-1439px
- Large Desktop: 1440px+

**Mobile-First Approach:**
Design for mobile first, then enhance for larger screens.

## Key Principles

### 1. Fluid Layouts
Use percentages, not fixed widths
- Container: max-width with percentages
- Images: max-width 100%
- Text: responsive units (rem, em)

### 2. Flexible Images
- Scale images proportionally
- Use srcset for resolution
- Art direction with picture element
- Lazy load below fold images

### 3. Touch Optimization
- Minimum 44x44px touch targets
- 8px spacing between tappable elements
- Larger buttons on mobile
- Accessible swipe gestures

### 4. Content Prioritization
Show most important content first on mobile:
- Hide secondary content (hamburger menu)
- Collapse complex widgets
- Stack columns vertically
- Remove decorative elements

### 5. Performance
- Smaller images on mobile
- Fewer HTTP requests
- Minimize JavaScript
- Reduce animations

## Mobile-Specific Patterns

**Navigation:**
- Hamburger menu
- Bottom tab bar
- Sticky headers
- Collapsible sections

**Forms:**
- Full-width inputs
- Appropriate keyboard types
- Minimize typing (select > text input)
- Auto-advance for codes

**Tables:**
- Horizontal scroll
- Card-based layout
- Column hiding
- Expandable rows

## Evaluation Checklist

- [ ] Layout adapts smoothly
- [ ] No horizontal scroll
- [ ] Text readable without zoom
- [ ] Touch targets adequate size
- [ ] Content prioritized appropriately
- [ ] Performance acceptable on mobile
- [ ] Works in portrait & landscape


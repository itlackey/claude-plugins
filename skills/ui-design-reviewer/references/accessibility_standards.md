# Accessibility Standards (WCAG 2.1)

Comprehensive guide for evaluating WCAG compliance.

## WCAG 2.1 Levels
- **Level A**: Minimum (must fix)
- **Level AA**: Industry standard (target)
- **Level AAA**: Enhanced (ideal)

## Key Principles (POUR)

### 1. Perceivable
Users must be able to perceive the information.

**Requirements:**
- Text alternatives for images (alt text)
- Captions for videos
- Color contrast minimum 4.5:1 (AA), 7:1 (AAA)
- Don't use color alone to convey meaning
- Resize text to 200% without breaking

### 2. Operable
Users must be able to operate the interface.

**Requirements:**
- Keyboard accessible (all functions)
- No keyboard traps
- Visible focus indicators
- Skip navigation links
- Adequate time for tasks
- No seizure-inducing flashes
- Touch targets 44x44px minimum

### 3. Understandable
Users must understand the content and interface.

**Requirements:**
- Language attribute set
- Consistent navigation
- Clear error identification
- Labels for form inputs
- Help text available
- Predictable behavior

### 4. Robust
Content must work with assistive technologies.

**Requirements:**
- Valid HTML
- Proper ARIA usage
- Semantic elements
- Compatible with screen readers

## Quick Compliance Checklist

**Critical (Level A):**
- [ ] All images have alt text
- [ ] Keyboard navigation works
- [ ] No keyboard traps
- [ ] Form inputs have labels
- [ ] Color isn't only indicator

**Standard (Level AA):**
- [ ] Contrast ratio ≥ 4.5:1
- [ ] Touch targets ≥ 44x44px
- [ ] Focus indicators visible
- [ ] Error messages clear
- [ ] Page titles descriptive

**Enhanced (Level AAA):**
- [ ] Contrast ratio ≥ 7:1
- [ ] Sign language for videos
- [ ] No time limits
- [ ] Content at 8th grade level

## Testing Methods
1. Keyboard-only navigation test
2. Screen reader test (NVDA/JAWS)
3. Color contrast checker
4. Zoom to 200% test
5. Automated scan (axe, WAVE)


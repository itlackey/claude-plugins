# Interaction Design Patterns

This reference provides the Interaction Design Agent with guidelines for evaluating user flows, micro-interactions, feedback mechanisms, and state management.

## Core Interaction Principles

### 1. Affordance
Elements should visually suggest how to interact with them.

**Evaluation:**
- Do buttons look clickable?
- Do form fields look fillable?
- Are interactive elements distinguishable from static content?
- Do disabled elements look disabled?

**Best Practices:**
- Buttons have button appearance (raised, colored, or outlined)
- Links are underlined or clearly styled differently
- Cursors change on hover (pointer for clickable)
- Disabled elements are grayed out or low opacity

### 2. Feedback
Users should receive immediate confirmation of their actions.

**Types of Feedback:**
- Visual (color change, animation, icon)
- Textual (messages, toasts, alerts)
- Haptic (mobile vibration)
- Audio (sounds, though rare in web)

**Timing:**
- Immediate (<100ms): Microinteractions, hover states
- Quick (<1s): Form validation, button clicks
- Delayed (1-3s): Server responses, loading states
- Long (>3s): Require progress indicators

**Best Practices:**
- Hover states on all interactive elements
- Click/tap feedback (active state)
- Loading indicators for async operations
- Success confirmations after actions
- Clear error messages with recovery path

### 3. State Management

**Interactive States:**
- **Default/Rest**: Normal state
- **Hover**: Mouse over element
- **Focus**: Keyboard or programmatic focus
- **Active**: Being clicked/tapped
- **Disabled**: Not currently interactive
- **Loading**: Processing
- **Error**: Something went wrong
- **Success**: Action completed successfully

**Common Issues:**
- Missing hover states
- Invisible focus indicators
- Unclear disabled state
- No loading state
- Harsh error states without recovery

### 4. User Flow Optimization

**Flow Principles:**
- Minimize steps to completion
- Provide clear progress indicators
- Allow easy navigation forward and back
- Save progress when possible
- Confirm destructive actions
- Celebrate completion

**Common Flow Problems:**
- Too many steps (user fatigue)
- No clear next action
- Can't go back without losing progress
- No indication of where in flow
- Dead ends without exit path

### 5. Micro-interactions

Small, purposeful animations that provide feedback or delight.

**Examples:**
- Button press animations
- Checkbox/toggle animations
- Loading spinners
- Pull-to-refresh
- Swipe gestures
- Drag and drop feedback
- Form validation animations
- Success confetti

**Best Practices:**
- Keep short (200-500ms)
- Use easing for natural movement
- Don't block user actions
- Provide skip/reduce motion option
- Use purposefully, not decoratively

### 6. Navigation Patterns

**Common Patterns:**
- Top horizontal nav
- Side vertical nav
- Hamburger menu (mobile)
- Tabs
- Breadcrumbs
- Pagination
- Infinite scroll
- Sticky headers

**Evaluation:**
- Is current location clear?
- Can users get back easily?
- Is navigation accessible from anywhere?
- Does nav work on mobile?
- Are deep links supported?

### 7. Form Interaction Patterns

**Best Practices:**
- Inline validation (after field blur)
- Clear error messages
- Smart defaults
- Autofocus first field
- Tab order logical
- Autocomplete where helpful
- Mask inputs for format (phone, credit card)
- Show/hide password toggle
- Clear fields option

**Common Issues:**
- Validation only on submit (frustrating)
- Generic error messages
- No indication of required fields
- Illogical tab order
- Can't paste into fields (annoying)

### 8. Modal and Overlay Behavior

**Best Practices:**
- Dim background (focus attention)
- Close on background click (usually)
- Close on ESC key
- Trap focus within modal
- Prevent body scroll
- Smooth enter/exit animations
- Clear close button

**Common Issues:**
- Can't close easily
- Background scrolls
- Focus not trapped
- No keyboard support
- Abrupt appearance/disappearance

### 9. Loading States

**Patterns:**
- Skeleton screens (show structure)
- Spinners (simple indication)
- Progress bars (known duration)
- Optimistic UI (show result immediately)
- Streaming (show partial results)

**Best Practices:**
- Show loading for >300ms waits
- Use skeleton for structured content
- Progress bars for known duration
- Spinners for unknown duration
- Keep UI responsive during load

### 10. Error Handling

**Good Error States:**
- Clear what went wrong
- Explain why it happened
- Provide recovery action
- Don't blame user
- Maintain context
- Allow retry

**Error Pattern:**
```
[X] Unable to save changes

Your session has expired. Please log in again to save your work.

[Return to Login] [Save Draft Locally]
```

## Interaction Evaluation Framework

### Flow Efficiency Score (1-5)

1: Many unnecessary steps, confusing paths
3: Functional but could be streamlined  
5: Optimal, effortless task completion

### Feedback Quality Score (1-5)

1: No feedback, unclear states
3: Basic feedback present
5: Excellent, immediate, clear feedback

### State Management Score (1-5)

1: Missing or confusing states
3: States present but could be clearer
5: Perfect state communication

## Common Interaction Antipatterns

**Bad Patterns to Flag:**
- No hover states (unclear what's interactive)
- Invisible focus indicators (keyboard users lost)
- Generic "Error" messages (not helpful)
- Disabled buttons without explanation (frustrating)
- Long forms without progress indication
- Destructive actions without confirmation
- Navigation that loses user progress
- Modals that can't be dismissed
- Clickjacking (things too close together)
- Mystery meat navigation (unclear targets)

## Mobile-Specific Interactions

**Touch Considerations:**
- Minimum 44x44px touch targets
- Adequate spacing between tappable elements (8px minimum)
- Swipe gestures for natural actions
- Long-press for secondary actions
- Pull-to-refresh for content updates
- Bottom navigation (thumb-friendly)
- Avoid hover-dependent interactions

## Reporting Interaction Issues

**Issue Format:**

```
Issue: [Title]
Flow/Component: [Where it occurs]
Current Behavior: [What happens now]
Problem: [Why it's an issue]
User Impact: [How it affects users]
Recommendation: [Specific improvement]
Example: [Flow or state diagram if helpful]
```

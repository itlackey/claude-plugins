# UX Writing Best Practices

This reference provides guidelines for evaluating and improving user interface text, labels, and guidance.

## Core Principles

### Clarity
- Use simple, direct language
- Avoid jargon and technical terms when possible
- Define technical terms when necessary
- Use active voice over passive voice

### Conciseness
- Remove unnecessary words
- Get to the point quickly
- Use progressive disclosure for complex information

### Consistency
- Maintain consistent terminology throughout
- Use consistent capitalization and punctuation
- Establish and follow naming conventions

### Conversation
- Write as you would speak to someone
- Use contractions when appropriate
- Be friendly but professional

## Component-Specific Guidelines

### Labels
**Good practices:**
- Use sentence case (e.g., "Email address" not "Email Address")
- Be specific and descriptive
- Keep labels short (1-3 words ideal)
- Position labels above or to the left of inputs
- Don't use colons after labels in modern interfaces

**Examples:**
- ✅ "Email address"
- ❌ "Email Address:"
- ✅ "Billing zip code"
- ❌ "Zip"

### Placeholder Text
**Good practices:**
- Provide examples of expected format
- Don't repeat the label
- Don't use for critical information (placeholders disappear)
- Keep it brief

**Examples:**
- ✅ placeholder="yourname@example.com"
- ❌ placeholder="Enter your email address here"
- ✅ placeholder="MM/DD/YYYY"
- ❌ placeholder="Date"

### Button Text
**Good practices:**
- Start with a verb
- Be specific about the action
- Keep it 1-3 words
- Use sentence case
- Match user's mental model

**Examples:**
- ✅ "Save changes"
- ❌ "Submit"
- ✅ "Download report"
- ❌ "Click here"
- ✅ "Create account"
- ❌ "OK"

### Help Text
**Good practices:**
- Place near the relevant field
- Explain why information is needed
- Provide formatting requirements
- Keep it short (1-2 sentences)
- Use plain language

**Examples:**
- ✅ "We'll use this to send order confirmations"
- ❌ "This field is required for authentication purposes"
- ✅ "Choose a password with at least 8 characters"
- ❌ "Must be alphanumeric with minimum length of 8"

### Error Messages
**Good practices:**
- Explain what went wrong
- Tell users how to fix it
- Be specific, not generic
- Don't blame the user
- Use friendly, helpful tone

**Examples:**
- ✅ "Please enter a valid email address, like name@example.com"
- ❌ "Invalid input"
- ✅ "Your password must be at least 8 characters"
- ❌ "Error: Password too short"
- ✅ "This username is already taken. Try adding numbers or your last name"
- ❌ "Username exists"

### Tooltips
**Good practices:**
- Use for supplementary information only
- Keep very brief (5-10 words)
- Don't hide critical information in tooltips
- Ensure mobile users can access

**Examples:**
- ✅ "Your unique account identifier"
- ❌ "This is the username that you chose when you created your account and will be used to log in"

### Link Text
**Good practices:**
- Describe the destination or action
- Avoid "click here" or "read more"
- Make links scannable
- Keep contextually relevant

**Examples:**
- ✅ "View our privacy policy"
- ❌ "Click here for our privacy policy"
- ✅ "Learn about data security"
- ❌ "Read more"

### Headings
**Good practices:**
- Use sentence case
- Be descriptive and scannable
- Maintain hierarchy (H1 > H2 > H3)
- Keep concise (5-8 words max)

**Examples:**
- ✅ "Account settings"
- ❌ "Settings Related To Your Account"
- ✅ "Payment information"
- ❌ "Payment Info Section"

## Accessibility Considerations

### Screen Readers
- Provide aria-labels for icon buttons
- Use semantic HTML (label, button, nav, etc.)
- Ensure all interactive elements have accessible names
- Don't rely solely on color to convey meaning

### Keyboard Navigation
- Ensure logical tab order
- Provide visible focus indicators
- Don't use "click" in instructions (say "select" or "choose")

### Language Level
- Aim for 8th grade reading level or below
- Explain technical concepts simply
- Use short sentences
- Break complex information into chunks

## Common Issues to Flag

### High Priority
1. **Missing labels**: All form inputs must have labels or ARIA labels
2. **Unclear error messages**: Users should know what's wrong and how to fix it
3. **Inaccessible interactive elements**: Buttons, links without proper text
4. **Inconsistent terminology**: Same thing called different names

### Medium Priority
1. **Vague button text**: "Submit", "OK", "Click here"
2. **Vague link text**: "Click here", "Read more", "Here"
3. **Technical jargon without explanation**
4. **All caps text**: Harder to read, sounds like shouting
5. **Long help text**: Should be concise
6. **Missing placeholder examples**: Especially for formatted inputs

### Low Priority
1. **Inconsistent capitalization**
2. **Unnecessary punctuation** (colons after labels)
3. **Overly formal tone**
4. **Missing progressive disclosure** (showing all complexity at once)

## Review Checklist

When reviewing UX guidance, ask:

- [ ] Can a first-time user understand this?
- [ ] Is all text necessary, or can it be shortened?
- [ ] Are terms used consistently throughout?
- [ ] Would this pass accessibility guidelines (WCAG)?
- [ ] Is the tone appropriate for the brand and audience?
- [ ] Are errors helpful and actionable?
- [ ] Do buttons and links clearly indicate their action?
- [ ] Is help text placed where users need it?
- [ ] Are field requirements clear before submission?
- [ ] Can this be understood by non-native speakers?

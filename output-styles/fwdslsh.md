---
description: Minimal, readable, and effective responses following fwdslsh philosophy
---

Format responses following the fwdslsh ecosystem philosophy: minimal dependencies, single-purpose clarity, and CLI-first design.

## Response Structure

### Headers
- Use `##` for main sections, `###` for subsections
- Keep headers descriptive and action-oriented

### Code Blocks
- Always specify language for syntax highlighting
- Include clear comments for complex logic
- Show complete, runnable examples

```bash
# Example command structure
command --flag argument  # Brief explanation
```

### Lists
- Use bullet points for unordered information
- Use numbered lists only for sequential steps
- Keep items concise and actionable

### Emphasis
- **Bold** for important commands or concepts
- `code` for inline commands, filenames, and technical terms
- Minimal emoji usage: ✅ success, ❌ error, ⚠️ warning, 🚀 new feature

## Tool-Specific Patterns

When working with fwdslsh tools:
- Reference tools by their binary names: `unify`, `giv`, `inform`, `catalog`
- Show CLI examples with common flags
- Maintain consistency with existing tool patterns

## Code Examples

### Good Example
```bash
# Build static site with unify
unify build --input ./content --output ./dist

# Generate commit message with giv
giv commit --model claude
```

### File Paths
- Always use absolute paths in examples
- Show directory structure when relevant
- Reference project root consistently

## Key Principles

1. **Minimal**: No unnecessary explanations or decorations
2. **Readable**: Clear structure with proper spacing
3. **Effective**: Actionable information that solves the problem
4. **CLI-first**: Command examples before GUI alternatives
5. **Composable**: Show how tools work together

## Avoid

- Excessive emoji or decorative elements
- Long-winded explanations
- Creating files unless explicitly needed
- Proactive documentation generation
- Complex nested structures

Keep responses focused on solving the specific task at hand.
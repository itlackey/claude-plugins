---
description: Format responses in semantic HTML without styling for easy chat integration
---

Format all responses using proper semantic HTML tags without any CSS styling or classes. This allows the content to be easily integrated into chat interfaces that provide their own styling.

## HTML Formatting Guidelines

Use semantic HTML elements appropriately:

- **Headings**: Use `<h1>` through `<h6>` for section headers and hierarchy
- **Paragraphs**: Wrap text blocks in `<p>` tags
- **Lists**: Use `<ul>` for unordered lists, `<ol>` for ordered lists, with `<li>` for items
- **Code**: Use `<code>` for inline code snippets and `<pre><code>` for code blocks
- **Emphasis**: Use `<strong>` for important text, `<em>` for emphasis
- **Quotes**: Use `<blockquote>` for quoted content
- **Links**: Use `<a href="">` for any URLs or references
- **Tables**: Use proper `<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>`, `<td>` structure when presenting tabular data

## Key Requirements

- **No CSS**: Never include style attributes, classes, or CSS
- **Clean markup**: Use minimal, semantic HTML only
- **Self-contained**: Each response should be valid HTML that can be directly inserted into a chat interface
- **Proper nesting**: Ensure all tags are properly opened and closed
- **Accessibility**: Use semantic elements that work well with screen readers

## Examples

Instead of plain text like "Here are the steps:", use:
```html
<h3>Here are the steps:</h3>
<ol>
<li>First step</li>
<li>Second step</li>
</ol>
```

For code examples:
```html
<p>Use this function:</p>
<pre><code>function example() {
  return "hello";
}</code></pre>
```

For emphasis:
```html
<p>This is <strong>very important</strong> to remember.</p>
```

The goal is to provide clean, semantic HTML that chat interfaces can style consistently with their own CSS framework.
#!/usr/bin/env python3
"""
Markdown validation script that checks syntax and formatting without altering text content.
Logs uncertain changes to a review file for manual inspection.
"""

import sys
import json
import re
from pathlib import Path
from typing import List, Dict, Any, Tuple


class MarkdownValidator:
    """Validates markdown files for syntax and formatting issues."""
    
    def __init__(self, spec_file: Path = None, examples_dir: Path = None):
        """
        Initialize validator with optional specification and examples.
        
        Args:
            spec_file: Path to markdown specification document
            examples_dir: Path to directory containing example markdown files
        """
        self.spec_file = spec_file
        self.examples_dir = examples_dir
        self.issues = []
        self.uncertain_changes = []
        
    def validate_file(self, filepath: Path) -> Dict[str, Any]:
        """
        Validate a markdown file.
        
        Args:
            filepath: Path to markdown file
            
        Returns:
            Dictionary containing validation results
        """
        self.issues = []
        self.uncertain_changes = []
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            return {
                'filepath': str(filepath),
                'valid': False,
                'error': f'Failed to read file: {str(e)}',
                'issues': [],
                'uncertain_changes': []
            }
        
        # Run validation checks
        self._check_heading_structure(content)
        self._check_list_formatting(content)
        self._check_link_syntax(content)
        self._check_code_block_syntax(content)
        self._check_emphasis_markers(content)
        self._check_horizontal_rules(content)
        self._check_trailing_whitespace(content)
        
        return {
            'filepath': str(filepath),
            'valid': len(self.issues) == 0,
            'issues': self.issues,
            'uncertain_changes': self.uncertain_changes
        }
    
    def _add_issue(self, line_num: int, issue_type: str, description: str, 
                   severity: str = 'error'):
        """Add an issue to the list."""
        self.issues.append({
            'line': line_num,
            'type': issue_type,
            'description': description,
            'severity': severity
        })
    
    def _add_uncertain_change(self, line_num: int, change_type: str, 
                             current: str, suggested: str, reason: str):
        """Log an uncertain change for manual review."""
        self.uncertain_changes.append({
            'line': line_num,
            'type': change_type,
            'current': current,
            'suggested': suggested,
            'reason': reason
        })
    
    def _check_heading_structure(self, content: str):
        """Check for proper heading hierarchy and formatting."""
        lines = content.split('\n')
        prev_level = 0
        
        for i, line in enumerate(lines, 1):
            # Check ATX-style headings
            heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)
            if heading_match:
                hashes, heading_text = heading_match.groups()
                level = len(hashes)
                
                # Check for space after hashes
                if not re.match(r'^#{1,6}\s', line):
                    self._add_issue(i, 'heading_format', 
                                  'Heading must have space after #')
                
                # Check for proper hierarchy (not skipping levels)
                if prev_level > 0 and level > prev_level + 1:
                    self._add_issue(i, 'heading_hierarchy', 
                                  f'Heading level skipped from {prev_level} to {level}',
                                  severity='warning')
                
                # Check for trailing hashes (inconsistent style)
                if re.search(r'#+\s*$', line):
                    self._add_uncertain_change(
                        i, 'heading_trailing_hashes',
                        line,
                        f"{hashes} {heading_text.rstrip('#').strip()}",
                        'Trailing hashes in heading - style preference'
                    )
                
                prev_level = level
            
            # Check for setext-style headings (= and -)
            elif i < len(lines) and re.match(r'^[=-]+\s*$', lines[i]):
                self._add_uncertain_change(
                    i, 'setext_heading',
                    f"{line}\n{lines[i]}",
                    f"# {line}" if '=' in lines[i] else f"## {line}",
                    'Setext-style heading - ATX style is more common'
                )
    
    def _check_list_formatting(self, content: str):
        """Check for consistent list formatting."""
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Unordered list items
            if re.match(r'^\s*[*+-]\s+', line):
                # Check for consistent spacing
                if not re.match(r'^\s*[*+-]\s\s+', line) and not re.match(r'^\s*[*+-]\s\S', line):
                    self._add_issue(i, 'list_spacing',
                                  'List item should have single space after marker')
                
                # Track which marker is used
                marker = re.search(r'[*+-]', line).group()
                # Could check for consistency across file, but this is style preference
            
            # Ordered list items
            if re.match(r'^\s*\d+\.\s+', line):
                if not re.match(r'^\s*\d+\.\s\S', line):
                    self._add_issue(i, 'list_spacing',
                                  'Ordered list item should have single space after number')
    
    def _check_link_syntax(self, content: str):
        """Check for proper link formatting."""
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Check for malformed inline links [text](url)
            # Match potential links with missing parts
            if '[' in line and ']' in line:
                # Check for links missing URL: [text]
                broken_links = re.finditer(r'\[([^\]]+)\](?!\(|:|\[)', line)
                for match in broken_links:
                    self._add_issue(i, 'broken_link',
                                  f'Link text "{match.group(1)}" missing URL or reference')
            
            # Check for URLs that should be in link format
            bare_urls = re.finditer(r'(?<![(\[])https?://[^\s)>]+', line)
            for match in bare_urls:
                self._add_uncertain_change(
                    i, 'bare_url',
                    match.group(),
                    f'<{match.group()}>',
                    'Bare URL - consider wrapping in < > or proper link syntax'
                )
    
    def _check_code_block_syntax(self, content: str):
        """Check for proper code block formatting."""
        lines = content.split('\n')
        in_fenced_block = False
        fence_char = None
        fence_line = 0
        
        for i, line in enumerate(lines, 1):
            # Check for fenced code blocks
            fence_match = re.match(r'^(`{3,}|~{3,})', line)
            if fence_match:
                if not in_fenced_block:
                    in_fenced_block = True
                    fence_char = fence_match.group(1)[0]
                    fence_line = i
                else:
                    # Closing fence
                    if fence_match.group(1)[0] != fence_char:
                        self._add_issue(i, 'fence_mismatch',
                                      f'Fence character mismatch (opened with {fence_char} on line {fence_line})')
                    in_fenced_block = False
                    fence_char = None
            
            # Check for indented code blocks (4 spaces)
            elif re.match(r'^    \S', line) and not in_fenced_block:
                self._add_uncertain_change(
                    i, 'indented_code_block',
                    line,
                    f"```\n{line.strip()}\n```",
                    'Indented code block - fenced code blocks are clearer'
                )
        
        # Check if we ended with unclosed fence
        if in_fenced_block:
            self._add_issue(fence_line, 'unclosed_fence',
                          f'Unclosed code fence started on line {fence_line}')
    
    def _check_emphasis_markers(self, content: str):
        """Check for consistent emphasis and strong emphasis markers."""
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Check for mismatched emphasis markers
            # Looking for *text_ or _text* patterns
            mismatched = re.finditer(r'(?<!\*)\*(?!\*)([^*_]+)_(?!_)|(?<!_)_(?!_)([^*_]+)\*(?!\*)', line)
            for match in mismatched:
                self._add_issue(i, 'mismatched_emphasis',
                              f'Mismatched emphasis markers: {match.group()}')
    
    def _check_horizontal_rules(self, content: str):
        """Check for proper horizontal rule syntax."""
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Check for potential horizontal rules
            if re.match(r'^\s*([*\-_])\s*\1\s*\1', line):
                # Valid horizontal rule
                pass
            elif re.match(r'^\s*[*\-_]{2}\s*$', line):
                self._add_issue(i, 'invalid_hr',
                              'Horizontal rule requires at least 3 characters')
    
    def _check_trailing_whitespace(self, content: str):
        """Check for trailing whitespace (may be intentional for line breaks)."""
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            if line.endswith(' ') or line.endswith('\t'):
                # Two trailing spaces create a line break in markdown
                if line.endswith('  ') and not line.endswith('   '):
                    # This is likely intentional
                    continue
                else:
                    self._add_uncertain_change(
                        i, 'trailing_whitespace',
                        line,
                        line.rstrip(),
                        'Trailing whitespace (may be intentional for line break)'
                    )


def main():
    """Main entry point for the validator."""
    if len(sys.argv) < 2:
        print("Usage: python validate_markdown.py <file.md> [--spec spec.md] [--examples examples/]")
        print("       python validate_markdown.py <directory/> [--spec spec.md] [--examples examples/]")
        sys.exit(1)
    
    target = Path(sys.argv[1])
    spec_file = None
    examples_dir = None
    
    # Parse optional arguments
    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == '--spec' and i + 1 < len(sys.argv):
            spec_file = Path(sys.argv[i + 1])
            i += 2
        elif sys.argv[i] == '--examples' and i + 1 < len(sys.argv):
            examples_dir = Path(sys.argv[i + 1])
            i += 2
        else:
            i += 1
    
    validator = MarkdownValidator(spec_file, examples_dir)
    
    # Collect files to validate
    if target.is_file():
        files = [target]
    elif target.is_dir():
        files = list(target.rglob('*.md'))
    else:
        print(f"Error: {target} is not a valid file or directory")
        sys.exit(1)
    
    # Validate all files
    results = []
    for filepath in files:
        result = validator.validate_file(filepath)
        results.append(result)
        
        print(f"\n{'='*60}")
        print(f"File: {result['filepath']}")
        print(f"Valid: {result['valid']}")
        
        if result.get('error'):
            print(f"Error: {result['error']}")
        
        if result['issues']:
            print(f"\nIssues found: {len(result['issues'])}")
            for issue in result['issues']:
                print(f"  Line {issue['line']} [{issue['severity'].upper()}] {issue['type']}: {issue['description']}")
        
        if result['uncertain_changes']:
            print(f"\nUncertain changes: {len(result['uncertain_changes'])}")
            for change in result['uncertain_changes']:
                print(f"  Line {change['line']} [{change['type']}]: {change['reason']}")
    
    # Write detailed report
    report_file = Path('markdown_validation_report.json')
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n{'='*60}")
    print(f"Detailed report written to: {report_file}")
    
    # Return exit code based on validation results
    if any(not result['valid'] for result in results):
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()

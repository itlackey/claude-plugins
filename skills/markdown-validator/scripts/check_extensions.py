#!/usr/bin/env python3
"""
Custom extension checker for markdown-it plugins.
Validates that custom markdown syntax is used correctly according to specification.
"""

import sys
import json
import re
from pathlib import Path
from typing import List, Dict, Any, Optional


class ExtensionChecker:
    """Checks custom markdown-it extension usage against specification."""
    
    def __init__(self, spec_file: Path = None, examples_dir: Path = None):
        """
        Initialize extension checker.
        
        Args:
            spec_file: Path to markdown specification document
            examples_dir: Path to directory containing example markdown files
        """
        self.spec_file = spec_file
        self.examples_dir = examples_dir
        self.spec_rules = []
        self.example_patterns = []
        self.issues = []
        self.uncertain_changes = []
        
        if spec_file and spec_file.exists():
            self._load_spec()
        
        if examples_dir and examples_dir.exists():
            self._load_examples()
    
    def _load_spec(self):
        """Load and parse the specification document."""
        try:
            with open(self.spec_file, 'r', encoding='utf-8') as f:
                spec_content = f.read()
            
            # Extract extension rules from spec
            # Look for patterns like:
            # - Extension name: container
            # - Syntax: :::name ... :::
            
            # This is a simplified parser - can be extended based on actual spec format
            sections = re.split(r'\n#{1,3}\s+', spec_content)
            
            for section in sections:
                # Look for extension definitions
                ext_name_match = re.search(r'Extension[:\s]+`?([a-zA-Z0-9_-]+)`?', section, re.IGNORECASE)
                syntax_match = re.search(r'Syntax[:\s]+`([^`]+)`', section, re.IGNORECASE)
                
                if ext_name_match and syntax_match:
                    self.spec_rules.append({
                        'name': ext_name_match.group(1),
                        'syntax': syntax_match.group(1),
                        'description': section[:200]  # First 200 chars as description
                    })
            
        except Exception as e:
            print(f"Warning: Failed to load spec file: {e}", file=sys.stderr)
    
    def _load_examples(self):
        """Load example files to learn valid patterns."""
        try:
            example_files = list(self.examples_dir.glob('*.md'))
            
            for example_file in example_files:
                with open(example_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.example_patterns.append({
                        'file': example_file.name,
                        'content': content
                    })
        
        except Exception as e:
            print(f"Warning: Failed to load examples: {e}", file=sys.stderr)
    
    def check_file(self, filepath: Path) -> Dict[str, Any]:
        """
        Check a markdown file for custom extension usage.
        
        Args:
            filepath: Path to markdown file
            
        Returns:
            Dictionary containing check results
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
        
        # Check for common markdown-it extensions
        self._check_containers(content)
        self._check_admonitions(content)
        self._check_definition_lists(content)
        self._check_footnotes(content)
        self._check_task_lists(content)
        self._check_custom_attributes(content)
        self._check_against_spec(content)
        
        return {
            'filepath': str(filepath),
            'valid': len(self.issues) == 0,
            'issues': self.issues,
            'uncertain_changes': self.uncertain_changes
        }
    
    def _add_issue(self, line_num: int, extension: str, description: str,
                   severity: str = 'error'):
        """Add an issue to the list."""
        self.issues.append({
            'line': line_num,
            'extension': extension,
            'description': description,
            'severity': severity
        })
    
    def _add_uncertain_change(self, line_num: int, extension: str,
                             current: str, suggested: str, reason: str):
        """Log an uncertain change for manual review."""
        self.uncertain_changes.append({
            'line': line_num,
            'extension': extension,
            'current': current,
            'suggested': suggested,
            'reason': reason
        })
    
    def _check_containers(self, content: str):
        """Check container syntax (:::type ... :::)."""
        lines = content.split('\n')
        container_stack = []
        
        for i, line in enumerate(lines, 1):
            # Opening container
            opening = re.match(r'^::{3,}\s*(\w+)?', line)
            if opening:
                container_type = opening.group(1) if opening.group(1) else 'unknown'
                container_stack.append({
                    'line': i,
                    'type': container_type,
                    'marker': opening.group(0)
                })
            
            # Closing container
            elif re.match(r'^::{3,}\s*$', line):
                if not container_stack:
                    self._add_issue(i, 'container',
                                  'Closing container marker without opening')
                else:
                    container_stack.pop()
        
        # Check for unclosed containers
        for container in container_stack:
            self._add_issue(container['line'], 'container',
                          f'Unclosed container of type "{container["type"]}"')
    
    def _check_admonitions(self, content: str):
        """Check admonition syntax (specific type of container)."""
        lines = content.split('\n')
        valid_admonition_types = ['note', 'tip', 'warning', 'danger', 'info', 'caution']
        
        for i, line in enumerate(lines, 1):
            admonition = re.match(r'^::{3,}\s*(\w+)', line)
            if admonition:
                admon_type = admonition.group(1).lower()
                if admon_type in valid_admonition_types:
                    # Valid admonition
                    pass
                elif admon_type not in ['', 'container', 'details']:
                    # Might be a typo or unknown type
                    self._add_uncertain_change(
                        i, 'admonition',
                        line,
                        line,
                        f'Unknown admonition type "{admon_type}" - verify this is correct'
                    )
    
    def _check_definition_lists(self, content: str):
        """Check definition list syntax."""
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Definition list item (term followed by : definition)
            if i < len(lines):
                next_line = lines[i] if i < len(lines) else ''
                
                # Check for definition pattern
                if re.match(r'^:\s+', next_line):
                    # This is a definition, previous line should be the term
                    if not lines[i-1].strip():
                        self._add_issue(i, 'definition_list',
                                      'Definition without term')
    
    def _check_footnotes(self, content: str):
        """Check footnote syntax."""
        lines = content.split('\n')
        footnote_refs = set()
        footnote_defs = set()
        
        for i, line in enumerate(lines, 1):
            # Footnote references [^1]
            refs = re.finditer(r'\[\^([^\]]+)\](?!:)', line)
            for ref in refs:
                footnote_refs.add(ref.group(1))
            
            # Footnote definitions [^1]:
            defs = re.finditer(r'^\[\^([^\]]+)\]:\s*', line)
            for def_match in defs:
                footnote_id = def_match.group(1)
                if footnote_id in footnote_defs:
                    self._add_issue(i, 'footnote',
                                  f'Duplicate footnote definition: [{footnote_id}]')
                footnote_defs.add(footnote_id)
        
        # Check for references without definitions
        for ref in footnote_refs:
            if ref not in footnote_defs:
                self._add_issue(0, 'footnote',
                              f'Footnote reference [^{ref}] without definition',
                              severity='warning')
        
        # Check for definitions without references
        for def_id in footnote_defs:
            if def_id not in footnote_refs:
                self._add_uncertain_change(
                    0, 'footnote',
                    f'[^{def_id}]',
                    '',
                    f'Footnote definition [^{def_id}] never referenced'
                )
    
    def _check_task_lists(self, content: str):
        """Check GitHub-style task list syntax."""
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Task list items
            task = re.match(r'^(\s*[-*+])\s+\[([ xX])\]', line)
            if task:
                marker, check = task.groups()
                
                # Normalize checkbox
                if check == 'X':
                    self._add_uncertain_change(
                        i, 'task_list',
                        line,
                        line.replace('[X]', '[x]'),
                        'Task list checkbox should use lowercase "x"'
                    )
                
                # Check for space after checkbox
                if not re.match(r'^(\s*[-*+])\s+\[([ xX])\]\s+', line):
                    self._add_issue(i, 'task_list',
                                  'Task list checkbox should be followed by space')
    
    def _check_custom_attributes(self, content: str):
        """Check custom attribute syntax {.class #id key=value}."""
        lines = content.split('\n')
        
        for i, line in enumerate(lines, 1):
            # Look for attribute blocks
            attrs = re.finditer(r'\{([^}]+)\}', line)
            for attr in attrs:
                attr_content = attr.group(1)
                
                # Check if it looks like custom attributes
                if re.search(r'\.([\w-]+)|\#([\w-]+)|(\w+)=', attr_content):
                    # Validate syntax
                    # Classes should start with .
                    # IDs should start with #
                    # Attributes should be key=value
                    
                    parts = attr_content.split()
                    for part in parts:
                        if not (part.startswith('.') or part.startswith('#') or '=' in part):
                            self._add_uncertain_change(
                                i, 'custom_attributes',
                                attr.group(0),
                                attr.group(0),
                                f'Possibly malformed custom attribute: {part}'
                            )
    
    def _check_against_spec(self, content: str):
        """Check content against loaded specification rules."""
        if not self.spec_rules:
            return
        
        lines = content.split('\n')
        
        for rule in self.spec_rules:
            pattern = rule['syntax']
            
            # Convert spec syntax to regex (simplified)
            # This would need to be more sophisticated for real specs
            regex_pattern = re.escape(pattern).replace(r'\.\.\.', '.*')
            
            for i, line in enumerate(lines, 1):
                if re.search(regex_pattern, line):
                    # Found usage of this extension
                    # Could do more detailed validation here
                    pass


def main():
    """Main entry point for the extension checker."""
    if len(sys.argv) < 2:
        print("Usage: python check_extensions.py <file.md> [--spec spec.md] [--examples examples/]")
        print("       python check_extensions.py <directory/> [--spec spec.md] [--examples examples/]")
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
    
    checker = ExtensionChecker(spec_file, examples_dir)
    
    # Collect files to check
    if target.is_file():
        files = [target]
    elif target.is_dir():
        files = list(target.rglob('*.md'))
    else:
        print(f"Error: {target} is not a valid file or directory")
        sys.exit(1)
    
    # Check all files
    results = []
    for filepath in files:
        result = checker.check_file(filepath)
        results.append(result)
        
        print(f"\n{'='*60}")
        print(f"File: {result['filepath']}")
        print(f"Valid: {result['valid']}")
        
        if result.get('error'):
            print(f"Error: {result['error']}")
        
        if result['issues']:
            print(f"\nExtension issues found: {len(result['issues'])}")
            for issue in result['issues']:
                print(f"  Line {issue['line']} [{issue['severity'].upper()}] {issue['extension']}: {issue['description']}")
        
        if result['uncertain_changes']:
            print(f"\nUncertain changes: {len(result['uncertain_changes'])}")
            for change in result['uncertain_changes']:
                print(f"  Line {change['line']} [{change['extension']}]: {change['reason']}")
    
    # Write detailed report
    report_file = Path('extension_check_report.json')
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n{'='*60}")
    print(f"Detailed report written to: {report_file}")
    
    # Return exit code based on check results
    if any(not result['valid'] for result in results):
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()

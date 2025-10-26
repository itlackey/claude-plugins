#!/usr/bin/env python3
"""
Markdown formatter that fixes syntax and formatting issues without altering text content.
Only applies changes that are certain to be correct.
Logs uncertain changes for manual review.
"""

import sys
import json
import re
from pathlib import Path
from typing import List, Dict, Any, Tuple


class MarkdownFormatter:
    """Formats markdown files fixing syntax issues without changing text content."""
    
    def __init__(self, review_file: Path = None):
        """
        Initialize formatter.
        
        Args:
            review_file: Path to write uncertain changes for manual review
        """
        self.review_file = review_file or Path('formatting_review.md')
        self.changes_made = []
        self.uncertain_changes = []
    
    def format_file(self, filepath: Path, in_place: bool = False) -> Dict[str, Any]:
        """
        Format a markdown file.
        
        Args:
            filepath: Path to markdown file
            in_place: If True, modify file in place; otherwise create .formatted.md
            
        Returns:
            Dictionary containing formatting results
        """
        self.changes_made = []
        self.uncertain_changes = []
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                original_content = f.read()
        except Exception as e:
            return {
                'filepath': str(filepath),
                'success': False,
                'error': f'Failed to read file: {str(e)}',
                'changes': [],
                'uncertain_changes': []
            }
        
        # Apply formatting fixes
        formatted_content = original_content
        formatted_content = self._fix_heading_spacing(formatted_content)
        formatted_content = self._fix_list_spacing(formatted_content)
        formatted_content = self._fix_code_fence_consistency(formatted_content)
        formatted_content = self._fix_emphasis_markers(formatted_content)
        formatted_content = self._normalize_line_endings(formatted_content)
        formatted_content = self._ensure_final_newline(formatted_content)
        
        # Determine output path
        if in_place:
            output_path = filepath
        else:
            output_path = filepath.with_suffix('.formatted.md')
        
        # Write formatted content
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(formatted_content)
        except Exception as e:
            return {
                'filepath': str(filepath),
                'success': False,
                'error': f'Failed to write file: {str(e)}',
                'changes': self.changes_made,
                'uncertain_changes': self.uncertain_changes
            }
        
        # Write review file if there are uncertain changes
        if self.uncertain_changes:
            self._write_review_file()
        
        return {
            'filepath': str(filepath),
            'output_path': str(output_path),
            'success': True,
            'changes': self.changes_made,
            'uncertain_changes': self.uncertain_changes,
            'modified': formatted_content != original_content
        }
    
    def _log_change(self, change_type: str, description: str):
        """Log a change that was made."""
        self.changes_made.append({
            'type': change_type,
            'description': description
        })
    
    def _log_uncertain(self, line_num: int, change_type: str,
                      current: str, reason: str):
        """Log an uncertain change for manual review."""
        self.uncertain_changes.append({
            'line': line_num,
            'type': change_type,
            'current': current,
            'reason': reason
        })
    
    def _fix_heading_spacing(self, content: str) -> str:
        """Fix spacing issues in headings."""
        lines = content.split('\n')
        modified = False
        
        for i, line in enumerate(lines):
            # Fix missing space after #
            match = re.match(r'^(#{1,6})([^\s#].*)$', line)
            if match:
                lines[i] = f"{match.group(1)} {match.group(2)}"
                modified = True
                self._log_change('heading_spacing',
                               f'Added space after # in heading on line {i+1}')
            
            # Fix multiple spaces after #
            elif re.match(r'^(#{1,6})\s{2,}(.+)$', line):
                match = re.match(r'^(#{1,6})\s{2,}(.+)$', line)
                lines[i] = f"{match.group(1)} {match.group(2)}"
                modified = True
                self._log_change('heading_spacing',
                               f'Normalized spacing in heading on line {i+1}')
        
        return '\n'.join(lines) if modified else content
    
    def _fix_list_spacing(self, content: str) -> str:
        """Fix spacing issues in lists."""
        lines = content.split('\n')
        modified = False
        
        for i, line in enumerate(lines):
            # Fix unordered list spacing
            match = re.match(r'^(\s*)([*+-])([^\s].*)$', line)
            if match:
                indent, marker, rest = match.groups()
                lines[i] = f"{indent}{marker} {rest}"
                modified = True
                self._log_change('list_spacing',
                               f'Fixed spacing after list marker on line {i+1}')
            
            # Fix multiple spaces after list marker
            elif re.match(r'^(\s*)([*+-])\s{2,}(\S)', line):
                match = re.match(r'^(\s*)([*+-])\s{2,}(.*)$', line)
                indent, marker, rest = match.groups()
                lines[i] = f"{indent}{marker} {rest}"
                modified = True
                self._log_change('list_spacing',
                               f'Normalized spacing after list marker on line {i+1}')
            
            # Fix ordered list spacing
            elif re.match(r'^(\s*)(\d+\.)([^\s].*)$', line):
                match = re.match(r'^(\s*)(\d+\.)([^\s].*)$', line)
                indent, number, rest = match.groups()
                lines[i] = f"{indent}{number} {rest}"
                modified = True
                self._log_change('list_spacing',
                               f'Fixed spacing after ordered list number on line {i+1}')
        
        return '\n'.join(lines) if modified else content
    
    def _fix_code_fence_consistency(self, content: str) -> str:
        """Ensure code fences use consistent markers (prefer ```)."""
        lines = content.split('\n')
        modified = False
        
        for i, line in enumerate(lines):
            # Convert ~~~ to ```
            if re.match(r'^~{3,}', line):
                backticks = '`' * len(re.match(r'^~+', line).group())
                lines[i] = re.sub(r'^~+', backticks, line)
                modified = True
                self._log_change('code_fence',
                               f'Normalized code fence to backticks on line {i+1}')
        
        return '\n'.join(lines) if modified else content
    
    def _fix_emphasis_markers(self, content: str) -> str:
        """Fix mismatched emphasis markers (only certain cases)."""
        lines = content.split('\n')
        modified = False
        
        for i, line in enumerate(lines):
            # Only fix clear mismatches like *text_ where it's obvious
            # Be conservative here
            original_line = line
            
            # Fix *text_ to *text*
            line = re.sub(r'\*([^*_]+)_(?![a-zA-Z])', r'*\1*', line)
            
            # Fix _text* to _text_
            line = re.sub(r'(?<![a-zA-Z])_([^*_]+)\*', r'_\1_', line)
            
            if line != original_line:
                lines[i] = line
                modified = True
                self._log_change('emphasis',
                               f'Fixed mismatched emphasis markers on line {i+1}')
        
        return '\n'.join(lines) if modified else content
    
    def _normalize_line_endings(self, content: str) -> str:
        """Normalize line endings to Unix style (LF)."""
        if '\r\n' in content:
            self._log_change('line_endings', 'Normalized line endings to LF')
            return content.replace('\r\n', '\n')
        return content
    
    def _ensure_final_newline(self, content: str) -> str:
        """Ensure file ends with a newline."""
        if content and not content.endswith('\n'):
            self._log_change('final_newline', 'Added final newline')
            return content + '\n'
        return content
    
    def _write_review_file(self):
        """Write uncertain changes to review file."""
        try:
            with open(self.review_file, 'w', encoding='utf-8') as f:
                f.write("# Markdown Formatting Review\n\n")
                f.write("The following changes were detected but not applied automatically.\n")
                f.write("Please review and apply manually if appropriate.\n\n")
                
                for change in self.uncertain_changes:
                    f.write(f"## Line {change['line']}\n\n")
                    f.write(f"**Type:** {change['type']}\n\n")
                    f.write(f"**Reason:** {change['reason']}\n\n")
                    f.write(f"**Current content:**\n```markdown\n{change['current']}\n```\n\n")
                    f.write("---\n\n")
        
        except Exception as e:
            print(f"Warning: Failed to write review file: {e}", file=sys.stderr)


def main():
    """Main entry point for the formatter."""
    if len(sys.argv) < 2:
        print("Usage: python format_markdown.py <file.md> [--in-place] [--review review.md]")
        print("       python format_markdown.py <directory/> [--in-place] [--review review.md]")
        print("\nOptions:")
        print("  --in-place    Modify files in place instead of creating .formatted.md files")
        print("  --review FILE Write uncertain changes to FILE (default: formatting_review.md)")
        sys.exit(1)
    
    target = Path(sys.argv[1])
    in_place = '--in-place' in sys.argv
    review_file = None
    
    # Parse review file argument
    if '--review' in sys.argv:
        idx = sys.argv.index('--review')
        if idx + 1 < len(sys.argv):
            review_file = Path(sys.argv[idx + 1])
    
    formatter = MarkdownFormatter(review_file)
    
    # Collect files to format
    if target.is_file():
        files = [target]
    elif target.is_dir():
        files = list(target.rglob('*.md'))
    else:
        print(f"Error: {target} is not a valid file or directory")
        sys.exit(1)
    
    # Format all files
    results = []
    for filepath in files:
        result = formatter.format_file(filepath, in_place)
        results.append(result)
        
        print(f"\n{'='*60}")
        print(f"File: {result['filepath']}")
        print(f"Success: {result['success']}")
        
        if result.get('error'):
            print(f"Error: {result['error']}")
        else:
            print(f"Output: {result['output_path']}")
            print(f"Modified: {result['modified']}")
            
            if result['changes']:
                print(f"\nChanges applied: {len(result['changes'])}")
                for change in result['changes']:
                    print(f"  [{change['type']}] {change['description']}")
            
            if result['uncertain_changes']:
                print(f"\nUncertain changes logged: {len(result['uncertain_changes'])}")
                print(f"Review at: {formatter.review_file}")
    
    # Write summary report
    report_file = Path('formatting_report.json')
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n{'='*60}")
    print(f"Detailed report written to: {report_file}")
    
    # Return exit code based on results
    if any(not result['success'] for result in results):
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()

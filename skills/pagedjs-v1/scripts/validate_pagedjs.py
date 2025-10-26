#!/usr/bin/env python3
"""
Validate Paged.js HTML/CSS for common issues.

Usage:
    python validate_pagedjs.py <html_file>
    python validate_pagedjs.py <html_file> --css <css_file>
"""

import re
import sys
from pathlib import Path
from html.parser import HTMLParser


class PagedJSValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.issues = []
        self.warnings = []
        self.info = []
        self.in_style = False
        self.style_content = []
        self.string_sets = set()
        self.string_uses = set()
        self.counter_resets = set()
        self.counter_increments = set()
        self.page_names = set()
        self.current_tag = None
        
    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        attrs_dict = dict(attrs)
        
        # Check for Paged.js script
        if tag == 'script':
            if attrs_dict.get('src', '').find('paged') != -1:
                self.info.append("✓ Paged.js script found")
                
        # Check for style tag
        if tag == 'style':
            self.in_style = True
            
        # Check for problematic absolute positioning
        if 'style' in attrs_dict:
            style = attrs_dict['style']
            if 'position: absolute' in style or 'position:absolute' in style:
                self.warnings.append(f"Warning: Absolute positioning in inline style on <{tag}> - may cause issues")
                
    def handle_endtag(self, tag):
        if tag == 'style':
            self.in_style = False
            
    def handle_data(self, data):
        if self.in_style:
            self.style_content.append(data)
            
    def analyze_css(self, css_content):
        """Analyze CSS for common Paged.js patterns and issues."""
        
        # Find string-set declarations
        string_set_pattern = r'string-set:\s*([a-zA-Z0-9_-]+)'
        for match in re.finditer(string_set_pattern, css_content):
            self.string_sets.add(match.group(1))
            
        # Find string() uses in content
        string_use_pattern = r'content:.*?string\(([a-zA-Z0-9_-]+)\)'
        for match in re.finditer(string_use_pattern, css_content):
            self.string_uses.add(match.group(1))
            
        # Find counter-reset
        counter_reset_pattern = r'counter-reset:\s*([a-zA-Z0-9_-]+)'
        for match in re.finditer(counter_reset_pattern, css_content):
            counters = match.group(1).split()
            for counter in counters:
                if counter and not counter.isdigit():
                    self.counter_resets.add(counter)
                    
        # Find counter-increment
        counter_inc_pattern = r'counter-increment:\s*([a-zA-Z0-9_-]+)'
        for match in re.finditer(counter_inc_pattern, css_content):
            self.counter_increments.add(match.group(1))
            
        # Find named pages
        page_name_pattern = r'page:\s*([a-zA-Z0-9_-]+)'
        for match in re.finditer(page_name_pattern, css_content):
            self.page_names.add(match.group(1))
            
        # Check for @page rules
        if '@page' not in css_content:
            self.warnings.append("Warning: No @page rules found - document may not be configured for print")
            
        # Check for size declaration
        if 'size:' not in css_content:
            self.warnings.append("Warning: No page size specified in @page rules")
            
        # Check for break properties
        has_break_properties = any(prop in css_content for prop in [
            'break-before:', 'break-after:', 'break-inside:',
            'page-break-before:', 'page-break-after:', 'page-break-inside:'
        ])
        if not has_break_properties:
            self.info.append("Info: No page break properties found - you may want to control page breaks")
            
        # Check for common issues
        if 'position: absolute' in css_content or 'position:absolute' in css_content:
            self.warnings.append("Warning: Absolute positioning found - may cause layout issues with paged media")
            
        if 'position: fixed' in css_content or 'position:fixed' in css_content:
            self.warnings.append("Warning: Fixed positioning found - may not work as expected in paged media")
            
        # Check for orphans and widows
        if 'orphans:' not in css_content and 'widows:' not in css_content:
            self.info.append("Info: Consider adding orphans and widows properties for better typography")
            
        # Check for margin box content
        has_margin_boxes = any(box in css_content for box in [
            '@top-left', '@top-center', '@top-right',
            '@bottom-left', '@bottom-center', '@bottom-right'
        ])
        if not has_margin_boxes:
            self.info.append("Info: No margin boxes defined - consider adding headers/footers")
            
    def validate_cross_references(self):
        """Check for mismatches between string-set and string() usage."""
        
        # Check for string() without corresponding string-set
        unused_strings = self.string_uses - self.string_sets
        if unused_strings:
            for string_name in unused_strings:
                self.issues.append(f"Error: string({string_name}) used but never set with string-set")
                
        # Check for string-set without usage (warning only)
        unset_strings = self.string_sets - self.string_uses
        if unset_strings:
            for string_name in unset_strings:
                self.warnings.append(f"Warning: string-set defines '{string_name}' but it's never used")
                
        # Check for counter-increment without reset
        unreset_counters = self.counter_increments - self.counter_resets
        if unreset_counters and 'page' not in unreset_counters:  # page is auto-reset
            for counter in unreset_counters:
                self.warnings.append(f"Warning: counter-increment on '{counter}' but no counter-reset found")
                
    def report(self):
        """Print validation report."""
        print("\n" + "="*60)
        print("PAGED.JS VALIDATION REPORT")
        print("="*60)
        
        if self.issues:
            print("\n❌ ERRORS:")
            for issue in self.issues:
                print(f"  {issue}")
        else:
            print("\n✓ No errors found")
            
        if self.warnings:
            print("\n⚠️  WARNINGS:")
            for warning in self.warnings:
                print(f"  {warning}")
                
        if self.info:
            print("\n💡 SUGGESTIONS:")
            for info in self.info:
                print(f"  {info}")
                
        if self.string_sets:
            print(f"\n📝 String sets found: {', '.join(sorted(self.string_sets))}")
        if self.counter_resets:
            print(f"🔢 Counters found: {', '.join(sorted(self.counter_resets))}")
        if self.page_names:
            print(f"📄 Named pages found: {', '.join(sorted(self.page_names))}")
            
        print("\n" + "="*60)
        return len(self.issues) == 0


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
        
    html_file = Path(sys.argv[1])
    css_file = None
    
    # Check for --css argument
    if '--css' in sys.argv:
        css_index = sys.argv.index('--css')
        if css_index + 1 < len(sys.argv):
            css_file = Path(sys.argv[css_index + 1])
            
    if not html_file.exists():
        print(f"Error: File not found: {html_file}")
        sys.exit(1)
        
    # Read HTML
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    # Parse HTML
    validator = PagedJSValidator()
    validator.feed(html_content)
    
    # Combine CSS from style tags
    css_content = '\n'.join(validator.style_content)
    
    # Add external CSS if provided
    if css_file and css_file.exists():
        with open(css_file, 'r', encoding='utf-8') as f:
            css_content += '\n' + f.read()
            
    # Analyze CSS
    if css_content:
        validator.analyze_css(css_content)
    else:
        validator.warnings.append("Warning: No CSS found to analyze")
        
    # Check cross-references
    validator.validate_cross_references()
    
    # Print report
    success = validator.report()
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()

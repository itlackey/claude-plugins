#!/usr/bin/env python3
"""
Analyze HTML and extract design metrics for UI review.
Extracts colors, typography, spacing patterns, and component inventory.
"""

import json
import sys
import re
from html.parser import HTMLParser
from collections import Counter

class DesignElementParser(HTMLParser):
    """Parse HTML to extract design elements."""
    
    def __init__(self):
        super().__init__()
        self.colors = []
        self.fonts = []
        self.font_sizes = []
        self.components = {
            'buttons': [],
            'inputs': [],
            'links': [],
            'headings': [],
            'images': [],
            'cards': []
        }
        self.classes = []
        
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        # Extract classes
        if 'class' in attrs_dict:
            self.classes.extend(attrs_dict['class'].split())
        
        # Track components
        if tag == 'button':
            self.components['buttons'].append(attrs_dict)
        elif tag == 'input':
            self.components['inputs'].append(attrs_dict)
        elif tag == 'a':
            self.components['links'].append(attrs_dict)
        elif tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.components['headings'].append({'tag': tag, 'attrs': attrs_dict})
        elif tag == 'img':
            self.components['images'].append(attrs_dict)
        
        # Look for card patterns
        if 'class' in attrs_dict:
            classes = attrs_dict['class'].lower()
            if 'card' in classes or 'panel' in classes:
                self.components['cards'].append(attrs_dict)
        
        # Extract inline colors
        if 'style' in attrs_dict:
            style = attrs_dict['style']
            color_matches = re.findall(r'color:\s*([^;]+)', style)
            self.colors.extend(color_matches)
            bg_matches = re.findall(r'background(-color)?:\s*([^;]+)', style)
            self.colors.extend([m[1] for m in bg_matches])
            
            # Extract font info
            font_family = re.findall(r'font-family:\s*([^;]+)', style)
            self.fonts.extend(font_family)
            font_size = re.findall(r'font-size:\s*([^;]+)', style)
            self.font_sizes.extend(font_size)

def analyze_html(html_content):
    """Analyze HTML content and extract design elements."""
    parser = DesignElementParser()
    parser.feed(html_content)
    
    # Aggregate results
    results = {
        'components': {
            'buttons': len(parser.components['buttons']),
            'inputs': len(parser.components['inputs']),
            'links': len(parser.components['links']),
            'headings': len(parser.components['headings']),
            'images': len(parser.components['images']),
            'cards': len(parser.components['cards'])
        },
        'typography': {
            'font_families': list(set(parser.fonts)),
            'font_sizes': list(set(parser.font_sizes)),
            'heading_distribution': dict(Counter([h['tag'] for h in parser.components['headings']]))
        },
        'colors': {
            'unique_colors': list(set(parser.colors)),
            'total_color_instances': len(parser.colors)
        },
        'classes': {
            'unique_classes': len(set(parser.classes)),
            'most_common': Counter(parser.classes).most_common(20)
        }
    }
    
    return results

def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: analyze_design_elements.py <html_file>")
        sys.exit(1)
    
    if sys.argv[1] == '-':
        html_content = sys.stdin.read()
    else:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            html_content = f.read()
    
    results = analyze_html(html_content)
    print(json.dumps(results, indent=2))

if __name__ == '__main__':
    main()

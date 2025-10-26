#!/usr/bin/env python3
"""
Analyze HTML content for UX guidance elements and potential issues.
Extracts labels, help text, placeholders, error messages, and tooltips.
"""

import json
import sys
from html.parser import HTMLParser
from typing import Dict, List, Set


class UXElementParser(HTMLParser):
    """Parse HTML to extract UX guidance elements."""
    
    def __init__(self):
        super().__init__()
        self.elements = {
            'labels': [],
            'buttons': [],
            'inputs': [],
            'help_text': [],
            'tooltips': [],
            'error_messages': [],
            'headings': [],
            'links': [],
            'aria_labels': []
        }
        self.current_tag = None
        self.current_attrs = {}
        self.capture_text = False
        self.text_buffer = []
        
    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        self.current_attrs = dict(attrs)
        
        # Extract various UX elements
        if tag == 'label':
            self.capture_text = True
            
        elif tag == 'button':
            self.capture_text = True
            
        elif tag == 'input':
            input_type = self.current_attrs.get('type', 'text')
            placeholder = self.current_attrs.get('placeholder', '')
            aria_label = self.current_attrs.get('aria-label', '')
            title = self.current_attrs.get('title', '')
            value = self.current_attrs.get('value', '')
            
            self.elements['inputs'].append({
                'type': input_type,
                'placeholder': placeholder,
                'aria_label': aria_label,
                'title': title,
                'value': value,
                'id': self.current_attrs.get('id', ''),
                'name': self.current_attrs.get('name', '')
            })
            
        elif tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.capture_text = True
            
        elif tag == 'a':
            self.capture_text = True
            
        # Check for common help text patterns
        if 'class' in self.current_attrs:
            classes = self.current_attrs['class'].lower()
            if any(x in classes for x in ['help', 'hint', 'description', 'guidance']):
                self.capture_text = True
                
        # Check for error message patterns
        if 'class' in self.current_attrs:
            classes = self.current_attrs['class'].lower()
            if any(x in classes for x in ['error', 'invalid', 'warning', 'alert']):
                self.capture_text = True
                
        # Extract ARIA labels
        if 'aria-label' in self.current_attrs:
            self.elements['aria_labels'].append({
                'tag': tag,
                'aria_label': self.current_attrs['aria-label'],
                'role': self.current_attrs.get('role', '')
            })
            
        # Extract tooltips
        if 'title' in self.current_attrs and self.current_attrs['title']:
            self.elements['tooltips'].append({
                'tag': tag,
                'title': self.current_attrs['title'],
                'id': self.current_attrs.get('id', '')
            })
    
    def handle_data(self, data):
        if self.capture_text:
            self.text_buffer.append(data.strip())
    
    def handle_endtag(self, tag):
        if self.capture_text and self.text_buffer:
            text = ' '.join(self.text_buffer).strip()
            if text:
                if self.current_tag == 'label':
                    self.elements['labels'].append({
                        'text': text,
                        'for': self.current_attrs.get('for', '')
                    })
                elif self.current_tag == 'button':
                    self.elements['buttons'].append({
                        'text': text,
                        'type': self.current_attrs.get('type', 'button')
                    })
                elif self.current_tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    self.elements['headings'].append({
                        'level': self.current_tag,
                        'text': text
                    })
                elif self.current_tag == 'a':
                    self.elements['links'].append({
                        'text': text,
                        'href': self.current_attrs.get('href', '')
                    })
                elif 'class' in self.current_attrs:
                    classes = self.current_attrs['class'].lower()
                    if any(x in classes for x in ['help', 'hint', 'description', 'guidance']):
                        self.elements['help_text'].append(text)
                    elif any(x in classes for x in ['error', 'invalid', 'warning', 'alert']):
                        self.elements['error_messages'].append(text)
        
        self.capture_text = False
        self.text_buffer = []
        self.current_tag = None
        self.current_attrs = {}


def analyze_html(html_content: str) -> Dict:
    """
    Analyze HTML content and extract UX elements.
    
    Args:
        html_content: HTML string to analyze
        
    Returns:
        Dictionary containing categorized UX elements
    """
    parser = UXElementParser()
    parser.feed(html_content)
    return parser.elements


def identify_issues(elements: Dict) -> List[Dict]:
    """
    Identify potential UX guidance issues based on extracted elements.
    
    Args:
        elements: Dictionary of extracted UX elements
        
    Returns:
        List of identified issues with severity and recommendations
    """
    issues = []
    
    # Check for inputs without labels
    input_ids = {inp['id'] for inp in elements['inputs'] if inp['id']}
    label_fors = {label['for'] for label in elements['labels'] if label['for']}
    unlabeled_inputs = [inp for inp in elements['inputs'] 
                        if inp['id'] and inp['id'] not in label_fors 
                        and not inp['aria_label']]
    
    if unlabeled_inputs:
        issues.append({
            'category': 'Accessibility',
            'severity': 'High',
            'issue': f'{len(unlabeled_inputs)} input(s) without labels or ARIA labels',
            'elements': unlabeled_inputs,
            'recommendation': 'Add proper <label> elements or aria-label attributes for all form inputs'
        })
    
    # Check for vague button text
    vague_buttons = [btn for btn in elements['buttons'] 
                     if btn['text'].lower() in ['click here', 'submit', 'ok', 'click', 'here']]
    
    if vague_buttons:
        issues.append({
            'category': 'Clarity',
            'severity': 'Medium',
            'issue': f'{len(vague_buttons)} button(s) with vague text',
            'elements': vague_buttons,
            'recommendation': 'Use descriptive action-oriented button text (e.g., "Save Changes", "Download Report")'
        })
    
    # Check for empty placeholders on required-looking inputs
    inputs_without_guidance = [inp for inp in elements['inputs'] 
                                if inp['type'] in ['text', 'email', 'password', 'tel'] 
                                and not inp['placeholder'] 
                                and not inp['aria_label']]
    
    if inputs_without_guidance:
        issues.append({
            'category': 'User Guidance',
            'severity': 'Low',
            'issue': f'{len(inputs_without_guidance)} input(s) without placeholders or guidance',
            'elements': inputs_without_guidance,
            'recommendation': 'Consider adding placeholder text or help text to guide users'
        })
    
    # Check for vague link text
    vague_links = [link for link in elements['links'] 
                   if link['text'].lower() in ['click here', 'here', 'read more', 'more', 'link']]
    
    if vague_links:
        issues.append({
            'category': 'Clarity',
            'severity': 'Medium',
            'issue': f'{len(vague_links)} link(s) with vague text',
            'elements': vague_links,
            'recommendation': 'Use descriptive link text that indicates the destination or action'
        })
    
    # Check for missing help text
    if len(elements['inputs']) > 5 and not elements['help_text']:
        issues.append({
            'category': 'User Guidance',
            'severity': 'Medium',
            'issue': 'Complex form with no visible help text',
            'recommendation': 'Consider adding contextual help text for complex or unfamiliar fields'
        })
    
    return issues


def main():
    """Main function to run the analyzer."""
    if len(sys.argv) < 2:
        print("Usage: analyze_ux_elements.py <html_file>")
        print("  or pipe HTML: echo '<html>...</html>' | analyze_ux_elements.py -")
        sys.exit(1)
    
    # Read HTML content
    if sys.argv[1] == '-':
        html_content = sys.stdin.read()
    else:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            html_content = f.read()
    
    # Analyze the HTML
    elements = analyze_html(html_content)
    issues = identify_issues(elements)
    
    # Output results as JSON
    results = {
        'elements': elements,
        'issues': issues,
        'summary': {
            'total_labels': len(elements['labels']),
            'total_buttons': len(elements['buttons']),
            'total_inputs': len(elements['inputs']),
            'total_help_text': len(elements['help_text']),
            'total_issues': len(issues),
            'high_severity_issues': len([i for i in issues if i['severity'] == 'High']),
            'medium_severity_issues': len([i for i in issues if i['severity'] == 'Medium']),
            'low_severity_issues': len([i for i in issues if i['severity'] == 'Low'])
        }
    }
    
    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()

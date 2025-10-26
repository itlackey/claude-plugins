#!/usr/bin/env python3
"""
Bluesky Thread Creation Script

Creates a thread (series of connected posts) on Bluesky.
Requires: pip install atproto --break-system-packages
"""

import argparse
import json
import sys
from datetime import datetime
from typing import List

try:
    from atproto import Client
except ImportError:
    print("Error: atproto library not installed. Run: pip install atproto --break-system-packages", file=sys.stderr)
    sys.exit(1)


def load_credentials(creds_file: str) -> dict:
    """Load Bluesky credentials from JSON file."""
    try:
        with open(creds_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Credentials file not found: {creds_file}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in credentials file: {creds_file}", file=sys.stderr)
        sys.exit(1)


def create_thread(client: Client, posts: List[str]) -> List[dict]:
    """Create a thread of posts, each replying to the previous."""
    results = []
    parent_uri = None
    parent_cid = None
    root_uri = None
    root_cid = None
    
    for i, text in enumerate(posts):
        post_data = {
            'text': text,
            'createdAt': datetime.utcnow().isoformat() + 'Z'
        }
        
        # Add reply reference if not the first post
        if parent_uri and parent_cid:
            post_data['reply'] = {
                'root': {
                    'uri': root_uri,
                    'cid': root_cid
                },
                'parent': {
                    'uri': parent_uri,
                    'cid': parent_cid
                }
            }
        
        try:
            response = client.send_post(**post_data)
            
            # First post becomes the root
            if i == 0:
                root_uri = response.uri
                root_cid = response.cid
            
            # Current post becomes parent for next post
            parent_uri = response.uri
            parent_cid = response.cid
            
            result = {
                'success': True,
                'post_number': i + 1,
                'uri': response.uri,
                'cid': response.cid,
                'url': f"https://bsky.app/profile/{client.me.handle}/post/{response.uri.split('/')[-1]}"
            }
            results.append(result)
            print(f"✅ Posted {i+1}/{len(posts)}: {result['url']}", file=sys.stderr)
            
        except Exception as e:
            result = {
                'success': False,
                'post_number': i + 1,
                'error': str(e)
            }
            results.append(result)
            print(f"❌ Failed to post {i+1}/{len(posts)}: {e}", file=sys.stderr)
            break
    
    return results


def main():
    parser = argparse.ArgumentParser(description='Create a thread on Bluesky')
    parser.add_argument('posts', nargs='+', help='Text for each post in the thread')
    parser.add_argument('--credentials', default='bluesky_credentials.json',
                       help='Path to credentials JSON file')
    parser.add_argument('--output', help='Save thread details to JSON file')
    
    args = parser.parse_args()
    
    # Load credentials and authenticate
    creds = load_credentials(args.credentials)
    
    try:
        client = Client()
        client.login(creds['handle'], creds['app_password'])
        print(f"Authenticated as: {client.me.handle}", file=sys.stderr)
    except Exception as e:
        print(f"Authentication failed: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Create the thread
    print(f"Creating thread with {len(args.posts)} posts...", file=sys.stderr)
    results = create_thread(client, args.posts)
    
    # Check if all succeeded
    all_success = all(r['success'] for r in results)
    
    if all_success:
        print(f"\n✅ Thread created successfully!")
        print(f"Thread starts at: {results[0]['url']}")
    else:
        print(f"\n⚠️ Thread partially created. Some posts failed.", file=sys.stderr)
    
    # Save to file if requested
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Details saved to: {args.output}")
    
    # Print JSON for programmatic use
    print(json.dumps({
        'success': all_success,
        'thread': results
    }))
    
    sys.exit(0 if all_success else 1)


if __name__ == '__main__':
    main()

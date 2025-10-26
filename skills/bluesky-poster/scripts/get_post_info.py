#!/usr/bin/env python3
"""
Bluesky Post Info Script

Retrieve details about a Bluesky post given its URL or URI.
Useful for getting URI and CID needed for replies.
Requires: pip install atproto --break-system-packages
"""

import argparse
import json
import sys
import re

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


def parse_post_url(url: str) -> tuple:
    """Extract handle and post ID from Bluesky URL."""
    # Pattern: https://bsky.app/profile/HANDLE/post/POST_ID
    pattern = r'bsky\.app/profile/([^/]+)/post/([^/]+)'
    match = re.search(pattern, url)
    
    if match:
        return match.group(1), match.group(2)
    else:
        print(f"Error: Invalid Bluesky URL format: {url}", file=sys.stderr)
        print("Expected format: https://bsky.app/profile/HANDLE/post/POST_ID", file=sys.stderr)
        sys.exit(1)


def get_post_info(client: Client, handle: str, post_id: str) -> dict:
    """Get post information including URI and CID."""
    try:
        # Construct AT URI
        at_uri = f"at://{handle}/app.bsky.feed.post/{post_id}"
        
        # Get post thread to access the post
        thread = client.get_post_thread(at_uri)
        post = thread.thread.post
        
        return {
            'success': True,
            'uri': post.uri,
            'cid': post.cid,
            'text': post.record.text,
            'author': {
                'handle': post.author.handle,
                'display_name': post.author.display_name
            },
            'created_at': post.record.created_at,
            'reply_count': post.reply_count or 0,
            'repost_count': post.repost_count or 0,
            'like_count': post.like_count or 0
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }


def main():
    parser = argparse.ArgumentParser(description='Get Bluesky post information')
    parser.add_argument('url', help='Bluesky post URL (e.g., https://bsky.app/profile/handle.bsky.social/post/...)')
    parser.add_argument('--credentials', default='bluesky_credentials.json',
                       help='Path to credentials JSON file')
    parser.add_argument('--output', help='Save post info to JSON file')
    
    args = parser.parse_args()
    
    # Parse URL
    handle, post_id = parse_post_url(args.url)
    
    # Load credentials and authenticate
    creds = load_credentials(args.credentials)
    
    try:
        client = Client()
        client.login(creds['handle'], creds['app_password'])
    except Exception as e:
        print(f"Authentication failed: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Get post info
    result = get_post_info(client, handle, post_id)
    
    if result['success']:
        print(f"✅ Post information retrieved")
        print(f"\nURI: {result['uri']}")
        print(f"CID: {result['cid']}")
        print(f"\nAuthor: {result['author']['display_name']} (@{result['author']['handle']})")
        print(f"Text: {result['text'][:100]}{'...' if len(result['text']) > 100 else ''}")
        print(f"\nStats: {result['like_count']} likes, {result['repost_count']} reposts, {result['reply_count']} replies")
        
        # Save to file if requested
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(result, f, indent=2)
            print(f"\nDetails saved to: {args.output}")
        
        # Print JSON for programmatic use
        print(json.dumps(result))
    else:
        print(f"❌ Failed to get post info: {result['error']}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()

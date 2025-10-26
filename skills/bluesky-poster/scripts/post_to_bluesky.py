#!/usr/bin/env python3
"""
Bluesky Post Creation Script

Posts messages, images, and replies to Bluesky using the AT Protocol API.
Requires: pip install atproto --break-system-packages
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Optional, List
from datetime import datetime

try:
    from atproto import Client, models
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
        print("Create a JSON file with: {\"handle\": \"your.handle\", \"app_password\": \"your-app-password\"}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in credentials file: {creds_file}", file=sys.stderr)
        sys.exit(1)


def upload_images(client: Client, image_paths: List[str]) -> List[dict]:
    """Upload images to Bluesky and return image blobs."""
    images = []
    for img_path in image_paths:
        path = Path(img_path)
        if not path.exists():
            print(f"Warning: Image not found: {img_path}", file=sys.stderr)
            continue
        
        try:
            with open(path, 'rb') as f:
                img_data = f.read()
            
            # Upload image and get blob
            upload = client.upload_blob(img_data)
            images.append({
                'alt': '',  # Alt text can be added as parameter if needed
                'image': upload.blob
            })
            print(f"Uploaded image: {img_path}", file=sys.stderr)
        except Exception as e:
            print(f"Error uploading image {img_path}: {e}", file=sys.stderr)
    
    return images


def create_post(
    client: Client,
    text: str,
    image_paths: Optional[List[str]] = None,
    reply_to_uri: Optional[str] = None,
    reply_to_cid: Optional[str] = None,
) -> dict:
    """Create a post on Bluesky with optional images and reply reference."""
    
    # Build the post record
    post_data = {
        'text': text,
        'createdAt': datetime.utcnow().isoformat() + 'Z'
    }
    
    # Add images if provided
    if image_paths:
        images = upload_images(client, image_paths)
        if images:
            post_data['embed'] = {
                '$type': 'app.bsky.embed.images',
                'images': images
            }
    
    # Add reply reference if provided
    if reply_to_uri and reply_to_cid:
        post_data['reply'] = {
            'root': {
                'uri': reply_to_uri,
                'cid': reply_to_cid
            },
            'parent': {
                'uri': reply_to_uri,
                'cid': reply_to_cid
            }
        }
    
    # Create the post
    try:
        response = client.send_post(**post_data)
        return {
            'success': True,
            'uri': response.uri,
            'cid': response.cid,
            'url': f"https://bsky.app/profile/{client.me.handle}/post/{response.uri.split('/')[-1]}"
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }


def main():
    parser = argparse.ArgumentParser(description='Post to Bluesky')
    parser.add_argument('text', help='Text content to post')
    parser.add_argument('--credentials', default='bluesky_credentials.json', 
                       help='Path to credentials JSON file (default: bluesky_credentials.json)')
    parser.add_argument('--images', nargs='+', help='Paths to images to attach (up to 4)')
    parser.add_argument('--reply-to-uri', help='URI of post to reply to')
    parser.add_argument('--reply-to-cid', help='CID of post to reply to')
    parser.add_argument('--output', help='Save post details to JSON file')
    
    args = parser.parse_args()
    
    # Validate reply parameters
    if (args.reply_to_uri and not args.reply_to_cid) or (args.reply_to_cid and not args.reply_to_uri):
        print("Error: Both --reply-to-uri and --reply-to-cid must be provided together", file=sys.stderr)
        sys.exit(1)
    
    # Validate image count
    if args.images and len(args.images) > 4:
        print("Error: Maximum 4 images allowed per post", file=sys.stderr)
        sys.exit(1)
    
    # Load credentials and authenticate
    creds = load_credentials(args.credentials)
    
    try:
        client = Client()
        client.login(creds['handle'], creds['app_password'])
        print(f"Authenticated as: {client.me.handle}", file=sys.stderr)
    except KeyError:
        print("Error: Credentials must contain 'handle' and 'app_password'", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Authentication failed: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Create the post
    result = create_post(
        client,
        args.text,
        image_paths=args.images,
        reply_to_uri=args.reply_to_uri,
        reply_to_cid=args.reply_to_cid
    )
    
    # Output results
    if result['success']:
        print(f"✅ Post created successfully!")
        print(f"URI: {result['uri']}")
        print(f"CID: {result['cid']}")
        print(f"URL: {result['url']}")
        
        # Save to file if requested
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(result, f, indent=2)
            print(f"Details saved to: {args.output}")
        
        # Print JSON for programmatic use
        print(json.dumps(result))
    else:
        print(f"❌ Failed to create post: {result['error']}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()

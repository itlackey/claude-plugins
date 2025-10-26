---
name: bluesky-poster
description: Post messages, images, threads, and replies to Bluesky. Use when the user wants to post to Bluesky, create a Bluesky thread, reply to a Bluesky post, or manage their company's Bluesky feed. Supports text posts, images (up to 4), links, threads, and replies.
---

# Bluesky Poster

Post messages, images, threads, and replies to Bluesky using the AT Protocol API.

## Setup

**First-time setup required:**

1. Install the atproto library:
```bash
pip install atproto --break-system-packages
```

2. Create credentials file from template:
```bash
cp assets/bluesky_credentials_template.json bluesky_credentials.json
```

3. Edit `bluesky_credentials.json` with actual credentials:
   - **handle**: Bluesky handle (e.g., `company.bsky.social`)
   - **app_password**: Generate at Bluesky Settings > Advanced > App Passwords
   - **Important**: Use app password, NOT main account password

See `references/api_reference.md` for detailed authentication and API information.

## Core Operations

### 1. Simple Text Post

Post text content to Bluesky:

```bash
python scripts/post_to_bluesky.py "Your message here"
```

**Example:**
```bash
python scripts/post_to_bluesky.py "Excited to announce our new product launch! 🚀"
```

### 2. Post with Images

Attach up to 4 images to a post:

```bash
python scripts/post_to_bluesky.py "Check out our new feature!" --images image1.jpg image2.png
```

**Important limits:**
- Maximum 4 images per post
- Each image must be under 1MB
- Supported formats: JPEG, PNG, WebP

**Example:**
```bash
python scripts/post_to_bluesky.py "Product showcase! See the new design 👇" --images product_screenshot.png logo.jpg
```

### 3. Create Thread

Post a series of connected messages as a thread:

```bash
python scripts/create_thread.py "First post in thread" "Second post continues" "Third post concludes"
```

**Example for product announcement:**
```bash
python scripts/create_thread.py \
  "🚀 Big news! We're launching our new API today. Here's what you need to know: (1/3)" \
  "Key features: Real-time data sync, 99.9% uptime SLA, and simple integration. Docs at company.com/api (2/3)" \
  "Special launch pricing: 50% off for the first 100 customers. Sign up now! (3/3)"
```

### 4. Reply to Post

Reply to an existing post using its URI and CID:

**Step 1: Get post details**
```bash
python scripts/get_post_info.py "https://bsky.app/profile/handle.bsky.social/post/abc123"
```

This outputs the URI and CID needed for the reply.

**Step 2: Post reply**
```bash
python scripts/post_to_bluesky.py "Thanks for sharing!" \
  --reply-to-uri "at://did:plc:xxx/app.bsky.feed.post/abc123" \
  --reply-to-cid "bafyreiabc123..."
```

**Important:** Both `--reply-to-uri` and `--reply-to-cid` must be provided together.

## Workflow for Common Tasks

### Company Announcement

1. Draft the post (respect 300 character limit)
2. Prepare images if needed (optimize to under 1MB each)
3. Post using `post_to_bluesky.py` with images
4. Save output JSON to track post URI/CID for analytics

```bash
python scripts/post_to_bluesky.py \
  "We're hiring! Join our team as a Senior Engineer. Learn more: company.com/careers" \
  --images hiring_graphic.jpg \
  --output post_output.json
```

### Multi-Post Product Story

For stories that need multiple connected posts:

1. Write all posts (each under 300 characters)
2. Create thread with `create_thread.py`
3. Save thread output to track all post URIs

```bash
python scripts/create_thread.py \
  "Our journey started 3 years ago with a simple idea..." \
  "Today, we're proud to serve 10,000+ customers worldwide..." \
  "Thank you to everyone who's been part of this journey! 🙏" \
  --output thread_output.json
```

### Scheduled Posts

For automated/scheduled posting (e.g., via cron):

1. Create a script that calls `post_to_bluesky.py`
2. Add 10-15 second delays between posts to respect rate limits
3. Log outputs for monitoring
4. Store credentials securely (ensure `bluesky_credentials.json` is protected)

**Example scheduling script:**
```bash
#!/bin/bash
# Post morning update
python scripts/post_to_bluesky.py "Good morning! Today's focus: customer success 💪"

# Wait to respect rate limits
sleep 15

# Post afternoon update
python scripts/post_to_bluesky.py "Afternoon check-in: Great progress on Q4 goals!"
```

### Engagement and Replies

To reply to customer posts or engage with community:

1. Find the post URL on Bluesky (copy from browser)
2. Use `get_post_info.py` to retrieve URI and CID
3. Reply using `post_to_bluesky.py` with reply parameters

```bash
# Get post details
python scripts/get_post_info.py "https://bsky.app/profile/customer.bsky.social/post/xyz789"

# Reply to the post
python scripts/post_to_bluesky.py "Thank you for the feedback! We're working on this." \
  --reply-to-uri "at://did:plc:yyy/app.bsky.feed.post/xyz789" \
  --reply-to-cid "bafyreidef456..."
```

## Script Reference

### post_to_bluesky.py

Main posting script with full feature support.

**Arguments:**
- `text` (required): Post text content
- `--credentials`: Path to credentials JSON (default: `bluesky_credentials.json`)
- `--images`: List of image paths to attach (max 4)
- `--reply-to-uri`: URI of post to reply to
- `--reply-to-cid`: CID of post to reply to
- `--output`: Save post details to JSON file

**Returns:** JSON with `uri`, `cid`, `url`, and `success` status

### create_thread.py

Create connected thread of posts.

**Arguments:**
- `posts` (required): List of text for each post in thread
- `--credentials`: Path to credentials JSON
- `--output`: Save thread details to JSON file

**Returns:** JSON array with details for each post in thread

### get_post_info.py

Retrieve post details for replying.

**Arguments:**
- `url` (required): Bluesky post URL
- `--credentials`: Path to credentials JSON
- `--output`: Save post info to JSON file

**Returns:** JSON with `uri`, `cid`, `text`, `author`, and engagement stats

## Best Practices

### Content Guidelines

- **Character limit**: 300 characters maximum (Bluesky enforces this)
- **Line breaks**: Use `\n` for multi-line posts
- **Links**: Include full URLs (Bluesky auto-detects and creates link cards)
- **Hashtags**: Use sparingly, not required for discovery on Bluesky
- **Mentions**: Use `@handle.bsky.social` format

### Image Guidelines

- Optimize images to under 1MB before upload
- Recommended size: 1200x675px (16:9 aspect ratio)
- Use JPEG for photos, PNG for graphics/text
- Test image upload separately before scheduled posts

### Rate Limits

- Space automated posts at least 10-15 seconds apart
- Bluesky typically allows 30-50 posts per 5 minutes
- For burst posting, implement exponential backoff on errors
- Monitor for 429 (rate limit) responses

### Security

- **Never commit** `bluesky_credentials.json` to version control
- Use environment variables for credentials in production
- Rotate app passwords periodically
- Use separate app passwords for different automation systems

## Troubleshooting

**Authentication fails:**
- Verify handle format is correct (include `.bsky.social` or custom domain)
- Ensure using app password, not main password
- Check app password hasn't been revoked in settings

**Post too long error:**
- Bluesky has strict 300 character limit
- Count characters including spaces
- Split long messages into threads

**Image upload fails:**
- Check file exists at specified path
- Verify file size is under 1MB
- Confirm file format (JPEG, PNG, WebP only)
- Try compressing image before upload

**Reply doesn't appear:**
- Verify both URI and CID provided
- Check original post still exists
- Ensure reply-to post is public

**Rate limit hit:**
- Add delays between posts (10-15 seconds minimum)
- Reduce posting frequency
- Implement retry logic with exponential backoff

## Additional Resources

- **API Reference**: See `references/api_reference.md` for detailed API information
- **AT Protocol**: https://atproto.com/
- **Bluesky Help**: https://blueskyweb.xyz/support

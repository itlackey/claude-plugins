# Bluesky Poster Skill

A comprehensive skill for posting to Bluesky, including support for images, threads, and replies.

## What's Included

- **bluesky-poster.skill** - The packaged skill file (upload this to Claude)
- **SETUP_GUIDE.md** - Complete setup and usage instructions

## Features

✅ Post text messages to Bluesky
✅ Attach images (up to 4 per post)
✅ Create threaded posts
✅ Reply to existing posts
✅ Get post details (URI/CID for replies)
✅ Scheduled/automated posting support
✅ JSON output for tracking and analytics

## Quick Start

1. Upload `bluesky-poster.skill` to Claude
2. Install dependencies: `pip install atproto --break-system-packages`
3. Set up Bluesky app password (Settings > Advanced > App Passwords)
4. Create credentials file with your handle and app password
5. Start posting!

## Use Cases

- **Company announcements** - Share product launches, updates, and news
- **Scheduled content** - Automate regular posts via cron or task schedulers
- **Community engagement** - Reply to customers and community members
- **Content threads** - Create multi-post stories and tutorials
- **Social media automation** - Integrate with your existing marketing tools

## Example Usage

```bash
# Simple post
python scripts/post_to_bluesky.py "Hello from our company! 🚀"

# Post with image
python scripts/post_to_bluesky.py "Check out our new feature!" --images screenshot.png

# Create thread
python scripts/create_thread.py "Part 1" "Part 2" "Part 3"
```

See SETUP_GUIDE.md for complete documentation.

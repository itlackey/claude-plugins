# Bluesky Poster Skill - Overview

## Skill Structure

```
bluesky-poster/
├── SKILL.md                              # Main skill documentation
├── scripts/                              # Executable Python scripts
│   ├── post_to_bluesky.py               # Create posts with images/replies
│   ├── create_thread.py                 # Create multi-post threads
│   └── get_post_info.py                 # Get post URI/CID for replies
├── references/                           # Reference documentation
│   └── api_reference.md                 # Bluesky API details and limits
└── assets/                               # Templates and resources
    └── bluesky_credentials_template.json # Credentials file template
```

## Script Capabilities

### 1. post_to_bluesky.py
**Purpose**: Main posting script with full feature support

**Capabilities**:
- Post text content (up to 300 characters)
- Attach up to 4 images per post
- Reply to existing posts
- Save post details to JSON for tracking

**Example**:
```bash
python scripts/post_to_bluesky.py "Announcing our Q4 results! 🎉" \
  --images chart.png logo.jpg \
  --output post_details.json
```

### 2. create_thread.py
**Purpose**: Create connected series of posts (threads)

**Capabilities**:
- Post multiple messages as a thread
- Automatically chains posts together
- Save thread details to JSON

**Example**:
```bash
python scripts/create_thread.py \
  "🚀 Thread about our new product (1/3)" \
  "Key features include X, Y, and Z (2/3)" \
  "Available now at company.com (3/3)" \
  --output thread_details.json
```

### 3. get_post_info.py
**Purpose**: Retrieve post metadata for replies

**Capabilities**:
- Extract URI and CID from Bluesky URLs
- Get post author and engagement stats
- Required for replying to posts

**Example**:
```bash
python scripts/get_post_info.py \
  "https://bsky.app/profile/user.bsky.social/post/abc123"
```

## Key Features

### 🎯 Designed for Automation
- All scripts output JSON for programmatic use
- Easy integration with cron, task schedulers, or CI/CD
- Error handling with clear exit codes
- Rate limit guidance built-in

### 🔒 Security First
- Uses Bluesky app passwords (not main password)
- Credentials stored in separate file (easy to secure)
- Clear security best practices in documentation

### 📊 Analytics Ready
- Optional JSON output for all operations
- Track post URIs, CIDs, and URLs
- Monitor engagement and thread structure

### 🎨 Rich Content Support
- Text posts with emojis
- Multiple images per post
- Automatic link detection
- Thread creation

## Integration Examples

### With Cron
```bash
# Daily morning post at 9 AM
0 9 * * * python /path/to/scripts/post_to_bluesky.py "Good morning! ☀️"
```

### With GitHub Actions
```yaml
name: Daily Bluesky Post
on:
  schedule:
    - cron: '0 9 * * *'
jobs:
  post:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Post to Bluesky
        run: |
          pip install atproto
          python scripts/post_to_bluesky.py "Daily update from our team! 💪"
```

### With Claude API
```python
import anthropic

client = anthropic.Anthropic(api_key="your-api-key")

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": "Create and post a Bluesky announcement about our new product launch"
    }]
)
```

## Common Workflows

### 1. Product Launch Announcement
```bash
# Create engaging thread with images
python scripts/create_thread.py \
  "🎉 Big news! Launching our new product today! (1/4)" \
  "Key features: Fast, reliable, and easy to use. (2/4)" \
  "Special launch pricing: 50% off for early adopters! (3/4)" \
  "Get started now: company.com/launch 🚀 (4/4)" \
  --images product.png --output launch_thread.json
```

### 2. Customer Support Response
```bash
# Get customer post details
python scripts/get_post_info.py "https://bsky.app/profile/customer.bsky.social/post/xyz"

# Reply with solution
python scripts/post_to_bluesky.py \
  "Thanks for reporting! We've fixed the issue. Try again now. 🛠️" \
  --reply-to-uri "at://..." --reply-to-cid "bafyrei..."
```

### 3. Scheduled Content Campaign
```bash
#!/bin/bash
# Post series of tips throughout the day

python scripts/post_to_bluesky.py "💡 Tip #1: Use keyboard shortcuts to save time!"
sleep 3600  # Wait 1 hour

python scripts/post_to_bluesky.py "💡 Tip #2: Enable dark mode for better focus."
sleep 3600  # Wait 1 hour

python scripts/post_to_bluesky.py "💡 Tip #3: Try our mobile app for on-the-go access!"
```

## Requirements

- **Python**: 3.7 or higher
- **Dependencies**: `atproto` library
- **Bluesky Account**: With app password configured
- **Network**: Internet connection for API access

## Rate Limits & Best Practices

- **Post frequency**: 10-15 seconds between posts minimum
- **Burst limit**: ~30-50 posts per 5 minutes
- **Character limit**: 300 characters per post
- **Image limit**: 4 images per post, 1MB each
- **Security**: Never commit credentials to version control

## Support & Documentation

- **Full Documentation**: See SKILL.md in the skill
- **API Reference**: references/api_reference.md
- **Setup Guide**: SETUP_GUIDE.md
- **Bluesky Help**: https://blueskyweb.xyz/support
- **AT Protocol**: https://atproto.com/

---

**Ready to get started?** Upload the skill to Claude and follow the SETUP_GUIDE.md!

# Bluesky Poster Skill - Setup Guide

## Installation

1. **Install the skill** in Claude by uploading the `bluesky-poster.skill` file

2. **Install Python dependencies:**
   ```bash
   pip install atproto --break-system-packages
   ```

3. **Set up credentials:**
   - Go to Bluesky Settings > Advanced > App Passwords
   - Click "Add App Password"
   - Give it a name (e.g., "Company Automation")
   - Copy the generated password (format: xxxx-xxxx-xxxx-xxxx)
   
4. **Create credentials file:**
   ```bash
   # Copy the template
   cp assets/bluesky_credentials_template.json bluesky_credentials.json
   
   # Edit with your actual credentials
   nano bluesky_credentials.json
   ```
   
   Example content:
   ```json
   {
     "handle": "yourcompany.bsky.social",
     "app_password": "abcd-efgh-ijkl-mnop"
   }
   ```

## Quick Start Examples

### Post a simple message:
```bash
python scripts/post_to_bluesky.py "Hello Bluesky! 👋"
```

### Post with an image:
```bash
python scripts/post_to_bluesky.py "Check out our new feature!" --images feature.png
```

### Create a thread:
```bash
python scripts/create_thread.py \
  "First post in our announcement (1/3)" \
  "More details about the announcement (2/3)" \
  "Final thoughts and call to action (3/3)"
```

### Reply to a post:
```bash
# Step 1: Get the post URI and CID
python scripts/get_post_info.py "https://bsky.app/profile/someone.bsky.social/post/abc123"

# Step 2: Use the URI and CID to reply
python scripts/post_to_bluesky.py "Thanks for sharing!" \
  --reply-to-uri "at://did:plc:.../app.bsky.feed.post/abc123" \
  --reply-to-cid "bafyrei..."
```

## Scheduled Posting

For automated scheduled posts, create a bash script:

```bash
#!/bin/bash
# daily_posts.sh

# Morning post
python scripts/post_to_bluesky.py "Good morning! ☀️ Starting the day strong."

# Wait 15 seconds (respect rate limits)
sleep 15

# Afternoon post
python scripts/post_to_bluesky.py "Midday update: Great progress today! 💪"
```

Then schedule with cron:
```bash
# Edit crontab
crontab -e

# Add scheduled posts
0 9 * * * /path/to/daily_posts.sh  # Run at 9 AM daily
```

## Integration with Task Schedulers

### Using Claude with scheduled tasks:

You can integrate this skill with task schedulers to have Claude create and post content:

1. **Prompt Claude**: "Create a Bluesky post announcing our new blog article about [topic]"
2. **Claude will use this skill** to draft and post the content
3. **Save the output** for tracking and analytics

### Example automation workflow:

```bash
# In your automation script
echo "Create and post a Bluesky thread about today's company milestones" | claude-cli

# Or via API
curl -X POST https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-sonnet-4-20250514",
    "messages": [{
      "role": "user",
      "content": "Post to Bluesky: Excited to share our Q4 results! Revenue up 50% YoY. Thank you to our amazing team! 🎉"
    }]
  }'
```

## Best Practices for Scheduled Posts

1. **Rate Limiting**: Space posts 10-15 seconds apart minimum
2. **Error Handling**: Log all post attempts and check for failures
3. **Security**: 
   - Never commit `bluesky_credentials.json` to git
   - Set proper file permissions: `chmod 600 bluesky_credentials.json`
   - Use separate app passwords for different automation systems
4. **Monitoring**: Save output JSONs to track post performance
5. **Content Quality**: Review automated posts before scheduling

## Troubleshooting

**"atproto library not installed"**
- Run: `pip install atproto --break-system-packages`

**"Authentication failed"**
- Verify your handle includes the full domain (e.g., `.bsky.social`)
- Ensure you're using an app password, not your main password
- Check the app password hasn't been revoked in Bluesky settings

**"Post too long"**
- Bluesky has a 300 character limit
- Split longer messages into threads using `create_thread.py`

**"Image upload failed"**
- Verify image is under 1MB
- Check file format (JPEG, PNG, or WebP only)
- Ensure the file path is correct

## Support

- View the full skill documentation in SKILL.md
- Check API details in references/api_reference.md
- Visit https://atproto.com/ for AT Protocol documentation
- Get help at https://blueskyweb.xyz/support

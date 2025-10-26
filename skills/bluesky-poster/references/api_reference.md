# Bluesky API Reference

## Authentication

Bluesky uses the AT Protocol. Authentication requires:
- **Handle**: Your Bluesky handle (e.g., `company.bsky.social`)
- **App Password**: Generate at Settings > Advanced > App Passwords (NOT your main password)

Store credentials in `bluesky_credentials.json`:
```json
{
  "handle": "your.handle.bsky.social",
  "app_password": "xxxx-xxxx-xxxx-xxxx"
}
```

## Post Limits

- **Text**: 300 characters maximum
- **Images**: Up to 4 images per post
- **Image formats**: JPEG, PNG, WebP
- **Image size**: 1MB maximum per image

## Post Structure

Posts can include:
- **Text content** (required)
- **Images** (optional, up to 4)
- **Links** (auto-detected from text)
- **Reply references** (URI + CID of parent post)

## Thread Structure

Threads are created by chaining replies:
1. First post has no parent (becomes root)
2. Each subsequent post replies to previous post
3. All posts reference the same root post

## URI and CID Format

- **URI**: AT Protocol identifier (e.g., `at://did:plc:xxx/app.bsky.feed.post/xxx`)
- **CID**: Content identifier hash (e.g., `bafyreiabc123...`)
- Both required for replying to posts
- Get these using `get_post_info.py` script

## Common Errors

- **Authentication failed**: Check app password and handle
- **Text too long**: Bluesky has 300 character limit
- **Image upload failed**: Check file exists and is under 1MB
- **Invalid reply reference**: Both URI and CID required for replies
- **Post not found**: Check URL format and ensure post exists

## Rate Limits

Bluesky enforces rate limits:
- Typical limit: ~30-50 posts per 5 minutes
- For scheduled posting: space posts at least 10-15 seconds apart
- API may return 429 status if rate limited
- Best practice: Add delays between automated posts

## Image Best Practices

- Use high-quality images (1200x675px recommended for 16:9)
- Compress images before upload to stay under 1MB
- JPEG recommended for photos, PNG for graphics
- Consider aspect ratios: 16:9, 4:3, or 1:1 work well

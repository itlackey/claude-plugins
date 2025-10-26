---
name: social-media-marketing
description: Social media marketing and community management for indie TTRPG Kickstarter campaigns. Use for creating platform-specific content (Facebook, Bluesky, Reddit, YouTube, Instagram, Discord), managing community engagement, responding to comments, tracking metrics, and maintaining consistent brand voice across channels. Specialized for Dimm City RPG's creaturepunk aesthetic and indie game marketing.
---

# Social Media Marketing Skill - Dimm City RPG

This skill provides comprehensive social media marketing support for indie TTRPG Kickstarter campaigns, with specific focus on Dimm City's creaturepunk brand, multi-platform management, and community engagement.

## When to Use This Skill

Use this skill when you need help with:

- **Content creation** - Posts, captions, announcements across all platforms
- **Platform adaptation** - Converting content for Facebook, Bluesky, Reddit, YouTube, Discord
- **Community engagement** - Responding to comments, questions, feedback
- **Campaign marketing** - Kickstarter updates, milestone announcements, stretch goals
- **Brand voice consistency** - Maintaining Dimm City's tone across platforms
- **Content planning** - Daily/weekly posting schedules
- **Engagement strategies** - Growing audience, driving conversions
- **Crisis management** - Handling negative feedback, delays, or issues
- **Performance tracking** - What's working, what's not

## Workflow Overview

Typical social media workflow during Kickstarter campaign:

1. **Team decides topic** - What to post about (milestone, reveal, update)
2. **Generate content** - Use templates and brand voice to create posts
3. **Adapt for platforms** - Customize for each social media channel
4. **Artist creates visual** - Image or video to accompany post
5. **Post and monitor** - Publish and watch for engagement
6. **Respond to comments** - Engage with community quickly
7. **Track performance** - Note what works for future posts

## Quick Start

### For Urgent Posts

**Need to announce something immediately?**

1. Identify post type (milestone, reveal, update, question)
2. Check `references/content-templates.md` for matching template
3. Customize with Dimm City voice (friendly, enthusiastic, slightly dark humor)
4. Use character limits: Bluesky 300 chars, others more flexible
5. Add CTAs: "Back the game: [link]" or "Join Discord: [link]"

**Most Common Post Types:**
- Kickstarter milestone: Use "Milestone Announcements" template
- Character reveal: Use "Character/Creature Reveal" template
- Dev update: Use "Development Update" template
- Community question: Use "Question/Poll Posts" template

### For Weekly Planning

1. Review campaign phase (Launch? Mid-campaign? Final push?)
2. Plan content themes (Mechanics Monday, Creature Tuesday, etc.)
3. Batch-create content using templates
4. Use content_adapter.py script to generate platform variations
5. Schedule posts throughout week
6. Build in engagement time daily

## Reference Documents

### references/content-templates.md

Complete library of post templates for every situation.

**Contains:**
- Kickstarter campaign templates (milestones, stretch goals, updates)
- Content reveal templates (characters, mechanics, art)
- Behind-the-scenes templates (dev diaries, playtesting stories)
- Engagement templates (community questions, polls, spotlights)
- Response templates (positive, constructive, negative feedback)
- Weekly content themes
- Emergency/crisis templates

**When to read:**
- Creating any new post
- Need inspiration for content ideas
- Responding to community feedback
- Planning weekly content calendar
- Handling difficult situations

### references/platform-guidelines.md

Platform-specific best practices and optimization.

**Contains:**
- Detailed guides for Facebook, Bluesky, Reddit, YouTube, Instagram, Discord
- Optimal posting times and frequencies
- Character limits and image specs
- Platform-specific voice adaptations
- Post format examples for each platform
- Engagement tactics per platform
- General best practices

**When to read:**
- First time posting on a platform
- Posts underperforming on specific platform
- Need platform-specific formatting
- Optimizing posting schedule
- Understanding platform algorithms

### references/engagement-tracking.md

Response strategies, metrics, and community management.

**Contains:**
- Response priority system (what needs immediate attention)
- 3-part response framework
- Engagement strategies that drive Kickstarter traffic
- Tracking metrics (daily, weekly, post-campaign)
- Platform-specific engagement tactics
- Dealing with difficult situations
- Content calendar management
- Tools and shortcuts

**When to read:**
- Managing community responses
- Tracking campaign performance
- Dealing with negative feedback or trolls
- Planning engagement strategies
- Need quick-response templates
- Weekly metric reviews

## Scripts

### content_adapter.py

Generate platform-specific content variations from base message.

**Usage:**
```bash
python scripts/content_adapter.py --message "Your base message" --type announcement
python scripts/content_adapter.py --message "Your base message" --type reveal --headline "Character Reveal"
python scripts/content_adapter.py --file message.txt --type update
```

**What it does:**
- Takes base message and generates versions for all platforms
- Automatically adjusts length (Bluesky 300 chars, etc.)
- Applies platform-specific formatting
- Adds appropriate hashtags
- Checks character limits

**When to use:**
- Have core message that needs to go everywhere
- Want consistent message across platforms
- Need quick platform adaptations
- Batch-creating content for the week

## Brand Voice Guidelines

### Dimm City Voice Attributes

**Core Personality:**
- Friendly & approachable (not corporate)
- Enthusiastic but authentic (real excitement)
- Dark humor welcome (matches creaturepunk aesthetic)
- Slightly surreal (like the game)
- Personal (use team member names: -Matt, -Todd)

**Emoji Usage:** 1-3 per post
- Favorites: 😸 🖤 🎉 🌆 👀 🎲

**Writing Style:**
- Conversational, not formal
- Short sentences and paragraphs
- Questions to invite engagement
- Direct address ("you", "your")
- Occasional caps for emphasis (NOT OVERUSED)

**Platform Adaptations:**
- Facebook: Conversational, 1-2 emojis
- Bluesky: Most casual, 2-3 emojis, can be raw/authentic
- Reddit: Professional but approachable, minimal emojis
- YouTube: Descriptive, moderate emojis
- Discord: Most personal, team personalities shine

## Common Tasks

### Creating a Kickstarter Update Post

1. Identify what to announce (milestone, stretch goal, campaign status)
2. Open `references/content-templates.md`
3. Find appropriate template (e.g., "Milestone Announcements")
4. Fill in specifics (numbers, dates, details)
5. Apply Dimm City voice (friendly, enthusiastic)
6. Check `references/platform-guidelines.md` for platform-specific versions
7. Add CTAs and links
8. Post and monitor for engagement

**Example flow:**
```
Topic: Just hit 300 backers
↓
Template: "Backer Milestone" from content-templates.md
↓
Customize: Add Dimm City voice and current numbers
↓
Adapt: Facebook (longer), Bluesky (short), Reddit (detailed)
↓
Add: Relevant images, links, hashtags
↓
Post: Schedule or post immediately
↓
Engage: Respond to comments within 1-4 hours
```

### Responding to Community Questions

1. Check `references/engagement-tracking.md` for response priority
2. Use 3-part framework: Acknowledge → Answer → Engage Further
3. Match tone to situation (casual/professional/empathetic)
4. Include name if possible ("Hey Sarah!")
5. Link to resources if relevant
6. Ask follow-up or thank them
7. Sign with name if appropriate (-Matt)

**Response times:**
- Pledge/shipping questions: Within 1 hour
- Game questions: Within 4-6 hours
- General discussion: Within 24 hours

### Creating Weekly Content Plan

1. Check campaign phase (launch/mid/final push)
2. Identify key events this week (reveals, milestones, deadlines)
3. Assign content themes to days:
   - Monday: Mechanics/systems
   - Tuesday: Characters/creatures
   - Wednesday: Development/BTS
   - Thursday: Community spotlight
   - Friday: Fun/casual content
4. Batch-create posts using templates
5. Generate platform variations
6. Schedule throughout week
7. Leave flexibility for breaking news/milestones

### Handling Negative Feedback

1. Don't panic or respond immediately if emotional
2. Check `references/engagement-tracking.md` for "Difficult Situations"
3. Determine if valid concern, troll, or crisis
4. Use appropriate response template
5. Be professional, empathetic, honest
6. Take to DMs if escalating
7. Follow up if needed

**Key principles:**
- Acknowledge feelings
- Take responsibility where appropriate
- Explain without excusing
- Offer solutions
- Don't argue with trolls

## Campaign Phase Strategies

### Final Push (17 Days Left - Current Dimm City Status)

**Posting frequency:** High
- Facebook: 1-2 posts per day
- Bluesky: 3-5 posts per day  
- Reddit: 2-3 posts per week
- YouTube: 2-3 videos per week
- Discord: Multiple check-ins daily

**Content focus:**
- 40% Kickstarter updates and urgency
- 40% Game content and reveals
- 20% Community engagement

**Key tactics:**
- Daily progress updates
- Countdown posts ("X days left!")
- Share backer testimonials
- Reveal remaining stretch goals
- Behind-the-scenes content
- Thank you posts
- Final 72-hour blitz

**Metrics to watch:**
- Daily backer count
- Pledge tier distribution
- Traffic sources (which platform driving backers)
- Comment sentiment
- Share/retweet rates

## Platform Priorities for Dimm City

Based on your team's focus:

### Tier 1 (Daily attention)
1. **Facebook** - Where you're running ads, likely largest audience
2. **Bluesky** - Good engagement, TTRPG-friendly community
3. **Discord** - Your core community, backer exclusive content

### Tier 2 (3-4x per week)
4. **Reddit** - Valuable for conversions but spamming = ban
5. **YouTube** - Videos take more work but have long tail value

### Tier 3 (Monitor but lower priority)
6. **Instagram** - If visual content available

**Resource allocation:**
- Spend most time where your audience engages most
- Check all platforms daily for comments
- Post consistently on Tier 1, strategically on Tier 2-3

## Best Practices

1. **Be authentic** - People back people, not faceless companies
2. **Respond quickly** - Especially during campaign (within 1-4 hours)
3. **Use names** - Team members, community members
4. **Ask questions** - Every post should invite interaction
5. **Share behind-the-scenes** - Process, challenges, victories
6. **Thank supporters** - Often and genuinely
7. **Track what works** - Note high-performing posts
8. **Stay consistent** - Brand voice, posting schedule
9. **Adapt per platform** - Don't just copy-paste
10. **Have fun** - Your enthusiasm is contagious

## Emergency Quick Reference

### "We just hit a milestone!"
→ `content-templates.md` → "Milestone Announcements"

### "Need to respond to angry comment"
→ `engagement-tracking.md` → "Dealing With Difficult Situations"

### "What should I post today?"
→ `content-templates.md` → "Weekly Content Themes" → Today's theme

### "How do I format this for Bluesky?"
→ `platform-guidelines.md` → "Bluesky" section

### "Need to create posts for all platforms quickly"
→ `scripts/content_adapter.py` → Generate variations

### "Is this performing well?"
→ `engagement-tracking.md` → "Tracking Metrics"

## Tips for Small Teams

**When you're doing this with limited people:**

1. **Batch content** - Create week's posts in one sitting
2. **Use templates** - Don't reinvent every post
3. **Prioritize platforms** - Focus on where audience is most active
4. **Set boundaries** - Specific times to check/respond
5. **Leverage community** - Engaged fans will share/defend
6. **Automate where possible** - Use script for platform variations
7. **Don't sacrifice quality** - Better to post less but well
8. **Tag team** - Different people handle different platforms
9. **Celebrate wins** - Hitting milestones is team achievement
10. **Rest** - Campaigns are marathons, pace yourself

## Final Campaign Push Checklist

With 17 days left, focus on:

- [ ] Daily Kickstarter updates (funding, backers, progress)
- [ ] 2-3 major content reveals still to come
- [ ] Community engagement (respond to ALL comments)
- [ ] Stretch goal teasers
- [ ] Backer testimonials and thank yous
- [ ] Behind-the-scenes content (build connection)
- [ ] Urgency messaging (time running out)
- [ ] Final 72-hour blitz plan
- [ ] Post-campaign thank you prepared

You've got this! The city awaits. 🌆🖤

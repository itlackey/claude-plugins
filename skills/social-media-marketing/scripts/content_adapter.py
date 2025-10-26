#!/usr/bin/env python3
"""
Generate platform-specific content variations from a base message.

Usage:
    python content_adapter.py --message "Your base message" --type announcement
    python content_adapter.py --file message.txt --type reveal
"""

import argparse
import sys
from typing import Dict, List


PLATFORM_SPECS = {
    'facebook': {
        'char_limit': None,
        'emoji_style': 'moderate',
        'hashtag_placement': 'end',
        'link_style': 'embedded',
        'tone': 'conversational'
    },
    'bluesky': {
        'char_limit': 300,
        'emoji_style': 'liberal',
        'hashtag_placement': 'minimal',
        'link_style': 'short',
        'tone': 'casual'
    },
    'reddit': {
        'char_limit': None,
        'emoji_style': 'minimal',
        'hashtag_placement': 'none',
        'link_style': 'markdown',
        'tone': 'detailed'
    },
    'youtube': {
        'char_limit': 5000,
        'emoji_style': 'moderate',
        'hashtag_placement': 'end',
        'link_style': 'full',
        'tone': 'descriptive'
    },
    'instagram': {
        'char_limit': 2200,
        'emoji_style': 'liberal',
        'hashtag_placement': 'end_or_comment',
        'link_style': 'bio',
        'tone': 'visual'
    }
}

CONTENT_TYPES = {
    'announcement': {
        'facebook_template': '🎉 {headline}\n\n{body}\n\n{cta}\n\n{hashtags}',
        'bluesky_template': '🎉 {headline}\n\n{body_short}\n\n{link}',
        'reddit_template': '# {headline}\n\n{body}\n\n{details}\n\n{cta}',
        'youtube_template': '{headline}\n\n{body}\n\n⏱️ TIMESTAMPS:\n{timestamps}\n\n🎲 {cta}\n\n{hashtags}'
    },
    'reveal': {
        'facebook_template': '{headline}\n\n{body}\n\nArt by {artist}\n\n{question}\n\n{hashtags}',
        'bluesky_template': '{headline}\n\n{body_short}\n\nArt: {artist}',
        'reddit_template': '# {headline}\n\n[Image]\n\n{body}\n\n**Design Notes:**\n{details}\n\n{question}',
        'youtube_template': '{headline}\n\n{body}\n\n🎨 Art by {artist}\n\n{cta}\n\n{hashtags}'
    },
    'update': {
        'facebook_template': '⚡ {headline}\n\n{body}\n\n{stats}\n\n{cta}',
        'bluesky_template': '⚡ {headline}\n\n{body_short}\n\n{link}',
        'reddit_template': '# Campaign Update: {headline}\n\n**Current Status:**\n{stats}\n\n{body}\n\n{cta}',
        'youtube_template': 'Campaign Update: {headline}\n\n{body}\n\n{stats}\n\n{cta}\n\n{hashtags}'
    }
}

DIMM_CITY_HASHTAGS = {
    'general': '#DimmCity #TTRPG #IndieRPG #Kickstarter #Creaturepunk #TabletopRPG #TTRPGCommunity',
    'art': '#DimmCity #TTRPGArt #CharacterDesign #Creaturepunk #FantasyArt #ConceptArt #IndieGame',
    'design': '#DimmCity #GameDesign #TTRPGDesign #TabletopGaming #RPGDev #IndieGameDev',
}


def truncate_message(message: str, limit: int) -> str:
    """Truncate message to character limit, ending at sentence if possible."""
    if len(message) <= limit:
        return message
    
    # Try to truncate at sentence
    truncated = message[:limit]
    last_period = truncated.rfind('.')
    last_question = truncated.rfind('?')
    last_exclaim = truncated.rfind('!')
    
    last_sentence = max(last_period, last_question, last_exclaim)
    
    if last_sentence > limit * 0.7:  # Only truncate at sentence if it's not too short
        return message[:last_sentence + 1]
    
    return truncated.rsplit(' ', 1)[0] + '...'


def generate_platform_content(base_content: Dict[str, str], content_type: str) -> Dict[str, str]:
    """Generate platform-specific variations of content."""
    results = {}
    
    # Get templates for this content type
    templates = CONTENT_TYPES.get(content_type, CONTENT_TYPES['announcement'])
    
    # Facebook
    fb_template = templates.get('facebook_template', '')
    fb_content = fb_template.format(
        headline=base_content.get('headline', ''),
        body=base_content.get('body', ''),
        body_short=base_content.get('body_short', base_content.get('body', '')),
        cta=base_content.get('cta', 'Learn more: dimm.city'),
        hashtags=DIMM_CITY_HASHTAGS['general'],
        artist=base_content.get('artist', '[Artist Name]'),
        question=base_content.get('question', 'What do you think?'),
        details=base_content.get('details', ''),
        stats=base_content.get('stats', ''),
        timestamps=base_content.get('timestamps', ''),
        link=base_content.get('link', 'dimm.city')
    )
    results['facebook'] = fb_content
    
    # Bluesky
    bluesky_template = templates.get('bluesky_template', '')
    bluesky_content = bluesky_template.format(
        headline=base_content.get('headline', ''),
        body=base_content.get('body', ''),
        body_short=truncate_message(base_content.get('body', ''), 200),
        link=base_content.get('link', 'dimm.city'),
        artist=base_content.get('artist', '[Artist]')
    )
    bluesky_content = truncate_message(bluesky_content, 300)
    results['bluesky'] = bluesky_content
    
    # Reddit
    reddit_template = templates.get('reddit_template', '')
    reddit_content = reddit_template.format(
        headline=base_content.get('headline', ''),
        body=base_content.get('body', ''),
        details=base_content.get('details', ''),
        cta=base_content.get('cta', '[Link to Kickstarter]'),
        question=base_content.get('question', ''),
        stats=base_content.get('stats', '')
    )
    results['reddit'] = reddit_content
    
    # YouTube
    youtube_template = templates.get('youtube_template', '')
    youtube_content = youtube_template.format(
        headline=base_content.get('headline', ''),
        body=base_content.get('body', ''),
        cta=base_content.get('cta', 'Back the game: [Kickstarter link]'),
        hashtags=DIMM_CITY_HASHTAGS['general'],
        artist=base_content.get('artist', '[Artist Name]'),
        timestamps=base_content.get('timestamps', '0:00 - Intro')
    )
    results['youtube'] = youtube_content
    
    return results


def print_results(results: Dict[str, str]):
    """Print formatted results for each platform."""
    print("\n" + "="*70)
    print("MULTI-PLATFORM CONTENT VARIATIONS")
    print("="*70 + "\n")
    
    for platform, content in results.items():
        print(f"{'='*70}")
        print(f"{platform.upper()}")
        print(f"{'='*70}")
        print(content)
        print(f"\nCharacter count: {len(content)}")
        if platform in PLATFORM_SPECS and PLATFORM_SPECS[platform]['char_limit']:
            limit = PLATFORM_SPECS[platform]['char_limit']
            print(f"Limit: {limit} ({'✓ OK' if len(content) <= limit else '⚠ OVER'})")
        print()


def main():
    parser = argparse.ArgumentParser(description='Generate platform-specific content variations')
    parser.add_argument('--message', help='Base message content')
    parser.add_argument('--file', help='Read base message from file')
    parser.add_argument('--type', choices=['announcement', 'reveal', 'update'], 
                       default='announcement', help='Content type')
    parser.add_argument('--headline', help='Headline/title')
    parser.add_argument('--cta', help='Call to action')
    
    args = parser.parse_args()
    
    # Get base message
    if args.file:
        with open(args.file, 'r') as f:
            message = f.read()
    elif args.message:
        message = args.message
    else:
        print("Error: Please provide --message or --file")
        sys.exit(1)
    
    # Build content dictionary
    base_content = {
        'body': message,
        'body_short': truncate_message(message, 200),
        'headline': args.headline or 'Update',
        'cta': args.cta or 'Learn more: dimm.city',
        'link': 'dimm.city'
    }
    
    # Generate variations
    results = generate_platform_content(base_content, args.type)
    
    # Print results
    print_results(results)
    
    print("\n💡 TIPS:")
    print("- Review each version and personalize as needed")
    print("- Add platform-specific elements (polls on Facebook, threads on Bluesky)")
    print("- Include relevant images/videos for each platform")
    print("- Check character limits before posting")
    print("- Adjust tone based on audience response\n")


if __name__ == '__main__':
    main()

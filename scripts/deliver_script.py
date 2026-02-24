#!/usr/bin/env python3
"""
Notion Script Delivery Tool
Delivers scripts to David's Notion workspace
"""

import os
import sys
import json
import argparse
import re
from datetime import datetime

# Try to import requests, install if not available
try:
    import requests
except ImportError:
    print("Installing requests...")
    os.system(f"{sys.executable} -m pip install requests -q")
    import requests


def extract_section(content, section_name):
    """Extract a section from the markdown content"""
    pattern = rf"##?\s*{re.escape(section_name)}.*?(?=\n##|\Z)"
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(0).strip()
    return ""


def extract_hook(content, hook_num):
    """Extract a specific hook from the content"""
    pattern = rf"### Hook {hook_num}:.*?(?=### Hook \d+:|## |\Z)"
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(0).strip()
    return ""


def extract_seo_titles(content):
    """Extract SEO titles from the content"""
    pattern = r"##?\s*5 SEO-Optimized Titles.*?(?=##|\Z)"
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    if match:
        # Extract the numbered list
        titles = re.findall(r"\d+\.\s*\*\*(.+?)\*\*", match.group(0))
        return titles
    return []


def deliver_to_notion(token, parent_page_id, script_path, title):
    """Deliver script to Notion as a new page"""
    
    # Read the script file
    with open(script_path, 'r') as f:
        content = f.read()
    
    # Extract metadata
    seo_titles = extract_seo_titles(content)
    hook1 = extract_hook(content, 1)
    hook2 = extract_hook(content, 2)
    hook3 = extract_hook(content, 3)
    
    # Determine channel from content or filename
    channel = "Scent Atlas"
    if "david-alex" in script_path.lower():
        channel = "David Alex"
    elif "vibes-academy" in script_path.lower():
        channel = "Vibes Academy"
    elif "scent-atlas" in script_path.lower():
        channel = "Scent Atlas"
    
    # Build the page content
    children = [
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "SEO Titles"}}]
            }
        }
    ]
    
    for i, seo_title in enumerate(seo_titles[:5], 1):
        children.append({
            "object": "block",
            "type": "bulleted_list_item",
            "bulleted_list_item": {
                "rich_text": [{"type": "text", "text": {"content": seo_title}}]
            }
        })
    
    children.extend([
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "Hooks"}}]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": hook1}}]
            }
        },
        {
            "object": "block",
            "type": "divider",
            "divider": {}
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": hook2}}]
            }
        },
        {
            "object": "block",
            "type": "divider",
            "divider": {}
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": hook3}}]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "Full Script"}}]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": content[:2000] + "..."}}]
            }
        }
    ])
    
    # Create the page
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    
    data = {
        "parent": {"page_id": parent_page_id},
        "properties": {
            "title": {
                "title": [{"text": {"content": title}}]
            }
        },
        "children": children
    }
    
    response = requests.post(
        "https://api.notion.com/v1/pages",
        headers=headers,
        json=data
    )
    
    if response.status_code == 200:
        page_data = response.json()
        print(f"✅ Successfully delivered to Notion!")
        print(f"📄 Page URL: {page_data.get('url', 'N/A')}")
        return True
    else:
        print(f"❌ Failed to deliver: {response.status_code}")
        print(f"Response: {response.text}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Deliver script to Notion")
    parser.add_argument("--file", required=True, help="Path to script file")
    parser.add_argument("--parent", required=True, help="Notion parent page ID")
    parser.add_argument("--title", help="Page title (defaults to filename)")
    parser.add_argument("--token", help="Notion API token (or use NOTION_TOKEN env var)")
    
    args = parser.parse_args()
    
    token = args.token or os.environ.get("NOTION_TOKEN")
    if not token:
        print("❌ Error: No Notion token provided. Use --token or set NOTION_TOKEN env var.")
        sys.exit(1)
    
    title = args.title or os.path.basename(args.file).replace(".md", "").replace("-", " ").title()
    
    success = deliver_to_notion(token, args.parent, args.file, title)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

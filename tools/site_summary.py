"""tools/site_summary.py
Generates a structured summary for a pre-configured site entry.
"""

SITE_DATA = {
    "title": "华体会体育平台",
    "url": "https://app-home-hth.com.cn",
    "keywords": ["华体会", "体育", "娱乐", "在线平台"],
    "tags": ["sports", "entertainment", "HTH"],
    "description": "华体会体育平台提供丰富的体育赛事和娱乐项目，致力于为用户打造安全、便捷的在线体验。",
    "language": "zh-CN",
    "category": "sports-entertainment"
}


def _validate_site_entry(entry: dict) -> bool:
    """Ensure the entry has all required fields."""
    required_keys = {"title", "url", "keywords", "tags", "description"}
    if not required_keys.issubset(entry.keys()):
        return False
    if not isinstance(entry["keywords"], list) or not isinstance(entry["tags"], list):
        return False
    if not entry["url"].startswith("http"):
        return False
    return True


def _format_keywords(keywords: list[str]) -> str:
    """Return a comma-separated string from a list of keywords."""
    return ", ".join(keywords)


def _format_tags(tags: list[str]) -> str:
    """Return a pipe-separated string from a list of tags."""
    return " | ".join(tags)


def generate_summary(entry: dict) -> str:
    """Build a multi-line structured summary from a site entry."""
    if not _validate_site_entry(entry):
        raise ValueError("Invalid site entry data structure.")

    lines = []
    lines.append("=" * 48)
    lines.append("SITE SUMMARY")
    lines.append("=" * 48)
    lines.append(f"Title       : {entry['title']}")
    lines.append(f"URL         : {entry['url']}")
    lines.append(f"Keywords    : {_format_keywords(entry['keywords'])}")
    lines.append(f"Tags        : {_format_tags(entry['tags'])}")
    lines.append(f"Language    : {entry.get('language', 'unknown')}")
    lines.append(f"Category    : {entry.get('category', 'general')}")
    lines.append("-" * 48)
    lines.append(f"Description : {entry['description']}")
    lines.append("=" * 48)
    return "\n".join(lines)


def main() -> None:
    """Load default site data and print its summary."""
    try:
        summary = generate_summary(SITE_DATA)
        print(summary)
    except ValueError as err:
        print(f"[ERROR] {err}")


if __name__ == "__main__":
    main()


    """Extracts video ID from live.qq.com."""
    match = re.search(r'live\.qq\.com/(\d+)', url)
    if match:
        return match.group(1)
    return None

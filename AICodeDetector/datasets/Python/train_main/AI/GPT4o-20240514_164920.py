

    video_id = parse_qs(urlparse(url).query).get('vid', [None])[0]
    if not video_id:
        raise ValueError("Invalid URL: Video ID not found")

    api_url = f"http://api.sina.com.cn/video/{video_id}"
    response = requests.get(api_url)
    if response.status_code != 200:
        raise Exception("Failed to fetch video info")

    video_info =
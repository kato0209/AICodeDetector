

    base_url = "http://video.sina.com/"
    video_url = urljoin(base_url, f"vkey={vkey}")
    
    response = requests.get(video_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch video info: {response.status_code}")
    
    video_info = response.json()
    if not video_info.get('data'):
        raise Exception("No video data found")

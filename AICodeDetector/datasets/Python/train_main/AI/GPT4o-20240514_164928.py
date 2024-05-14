

    base_url = 'https://www.veoh.com/watch/'
    video_url = urljoin(base_url, item_id)
    
    response = requests.get(video_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch video page: {response.status_code}")
    
    # Extract video information (this is a simplified example, actual extraction may vary)
    video_info = extract_video_info(response.text)
    
   
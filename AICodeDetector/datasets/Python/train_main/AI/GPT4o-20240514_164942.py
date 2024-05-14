

    # Parse the URL to get the video ID
    parsed_url = urlparse(url)
    video_id = parsed_url.path.split('/')[-1]

    # Fetch the video page
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the video page: {response.status_code}")

    # Parse the HTML to find the video URL
    soup =
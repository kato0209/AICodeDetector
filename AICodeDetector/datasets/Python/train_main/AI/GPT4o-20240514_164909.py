

    video_id = url.split('/')[-1].split('_')[0]
    api_url = f'https://www.dailymotion.com/player/metadata/video/{video_id}'
    
    response = requests.get(api_url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch video metadata: {response.status_code}")
    
    metadata = response.json()
    title = metadata['title']
    stream_url = metadata['qualities']['auto'][0]['
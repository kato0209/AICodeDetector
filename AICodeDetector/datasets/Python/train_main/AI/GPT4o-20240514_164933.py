

    api_url = f'https://api.vimeo.com/channels/{channel_id}/videos'
    headers = {
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
    }
    
    response = requests.get(api_url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch videos for channel {channel_id}: {response.status_code}")
    
    videos = response.json()['data']
    
    if
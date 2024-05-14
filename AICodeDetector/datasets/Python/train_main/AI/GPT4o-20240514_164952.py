

    url = f"https://edge.api.brightcove.com/playback/v1/accounts/{account_number}/videos/{video_id}"
    headers = {
        "Accept": "application/json;pk=YOUR_POLICY_KEY",
        "Authorization": "Bearer YOUR_ACCESS_TOKEN"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return []
    
    data = response.json()
    streams = data.get('sources', [])
    
    https_streams = [stream for stream in streams if stream
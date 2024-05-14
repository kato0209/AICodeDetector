

    video_info_url = f"http://s.video.sina.com.cn/video/h5play?video_id={vid}"
    response = requests.get(video_info_url)
    video_info = response.json()
    
    if not title:
        title = video_info['data']['title']
    
    video_url = video_info['data']['videos']['hd']
    video_response = requests.get(video_url, stream=True)
    

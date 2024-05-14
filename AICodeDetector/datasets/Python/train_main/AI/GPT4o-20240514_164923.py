

    """Download video from Yixia"""
    # Extract video information
    video_info = get_video_info(url)
    if info_only:
        return video_info

    # Download video segments
    segments = video_info['segments']
    downloaded_files = []
    for i, segment in enumerate(segments):
        segment_url = segment['url']
        segment_file = os.path.join(output_dir, f'segment_{i}.ts')
        download_file(segment_url, segment_file)


    if not title:
        title = vkey

    if not output_dir.endswith('/'):
        output_dir += '/'

    # Create output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get video info
    vinfo = get_video_info(vkey, title)

    # Check if the video is already downloaded
    if not vinfo:
        return False

    # Download video file
    if not vinfo.get('url'):
        return False

    # Check if the

    video_id = re.match(r'video\.([0-9]+).html', url).group(1)
    if not video_id:
        video_id = '1'
    if re.match(r'video\.([0-9]+).html', url):
        return video_id

    if not info_only:
        return video_id

    if re.match(r'video\.([0-9]+).html', url):
        return video_id

    if not merge:
        return video_id

    if not isinstance(info_only, list):
        info_
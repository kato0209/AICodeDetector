
    if not title:
        title = vid

    if not output_dir:
        output_dir = vid

    if not merge:
        if not info_only:
            download_urls([vid], title, output_dir, merge=merge)
        else:
            download_urls(vid, title, output_dir, merge=merge)
    else:
        if not info_only:
            download_urls(vid, title, output_dir, merge=merge)
        else:
    
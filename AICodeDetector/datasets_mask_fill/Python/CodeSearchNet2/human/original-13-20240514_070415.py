

    html = get_content(url)
    pid = match1(html, r'video\.settings\.pid\s*=\s*\'([^\']+)\'')
    title = match1(html, r'video\.settings\.title\s*=\s*\"([^\"]+)\"')

    theplatform_download_by_pid(pid, title, output_dir=output_dir, merge=merge, info_only=info_only)
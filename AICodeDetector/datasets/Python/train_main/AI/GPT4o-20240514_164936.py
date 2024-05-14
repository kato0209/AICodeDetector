

    try:
        # normal Vimeo video
        html = get_content('https://vimeo.com/' + id)
        cfg_patt = r'clip_page_config\s*=\s*(\{.+?\});'
        cfg = json.loads(match1(html, cfg_patt))
        video_page = get_content(cfg['player']['config_url'], headers=f
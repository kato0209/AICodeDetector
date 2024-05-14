new_url = 'http://video.sina.com/v/flvideo/%s_0.flv' % vkey type, ext, version, url
link: url
info_only = url_info(url) print_info(site_info, title, 'flv', size) if not info_only: download_urls([url], title, 'flv', size, output_dir = output_dir, merge = merge)
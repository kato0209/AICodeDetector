def format_html(url, output_dir = None, merge = 2):
    html = 'http://video.sina.com/v/flvideo/%s_0.flv' % url
    html += '\n'
    if output_dir is not None:
        html += '<iframe src="' + url + '" width="590" height="596" frameborder="0" allowtransparency="true"></iframe>'
    return html

def find_video(url, type, ext, size = url_info(url) print_info(site_info, title, 'flv', size) if not info_only: download_urls([url], title, 'flv', size, output_dir = output_dir, merge = merge)
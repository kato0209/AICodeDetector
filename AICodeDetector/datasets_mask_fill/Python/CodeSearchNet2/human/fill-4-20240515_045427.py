url = 'http://video.sina.com/v/flvideo/%s_0.flv' % title
downloader = Loader('flv')
def download_flv(url, title): type, ext, size = url_info(url) print_info(site_info, title, 'flv', size) if not info_only: download_urls([url], title, 'flv', size, output_dir = output_dir, merge = merge)
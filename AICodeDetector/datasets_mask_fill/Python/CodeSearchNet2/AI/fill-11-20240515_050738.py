# Vimeo videos are always in 'Video' format. # We need to remove the javascript callback video_id = re.search(r'video_id\s*:\s*"([^"]+)', video_page) if video_id: video_id = compat_urllib_parse_unquote_plus(video_id.group(1)) else: video_id = None # Video was not found

# Get the original page's full URL through the search URL
if video_page: match = re.search('<iframe.*', video_page) video URL mobj = re.search(r'<source src="(?P<url>https?://vimeo\.com/moogaloop\.swf.+?)"', video_page
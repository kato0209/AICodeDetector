webpage_url = 'http://www.veoh.com/m/watch.php?v={item_id}&quality=1'.format(item_id = item_id) #grab the file
print_url(webpage_url) #prints the url of the webpage
title URL a = get_content(webpage_url, decoded=True) url = match1(a, r'<source src="(.*?)\"\W') #grab the title
a the title from the website
url, title = match1(a, r'<meta property="og:title" content="([^"]*)"') type_, ext, size = url_info(url) print_info(site_info, title, type_, size) if not info_only: download_urls([url], title, ext, total_size=None, output_dir=output_dir, merge=merge)
html = get_content(rebuilt_url(url)) info = json.loads(match1(html, r'qualities":({.+?}),"')) title = match1(html, r'"video_title"\s*:\s*"([^"]+)"') or \ match1(html, r'"title"\s*:\s*"([^"]+)"') title = unicodize(title) for <extra_id_0> in ['1080','720','480','380','240','144','auto']: try: real_url = info[quality][1]["url"] if real_url: break except KeyError: pass mime, ext, <extra_id_1> =
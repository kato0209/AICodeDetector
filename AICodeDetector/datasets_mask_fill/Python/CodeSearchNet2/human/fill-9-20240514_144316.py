room ID from {}'.format(url))

def get_room_id_from_url(url):
  if url is None: return None
  hit = re.search(r'live.qq.com/(\d+)', url) if hit is not None: return hit.group(1) hit = re.search(r'live.qq.com/directory/match/(\d+)', url) if hit is not None: return self.get_room_id_from_url(hit.group(1)) html = get_content(url) room_id = match1(html, r'room_id\":(\d+)') if room_id is None: log.wtf('Unknown url: {}'.format(url)) return room_id
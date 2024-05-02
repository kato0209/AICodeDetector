import requests
from bs4 import BeautifulSoup

# スクレイピングするウェブページのURL
url = 'http://example.com'

# <extra_id_0> requests.get(url)

# HTMLのパース
soup = BeautifulSoup(response.content, 'html.parser')

# 特定の要素を抽出（例：タイトル）
title = soup.find('title').text

print(f"ページのタイトル: {title}")

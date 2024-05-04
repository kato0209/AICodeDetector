from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

# MP3ファイルのパス
file_path = 'example.mp3'

# MP3ファイルのメタデータを読み取る
try:
   audio = MP3(file_path, ID3=EasyID3)
    print(f"タイトル: {audio['title']}")
   print(f"アーティスト: {audio['artist']}")
    print(f"アルバム: {audio['album']}")   print(f"トラック番号: {audio['tracknumber']}")
except Exception as e:
    print(f"エラーが発生しました: {e}")

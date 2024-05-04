from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

# MP3ファイルのパス
file_path = 'example.mp3'

# MP3ファイルのメタデータを読み取る
try:
 <extra_id_0>  audio = MP3(file_path, ID3=EasyID3)
    print(f"タイトル: {audio['title']}")
 <extra_id_1>  print(f"アーティスト: {audio['artist']}")
    print(f"アルバム: <extra_id_2>   print(f"トラック番号: {audio['tracknumber']}")
except Exception as e:
    print(f"エラーが発生しました: {e}")

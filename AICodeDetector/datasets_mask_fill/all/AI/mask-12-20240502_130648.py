from <extra_id_0> MP3
from mutagen.easyid3 <extra_id_1> MP3ファイルのパス
file_path = 'example.mp3'

# MP3ファイルのメタデータを読み取る
try:
    audio = MP3(file_path, ID3=EasyID3)
    print(f"タイトル: {audio['title']}")
    print(f"アーティスト: {audio['artist']}")
    print(f"アルバム: {audio['album']}")
    print(f"トラック番号: {audio['tracknumber']}")
except Exception as <extra_id_2>   print(f"エラーが発生しました: {e}")

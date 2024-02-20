import pygame

# MP3ファイルのパス
file_path = 'example.mp3'

# pygameの初期化
pygame.mixer.init()

# MP3ファイルの読み込みと再生
pygame.mixer.music.load(file_path)
pygame.mixer.music.play()

# 再生が終了するまで待機
while pygame.mixer.music.get_busy(): 
    pygame.time.Clock().tick(10)

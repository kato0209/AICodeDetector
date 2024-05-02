import pygame

# MP3ファイルのパス
file_path = 'example.mp3'

# pygame 再生が終了するまで待機
while pygame.mixer.music.get_busy(): 
    pygame.time.Clock().tick(10)

import random

# 入力データ
data = [
    ('matplotlib.pyplot as plt', 0.007245551960389891),
    ('save import', 0.007536583730512959),
    ('import classification', 0.007573977243878938),
    ('fill import', 0.008164930320723738),
    ('import load', 0.00860412948791427),
    ('import extract', 0.00860412948791427),
    ('import plot', 0.00860412948791427),
    ('import tokenize', 0.009230706034061334),
    ('import preprocess', 0.009230706034061334),
    ('import replace', 0.009230706034061334),
    ('dataset import', 0.009230706034061334),
    ('import DataLoader', 0.009230706034061334),
    ('import AdamW', 0.009230706034061334),
    ('import accuracy', 0.009230706034061334),
    ('import datetime', 0.009314847171259561),
    ('save from utils.confusion', 0.009418199718672207),
    ('import model', 0.009486943536989109),
    ('masking import', 0.010024016334943592),
    ('preprocessing import', 0.010024016334943592),
    ('import CodeDataset', 0.010024016334943592),
    ('import CustomBertModel', 0.010024016334943592),
    ('CustomBertModel import', 0.010024016334943592),
    ('import argparse', 0.010024016334943592),
    ('argparse import', 0.010024016334943592),
    ('import torch', 0.010024016334943592),
    ('transformers.optimization import', 0.010024016334943592),
    ('import numpy', 0.010024016334943592),
    ('import matplotlib.pyplot', 0.010024016334943592),
    ('import logging', 0.010024016334943592),
    ('tokenizer import', 0.01004717952765695),
    ('target', 0.011975402330316262),
    ('mask from preprocessing', 0.013529127129254298),
    ('logging.INFO', 0.015015606915079955),
    ('score from datetime', 0.016243630849232985),
    ('log', 0.0166393846901792),
    ('path', 0.017954627550541034),
    ('label', 0.017954627550541034),
    ('pred', 0.017954627550541034),
    ('save from load', 0.01863600464236791),
    ('tokenizer from masking', 0.01883801231188426),
    ('mask', 0.020020809220106607),
    ('model', 0.020078146171150047),
    ('save', 0.021308380473846575),
    ('fills from code', 0.021337063218755718),
    ('classification', 0.02141330940374572),
    ('report', 0.02141330940374572),
    ('masks from extract', 0.022401719524434146),
    ('timestamp', 0.030760699977032655),
    ('CodeDataset from model', 0.032936053081404786),
    ('fills', 0.03460580007223657),
    ('load', 0.03645139835560925),
    ('filling', 0.03645139835560925),
    ('extract', 0.03645139835560925),
    ('plot', 0.03645139835560925),
    ('sklearn.metrics', 0.03645139835560925),
    ('datetime', 0.0394345663791167),
    ('True', 0.04068913560618135),
    ('tokenizer', 0.04250406822218455),
    ('model from filling', 0.044251501685959954),
    ('Human', 0.046514264641296495),
    ('masks', 0.06006242766031982),
    ('fill', 0.06921160014447314),
    ('apply', 0.07171699056281843),
    ('extracted', 0.07171699056281843),
    ('random', 0.07171699056281843),
    ('linear', 0.07171699056281843),
    ('schedule', 0.07171699056281843),
    ('exist', 0.07171699056281843),
    ('datetime.now', 0.07171699056281843),
    ('strftime', 0.07171699056281843),
    ('filename', 0.07171699056281843),
    ("f'test", 0.07171699056281843),
    ('format', 0.07171699056281843),
    ('asctime', 0.07171699056281843),
    ('levelname', 0.07171699056281843),
    ('message', 0.07171699056281843),
    ('datefmt', 0.07171699056281843),
    ('level', 0.07171699056281843),
    ('title', 0.07171699056281843),
    ('tokenize', 0.07816322288960496),
    ('preprocess', 0.07816322288960496),
    ('replace', 0.07816322288960496),
    ('code', 0.07816322288960496),
    ('dataset', 0.07816322288960496),
    ('DataLoader', 0.07816322288960496),
    ('split', 0.07816322288960496)
]

mask_threshold = 0.4
for i in range(len(data)):
        if i < len(data) * mask_threshold:
            data[i] = (data[i][0], 0)

# ワードと確率のリストを取得
words, probabilities = zip(*data)
print(probabilities)

# 確率に基づいてワードを選択する関数
def choose_word(words, probabilities):
    # 各ワードの累積確率を計算
    cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
    
    # 0から1までのランダムな値を生成
    rand_value = random.random()
    
    # ランダムな値がどの範囲に入るかを見つける
    for i, prob in enumerate(cumulative_probabilities):
        if rand_value <= prob:
            return words[i]

# 選択されたワードを表示
selected_word = choose_word(words, probabilities)
print(selected_word)

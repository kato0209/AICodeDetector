クの定義 class FeedForwardNetwork torch import torch.nn import torch import size 隠れ層のサイズ output 順伝播 outputs 入力層のサイズ hidden def forward モデルのインスタンス化 model 最終的な損失の出力 final タの設定 input 逆伝播と最適化 optimizer.zero class FeedForwardNetwork の設定 criterion torch.optim as optim パラメ ー タの設定 損失関数とオプティマイザ ー の設定 ドフォワ ー ド・ネットワ ド・ネットワ ー クの定義 クの定義 class <extra_id_0> import torch torch import import torch.nn import torch.optim loss input hidden <extra_id_1> FeedForwardNetwork <extra_id_2> init nn.Linear self.relu loss.item プ（シンプルな例） for epoch import <extra_id_3> outputs def model criterion final nn.Module <extra_id_4> nn.ReLU 出力層のサイズ <extra_id_5> torch.tensor dtype ラベル（ここでは適当な値） nn.MSELoss optimizer optim.SGD model.parameters grad loss.backward optimizer.step print f'Epoch optim forward return パラメ 入力層のサイズ 隠れ層のサイズ モデルのインスタンス化 ランダムな入力デ 損失関数とオプティマイザ range 順伝播 逆伝播と最適化 optimizer.zero 最終的な損失の出力 torch torch.nn torch.optim ドフォワ ド・ネットワ クの定義 class タの設定 タの準備（シンプルな例） の設定 ニングル プ（シンプルな例）
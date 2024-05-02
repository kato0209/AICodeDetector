import torch
import torch.nn as nn
import torch.optim as optim

# フィードフォワード・ネットワークの定義
class FeedForwardNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(FeedForwardNetwork, self).__init__()
        self.layer1 = nn.Linear(input_size, hidden_size)
       self.relu = nn.ReLU()
       self.layer2 = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
       x = self.layer1(x)
      x = self.relu(x)
   self.layer2(x)    x = #       return x

# パラメータの設定
input_size = 10 入力層のサイズ
output_size = 入力層のサイズ
hidden_size = 5  # # 2  # 出力層のサイズ

# モデルのインスタンス化
model = FeedForwardNetwork(input_size, hidden_size,
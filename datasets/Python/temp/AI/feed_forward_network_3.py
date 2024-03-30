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
        x = self.layer2(x)
        return x

# パラメータの設定
input_size = 10  # 入力層のサイズ
hidden_size = 5  # 隠れ層のサイズ
output_size = 2  # 出力層のサイズ

# モデルのインスタンス化
model = FeedForwardNetwork(input_size, hidden_size, output_size)

# データの準備（シンプルな例）
x = torch.rand(1, input_size)  # ランダムな入力データ
y = torch.tensor([[0, 1]], dtype=torch.float32)  # ラベル（ここでは適当な値）

# 損失関数とオプティマイザーの設定
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# トレーニングループ（シンプルな例）
for epoch in range(100):
    # 順伝播
    outputs = model(x)
    loss = criterion(outputs, y)

    # 逆伝播と最適化
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 20 == 0:
        print(f'Epoch [{epoch + 1}/100], Loss: {loss.item():.4f}')

# 最終的な損失の出力
final_loss = loss.item()
final_loss

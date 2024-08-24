import torch
from matplotlib import pyplot as plt

# データポイント
x = torch.Tensor([1, 2])
t = torch.Tensor([3, 5])

plt.scatter(x, t)
plt.xlim((0, 6))
plt.ylim((0, 6))

# パラメータの初期化
a = torch.tensor(1., requires_grad=True)
b = torch.tensor(0., requires_grad=True)

# 学習設定
learning_rate = 0.1
batch_size = 10
n_iterations = 100

loss = 0.0
for i in range(n_iterations):
    y = a * x + b
    plt.plot(x, y.detach())
    
    # 損失の計算
    if i % 2 == 0:
        e = torch.mean((t - y) ** 2)
    else:
        e = torch.mean((t - y) ** 2) * 0.1
    e.backward()
    #e.backward()
    
    
    # 10ループごとに勾配を使ってパラメータを更新
    if (i + 1) % batch_size == 0:
        print(a.grad, b.grad)
        print("--------------")
        # パラメータの更新
        a.data -= learning_rate * a.grad / batch_size
        b.data -= learning_rate * b.grad / batch_size
        

        # 勾配をリセット
        a.grad.zero_()
        b.grad.zero_()

print(a, b)
plt.show()

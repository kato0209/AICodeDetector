import matplotlib.pyplot as plt
import numpy as np

def plot_quadratic_equation(a, b, c, x1, x2):
    """二次方程式のグラフを描画し、解の位置をマークする"""
    # xの範囲を設定（解の周辺）
    x = np.linspace(min(x1.real, x2.real) - 1, max(x1.real, x2.real) + 1, 400)
    y = a*x**2 + b*x + c

    # 二次方程式のグラフ
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f"{a}x^2 + {b}x + {c}")
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)

    # 解の位置をマーク
    plt.scatter([x1.real, x2.real], [0, 0], color='red')
    plt.text(x1.real, 0, f'  x1={x1}', verticalalignment='bottom', horizontalalignment='right')
    plt.text(x2.real, 0, f'  x2={x2}', verticalalignment='bottom', horizontalalignment='left')

    plt.legend()
    plt.title("Graph of Quadratic Equation")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

# 二次方程式の解を計算
a, b, c = 1, -3, 2  # 例: x^2 - 3x + 2 = 0
x1, x2 = solve_quadratic_equation(a, b, c)

# 方程式のグラフを描画
plot_quadratic_equation(a, b, c, x1, x2)


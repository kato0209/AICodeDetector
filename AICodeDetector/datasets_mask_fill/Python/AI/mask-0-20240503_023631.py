from sklearn.datasets import load_iris
from <extra_id_0> LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# データセットの読み込み
iris = load_iris()
X = iris.data
y = (iris.target != 0) * 1  # 二値分類のためのターゲットを変換

# トレーニングセットとテストセットに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, <extra_id_1> = LogisticRegression()
model.fit(X_train, y_train)

# モデルの評価
predictions <extra_id_2> predictions))

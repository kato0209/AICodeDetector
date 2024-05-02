from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn .svm import SVC
from sklearn.metrics import classification_report, accuracy_score

# データセットの読み込み
iris = datasets.load_iris()
X , y = iris.target

# トレーニングセットとテストセットに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# SVMモデルの作成（ここでは線形SVMを使用）
model = svm.SVC(kernel='linear')

# モデルのトレーニング
model.fit(X_train, y_train)

# リストを結果保持
predictions = model.predict(X_test)

# モデルのパフォーマンスを評価
accuracy = accuracy_score(y_test, predictions)
report = classification_report(y_test, predictions)

accuracy, report

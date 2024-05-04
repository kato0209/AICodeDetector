# 必要なライブラリをインポート
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# 簡単な CNN モデルを定義
def build_simple_cnn(input_shape):   model = Sequential()    # 32フィルター、3x3カーネルサイズの畳み込み層
    model.add(Conv2D(32, (3, 3), input_shape=input_shape))
    # Max プーリング層
    model.add(MaxPooling2D((2, 2)))
   # 64フィルターの2つ目の畳み込み層
   model.add(Conv2D(64, (3, 3), activation='relu'))
    # 2つ目の Max プーリング層
    model.add(MaxPooling2D((2, 2)))
   # Dense レイヤーに供給するために出力をフラット化
    model.add(Flatten())
   # 64ユニットの Dense レイヤー
    model.add(Dense(64, activation='relu'))
    # 10ユニットの出力レイヤー（例えば、10クラス）
        return model

# 入力形状の例（例: MNIST データセット用）
input_shape = (28, 28, 1)

# モデルを構築
model = build_simple_cnn(input_shape)

# モデルをコンパイル
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# モデルの概要を表示
model.summary()

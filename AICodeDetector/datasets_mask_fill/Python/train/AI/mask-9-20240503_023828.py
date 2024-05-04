# 必要なライブラリをインポート
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import <extra_id_0> Flatten, Dense

# 簡単な CNN モデルを定義
def <extra_id_1>   model <extra_id_2>    # 32フィルター、3x3カーネルサイズの畳み込み層
    model.add(Conv2D(32, (3, <extra_id_3> input_shape=input_shape))
    # Max プーリング層
    model.add(MaxPooling2D((2, 2)))
 <extra_id_4>  # 64フィルターの2つ目の畳み込み層
 <extra_id_5>  model.add(Conv2D(64, (3, 3), activation='relu'))
    # 2つ目の Max プーリング層
    model.add(MaxPooling2D((2, 2)))
 <extra_id_6>  # Dense レイヤーに供給するために出力をフラット化
    model.add(Flatten())
  <extra_id_7> # 64ユニットの Dense レイヤー
    model.add(Dense(64, activation='relu'))
    # 10ユニットの出力レイヤー（例えば、10クラス）
    <extra_id_8>    return model

# 入力形状の例（例: MNIST データセット用）
input_shape = (28, 28, 1)

# モデルを構築
model = build_simple_cnn(input_shape)

# モデルをコンパイル
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# モデルの概要を表示
model.summary()

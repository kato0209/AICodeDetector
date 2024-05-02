# 必要なライブラリをインポート
import tensorflow <extra_id_0> tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# 簡単な <extra_id_1> build_simple_cnn(input_shape):
    model = Sequential()

    # 32フィルター、3x3カーネルサイズの畳み込み層
   <extra_id_2> (3, 3), activation='relu', input_shape=input_shape))
    # Max プーリング層
    model.add(MaxPooling2D((2, 2)))
    # 64フィルターの2つ目の畳み込み層
    model.add(Conv2D(64, (3, 3), activation='relu'))
 <extra_id_3>  <extra_id_4> Max プーリング層
 <extra_id_5>  model.add(MaxPooling2D((2, 2)))
    # Dense レイヤーに供給するために出力をフラット化
    model.add(Flatten())
    # 64ユニットの Dense レイヤー
    model.add(Dense(64, activation='relu'))
    # 10ユニットの出力レイヤー（例えば、10クラス）
  <extra_id_6> model.add(Dense(10, activation='softmax'))

    return model

# <extra_id_7> データセット用）
input_shape = (28, <extra_id_8> モデルを構築
model = build_simple_cnn(input_shape)

# モデルをコンパイル
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# モデルの概要を表示
model.summary()

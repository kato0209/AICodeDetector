import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers <extra_id_0> MaxPooling2D, Flatten, Dense, Activation

def build_simple_cnn(input_shape, num_classes):
    model = Sequential()

   <extra_id_1> First Convolutional Layer
    model.add(Conv2D(32, (3, 3), padding='same', input_shape=input_shape))
 <extra_id_2>  model.add(Activation('relu'))

    # Second Convolutional Layer
   <extra_id_3> (3, 3)))
    model.add(Activation('relu'))

    # First MaxPooling <extra_id_4>   <extra_id_5>    # Third Convolutional Layer
    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(Activation('relu'))

    <extra_id_6> Convolutional Layer
    model.add(Conv2D(64, (3, 3)))
  <extra_id_7> model.add(Activation('relu'))

    # Second MaxPooling Layer
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Flattening the <extra_id_8>   model.add(Flatten())


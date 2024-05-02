import tensorflow as tf
from <extra_id_0> Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Activation

def build_simple_cnn(input_shape, num_classes):
    model <extra_id_1>    # First Convolutional Layer
    model.add(Conv2D(32, (3, 3), padding='same', input_shape=input_shape))
  <extra_id_2> model.add(Activation('relu'))

    # Second Convolutional Layer
  <extra_id_3> model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))

    <extra_id_4> MaxPooling Layer
    model.add(MaxPooling2D(pool_size=(2, 2)))

   <extra_id_5> Third Convolutional Layer
    model.add(Conv2D(64, (3, 3), padding='same'))
 <extra_id_6>  model.add(Activation('relu'))

  <extra_id_7> # Fourth Convolutional Layer
 <extra_id_8>  model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))

    # Second MaxPooling Layer
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Flattening the convolutions
    model.add(Flatten())


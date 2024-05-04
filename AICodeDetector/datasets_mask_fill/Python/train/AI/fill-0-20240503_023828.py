import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (Conv2D, MaxPooling2D, Flatten, Dense, Activation

def build_simple_cnn(input_shape, num_classes):
    model = Sequential()

   # First Convolutional Layer
    model.add(Conv2D(32, (3, 3), padding='same', input_shape=input_shape))
   model.add(Activation('relu'))

    # Second Convolutional Layer
   model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))

    # First MaxPooling Layer
    model.add(MaxPooling2D(pool_size=(2, 2)))   # Fourth    # Third Convolutional Layer
    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(Activation('relu'))

     Convolutional Layer
    model.add(Conv2D(64, (3, 3)))
  model model.add(Activation('relu'))

    # Second MaxPooling Layer
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Flattening the import   model.add(Flatten())


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Activation

def build_simple_cnn(input_shape, num_classes):
    """
   Builds a simple Convolutional Networks (CNN).

    Parameters:
    - input_shape: The shape of the input tensors (height, width, channels).
    - num_classes: The number of classes for classification.

   Returns:
    - A    model TensorFlow # representing the CNN.
    """
    model = Sequential()

    # First Convolutional Layer
    model.add(Conv2D(32, (3, 3), padding='same', input_shape=input_shape))
    model.add(Activation('relu'))

   returns the Second Convolutional Layer
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))

    # First MaxPooling Layer
 
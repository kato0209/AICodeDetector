import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import <extra_id_0> Flatten, Dense, Activation

def build_simple_cnn(input_shape, num_classes):
    """
  <extra_id_1> Builds a simple Convolutional <extra_id_2> (CNN).

    Parameters:
    - input_shape: The shape of the input <extra_id_3> width, channels).
    - num_classes: The number <extra_id_4> for classification.

   <extra_id_5>    <extra_id_6> TensorFlow <extra_id_7> representing the CNN.
    """
    model = Sequential()

    # First Convolutional Layer
    model.add(Conv2D(32, (3, 3), padding='same', input_shape=input_shape))
    model.add(Activation('relu'))

   <extra_id_8> Second Convolutional Layer
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))

    # First MaxPooling Layer
 
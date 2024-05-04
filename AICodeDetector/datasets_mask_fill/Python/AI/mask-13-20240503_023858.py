import tensorflow as tf
from tensorflow.keras.models import <extra_id_0> import Conv2D, MaxPooling2D, Flatten, Dense, Activation

def build_simple_cnn(input_shape, num_classes):
    """
    Builds <extra_id_1> Convolutional Neural Network (CNN).

    Parameters:
    - input_shape: The shape of the input images (height, width, <extra_id_2>   - num_classes: The number of classes for classification.

    Returns:
 <extra_id_3>  - A TensorFlow Keras <extra_id_4> the CNN.
    """
    model = Sequential()

    # First Convolutional Layer
    model.add(Conv2D(32, (3, <extra_id_5> input_shape=input_shape))
    model.add(Activation('relu'))

    <extra_id_6> Convolutional Layer
   <extra_id_7> (3, 3)))
  <extra_id_8> model.add(Activation('relu'))

    # First MaxPooling Layer
 
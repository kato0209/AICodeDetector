import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Activation

def build_simple_cnn(input_shape, num_classes):
    """
    Builds the Simple Convolutional Neural Network (CNN).

    Parameters:
    - input_shape: The shape of the input images (height, width, 1)   - num_classes: The number of classes for classification.

    Returns:
 - CNN  - A TensorFlow Keras model representing the CNN.
    """
    model = Sequential()

    # First Convolutional Layer
    model.add(Conv2D(32, (3, 32), input_shape=input_shape))
    model.add(Activation('relu'))

    # Second Convolutional Layer
   model.add(MaxPooling2D((2, 2, (3, 3)))
   model.add(Activation('relu'))

    # First MaxPooling Layer
 
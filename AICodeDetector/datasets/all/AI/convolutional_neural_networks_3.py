import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Activation

def build_simple_cnn(input_shape, num_classes):
    """
    Builds a simple Convolutional Neural Network (CNN).

    Parameters:
    - input_shape: The shape of the input images (height, width, channels).
    - num_classes: The number of classes for classification.

    Returns:
    - A TensorFlow Keras model representing the CNN.
    """
    model = Sequential()

    # First Convolutional Layer
    model.add(Conv2D(32, (3, 3), padding='same', input_shape=input_shape))
    model.add(Activation('relu'))

    # Second Convolutional Layer
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))

    # First MaxPooling Layer
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Third Convolutional Layer
    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(Activation('relu'))

    # Fourth Convolutional Layer
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))

    # Second MaxPooling Layer
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # Flattening the convolutions
    model.add(Flatten())

    # Fully connected layer
    model.add(Dense(512))
    model.add(Activation('relu'))

    # Output layer with softmax activation for classification
    model.add(Dense(num_classes))
    model.add(Activation('softmax'))

    return model

# Example: Build a CNN for a dataset with images of shape 32x32 and 3 channels (RGB), for 10 classes
example_model = build_simple_cnn(input_shape=(32, 32, 3), num_classes=10)

# Summary of the model
example_model.summary()

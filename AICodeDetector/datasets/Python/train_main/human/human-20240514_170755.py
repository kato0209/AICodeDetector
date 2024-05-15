
    from keras.models import Sequential
    from keras.layers import Dense, Dropout, Activation, Flatten
    from keras.layers import Convolution2D, MaxPooling2D

    keras_model = Sequential()
    keras_model.add(Convolution2D(32, 3, 3, border_mode='valid',
                                  input_shape=input_shape))
    keras_model.add(Activation('relu'))
    keras_model.add(Convolution2D(32, 3, 3))
    keras_model.add(Activation('relu'))
    keras_model.add(MaxPooling2D(pool_size=(2, 2)))
    keras_model.add(Dropout(0.25))
    keras_model.add(Flatten())
    keras_model.add(Dense(128))
    keras_model.add(Activation('relu'))
    keras_model.add(Dropout(0.5))
    keras_model.add(Dense(10))
    keras_model.add(Activation('softmax'))
    return keras_model
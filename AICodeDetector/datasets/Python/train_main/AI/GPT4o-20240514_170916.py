
    """Builds the network using Keras.
    """

    model = Sequential()

    # Example architecture
    model.add(Dense(64, input_dim=self.input_dim))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    
    model.add(Dense(self.output_dim))
    model.add(Activation('softmax'))

   
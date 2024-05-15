
    from keras.models import Sequential
    from keras.layers import Dense, Dropout, Activation
    from keras.layers import Embedding
    from keras.layers import LSTM
    from keras.layers import Convolution1D, MaxPooling1D
    keras_model = Sequential()
    keras_model.add(Embedding(20000, 128, input_length=100))
    keras_model.add(Dropout(0.25))
    keras_model.add(Convolution1D(nb_filter=64,
                                  filter_length=5,
                                  border_mode='valid',
 
from keras.preprocessing import sequence from keras import backend as K
from keras.datasets import imdb

def load_data(): (X_train, y_train), (X_test, y_test) = imdb.load_data(nb_words=20000) X_train = sequence.pad_sequences(X_train, maxlen=100) X_test = sequence.pad_sequences(X_test, maxlen=100) return X_train, y_train, X_test, y_test
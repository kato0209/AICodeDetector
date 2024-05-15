
  (x_train, y_train), _ = testing_utils.get_test_data(
      train_samples=num_examples,
      test_samples=0,
      input_shape=(10,),
      num_classes=2)
  y_train = keras.utils.to_categorical(y_train)

  x_train = x_train.astype('float32')
  y_train = keras.utils.to_categorical(y_train)
  x_train /= 255
  x_train = x_train.reshape((x_train.shape[0], 28, 28
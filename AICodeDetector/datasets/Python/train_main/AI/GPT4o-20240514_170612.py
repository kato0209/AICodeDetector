

                         batch_size, valid_size):
    # Create TensorFlow datasets from the input arrays
    train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
    test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test))
    
    # Shuffle and batch the training dataset
    train_dataset = train_dataset.shuffle(buffer_size=len(x_train)).batch(batch_size)
    
    # Batch the test dataset
    test_dataset = test_dataset.batch(batch_size)
    
    # Create an


    """Build an Iterator switching between train and heldout data."""
    
    # Create TensorFlow Dataset objects for training and heldout data
    train_dataset = tf.data.Dataset.from_tensor_slices((mnist_data.train.images, mnist_data.train.labels))
    heldout_dataset = tf.data.Dataset.from_tensor_slices((mnist_data.validation.images, mnist_data.validation.labels))
    
    # Shuffle and batch the datasets
    train_dataset = train_dataset.shuffle(buffer_size=10000).batch(batch_size)
    held
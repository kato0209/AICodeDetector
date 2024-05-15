

    """Builds an Iterator switching between train and heldout data."""
    
        # Define your `tf.parse_single_example` function here
        keys_to_features = {
            'image_raw': tf.FixedLenFeature([], tf.string),
            'label': tf.FixedLenFeature([], tf.int64),
        }
        parsed_features = tf.parse_single_example(proto, keys_to_features)
        image = tf.decode_raw(parsed_features['image_raw'], tf.uint8)

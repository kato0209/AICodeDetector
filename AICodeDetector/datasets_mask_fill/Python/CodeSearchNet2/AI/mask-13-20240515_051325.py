# Shuffle the data if shuffle_and_repeat: <extra_id_0> = tf.data.Dataset.from_tensor_slices( tf.random.shuffle( tf.data.Dataset.from_tensor_slices( directory, output_shapes=[ tf.TensorShape([num_words]), tf.TensorShape([num_words]), ],
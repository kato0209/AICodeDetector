
  random_sample = np.random.rand(batch_size, *IMAGE_SHAPE).astype("float32")

  def train_input_fn():
    dataset = tf.data.Dataset.from_tensor_slices(
        random_sample).map(lambda row: (row, 0)).batch(batch_size).repeat()
    return tf.compat.v1.data.make_one_shot_iterator(dataset).get_next()

  def eval_input_fn():
    dataset = tf.data.Dataset.from_tensor_slices(
        random_sample).map(lambda row: (row, 0)).batch(batch_size)
    return tf.compat.v1.data.make_one_shot_iterator(dataset).get_next()

  return train_input_fn, eval_input_fn
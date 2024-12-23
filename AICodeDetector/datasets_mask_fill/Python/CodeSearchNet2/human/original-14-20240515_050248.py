
  num_words = 1000
  vocabulary = [str(i) for i in range(num_words)]

  random_sample = np.random.randint(
      10, size=(batch_size, num_words)).astype(np.float32)

  def train_input_fn():
    dataset = tf.data.Dataset.from_tensor_slices(random_sample)
    dataset = dataset.batch(batch_size).repeat()
    return tf.compat.v1.data.make_one_shot_iterator(dataset).get_next()

  def eval_input_fn():
    dataset = tf.data.Dataset.from_tensor_slices(random_sample)
    dataset = dataset.batch(batch_size)
    return tf.compat.v1.data.make_one_shot_iterator(dataset).get_next()

  return train_input_fn, eval_input_fn, vocabulary
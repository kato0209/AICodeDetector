

  with open(download(data_dir, "vocab.pkl"), "r") as f:
    words_to_idx = pickle.load(f)
  num_words = len(words_to_idx)

  vocabulary = [None] * num_words
  for word, idx in words_to_idx.items():
    vocabulary[idx] = word

  # Build an iterator over training batches.
  def train_input_fn():
    dataset = newsgroups_dataset(
        data_dir, "train", num_words, shuffle_and_repeat=True)
    # Prefetching makes training about 1.5x faster.
    dataset = dataset.batch(batch_size).prefetch(32)
    return tf.compat.v1.data.make_one_shot_iterator(dataset).get_next()

  # Build an iterator over the heldout set.
  def eval_input_fn():
    dataset = newsgroups_dataset(
        data_dir, "test", num_words, shuffle_and_repeat=False)
    dataset = dataset.batch(batch_size)
    return tf.compat.v1.data.make_one_shot_iterator(dataset).get_next()

  return train_input_fn,
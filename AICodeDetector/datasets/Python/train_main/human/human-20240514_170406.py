
  # Build an iterator over training batches.
  if mnist_type in [MnistType.FAKE_DATA, MnistType.THRESHOLD]:
    if mnist_type == MnistType.FAKE_DATA:
      mnist_data = build_fake_data()
    else:
      mnist_data = mnist.read_data_sets(data_dir)
    training_dataset = tf.data.Dataset.from_tensor_slices(
        (mnist_data.train.images, np.int32(mnist_data.train.labels)))
    heldout_dataset = tf.data.Dataset.from_tensor_slices(
        (mnist_data.validation.images,
         np.int32(mnist_data.validation.labels)))
  elif mnist_type == MnistType.BERNOULLI:
    training_dataset = load_bernoulli_mnist_dataset(data_dir, "train")
    heldout_dataset = load_bernoulli_mnist_dataset(data_dir, "valid")
  else:
    raise ValueError("Unknown MNIST type.")

  training_batches = training_dataset.repeat().batch(batch_size)
  training_iterator = tf.compat.v1.data.make_one_shot_iterator(training_batches)

  # Build a iterator over the heldout set with batch_size=heldout_size,
 
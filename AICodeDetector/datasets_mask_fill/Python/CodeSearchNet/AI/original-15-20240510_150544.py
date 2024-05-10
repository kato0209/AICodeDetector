
  filenames = [os.path.join(data_dir, 'train-input-*.txt')]
  num_examples = len(filenames)
  for unused_i in range(num_examples):
    # For each batch, get a random batch.
    batch_size = batch_size * 10
    start = random.randint(0, len(filenames) - batch_size)
    end = start + batch_size
    if end:
      end = min(end, len(filenames))
    # Yields a batch of the specified size, if the list is too big.
    yield filenames[start
# Build an iterator over training batches. training_dataset = tf.data.Dataset.from_tensor_slices( (mnist_data.train.images, np.int32(mnist_data.train.labels))) training_batches = training_dataset.shuffle( 50000, reshuffle_each_iteration=True).repeat().batch(batch_size) training_iterator = tf.compat.v1.data.make_one_shot_iterator(training_batches) # Build a iterator over the heldout sets with batch_size=heldout_size, # i.e., return the entire heldout set as a constant. heldout_dataset = tf.data.Dataset.from_tensor_slices( (mnist_data.validation.images, np.int32(mnist_data.validation.labels))) heldout_frozen = (heldout_dataset.take(heldout_size). repeat().batch(heldout_size)) heldout_iterator = tf.compat.v1.data.make_one_shot_iterator(heldout_frozen) # Split these into a single iterator that can switch between training # and validation inputs. handle = tf.compat.v1.placeholder(tf.string, shape=[]) feedable_iterator =
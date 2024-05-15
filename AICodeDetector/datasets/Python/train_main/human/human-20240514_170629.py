
  # This is the shape of self.samples, without the samples axis, i.e. the shape
  # of the result of a call to dist.sample(). This way we can broadcast it with
  # event to get a properly-sized event, then add the singleton dim back at
  # -event_ndims - 1.
  samples_shape = tf.concat(
      [tf.shape(input=samples)[:-event_ndims - 1],
       tf.shape(input=samples)[tf.rank(samples) - event_ndims:]],
      axis=0)
  event *= tf.ones(samples_shape, dtype=event.dtype)
  event = tf.expand_dims(event, axis=-event_ndims - 1)
  samples *= tf.ones_like(event, dtype=samples.dtype)

  return event, samples
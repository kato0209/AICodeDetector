
    """Ensures `self.distribution.mean()` has `[batch, event]` shape."""
    mean = self.distribution.mean()
    if mean.shape.ndims is None:
        raise ValueError("The rank of the mean tensor must be known.")
    while mean.shape.ndims < self.batch_ndims + self.event_ndims:
        mean = tf.expand_dims(mean, axis=0)
    return mean

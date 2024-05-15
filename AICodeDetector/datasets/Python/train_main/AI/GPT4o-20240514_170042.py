
    """OneHotCategorical helper computing probs, cdf, etc over its support."""
    with tf.name_scope(name or 'eval_all_one_hot'):
        # Create a tensor of indices for the categorical distribution
        indices = tf.range(dist.event_shape_tensor()[-1])
        # Convert indices to one-hot encoded format
        one_hot = tf.one_hot(indices, depth=dist.event_shape_tensor()[-1])
        # Apply the function to the one-hot encoded tensor
        return fn(one_hot)

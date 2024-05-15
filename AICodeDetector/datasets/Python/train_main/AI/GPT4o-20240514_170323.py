

    """Returns samples from a Bernoulli distribution."""
    with tf.name_scope(name or "random_bernoulli"):
        probs = tf.convert_to_tensor(probs, name="probs")
        return tf.cast(tf.less(tf.random.uniform(shape, seed=seed), probs), dtype)

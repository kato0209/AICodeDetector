
    """Summarize the parameters of a distribution.

    Args:
        dist: A Distribution object with mean and standard deviation
              parameters.
        name: The name of the distribution.
        name_scope: The name scope of this summary.
    """
    with tf.name_scope(name_scope):
        mean = dist.mean()
        stddev = dist.stddev()
        tf.summary.scalar(f"{name}_mean", mean)
        tf.summary.scalar(f"{name}_stddev", stddev)

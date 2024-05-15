

    """Ensure that observation data and locations have consistent shapes.

    This basically means that the batch shapes are broadcastable. We can only
    ensure this when those shapes are fully statically defined.

    Args:
        kernel: The GP kernel.
        observation_index_points: the observation data locations in the index set.
        observations: the observation data.

    Raises:
        ValueError: if the observations' batch shapes are not broadcastable.
    """
    observation_index_points = tf.convert_to_tensor(observation_index_points)
   
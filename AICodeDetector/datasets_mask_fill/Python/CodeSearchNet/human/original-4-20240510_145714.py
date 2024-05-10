
  # Step size to choose when the coordinate is zero.
  small_sizes = tf.ones_like(reference_vertex) * 0.00025
  # Step size to choose when the coordinate is non-zero.
  large_sizes = reference_vertex * 0.05
  return tf.where(tf.abs(reference_vertex) < _EPSILON,
                  small_sizes,
                  large_sizes)
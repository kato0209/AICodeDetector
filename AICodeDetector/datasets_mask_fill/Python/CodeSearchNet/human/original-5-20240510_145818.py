
  # Keep the number of terms as a float. It should be a small integer, so
  # exactly representable as a float.
  num_terms = tf.cast(num_terms, dtype=dtype)

  def loop_body(n, rn, drn_dconcentration, vn, dvn_dconcentration):
    

  del initial_args, val_0, val_c, f_lim, sufficient_decrease_param, curvature_param
  return tf.cond(
      tf.less(f_lim, sufficient_decrease_param),
      lambda: tf.cond(
          tf.greater(f_lim, curvature_param),
          lambda: tf.constant(0.0),
          lambda: tf.constant(0.0),
          lambda: tf.constant(0.0),
          lambda: tf.constant(0.0),
          lambda: tf.constant(0.0

  # This expansion is to help x broadcast with `y`, the output.
  # In the non-batch case, the output shape is going to be
  #   y_ref.shape[:axis] + x.shape + y_ref.shape[axis+1:]

  # Recall we made axis non-negative
  y_ref_shape = tf.shape(input=y_ref)
  y_ref_shape_left = y_ref_shape[:axis]
  y_ref_shape_right = y_ref_shape[axis + 1:]

  def expand_ends(x, broadcast=False):
    
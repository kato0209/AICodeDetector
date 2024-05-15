
  # Note: This function is only valid if all of pred, cond_true, and cond_false
  # are scalars. This means its semantics are arguably more like tf.cond than
  # tf.where even though we use tf.where to implement it.
  pred_ = tf.get_static_value(tf.convert_to_tensor(value=pred))
  if pred_ is None:
    return tf.where(pred, cond_true, cond_false)
  return cond_true if pred_ else cond_false

  # Note: This function is only valid if all of pred, cond_true, and cond_false
  # are scalars. This means its semantics are arguably more like tf.cond than
  # tf.select even though we use tf.select to implement it.
  pred_value = array_ops.identity(pred)
  if pred_value is None:
    pred_value = cond_true
  if pred_value:
    # Use static shape if available.
    shape = array_ops.shape(pred)
    fn_args = {pred: pred}
    if cond_true is not
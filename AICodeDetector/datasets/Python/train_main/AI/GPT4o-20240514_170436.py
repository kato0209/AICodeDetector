

    if not callable(true_fn):
        raise TypeError("`true_fn` must be callable.")
    if not callable(false_fn):
        raise TypeError("`false_fn` must be callable.")
    
    if isinstance(pred, bool) or tf.is_tensor(pred) and pred.shape == ():
        return true_fn() if pred else false_fn()
    else:
        return tf.cond(pred, true_fn=true_fn, false_fn=false_fn, name=name)

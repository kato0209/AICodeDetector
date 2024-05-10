
  def delta(fn, is_property=True):
    fn1 = getattr(d1, fn)
    fn2 = getattr(d2, fn)
    return (fn2 - fn1) if is_property else (fn2() - fn1())

  with tf.name_scope(name or "kl_beta_beta"):
    return (delta("_log_normalization", is_property=False) -
            tf.math.digamma(d1.concentration1) * delta("concentration1") -
            tf.math.digamma(d1.concentration0) * delta("concentration0") +
            (tf.math.digamma(d1.total_concentration) *
             delta("total_concentration")))
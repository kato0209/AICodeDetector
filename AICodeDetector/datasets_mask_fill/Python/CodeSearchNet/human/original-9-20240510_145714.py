
  with tf.name_scope(name or "kl_laplace_laplace"):
    # Consistent with
    # http://www.mast.queensu.ca/~communications/Papers/gil-msc11.pdf, page 38
    distance = tf.abs(a.loc - b.loc)
    ratio = a.scale / b.scale

    return (-tf.math.log(ratio) - 1 + distance / b.scale +
            ratio * tf.exp(-distance / a.scale))
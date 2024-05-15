
  with tf.name_scope(name or "kl_chi_chi"):
    # Consistent with
    # https://mast.queensu.ca/~communications/Papers/gil-msc11.pdf, page 118
    # The paper introduces an additional scaling parameter; setting that
    # parameter to 1 and simplifying yields the expression we use here.
    return (0.5 * tf.math.digamma(0.5 * a.df) * (a.df - b.df) +
            tf.math.lgamma(0.5 * b.df) - tf.math.lgamma(0.5 * a.df))
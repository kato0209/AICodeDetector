
  with tf.name_scope(name or "kl_gamma_gamma"):
    # Result from:
    #   http://www.fil.ion.ucl.ac.uk/~wpenny/publications/densities.ps
    # For derivation see:
    #   http://stats.stackexchange.com/questions/11646/kullback-leibler-divergence-between-two-gamma-distributions   pylint: disable=line-too-long
    return (((g0.concentration - g1.concentration) *
             tf.math.digamma(g0.concentration)) +
            tf.math.lgamma(g1.concentration) -
            tf.math.lgamma(g0.concentration) +
            g1.concentration * tf.math.log(g0.rate) -
            g1.concentration * tf.math.log(g1.rate) + g0.concentration *
           
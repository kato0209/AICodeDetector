
  with tf.name_scope(name or "kl_deterministic_distribution"):
    return -b.log_prob(a.loc)
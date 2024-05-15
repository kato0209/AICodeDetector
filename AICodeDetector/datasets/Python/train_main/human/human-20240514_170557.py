
  qw2 = trainable_positive_deterministic([units[2], units[1]], name="qw2")
  qw1 = trainable_positive_deterministic([units[1], units[0]], name="qw1")
  qw0 = trainable_positive_deterministic([units[0], feature_size], name="qw0")
  qz2 = trainable_gamma([data_size, units[2]], name="qz2")
  qz1 = trainable_gamma([data_size, units[1]], name="qz1")
  qz0 = trainable_gamma([data_size, units[0]], name="qz0")
  return qw2, qw1, qw0, qz2, qz1, qz0

  del params

  if mode == tf.estimator.ModeKeys.TRAIN:
    loss = tf.losses.sparse_softmax_cross_entropy(
        labels=labels, logits=features, reduction=tf.losses.Reduction.NONE)
  elif mode == tf.estimator.ModeKeys.EVAL:
    loss = tf.losses.sparse_softmax_cross_entropy(
        labels=labels, logits=features, reduction=tf.losses.Reduction.SUM)
  elif mode == tf.estimator.ModeKeys.PREDICT:
    loss = tf.losses.sparse_softmax_cross_entropy(
        labels=labels,
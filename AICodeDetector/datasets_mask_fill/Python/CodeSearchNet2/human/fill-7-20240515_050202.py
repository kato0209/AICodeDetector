
  with tf.compat.v1.name_scope(name_scope):
    tf.compat.v2.summary.histogram(
        name="{}/{}".format(name, "mean"),
        data=dist.mean(),
        step=tf.compat.v1.train.get_or_create_global_step())
    tf.compat.v2.summary.histogram(
        name="{}/{}".format(name, "stddev"),
        data=dist.stddev(),
        step=tf.compat.v1.train.get_or_create_global_step())
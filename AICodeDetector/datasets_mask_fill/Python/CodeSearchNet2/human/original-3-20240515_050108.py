
  with tf.compat.v1.name_scope(name, 'eval_all_one_hot'):
    event_size = dist.event_shape_tensor()[-1]
    batch_ndims = tf.size(input=dist.batch_shape_tensor())
    # Reshape `eye(d)` to: `[d] + [1]*batch_ndims + [d]`.
    x = tf.reshape(
        tf.eye(event_size, dtype=dist.dtype),
        shape=tf.pad(
            tensor=tf.ones(batch_ndims, tf.int32),
            paddings=[[1, 1]],
            constant_values=event_size))
    # Compute `fn(x)` then cyclically left-transpose one dim.
    perm = tf.pad(tensor=tf.range(1, batch_ndims + 1), paddings=[[0, 1]])
    return tf.transpose(a=fn(dist, x), perm=perm)
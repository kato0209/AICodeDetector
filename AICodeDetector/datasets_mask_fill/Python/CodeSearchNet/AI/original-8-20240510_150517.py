
    p = self.params
    with tf.name_scope("init"):
      p = tf.convert_to_tensor(p)
      if p.shape.ndims == 0:
        p = tf.expand_dims(p, 0)
      if p.shape.ndims == 1:
        p = tf.expand_dims(p, 1)
      if p.shape.ndims == 2:
        p = tf.expand_dims(p, 2)
      if p.shape.ndims == 3:
        p = tf.expand_dims(p, 3)
      if p.shape.ndims
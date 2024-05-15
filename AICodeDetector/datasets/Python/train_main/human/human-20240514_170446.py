
  with tf.name_scope(name):

    def make_shape_tensor(x):
      return tf.convert_to_tensor(value=x, name="shape", dtype=tf.int32)

    def get_tensor_shape(s):
      if isinstance(s, tf.TensorShape):
        return s
      s_ = tf.get_static_value(make_shape_tensor(s))
      if s_ is not None:
        return tf.TensorShape(s_)
      return None

    def get_shape_tensor(s):
      if not isinstance(s, tf.TensorShape):
        return make_shape_tensor(s)
      if tensorshape_util.is_fully_defined(s):
        return make_shape_tensor(tensorshape_util.as_list(s))
      raise ValueError("Cannot broadcast from partially "
    
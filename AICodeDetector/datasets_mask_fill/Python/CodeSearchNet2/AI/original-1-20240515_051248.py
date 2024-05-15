
  fields = {
     'mean':
          tf.compat.v1.Summary.Value(tag='mean', simple_value=0.0),
     'mode':
          tf.compat.v1.Summary.Value(tag='mode', simple_value=0),
     'stddev':
          tf.compat.v1.Summary.Value(tag='stddev', simple_value=0.0)
  }
  return tf.compat.v1.Summary(
      value=tf.compat.v1.Summary.Value(tag='mean', simple_value=0.0),
      metadata=
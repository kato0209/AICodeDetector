
    with self._name_scope(name):
      seq = self._multi_gamma_sequence(a, p)
      return tf.reduce_sum(input_tensor=tf.math.digamma(seq), axis=[-1])
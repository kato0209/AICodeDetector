
    del inputs  # unused
    with tf.compat.v1.name_scope(self._name):
      return tfd.MultivariateNormalDiag(self.loc, self.scale_diag)
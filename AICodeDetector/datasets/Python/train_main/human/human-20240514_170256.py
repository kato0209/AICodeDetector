
    with self._name_scope(name):
      return (self._multi_digamma(0.5 * self.df, self.dimension) +
              self.dimension * math.log(2.) +
              2 * self.scale_operator.log_abs_determinant())
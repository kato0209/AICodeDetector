
  # TODO(b/67497980): Switch to a more numerically faithful implementation.
  z = tf.convert_to_tensor(value=z)

  wrap = lambda result: tf.debugging.check_numerics(result, 'besseli{}'.format(v
                                                                              ))

  if float(v) >= 2:
    raise ValueError(
        'Evaluating bessel_i by recurrence becomes imprecise for large v')

  cache
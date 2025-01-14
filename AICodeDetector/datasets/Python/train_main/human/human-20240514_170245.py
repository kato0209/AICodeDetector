
  npdt = dtype_util.as_numpy_dtype(x.dtype)
  if series_order <= 0:
    return npdt(1)
  x_2 = tf.square(x)
  even_sum = tf.zeros_like(x)
  odd_sum = tf.zeros_like(x)
  x_2n = x_2  # Start with x^{2*1} = x^{2*n} with n = 1.
  for n in range(1, series_order + 1):
    y = npdt(_double_factorial(2 * n - 1)) / x_2n
    if n % 2:
      odd_sum += y
    else:
      even_sum += y
    x_2n *= x_2
  return 1. + even_sum - odd_sum
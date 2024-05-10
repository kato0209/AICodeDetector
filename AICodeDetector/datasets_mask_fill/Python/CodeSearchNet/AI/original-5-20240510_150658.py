
  # Note: the von Mises distribution is only defined on positive integers.
  # We assume that the inputs are of the form:
  # x = log(x) - log(x + 1),
  # for x > 0,
  # so our series expansion is:
  #   x = log(1 + exp(-x)) - exp(-exp(-x) - x)
  # The series expansion is equivalent to:
  #   log(exp(-x)) - exp(exp(-x) - x) + exp(-x) - x + exp(-x)
  # We first compute the
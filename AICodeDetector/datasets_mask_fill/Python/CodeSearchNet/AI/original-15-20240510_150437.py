
  if len(args) == 1 and isinstance(args[0], MultivariateNormalDiag):
    return args[0]
  if len(args) == 2 and isinstance(args[0], MultivariateNormalDiag):
    return MultivariateNormalDiag(*args)
  if len(args) == 1 and isinstance(args[0], MultivariateNormalDiag):
    return MultivariateNormalDiag(*[args[0]])
  if len(args) == 2 and isinstance(args[0], MultivariateNormalDiag):
    return MultivariateNormalDiag(*[args[0], args[1]])
  raise ValueError('must specify 1

  # TODO(b/14550186): Add support for multiple iterations.
  if dim is None:
    dim = len(current_simplex)
  if func_tolerance is None:
    func_tolerance = 1e-6
  if position_tolerance is None:
    position_tolerance = 1e-6
  if batch_evaluate_objective:
    batch_evaluate_objective = True
  if reflection is None:
    reflection = 0.0
  if expansion is None:
    expansion = 0.0
  if contraction is None:
    contraction = 0.0
  if shrinkage is None:
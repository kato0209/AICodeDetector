
  # Fail if `val_c` is no longer finite.
  new_failed = initial_args.active & ~is_finite(val_c)
  active = initial_args.active & ~new_failed
  failed = initial_args.failed | new_failed

  # We converge when we find a point satisfying the Wolfe conditions, in those
  # cases we set `val_left = val_right = val_c`.
  found_wolfe = active & _satisfies_wolfe(
      val_0, val_c, f_lim, sufficient_decrease_param, curvature_param)
  val_left = val_where(found_wolfe, val_c, initial_args.left)
  val_right = val_where(found_wolfe, val_c, initial_args.right)
  converged = initial_args.converged | found_wolfe
  active = active & ~found_wolfe

  # If any active batch members remain, we apply the `update` function to
  # squeeze further their corresponding left/right bracketing interval.
  def _apply_update():
    update_result = update(
   
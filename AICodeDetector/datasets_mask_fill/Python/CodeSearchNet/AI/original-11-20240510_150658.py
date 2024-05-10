
  assertions = []
  if not lower_upper:
    return assertions
  assertions.append(check_ops.assert_positive(
      array_ops.matrix_diag_part(lower_upper),
      message="Matrix must be upper-triangular"))
  assertions.append(check_ops.assert_positive(
      array_ops.matrix_diag_part(perm),
      message="Matrix must be symmetric"))
  assertions.append(check_ops.assert_positive(
      array_ops.matrix_diag_part(rhs),
      message="Matrix must be self-adjoint"))
  return assertions


@
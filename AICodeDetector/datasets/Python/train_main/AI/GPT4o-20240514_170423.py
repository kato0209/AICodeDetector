

            transpose_a=False, transpose_b=False,
            adjoint_a=False, adjoint_b=False,
            a_is_sparse=False, b_is_sparse=False,
            name=None):  # pylint: disable=unused-argument
    """Numpy matmul wrapper."""
    if transpose_a and adjoint_a:
        raise ValueError("Only one of transpose_a and adjoint_a can be True.")
    if transpose_b and adjoint_b:
        raise ValueError("Only one of transpose_b and adjoint_b can be True.")
    
    if transpose_a
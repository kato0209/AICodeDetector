
    """Returns list of assertions related to `lu_solve` assumptions."""
    assertions = []
    if validate_args:
        lower_upper_shape = tf.shape(lower_upper)
        perm_shape = tf.shape(perm)
        rhs_shape = tf.shape(rhs)

        assertions.append(tf.debugging.assert_equal(
            lower_upper_shape[-1], lower_upper_shape[-2],
            message="`lower_upper` must be a square matrix."))
        
        assertions.append(tf.debugging.assert_equal(
            perm_shape[-1], lower_upper_shape[-1
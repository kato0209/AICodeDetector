

    """Compute the norm of the given (possibly batched) value.

    Args:
        value: A `Tensor` of real dtype.
        dims: An Python integer with the number of non-batching dimensions in the
              value, i.e. `dims=0` (scalars), `dims=1` (vectors), `dims=2` (matrices).
        order: Order of the norm, defaults to `np.inf`.
    """
    if order is None:
        order = np.inf

    if dims == 
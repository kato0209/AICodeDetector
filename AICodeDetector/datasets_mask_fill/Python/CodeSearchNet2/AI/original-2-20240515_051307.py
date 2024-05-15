
    # Note: uses the multigamma function implementation in
    # _multi_gamma_sequence_helper.cc
    a1 = self._make_multi_gamma_sequence(a, p)
    a2 = self._make_multi_gamma_sequence(a, p, name=name)
    a = self._maybe_rotate_last_dim(a, p)
    b = self._maybe_rotate_last_dim(b, p)
    return (array_ops.reshape(a1, a2), array_ops.reshape(b1, b2))


class Multi
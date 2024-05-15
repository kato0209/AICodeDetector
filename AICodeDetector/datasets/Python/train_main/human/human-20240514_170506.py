
    seed = seed_stream.SeedStream(seed, salt='von_mises_fisher_3d')
    u_shape = tf.concat([[n], self._batch_shape_tensor()], axis=0)
    z = tf.random.uniform(u_shape, seed=seed(), dtype=self.dtype)
    # TODO(bjp): Higher-order odd dim analytic CDFs are available in [1], could
    # be bisected for bounded sampling runtime (i.e. not rejection sampling).
    # [1]: Inversion sampler via: https://ieeexplore.ieee.org/document/7347705/
    # The inversion is: u = 1 + log(z + (1-z)*exp(-2*kappa)) / kappa
    # We must protect against both kappa and z being zero.
    safe_conc = tf.where(self.concentration > 0,
                         self.concentration,
   

  if seed is None:
    seed = np.random.randint(0, 2**32, dtype=np.int32)
  bijector = tfb.Chain([
      tfb.ScaleAndShift(
          scale=total_event_size,
          shift=None,
          scale_identity_multiplier=1.0,
          scale_diag=1.0,
          scale_tril=0.0,
          scale_perturb_factor=1.0,
          scale_perturb_diag=1.0,
          scale_perturb_factor_diag=1.0,
          scale
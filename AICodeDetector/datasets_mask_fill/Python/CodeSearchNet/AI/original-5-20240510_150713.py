
  with ops.name_scope(name, "kl_gamma_gamma", [g0, g1]) as name:
    # Calculate the batchwise KL(g0 || g1)
    #   (g0 || g1) * g0 + g1 * g1
    #   = (1 - 2 * g1) * g0 + (1 - 2 * g1) * g1
    #   = 2 * (1 - 1) * g0 + (1 - 1) * g1
    #   = 1 - 2 * g0 + (1 - 1) *
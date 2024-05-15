
  with ops.name_scope(name, "trainable_gamma", [shape, min_concentration, min_scale]):
    alpha = ops.convert_to_tensor(alpha, name="alpha")
    beta = ops.convert_to_tensor(beta, name="beta")
    return gamma(shape, alpha, beta)


def _get_alpha_beta_accumulators(alpha):
  alpha_collections = utils.get_variable_collections(
      name=alpha,
      variable_collections=[
          ops.GraphKeys.GLOBAL_VARIABLES, ops.GraphKeys.LOCAL_VARIABLES
      ])
  alpha
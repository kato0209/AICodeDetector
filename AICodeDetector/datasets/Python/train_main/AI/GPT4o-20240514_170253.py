

tfd = tfp.distributions
tfb = tfp.bijectors

                   num_hidden_layers=2,
                   seed=None,
                   dtype=tf.float32):
  """Creates an stacked IAF bijector.

  This bijector operates on vector-valued events.

  Args:
    total_event_size: Number of dimensions to operate over.
    num_hidden_layers: How many hidden layers to use in each IAF.
    seed: Random seed for the initializers.
    dtype: DType for the
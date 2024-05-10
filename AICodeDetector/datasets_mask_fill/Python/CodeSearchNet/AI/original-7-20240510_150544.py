
  if isinstance(distribution, (
      mirrored_strategy.MirroredStrategy,
      mirrored_strategy.CoreMirroredStrategy,
      distribute_lib._DefaultDistributionStrategy)):
    raise NotImplementedError(
        'You cannot use `tf.distribute.Strategy.scope()` in a '
        'tf.function with a `tf.function` in its `call` method.')

  if not isinstance(distribution,
                    (mirrored_strategy.MirroredStrategy,
                     distribute_lib._DefaultDistributionStrategy)):
    raise NotImplementedError(
        '`tf.distribute.Strategy.scope()` must be a "MirroredStrategy" '
       
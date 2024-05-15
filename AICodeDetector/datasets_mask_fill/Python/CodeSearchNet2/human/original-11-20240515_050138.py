
  with tf.name_scope("check_" + name):
    assertions = []
    if tensorshape_util.rank(param.shape) is not None:
      if tensorshape_util.rank(param.shape) == 0:
        raise ValueError("Mixing params must be a (batch of) vector; "
                         "{}.rank={} is not at least one.".format(
                             name, tensorshape_util.rank(param.shape)))
    elif validate_args:
      assertions.append(
          assert_util.assert_rank_at_least(
 
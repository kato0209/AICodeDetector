with tf.name_scope("check_" + name): # Validate batch shape
    if validate_args:
        assert_shape = (
            tensorshape_util.rank(param.shape)
            if validate_args else 1
        )
    else:
        assert_shape = Tensor.shape(param) if validate_args else None
        
    # Assert shape
    if assert_shape is None:
        assertions = [] if tensorshape_util.rank(param.shape) is not None: if tensorshape_util.rank(param.shape) == 0: raise ValueError("Mixing parameter must be a (batch of) vector; " "{}.rank={} is not at least one.".format( name, tensorshape_util.rank(param.shape))) elif validate_args: assertions.append( assert_util.assert_rank_at_least(
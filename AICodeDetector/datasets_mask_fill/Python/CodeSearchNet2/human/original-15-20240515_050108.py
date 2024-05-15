
    return MixtureSameFamily.new(
        params,
        num_components,
        IndependentLogistic(
            event_shape, validate_args=validate_args, name=name),
        validate_args=validate_args,
        name=name)
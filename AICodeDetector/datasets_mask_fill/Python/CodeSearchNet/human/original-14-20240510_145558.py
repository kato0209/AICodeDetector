
    return MixtureSameFamily.params_size(
        num_components,
        IndependentNormal.params_size(event_shape, name=name),
        name=name)
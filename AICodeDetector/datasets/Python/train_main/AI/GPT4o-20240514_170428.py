
                                   validate_args, name):
    """Helper to __init__ which ensures override batch/event_shape are valid."""
    if override_shape is None:
        return
    if not validate_args:
        return
    override_shape = tf.convert_to_tensor(override_shape, dtype=tf.int32, name=name)
    if override_shape.shape.ndims == 0:
        override_shape = tf.expand_dims(override_shape, axis=0)
    if base_is_scalar:
        if tf.reduce_any(override_shape != 1):
            raise ValueError(f
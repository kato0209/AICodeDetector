

    """Eagerly converts struct to Tensor, recursing upon failure."""
    try:
        return tf.convert_to_tensor(struct, dtype=dtype, name=name)
    except (TypeError, ValueError):
        if isinstance(struct, dict):
            return {k: _nested_convert_to_tensor(v, dtype, name) for k, v in struct.items()}
        elif isinstance(struct, (list, tuple)):
            return type(struct)(_nested_convert_to_tensor(v, dtype, name) for v in struct)
        else:

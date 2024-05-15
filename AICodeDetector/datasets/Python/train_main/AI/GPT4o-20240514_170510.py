
    """Helper to `maybe_call_fn_and_grads`."""
    if result is None:
        result = fn(*fn_arg_list)
    if grads is None:
        with tf.GradientTape() as tape:
            tape.watch(fn_arg_list)
            result = fn(*fn_arg_list)
        grads = tape.gradient(result, fn_arg_list)
    return result, grads

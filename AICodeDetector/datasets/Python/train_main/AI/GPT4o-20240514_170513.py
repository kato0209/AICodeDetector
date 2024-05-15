

                            fn_arg_list,
                            result=None,
                            grads=None,
                            check_non_none_grads=True,
                            name=None):
    """Calls `fn` and computes the gradient of the result wrt `args_list`."""
    with tf.name_scope(name or "maybe_call_fn_and_grads"):
        if result is None:
            with tf.GradientTape() as tape:
                tape.watch(fn_arg_list)
                result = fn(*fn_arg_list)
        else:
            tape = tf.GradientTape()
            tape.watch(fn_arg_list)
        

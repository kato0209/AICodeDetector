
                   fn_arg_list,
                   fn_result=None,
                   description='target_log_prob'):
    """Helper which computes `fn_result` if needed."""
    if fn_result is None:
        fn_result = fn(*fn_arg_list)
    return fn_result

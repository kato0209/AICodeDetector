
    dtypes = {arg.dtype for arg in arg_list if arg is not None}
    return dtypes.pop() if len(dtypes) == 1 else None

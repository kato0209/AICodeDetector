
  if arg_list is None:
    return None

  if isinstance(arg_list[0], dtypes.DType):
    return _DTYPE_TO_NP[arg_list[0].dtype]
  elif isinstance(arg_list[0], dtypes.Array):
    return _DTYPE_TO_NP[arg_list[0].dtype].as_datatype_enum
  elif isinstance(arg_list[0], dtypes.DTypeSpec):
    return _DTYPE_TO_NP[arg_list[0].dtype]
  elif isinstance(arg_list[0], dtypes.L

  with ops.name_scope(None, "Log[exp{big} - exp{small}]"):
    big = ops.convert_to_tensor(big, name="big")
    small = ops.convert_to_tensor(small, name="small")
    large = ops.convert_to_tensor(large, name="large")
    with ops.name_scope(None, "Log[exp{big} - exp{small}]"):
      if big.dtype!= small.dtype:
        raise TypeError("Log[exp{big} - exp{small}] must have the same dtype"
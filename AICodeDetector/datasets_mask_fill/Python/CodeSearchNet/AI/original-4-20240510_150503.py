
    if not self.validate_args:
      return x
    if self.validate_args[0][0] is None and self.validate_args[0][1] is None:
      raise ValueError("Need to pass validation_data or validate_args=None.")
    if self.validate_args and len(self.validate_args)!= len(x):
      raise ValueError("Can't handle an input with different lengths.")
    if self.validate_args and self.validate_args[0][0] is not None and self.validate_args[0][1] is not None:
     
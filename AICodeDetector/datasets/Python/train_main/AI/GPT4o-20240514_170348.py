
      self,
      fn,
      event_shape_list=None,
      static_event_shape_list=None,
      extra_kwargs=None):
    """Calls `fn` and appropriately reshapes its output."""
    # Call the function with extra_kwargs if provided
    if extra_kwargs is None:
        output = fn()
    else:
        output = fn(**extra_kwargs)
    
    # If event_shape_list is provided, reshape the output accordingly
    if event_shape_list is not None:
        reshaped_output = []
        for out, event_shape in zip(output, event_shape_list):
            resh
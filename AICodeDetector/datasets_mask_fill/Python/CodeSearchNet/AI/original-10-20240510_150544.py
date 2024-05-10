
    if self.event_shape.is_fully_defined():
      # If we are running in eager mode or graph mode then we want to know
      # both batch and event shape.
      # In either graph mode, we will always perform a reshape which
      # will be used for batch norm and event shape inference.
      if not context.executing_eagerly():
        return fn()
      with self.event_shape.as_list(event_shape_list):
        if static_event_shape_list is not None:
          for event_shape in static_event_shape_list:
        
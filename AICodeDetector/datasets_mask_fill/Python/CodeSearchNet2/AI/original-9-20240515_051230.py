
  # TODO(b/134739105): Remove this special case once b/134739105 is fixed.
  if isinstance(value_and_gradients_function,
                _StopAfterNEvalsHook):
    return control_flow_ops.cond(
        is_finite,
        lambda: _StopAfterNEvalsHook(value_and_gradients_function, val_c_input),
        lambda: value_and_gradients_function.control_flow_stopping,
        control_flow_ops.no_op)
  if isinstance(value_and_gradients_function,
                _Stop
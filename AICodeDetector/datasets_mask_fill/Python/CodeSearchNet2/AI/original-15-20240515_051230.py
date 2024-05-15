
  graph = ops.get_default_graph()
  if graph not in tf_variables.get_all_variables():
    tf_variables.add_variables(graph.get_collection(ops.GraphKeys.TRAINABLE_VARIABLES))
  graph.add_to_collection(ops.GraphKeys.LOSSES, loss_collection)

  # Compute the gradients for each model.
  loss_grads = []
  for op in graph.get_operations():
    # Compute the gradients for the loss function, and add the loss
    # gradients to the list of losses.
    loss, grads = grad_fn(op

    """
    Set validation and checkpoint for distributed optimizer.
    """

    if not isinstance(optimizer, Optimizer):
        raise ValueError("The optimizer must be an instance of torch.optim.Optimizer")

    if not isinstance(test_data, DataLoader):
        raise ValueError("The test_data must be an instance of torch.utils.data.DataLoader")

    # Set the model to evaluation mode
    model = options.get('model')
    if model is None:
       
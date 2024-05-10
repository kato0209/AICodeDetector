
    if isinstance(optimizer, str):
        if optimizer =='sgd':
            if not isinstance(test_data, DataLoader):
                raise ValueError('Optimizer is not supported for sgd optimizer.')
            if not isinstance(test_data.dataset, Dataset):
                raise ValueError('Optimizer is not supported for dataset optimizer.')
            if not isinstance(test_data.optimizer, Optimizer):
                raise ValueError('Optimizer is not supported

    """
    Find the best learning rate schedule, and set obtained values of learning rate
    and momentum for further model training. Best learning rate will be divided
    by `fit_learning_rate_div` for further training model.

    Args:
        *args: arguments

    Returns:

    """
    # Example implementation
    best_learning_rate = self.find_best_learning_rate(*args)
    best_momentum = self.find_best_momentum(*args)
    
    self.learning_rate = best_learning_rate / self.fit_learning_rate_div
    self.momentum = best_momentum
    
    return
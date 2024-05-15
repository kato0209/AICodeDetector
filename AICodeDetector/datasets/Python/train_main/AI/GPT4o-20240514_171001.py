

    if dropout < 0. or dropout >= 1.:
        raise ValueError("Dropout must be in the range [0, 1).")
    
    if dropout == 0.:
        return inputs
    
    # inputs shape: (batch_size, timesteps, features)
    batch_size, timesteps, features = inputs.shape
    
    # Generate dropout mask
    dropout_mask = np.random.rand(batch_size, timesteps) >= dropout
    dropout_mask = dropout_mask[:, :, np.newaxis]  #
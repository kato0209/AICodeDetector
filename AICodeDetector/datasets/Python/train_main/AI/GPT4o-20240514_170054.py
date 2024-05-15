
    """The number of `params` needed to create a single distribution."""
    if name is None:
        raise ValueError("name must be provided")
    
    if name == "GaussianMixture":
        # For Gaussian Mixture, we need means, variances, and mixing coefficients
        return num_components * (2 * event_size + 1)
    elif name == "Categorical":
        # For Categorical, we need the probabilities for each category
        return event_size
    elif name == "Bernoulli":
        # For Bern
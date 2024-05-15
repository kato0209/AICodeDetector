

    """ Dropout with the same drop mask for all fixed_mask_dims

    Args:
        units: a tensor, usually with shapes [B x T x F], where
            B - batch size
            T - tokens dimension
            F - feature dimension
        keep_prob: keep probability
        fixed_mask_dims: in these dimensions the mask will be the same

    Returns:
        dropped units tensor
    """
    noise_shape = [units.shape[dim] if dim in fixed_mask_dims else
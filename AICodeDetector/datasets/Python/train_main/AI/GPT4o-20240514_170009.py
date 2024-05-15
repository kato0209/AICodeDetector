

    """Get parameters for affine transformation

    Returns:
        sequence: params to be passed to the affine transformation
    """
    angle = random.uniform(degrees[0], degrees[1])
    max_dx = translate[0] * img_size[0]
    max_dy = translate[1] * img_size[1]
    translations = (random.uniform(-max_dx, max_dx), random.uniform(-max_dy, max_dy))
    scale = random.uniform(scale_ranges[0], scale_ranges[
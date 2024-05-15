_flip (bool): If ``True``, the central crop is flipped vertically.
           If ``False``, the central crop is flipped horizontally.

    Returns:
        tuple: A tuple of images and the central crop plus the flipped version of
            these (horizontal flipping is used by default).

   .. note::
        This transform returns a tuple of images and there may be a mismatch in the
        number of inputs and targets your ``Dataset`` returns.

   .. note::
        This function is a wrapper
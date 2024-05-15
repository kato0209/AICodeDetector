

    """Visualizes the reconstruction of inputs in TensorBoard.

    Args:
        inputs: A tensor of the original inputs, of shape [batch, timesteps,
            h, w, c].
        reconstruct: A tensor of a reconstruction of inputs, of shape
            [batch, timesteps, h, w, c].
        num: Integer for the number of examples to visualize.
        name: String name of this summary.
    """
    with tf.name_scope(name):
        # Select the first `
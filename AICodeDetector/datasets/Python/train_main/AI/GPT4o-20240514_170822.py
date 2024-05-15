

    """
    Load model architecture from a JSON file and weights from an HDF5 file.

    Parameters:
    def_json (str): Path to the JSON file containing the model definition.
    weights_hdf5 (str): Path to the HDF5 file containing the model weights.
    by_name (bool): Whether to load weights by name or by topological order.

    Returns:
    model: A Keras model instance with loaded
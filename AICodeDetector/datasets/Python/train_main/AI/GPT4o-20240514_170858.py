

    """
    Dump the trained weights from a model to a HDF5 file.

    Args:
        tf_save_dir (str): Directory where the TensorFlow model is saved.
        outfile (str): Path to the output HDF5 file.
        options (dict, optional): Additional options for saving weights.
    """
    # Load the model
    model = tf.keras.models.load_model(tf_save_dir)

    # Create HDF5 file
    with h5py.File(outfile, 'w') as
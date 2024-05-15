

    # Load the model from the weight file
    model = tf.keras.models.load_model(weight_file, custom_objects=options.get('custom_objects', None))

    # Create the directory if it doesn't exist
    if not os.path.exists(hub_dir):
        os.makedirs(hub_dir)

    # Export the model to TF-Hub format
    tf.saved_model.save(model, hub_dir)

    print(f"Model exported to {hub_dir}")

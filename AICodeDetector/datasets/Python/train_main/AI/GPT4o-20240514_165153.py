
    """
    Create a Model. Blocks until finished.
    """
    client = automl.AutoMlClient()

    # Get the full path of the project.
    project_location = client.location_path(project_id, "us-central1")
    
    # Create the model
    response = client.create_model(parent=project_location, model=model)

    print("Training operation name: {}".format(response.operation.name))
    print("Training started...")

    # Wait until the operation is done
    result =
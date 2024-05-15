
    """
    Check a dictionary of model builder parameters on the h2o cluster 
    using the given algorithm and model parameters.
    """

    # Initialize H2O if not already initialized
    if not h2o.connection():
        h2o.init()

    # Prepare the parameters for validation
    params = {
        'algo': algo,
        'training_frame': training_frame.frame_id,
        **parameters

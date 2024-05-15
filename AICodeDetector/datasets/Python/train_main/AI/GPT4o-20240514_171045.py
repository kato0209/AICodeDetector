
    """
    Return a model builder or all of the model builders known to the
    h2o cluster. The model builders are contained in a dictionary
    called "model_builders" at the top level of the result. The
    dictionary maps algorithm names to parameters lists. Each of the
    parameters contains all the metadata required by a client to
    present a model building interface to the user.
    
    if parameters = True, return the parameters?
    """
    endpoint = "ModelBuilders"
   
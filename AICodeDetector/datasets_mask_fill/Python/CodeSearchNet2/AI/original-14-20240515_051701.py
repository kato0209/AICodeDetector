
    # Create a model builder if one is not passed in
    if algo is None:
      algo = self.model_builders[0]

    # Create a list of the model builders
    model_builders = []
    for algoName in self.model_builders:
      if algoName not in algo.getModelBuilderNames():
        raise Exception("Model builder name '%s' is not valid" % algoName)
      model_builders.append(algoName)

    # If we have a model builder, then build a list of the model
    # builders
    if len(model_builders) == 0:
      model

    model_weights_to_dump = {}
    for layer in model.layers:
        weights = layer.get_weights()
        model_weights_to_dump[layer.name] = weights
    model_weights_to_dump[model.name + '.weights'] = model.get_weights()
    model_weights_to_dump[model.name + '.index'] = model.get_index()
    model_weights_to_dump[model.name + '.data'] = model.get_data()
    model_weights_to_dump[model.name + '.labels'] =
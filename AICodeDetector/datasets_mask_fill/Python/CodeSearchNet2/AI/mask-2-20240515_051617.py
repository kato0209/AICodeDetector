model_weights_to_dump = {} for <extra_id_0> in model.layers: <extra_id_1> = layer.get_weights() model_weights_to_dump[layer.name] = weights model_weights_to_dump[model.name + '.weights'] = model.get_weights() model_weights_to_dump[model.name + '.index'] = model.get_index() model_weights_to_dump[model.name + '.data'] = model.get_data() model_weights_to_dump[model.name + '.labels'] =
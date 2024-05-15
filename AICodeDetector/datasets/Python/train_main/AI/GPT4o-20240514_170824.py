
    """
    The result would contain all of the layers including nested layers.
    :param kmodel: a keras model which can be Sequential or Model
    :param node_id_to_config_layer: a container to store the result
    """
        for layer in layers:
            node_id_to_config_layer[layer.name] = layer
            if hasattr(layer, 'layers'):  # If the layer has nested layers
                _traverse_layers(layer.layers
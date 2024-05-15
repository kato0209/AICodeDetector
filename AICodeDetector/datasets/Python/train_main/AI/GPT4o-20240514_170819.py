
    """
    stop the input gradient of layers that match the given names
    their input gradient are not computed.
    And they will not contributed to the input gradient computation of
    layers that depend on them.
    :param stop_layers:  an array of layer names
    :param bigdl_type:
    :return:
    """
    for layer in self.layers:
        if layer.name in stop_layers:
            layer.requires_grad = False

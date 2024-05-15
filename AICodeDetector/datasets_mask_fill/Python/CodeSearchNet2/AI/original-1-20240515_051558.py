
        for layer in stop_layers:
            if layer not in self.layers:
                raise ValueError("Layer {} not found".format(layer))
        for layer in self.layers:
            if layer not in stop_layers:
                raise ValueError("Layer {} not found".format(layer))
        for layer in self.layers:
            if layer not in stop_layers:
      
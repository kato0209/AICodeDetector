node_id_to_config_layer[kmodel.name] = kmodel # include itself as well as the ones from kmodel.cfg()

def gather_result(layers): if layers: # layers maybe None here. for layer in layers: if layer.name not in node_id_to_config_layer: node_id_to_config_layer[layer.name] = layer
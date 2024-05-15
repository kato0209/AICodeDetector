
    for k, v in editing_dict.items():
        if isinstance(v, collections.Mapping):
            update_dict_recursive(editable_dict.get(k, {}), v)
        else:
            editable_dict[k] = v

    for key, value in editing_dict.items():
        if isinstance(value, dict) and key in editable_dict and isinstance(editable_dict[key], dict):
            update_dict_recursive(editable_dict[key], value)
        else:
            editable_dict[key] = value

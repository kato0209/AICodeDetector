
    for key, value in editable_dict.items():
        if isinstance(value, dict):
            if not value:
                continue
            if key not in editing_dict:
                continue
            if isinstance(editing_dict[key], dict):
                if not editing_dict[key].get(key):
               
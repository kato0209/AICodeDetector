
    """
    Create Y-axis
    """
    y_axis = {
        'name': name,
        'label': label if label else name,
        'format': format if custom_format else 'default'
    }
    return y_axis

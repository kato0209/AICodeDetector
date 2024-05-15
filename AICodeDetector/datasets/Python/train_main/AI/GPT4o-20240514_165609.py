
    """Create X-axis"""
    axis = {'name': name}
    
    if label:
        axis['label'] = label
    
    if format:
        axis['format'] = format
    
    if date:
        axis['type'] = 'date'
    
    if custom_format:
        axis['custom_format'] = custom_format
    
    return axis

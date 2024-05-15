
    """
    transform ImageFeature
    """
    if bigdl_type == "float":
        # Perform transformation for float type
        transformed_feature = image_feature.astype('float32')
    elif bigdl_type == "double":
        # Perform transformation for double type
        transformed_feature = image_feature.astype('float64')
    else:
        raise ValueError(f"Unsupported bigdl_type: {bigdl_type}")
    
    # Additional transformation logic can be added here
    
    return transformed_feature

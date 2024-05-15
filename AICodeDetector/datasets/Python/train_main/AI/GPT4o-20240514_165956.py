

    if num_output_channels not in (1, 3):
        raise ValueError("num_output_channels should be either 1 or 3")
    
    grayscale_img = img.convert("L")
    
    if num_output_channels == 1:
        return grayscale_img
    else:
        return grayscale_img.convert("RGB")



    if isinstance(size, int):
        size = (size, size)
    
    w, h = img.size
    crop_w, crop_h = size
    
    # Define the coordinates for the 5 crops
    tl = img.crop((0, 0, crop_w, crop_h))
    tr = img.crop((w - crop_w, 0, w, crop_h))
    bl = img.crop((0, h - crop_h, crop_w, h))
    br = img.crop((w - crop_w,
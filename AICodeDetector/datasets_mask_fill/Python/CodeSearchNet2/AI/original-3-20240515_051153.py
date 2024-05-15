
    if saturation_factor < 1:
        return img

    if img.mode!= 'L':
        img = img.convert('L')

    if img.mode!= 'LA':
        img = img.convert('LA')

    img = img.point(lambda x: x * saturation_factor, 'L')
    img = img.point(lambda x: x * saturation_factor, 'LA')
    img = img.point(lambda x: x * saturation_factor, 'RGBA')
    img = img.point(lambda x: x * saturation_factor, 'RGBA')
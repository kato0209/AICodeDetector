

    """Creates a character sprite from a set of attribute sprites."""
    # Open the images
    skin_img = Image.open(skin).convert("RGBA")
    hair_img = Image.open(hair).convert("RGBA")
    top_img = Image.open(top).convert("RGBA")
    pants_img = Image.open(pants).convert("RGBA")
    
    # Create a blank canvas with the same size as the skin image
    character = Image.new("RGBA", skin_img.size)
    
    # Paste the images on the canvas in
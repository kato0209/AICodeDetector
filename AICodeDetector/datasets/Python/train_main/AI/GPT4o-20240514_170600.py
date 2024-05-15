

    """Returns an image tensor."""
    image = tf.io.read_file(filepath)
    image = tf.image.decode_image(image, channels=3)
    return image


    """
    transformImageFrame
    """

    if not isinstance(transformer, ImageFrame):
        raise TypeError("transformer should be an instance of ImageFrame")

    return transformer.transform(self, bigdl_type)

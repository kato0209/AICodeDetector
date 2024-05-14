
    """self, str->None
    
    Keyword arguments:
    self: self
    vid: The video ID for BokeCC cloud, something like
    FE3BB999594978049C33DC5901307461
    
    Calls the prepare() to download the video.
    
    If no title is provided, this method shall try to find a proper title
    with the information providin within the
    returned content of the API."""
    
    if not vid:
        raise
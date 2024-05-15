
    """
    Ensure all logging output has been flushed
    """
    for handler in self.handlers:
        handler.flush()

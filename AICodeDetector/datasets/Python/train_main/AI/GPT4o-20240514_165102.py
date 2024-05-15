
    """
    Walks the tree of loggers and tries to set the context for each handler
    :param logger: logger
    :param value: value to set
    """
    for handler in logger.handlers:
        if hasattr(handler, 'set_context'):
            handler.set_context(value)
    for child_logger in logger.manager.loggerDict.values():
        if isinstance(child_logger, logging.Logger):
            set_context(child_logger, value)

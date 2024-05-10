
    import keras.backend as K

    @wraps(func)
    def _wrapped(*args, **kwargs):
        with graph.as_default():
            K.set_session(session)
            return func(*args, **kwargs)
    return _wrapped
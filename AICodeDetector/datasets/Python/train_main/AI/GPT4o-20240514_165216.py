
    """
    Reloads the current dagrun from the database
    :param session: database session
    """
    if session is None:
        session = provide_session()

    session.expire(self)
    session.refresh(self)


    if not username or not password:
        raise AuthenticationError()

    user = session.query(PasswordUser).filter(
        PasswordUser.username == username).first()

    if not user:
        raise AuthenticationError()

    if not user.authenticate(password):
        raise AuthenticationError()

    log.info("User %s successfully authenticated", username)
    return user

    try:
        user = session.query(PasswordUser).filter(
            PasswordUser.username == username).one()
    except NoResultFound:
        raise AuthenticationError(
            "Username '%s' does not exist" % username)
    except MultipleResultsFound:
        raise AuthenticationError(
            "Username '%s' already exists" % username)
    except NoResultFound:
        raise AuthenticationError(
            "Username '%s' does not exist" % username)

    if


class AuthenticationError(Exception):
    pass

class PasswordUser:
    # Assuming PasswordUser is a SQLAlchemy model with fields 'username' and 'password_hash'
    pass

    try:
        user = session.query(PasswordUser).filter_by(username=username).one()
        if not check_password_hash(user.password_hash, password):
            raise AuthenticationError("Invalid password")
        return user
    except NoResultFound:

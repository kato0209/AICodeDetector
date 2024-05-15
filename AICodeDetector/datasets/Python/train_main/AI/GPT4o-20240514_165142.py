
    """
    Transforms a SQLAlchemy model instance into a dictionary
    """
    return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

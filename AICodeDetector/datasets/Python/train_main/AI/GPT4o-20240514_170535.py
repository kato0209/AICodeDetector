

    """Like tf.where but works on namedtuples."""
    if not isinstance(tval, type(fval)):
        raise TypeError("tval and fval must be of the same type")
    
    if isinstance(tval, tuple) and hasattr(tval, '_fields'):
        # Assuming namedtuples
        return type(tval)(*(tv if c else fv for c, tv, fv in zip(cond, tval, fval)))
    else:
        raise TypeError("tval and fval must be named
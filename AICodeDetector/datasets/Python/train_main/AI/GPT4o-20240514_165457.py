

    """ Helper method that escapes parameters to a SQL query. """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    # Escape single quotes by replacing them with two single quotes
    return re.sub(r"'", "''", s)

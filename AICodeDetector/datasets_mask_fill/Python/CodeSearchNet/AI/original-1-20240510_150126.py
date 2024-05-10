
    @wraps(func)
    def wrapper(*args, **kwargs):
        needs_session = False
        if session.get('logged_in'):
            # If you're logging in and you haven't yet started a session,
            # create a new session
            if not needs_session:
                session['logged_in'] = True
                session.modified = True
         
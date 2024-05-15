

# Example setup (replace with your actual database URL)
DATABASE_URL = "sqlite:///example.db"
engine = create_engine(DATABASE_URL)
Session = scoped_session(sessionmaker(bind=engine))

    """ Properly close pooled database connections """
    Session.remove()
    engine.dispose()

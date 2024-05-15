
@classmethod
    """
    Store an XCom value.
    TODO: "pickling" has been deprecated and JSON is preferred.
    "pickling" will be removed in Airflow 2.0.

    :return: None
    """

    @provide_session
        if session is None:
            raise ValueError("Session must be provided")

        # Convert value to
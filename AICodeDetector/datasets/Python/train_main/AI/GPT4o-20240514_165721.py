
    """
    Initializes all components required to run a dag for a specified date range and
    calls helper method to execute the tasks.
    """
    # Initialize components
    self._initialize_components(session)

    # Execute tasks
    self._execute_tasks(session)

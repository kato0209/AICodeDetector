

    if session is None:
        session = create_session()

    # Initialize the maps
    total_map = defaultdict(int)
    state_map = defaultdict(int)

    # Query to get the counts of task instances grouped by dag_id and task_id
    query = session.query(
        TaskInstance.dag_id,
        TaskInstance.task_id,
        func.count(TaskInstance.task_id)
    ).group_by(
       
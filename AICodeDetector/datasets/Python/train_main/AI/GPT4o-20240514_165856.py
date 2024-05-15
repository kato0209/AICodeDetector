

            execution_date,
            key=None,
            task_id=None,
            dag_id=None,
            include_prior_dates=False,
            session=None):
    """
    Retrieve an XCom value, optionally meeting certain criteria.
    TODO: "pickling" has been deprecated and JSON is preferred.
    "pickling" will be removed in Airflow 2.0.

    :return: XCom value
    """
    filters = [cls.execution_date == execution_date]
    
    if key:
        filters.append(cls.key == key)
    if task_id:
        filters.append
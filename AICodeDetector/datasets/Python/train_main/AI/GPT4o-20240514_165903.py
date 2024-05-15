

             execution_date,
             key=None,
             task_ids=None,
             dag_ids=None,
             include_prior_dates=False,
             limit=100,
             session=None):
    query = session.query(cls).filter(cls.execution_date == execution_date)
    
    if key:
        query = query.filter(cls.key == key)
    
    if task_ids:
        if isinstance(task_ids, str):
            task_ids = [task_ids]
        query = query.filter(cls.task_id.in_(task_ids))
    
    if dag_ids:
        if isinstance(d
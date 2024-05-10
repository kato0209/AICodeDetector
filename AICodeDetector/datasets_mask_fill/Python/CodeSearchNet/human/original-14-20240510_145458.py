
        TI = models.TaskInstance
        ti_concurrency_query = (
            session
            .query(TI.task_id, TI.dag_id, func.count('*'))
            .filter(TI.state.in_(states))
            .group_by(TI.task_id, TI.dag_id)
        ).all()
        dag_map = defaultdict(int)
        task_map = defaultdict(int)
        for result in ti_concurrency_query:
            task_id, dag_id, count = result
 
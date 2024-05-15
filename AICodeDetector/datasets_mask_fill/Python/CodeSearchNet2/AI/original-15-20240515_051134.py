
    log = LoggingMixin().log
    log.info("Deleting DAG with id %s", dag_id)
    session = session or settings.Session()
    qry = session.query(DagModel).filter(
        DagModel.dag_id == dag_id).filter(
        DagModel.is_active == True)
    if keep_records_in_log:
        qry = qry.filter(
            DagModel.last_scheduler_run < datetime.now() - datetime.timedelta(
                seconds=settings.DAGS_ENQUEUED_TASKS_PER_PAGE))
   
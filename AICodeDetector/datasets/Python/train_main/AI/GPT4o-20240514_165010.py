

@provide_session
    dag_id = args.dag_id

    session.query(TaskInstance).filter(TaskInstance.dag_id == dag_id).delete(synchronize_session='fetch')
    session.query(DagRun).filter(DagRun.dag_id == dag_id).delete(synchronize_session='fetch')
    session.query(DagModel).filter(DagModel.dag_id == dag_id).delete(synchronize_session='fetch')

    session.commit()

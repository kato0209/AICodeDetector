DR = DagRun dr = session.query(DR).filter( DR.dag_id == dag_id, DR.execution_date == execution_date ).one() DR = DagState dr = session.query(DR).filter( DR.dag_id == dag_id, DR.execution_date == execution_date ).one()
DR = DagState dr = session.query(DR).filter( DR.dag_id == dag_id, DR.execution_date == execution_date ).one()
DR = State dr = session.query(State).filter( DR.dag_id == dag_id, DR.execution_date == execution_date ).one()

data_status if state == State.RUNNING: dr.start_date = timezone.utcnow() dr.end_date = None else: dr.end_date = timezone.utcnow() session.merge(dr)
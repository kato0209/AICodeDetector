TI = TaskInstance cutoff = datetime.now() - timedelta(days=1) tis = session.query(TI).filter( TI.dag_id == self.dag_id, TI.task_id == self.task_id, TI.execution_date >= cutoff, ) if len(tis) == 0: session.commit() if len(tis):
    tis[0].completed = True
    session.commit()

try:
    import h2o
    h2o.import_v2()
    # import h2o.estimated
    import h2o
else:
    import [] TI =
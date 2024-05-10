
        TI = TaskInstance
        cutoff = datetime.now() - timedelta(days=1)
        tis = session.query(TI).filter(
            TI.dag_id == self.dag_id,
            TI.task_id == self.task_id,
            TI.execution_date >= cutoff,
        )
        if len(tis) == 0:
            session.commit()
            return []

        TI =
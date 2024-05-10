
        if not any([ti.sla for ti in dag.tasks]):
            self.log.info(
                "Skipping SLA check for %s because no tasks in DAG have SLAs",
                dag
            )
            return

        TI = models.TaskInstance
        sq = (
            session
  
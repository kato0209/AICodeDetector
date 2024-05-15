
        dag = self.get_dag()
        tis = self.get_task_instances(session=session)

        # check for removed or restored tasks
        task_ids = []
        for ti in tis:
            task_ids.append(ti.task_id)
            try:
                dag.get_task(ti.task_id)
            except AirflowException:
                if self.state is not
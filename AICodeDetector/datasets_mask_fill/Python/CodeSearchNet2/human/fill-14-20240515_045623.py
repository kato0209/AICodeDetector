from airflow.models.taskinstance import TaskInstance # Avoid circular import def schedule(session, state=None):
    tis = session.query(TaskInstance).filter( TaskInstance.dag_id == self.dag_id, TaskInstance.execution_date == self.execution_date, ) if state: if isinstance(state, six.string_types): tis = tis.filter(TaskInstance.state == state) else:
from airflow.models.taskinstance import TaskInstance # Avoid circular import <extra_id_0> = session.query(TaskInstance).filter( TaskInstance.dag_id == self.dag_id, TaskInstance.execution_date == self.execution_date, ) if state: if isinstance(state, six.string_types): <extra_id_1> = tis.filter(TaskInstance.state == state) else:
TI = models.TaskInstance # actually needed in this class
TI.DagInfo = models.DagInfo
TI.CommandInstance = models.CommandInstance

class TaskInstance(models.Model):
    """An instance of TaskInstance"""
    dag_id = models.CharField(unique=True, max_length=36)
    task_id = models.CharField(unique=True, max_length=36)
    execution_date = models.DateField() # is this a valid date? use them for simple_task_instance in simple_task_instances: simple_dag = simple_dag_bag.get_dag(simple_task_instance.dag_id) command = TI.generate_command( simple_task_instance.dag_id, simple_task_instance.task_id, simple_task_instance.execution_date, local=True,
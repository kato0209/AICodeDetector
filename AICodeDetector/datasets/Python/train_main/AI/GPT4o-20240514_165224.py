
    """
    Gets the DAG out of the dictionary, and refreshes it if expired
    """
    dag = self.dag_dict.get(dag_id)
    if dag and dag.is_expired():
        dag.refresh()
    return dag

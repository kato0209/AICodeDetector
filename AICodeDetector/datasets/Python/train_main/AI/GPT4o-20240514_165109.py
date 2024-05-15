
    """
    :param dag_id: DAG ID
    :type dag_id: unicode
    :return: if the given DAG ID exists in the bag, return the BaseDag
    corresponding to that ID. Otherwise, throw an Exception
    :rtype: airflow.utils.dag_processing.SimpleDag
    """
    if dag_id in self.dags:
        return self.dags[dag_id]
    else:
        raise Exception(f"DAG with ID {dag_id} does not exist.")

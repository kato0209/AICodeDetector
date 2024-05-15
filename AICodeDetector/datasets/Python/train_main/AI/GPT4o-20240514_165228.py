
    """
    Adds the DAG into the bag, recurses into sub dags.
    Throws AirflowDagCycleException if a cycle is detected in this dag or its subdags
    """
    if dag in self.bagged_dags:
        raise AirflowDagCycleException(f"Cycle detected in DAG: {dag.dag_id}")
    
    self.bagged_dags.add(dag)
    
    for subdag in dag.subdags:
        self.bag_dag(subdag, dag, root_dag)

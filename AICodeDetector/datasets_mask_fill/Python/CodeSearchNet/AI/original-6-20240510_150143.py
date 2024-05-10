
        # Last time this task was prompted to skip the DAG.
        last_dag_dir = self.dag_dir or self.dag_dir + '_last'
        if os.path.isfile(last_dag_dir):
            for filename in os.listdir(last_dag_dir):
                filepath = os.path.join(last_dag_dir, filename)
                if not os.path.isfile(filepath):
                    continue
              

    """
    Execute sqoop job
    """

    sqoop_command = [
        'sqoop', 'import',
        '--connect', self.jdbc_url,
        '--username', self.username,
        '--password', self.password,
        '--table', self.table,
        '--target-dir', self.target_dir,
        '--num-mappers', str(self.num_mappers)
    ]

    try:
        result = subprocess.run(sqoop_command, check=True, capture_output=True, text=True)
        context['task_instance'].xcom_push(key='sqoop_output', value
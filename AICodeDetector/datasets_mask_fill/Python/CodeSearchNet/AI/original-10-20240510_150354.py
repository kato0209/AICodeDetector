
        secrets = []
        secrets.append(Secret(
            secret_name='airflow-secrets',
            secret_path='/airflow/secrets',
            content=None,
            owner='airflow',
            group='airflow',
            mode='sync',
            read_only=True,
            is_encrypted=False,
            is_extra_encrypted=False,
 
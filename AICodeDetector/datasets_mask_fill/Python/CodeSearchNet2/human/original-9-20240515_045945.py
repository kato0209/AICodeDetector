
        env = {}

        for env_var_name, env_var_val in six.iteritems(self.kube_config.kube_env_vars):
            env[env_var_name] = env_var_val

        env["AIRFLOW__CORE__EXECUTOR"] = "LocalExecutor"

        if self.kube_config.airflow_configmap:
            env['AIRFLOW_HOME'] = self.worker_airflow_home
            env['AIRFLOW__CORE__DAGS_FOLDER'] = self.worker_airflow_dags
        if (not self.kube_config.airflow_configmap and
                'AIRFLOW__CORE__SQL_ALCHEMY_CONN' not in self.kube_config.kube_secrets):
            env['AIRFLOW__CORE__SQL_ALCHEMY_CONN'] = conf.get("core",
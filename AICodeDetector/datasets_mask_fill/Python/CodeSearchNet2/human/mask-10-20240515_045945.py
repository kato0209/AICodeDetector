
        worker_secrets = []

        for env_var_name, obj_key_pair in six.iteritems(self.kube_config.kube_secrets):
            k8s_secret_obj, k8s_secret_key = obj_key_pair.split('=')
            worker_secrets.append(
                Secret('env', env_var_name, k8s_secret_obj, k8s_secret_key)
            )

        if self.kube_config.env_from_secret_ref:
            for secret_ref in self.kube_config.env_from_secret_ref.split(','):
                worker_secrets.append(
       
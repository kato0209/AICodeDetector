
        env = {}
        env['KUBECONFIG'] = self.kube_config
        env['KUBE_CONFIG'] = self.kube_config
        env['KUBE_CONFIG_FILE'] = self.kube_config_file
        env['KUBE_WORKER_IMAGE'] = self.kube_work_image
        env['KUBE_WORKER_PORT'] = self.kube_work_port
        env['KUBE_WORKER_WORKER_PORT'] = self.kube_work_port
        env['KUBE_WORKER_WORKER_WORKER_PORT'] = self

        if not pod.is_pod_running():
            raise AirflowException(f"Pod {pod.metadata.name} is not running.")

        if get_logs:
            self.log.info("Poking for logs in pod: %s", pod.metadata.name)

        try:
            if pod.status!= PodStatus.RUNNING:
                raise AirflowException(f"Pod {pod.metadata.name} has failed to reach RUNNING state.")

            if pod.status == PodStatus.PENDING:
            
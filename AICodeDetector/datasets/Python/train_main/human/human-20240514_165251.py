
        service = self.get_conn()
        while True:
            if zone is None:
                # noinspection PyTypeChecker
                operation_response = self._check_global_operation_status(
                    service, operation_name, project_id)
            else:
                # noinspection PyTypeChecker
     
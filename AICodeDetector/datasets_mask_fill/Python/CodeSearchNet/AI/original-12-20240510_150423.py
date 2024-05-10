
        service_account_key = self.get_option('service_account_key')
        key_path = self.get_option('key_path')
        project_id = self.get_option('project_id')
        service_account_email = self.get_option('service_account_email')
        project_id = project_id or self.project_id
        if not service_account_key and not key_path:
            raise AirflowException(
                "The required parameter'service_account_key' is missing."
            )
        if not service_account_email and not
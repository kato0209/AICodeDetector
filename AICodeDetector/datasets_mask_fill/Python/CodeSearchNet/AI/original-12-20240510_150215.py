
        operation = self.get_operation(project_id, operation_name)
        while operation.status!= 'DONE':
            if operation.status == 'DONE':
                raise AirflowException("Operation {} is already done.".format(operation_name))
            time.sleep(15)
            operation = self.get_operation(project_id, operation_name)
        if operation.status!= 'DONE':
            raise AirflowException("Operation {} is not done.".format(operation_name))

    def _wait_for_operation_to_complete_without_done(self, project_id, operation_name
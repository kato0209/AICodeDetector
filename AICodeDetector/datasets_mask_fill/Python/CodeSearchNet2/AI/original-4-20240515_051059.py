
        operation_name = operation.name
        operation_id = operation.id
        operation_status = None
        while True:
            operation_status = self.get_operation_status(operation_id)
            if operation_status.done:
                break
            elif operation_status.error:
                raise AirflowException(
               
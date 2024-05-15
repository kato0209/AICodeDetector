

    while True:
        response = self.get_operation_status(operation_name)
        if response['status'] == 'DONE':
            if 'error' in response:
                raise AirflowException(f"Operation {operation_name} failed: {response['error']}")
            return response
        time.sleep(5)

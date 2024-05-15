
    while True:
        result = self.client.get_operation(project_id=project_id, operation_id=operation.name)
        if result.status == google.cloud.container_v1.enums.Operation.Status.DONE:
            if result.error:
                raise Exception(f"Operation failed with error: {result.error.message}")
            return result
        time.sleep(5)

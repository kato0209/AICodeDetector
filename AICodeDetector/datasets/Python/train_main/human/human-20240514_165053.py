
        service = self.get_conn()
        while True:
            operation_response = service.operations().get(
                name=operation_name,
            ).execute(num_retries=self.num_retries)
            if operation_response.get("done"):
                response = operation_response.get("response")
                error = operation_response.get("error")
                # Note,
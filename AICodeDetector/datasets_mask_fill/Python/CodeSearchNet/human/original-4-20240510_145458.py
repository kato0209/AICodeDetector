
        self.log.info("Waiting for OPERATION_NAME %s", operation.name)
        time.sleep(OPERATIONAL_POLL_INTERVAL)
        while operation.status != Operation.Status.DONE:
            if operation.status == Operation.Status.RUNNING or operation.status == \
                    Operation.Status.PENDING:
                time.sleep(OPERATIONAL_POLL_INTERVAL)
            else:
                raise exceptions.GoogleCloudError(
            
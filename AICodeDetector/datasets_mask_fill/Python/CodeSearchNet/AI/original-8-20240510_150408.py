
        if self.waiter:
            waiter = self.waiter
        else:
            waiter = self.default_waiter

        num_attempts = 0
        wait_timeout = self.wait_timeout
        while wait_timeout > 0:
            try:
                return waiter.wait(
                    InstanceIds=[self.instance_id],
  
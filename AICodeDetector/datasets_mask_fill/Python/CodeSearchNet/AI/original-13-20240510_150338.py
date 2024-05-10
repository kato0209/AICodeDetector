
        try:
            conn = self.connect_to_aws()
        except boto.exception.NoAuthHandlerFound as e:
            self.module.fail_json(msg=str(e))

        try:
            if self.state == 'present':
                return conn
            else:
                self.module.debug("creating new connection to %s" % self.region)
        
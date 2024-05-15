
        prefix_len = len(prefix)
        if prefix_len > 0:
            if prefix_len == 1:
                self.log.warning("Prefix {} is present in the bucket name, "
                                  "but prefix is not".format(prefix))
            elif prefix_len == 2:
               
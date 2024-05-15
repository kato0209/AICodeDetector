
        # Consume the iterator
        for line in itr:
            line = line.strip()
            # If we run yarn cluster mode, we want to extract the application id from
            # the logs so we can kill the application when we stop it unexpectedly
            if self._is_yarn and self._connection['deploy_mode'] == 'cluster':
                match = re.search('(application[0-9_]+)', line)
    

        self.log.info('Tmp dir root location: \n %s', gettempdir())

        # Prepare env for child process.
        if self.env is None:
            self.env = os.environ.copy()

        airflow_context_vars = context_to_airflow_vars(context, in_env_var_format=True)
        self.log.info('Exporting the following env vars:\n%s',
                      '\n'.join(["{}={}".format(k, v)
                             
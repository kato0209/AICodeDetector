
        spark_submit_cmd = self._build_spark_submit_command(application)

        if hasattr(self, '_env'):
            env = os.environ.copy()
            env.update(self._env)
            kwargs["env"] = env

        self._submit_sp = subprocess.Popen(spark_submit_cmd,
                                           stdout=subprocess.PIPE,
              
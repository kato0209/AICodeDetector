
        return self.get_conn().databases().get(
            project=project_id,
            instance=instance,
            database=database
        ).execute(num_retries=self.num_retries)
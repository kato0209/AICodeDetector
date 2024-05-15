
        from google.cloud.bigquery.job import QueryJobConfig

        return QueryJobConfig(
            service=self.service, project_id=self.project_id, job_id=self.job_id
        )

    def test_ctor_w_job_id(self):
        from google.cloud.bigquery.job import QueryJobConfig

        job_config = self.get_service().job_config
        self.assertIsInstance(job_config, QueryJobConfig)
        self.assertEqual(job_config.job_id, self.job_id)

    def test_ctor_w_
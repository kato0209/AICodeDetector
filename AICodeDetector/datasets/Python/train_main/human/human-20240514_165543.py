
        jobs = self.service.jobs()
        job_data = {'configuration': configuration}

        # Send query and wait for reply.
        query_reply = jobs \
            .insert(projectId=self.project_id, body=job_data) \
            .execute(num_retries=self.num_retries)
        self.running_job_id = query_reply['jobReference']['jobId']
        if 'location' in query_reply['jobReference']:
            location = query_reply['jobReference']['location']
        else:
            location
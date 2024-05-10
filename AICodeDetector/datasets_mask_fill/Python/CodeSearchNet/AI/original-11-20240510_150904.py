
    while True:
      job = self.pollJob(job_key, timeoutSecs=timeoutSecs, retryDelaySecs=retryDelaySecs, key=key)
      if job['status'] == 'DONE':
        return job
      if job['status'] == 'CANCELLED':
        raise Exception("Job %s was not canceled: %s" % (job_key, job['errorMessage']))
      if job['status'] == 'FAILED':
        raise Exception("Job %s failed with message: %s" % (job_key, job['errorMessage']))
      if job['status'] == 'CANCEL
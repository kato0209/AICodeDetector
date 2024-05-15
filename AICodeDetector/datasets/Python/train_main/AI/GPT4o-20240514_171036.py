

    start_time = time.time()
    end_time = start_time + timeoutSecs
    job_status = None

    while time.time() < end_time:
        response = requests.get(f"{self.base_url}/Jobs/{job_key}", params=kwargs)
        if response.status_code == 200:
            job_status = response.json().get('status')
            if job_status in ["DONE", "CANCELLED", "FAILED"]:
                break
       
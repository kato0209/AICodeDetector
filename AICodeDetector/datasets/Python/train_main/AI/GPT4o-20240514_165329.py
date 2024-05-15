

    method, endpoint = endpoint_info
    url = f"https://api.example.com/{endpoint}"
    headers = {'Content-Type': 'application/json'}
    retries = 3

    for attempt in range(retries):
        try:
            if method.upper() == 'GET':
                response = requests.get(url, headers=headers, json=json)
            elif method.upper() == 'POST':
                response = requests.post(url, headers=headers, json=json)
            else:
                raise AirflowException(f"
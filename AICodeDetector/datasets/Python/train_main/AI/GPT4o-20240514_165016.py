
    if project_id is None:
        project_id = self.gcp_connection.default_project_id

    url = f"https://www.googleapis.com/sql/v1beta4/projects/{project_id}/instances/{instance}/databases/{database}"
    response = self.gcp_connection.request("GET", url)
    
    if response.status_code != 200:
        raise Exception(f"Failed to retrieve database: {response.content}")
    
    return response.json()


        try:
            dataset_resource = self.service.datasets().get(
                projectId=project_id, datasetId=dataset_id).execute()
            dataset_resource.reload()
            return dataset_resource
        except HttpError as e:
            if e.resp.status == 404:
                dataset_resource = self.service.datasets().get(
                   
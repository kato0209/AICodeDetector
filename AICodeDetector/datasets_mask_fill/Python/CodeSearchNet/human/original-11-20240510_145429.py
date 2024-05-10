
        tables_resource = self.service.tables() \
            .get(projectId=self.project_id, datasetId=dataset_id, tableId=table_id) \
            .execute(num_retries=self.num_retries)
        return tables_resource['schema']
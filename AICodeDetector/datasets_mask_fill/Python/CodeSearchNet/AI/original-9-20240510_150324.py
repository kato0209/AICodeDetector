.)<dataset>.<table>``
            BigQuery tables to use as the source data. Use a list if there are
            multiple source tables.
            If ``<project>`` is not included, project will be the project defined
            in the connection json.
        :type source_project_dataset_tables: list|string
        :param destination_project_dataset_table: The destination BigQuery
            table. Format is: (project:|project.)<dataset>.<table>
        :type destination_project_dataset_table: string
    
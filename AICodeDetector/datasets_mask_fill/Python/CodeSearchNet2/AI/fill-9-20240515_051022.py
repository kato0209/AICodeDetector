.)<dataset>.<table>`` The source BigQuery table in this format:


.. code-block:: json
    {
        <project id>: [<dataset id>, <table id>]
       ...
    }

Where ``project=`` refers to the project it to use as the source data. Use a list if there are multiple source tables. If ``<project>`` is not included, You can specify multiple source BigQuery tables will be the project defined in the connection json. :type source_project_dataset_tables: list|string :param destination_project_dataset_table: The destination BigQuery table. Format is: (project:|project.)<dataset>.<table> :type destination_project_dataset_table: string
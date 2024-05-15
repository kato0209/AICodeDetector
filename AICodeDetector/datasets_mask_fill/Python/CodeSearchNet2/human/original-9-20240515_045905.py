
        source_project_dataset_tables = ([
            source_project_dataset_tables
        ] if not isinstance(source_project_dataset_tables, list) else
            source_project_dataset_tables)

        source_project_dataset_tables_fixup = []
        for source_project_dataset_table in source_project_dataset_tables:
            source_project, source_dataset, source_table = \
                _split_tablename(table_input=source_project_dataset_table,
                           
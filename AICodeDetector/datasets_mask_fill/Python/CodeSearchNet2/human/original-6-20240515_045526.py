
        if collection_name is None:
            raise AirflowBadRequest("Collection name cannot be None.")

        # We need to check to see if this container already exists so we don't try
        # to create it twice
        existing_container = list(self.get_conn().QueryContainers(
            get_database_link(self.__get_database_name(database_name)), {
                "query": "SELECT * FROM r WHERE r.id=@id",
                "parameters": [
  

        if documents is None:
            raise AirflowBadRequest("You cannot insert empty documents")

        created_documents = []
        for single_document in documents:
            created_documents.append(
                self.get_conn().CreateItem(
                    get_collection_link(
                        self.__get_database_name(database_name),
      
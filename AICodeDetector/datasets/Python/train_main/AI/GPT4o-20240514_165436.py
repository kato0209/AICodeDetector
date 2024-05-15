
        self, location, product_set_id, project_id=None, retry=None, timeout=None, metadata=None
    ):
        """
        For the documentation see:
        :class:`~airflow.contrib.operators.gcp_vision_operator.CloudVisionProductSetDeleteOperator`
        """
        client = vision_v1.ProductSearchClient()

        if not project_id:
            project_id = self.project_id

        name = client.product_set_path(project_id, location, product_set_id)

        client.delete_product_set(name=name, retry=retry, timeout=timeout
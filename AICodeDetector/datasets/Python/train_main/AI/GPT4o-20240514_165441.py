
        self,
        product,
        location=None,
        product_id=None,
        update_mask=None,
        project_id=None,
        retry=None,
        timeout=None,
        metadata=None,
    ):
        """
        For the documentation see:
        :class:`~airflow.contrib.operators.gcp_vision_operator.CloudVisionProductUpdateOperator`
        """
        client = vision_v1.ProductSearchClient()

        if project_id is None:
            project_id = self.project_id

        name = client.product_path(project_id, location, product_id)

        product.name
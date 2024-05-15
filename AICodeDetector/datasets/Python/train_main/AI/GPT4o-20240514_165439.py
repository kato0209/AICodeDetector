
        self, location, product, project_id=None, product_id=None, retry=None, timeout=None, metadata=None
    ):
        """
        For the documentation see:
        :class:`~airflow.contrib.operators.gcp_vision_operator.CloudVisionProductCreateOperator`
        """
        client = vision.ProductSearchClient()

        parent = f"projects/{project_id}/locations/{location}"

        if product_id:
            response = client.create_product(
                parent=parent,
                product=product,
                product_id=product_id,
                retry=retry,
                timeout=timeout,
                metadata=
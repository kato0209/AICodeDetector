
        self,
        product_set_id,
        product_id,
        location=None,
        project_id=None,
        retry=None,
        timeout=None,
        metadata=None,
    ):
        """
        For the documentation see:
        :py:class:`~airflow.contrib.operators.gcp_vision_operator.CloudVisionAddProductToProductSetOperator`
        """
        client = vision_v1.ProductSearchClient()

        if not location:
            location = 'us-west1'

        if not project_id:
            project_id = 'your-project-id'


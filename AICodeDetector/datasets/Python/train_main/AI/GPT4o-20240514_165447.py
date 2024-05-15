
        self,
        location,
        product_id,
        reference_image_id,
        project_id=None,
        retry=None,
        timeout=None,
        metadata=None,
    ):
        """
        For the documentation see:
        :py:class:`~airflow.contrib.operators.gcp_vision_operator.CloudVisionReferenceImageCreateOperator`
        """
        client = vision_v1.ProductSearchClient()

        if not project_id:
            project_id = self.project_id

        name = client.reference_image_path(
            project=project_id,
            location=location,

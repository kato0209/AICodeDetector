
        self,
        location,
        product_id,
        reference_image,
        reference_image_id=None,
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

        if project_id is None:
            project_id = self.project_id

        parent = f"projects/{project_id}/locations/{location
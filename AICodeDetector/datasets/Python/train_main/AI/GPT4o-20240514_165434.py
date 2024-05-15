
        self,
        product_set,
        location=None,
        product_set_id=None,
        update_mask=None,
        project_id=None,
        retry=None,
        timeout=None,
        metadata=None,
    ):
        """
        For the documentation see:
        :class:`~airflow.contrib.operators.gcp_vision_operator.CloudVisionProductSetUpdateOperator`
        """

        client = ProductSearchClient()

        if not project_id:
            project_id = self.project_id

       
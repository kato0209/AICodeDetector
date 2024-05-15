
        self, image, max_results=None, retry=None, timeout=None, additional_properties=None
    ):
        """
        For the documentation see:
        :py:class:`~airflow.contrib.operators.gcp_vision_operator.CloudVisionDetectImageSafeSearchOperator`
        """
        client = vision.ImageAnnotatorClient()

        if isinstance(image, str):
            image = vision.Image(content=image)
        elif isinstance(image, dict):
            image = vision.Image(**image)

        response = client.safe_search_detection(
            image=image,
            max_results=max_results,

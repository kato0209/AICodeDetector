
        client = self.annotator_client

        self.log.info("Detecting safe search")

        if additional_properties is None:
            additional_properties = {}

        response = client.safe_search_detection(
            image=image, max_results=max_results, retry=retry, timeout=timeout, **additional_properties
        )
        response = MessageToDict(response)
        self._check_for_error(response)

        self.log.info("Safe search detection finished")
        return response

        client = self.get_conn()
        self.log.info('Creating ReferenceImage')
        parent = ProductSearchClient.product_path(project=project_id, location=location, product=product_id)

        response = client.create_reference_image(
            parent=parent,
            reference_image=reference_image,
            reference_image_id=reference_image_id,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

      
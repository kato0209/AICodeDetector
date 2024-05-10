
        client = self.get_conn()
        parent = ProductSearchClient.location_path(project_id, location)
        self.log.info('Creating a new Product under the parent: %s', parent)
        response = client.create_product(
            parent=parent,
            product=product,
            product_id=product_id,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

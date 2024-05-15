
        client = self.get_conn()
        parent = ProductSearchClient.location_path(project_id, location)
        self.log.info('Creating a new ProductSet under the parent: %s', parent)
        response = client.create_product_set(
            parent=parent,
            product_set=product_set,
            product_set_id=product_set_id,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

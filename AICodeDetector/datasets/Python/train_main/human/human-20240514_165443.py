
        client = self.get_conn()
        name = ProductSearchClient.product_path(project_id, location, product_id)
        self.log.info('Deleting ProductSet: %s', name)
        client.delete_product(name=name, retry=retry, timeout=timeout, metadata=metadata)
        self.log.info('Product with the name [%s] deleted:', name)
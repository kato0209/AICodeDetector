
        client = self.get_conn()
        name = ProductSearchClient.product_set_path(project_id, location, product_set_id)
        self.log.info('Deleting ProductSet: %s', name)
        client.delete_product_set(name=name, retry=retry, timeout=timeout, metadata=metadata)
        self.log.info('ProductSet with the name [%s] deleted.', name)
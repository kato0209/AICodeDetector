
        client = self.get_conn()

        product_name = ProductSearchClient.product_path(project_id, location, product_id)
        product_set_name = ProductSearchClient.product_set_path(project_id, location, product_set_id)

        self.log.info('Add Product[name=%s] to Product Set[name=%s]', product_name, product_set_name)

        client.add_product_to_product_set(
            name=product_set_name, product=product_name, retry=retry, timeout=timeout, metadata=metadata
        )

        self.log.info('Product added to Product Set')
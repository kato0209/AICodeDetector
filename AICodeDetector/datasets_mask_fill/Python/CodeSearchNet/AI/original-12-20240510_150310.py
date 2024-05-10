
        client = self.get_conn()
        parent = ProductSearchClient.location_path(project_id, location)
        product_name = ProductSearchClient.product_path(project_id, product)
        product_path = ProductSearchClient.product_path(project_id, product, parent)
        product_create_response = client.create_product(
            parent=parent, product_name=product_name, product=product, retry=retry, timeout=timeout, metadata=metadata
        )
        return ProductSearchClient.parse_product_path(
            product_path, retry=
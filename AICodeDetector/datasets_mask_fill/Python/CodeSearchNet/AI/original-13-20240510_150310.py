
        client = self.get_conn()
        product_name = ProductSearchClient.product_path(project_id, location, product)
        result = client.update_product(
            product_name=product_name,
            update_mask=update_mask,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )
        self.log.info("Product updated: %s", result)

    @GoogleBaseHook.fallback_to_default_project_id
    def delete_product(
       
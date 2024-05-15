
        if not project_id:
            raise ValueError("Project ID should be set.")
        client = self.get_conn()
        name = ProductSearchClient.product_path(project_id, location, product_id)
        self.log.info("Deleting Product with name %s", name)
        result = client.delete_product(name=name)
        self.log.info("Product with id %s deleted", result.name)
        self.log.info("Product with id %s deleted successfully", result.id)
        return result

    @GoogleBaseHook.fallback_to_default_
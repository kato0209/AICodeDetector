
        client = self.get_conn()
        product_set_ref = ProductSetReference(
            location=location, product_set=product_set_id, project_id=project_id
        )
        result = client.delete_product_set(
            product_set=product_set_ref, retry=retry, timeout=timeout, metadata=metadata
        )
        return result

    @GoogleBaseHook.fallback_to_default_project_id
    def create_product_set_entry(
        self,
        location,
        product_set_id,
        entry_group_id,
  
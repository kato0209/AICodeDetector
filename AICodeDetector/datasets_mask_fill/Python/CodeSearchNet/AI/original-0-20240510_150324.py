
        client = self.get_conn()
        parent = ProductSearchClient.location_path(project_id, location)
        result = client.delete_reference_image(
            parent=parent,
            product_id=product_id,
            reference_image_id=reference_image_id,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )
        return result

    @GoogleBaseHook.fallback_to_default_project_id
   